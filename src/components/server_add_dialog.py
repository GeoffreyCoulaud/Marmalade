import json
import logging
import socket
import time
from socket import (
    AF_INET,
    AF_INET6,
    IPPROTO_UDP,
    SO_BINDTODEVICE,
    SO_BROADCAST,
    SOCK_DGRAM,
    SOL_SOCKET,
)
from typing import Set

import psutil
from gi.repository import Adw, Gio, GLib, GObject, Gtk
from httpx import InvalidURL, RequestError
from jellyfin_api_client.api.system import get_public_system_info
from jellyfin_api_client.client import Client as JfClient
from jellyfin_api_client.models.public_system_info import PublicSystemInfo

from src.components.servers_list_row import ServersListRow
from src.components.widget_builder import (
    Children,
    Handlers,
    Properties,
    TypedChild,
    build,
)
from src.database.api import ServerInfo
from src.task import Task


class KnownAddressError(Exception):
    """Error raised when trying to add a duplicate server address"""


class ServerAddDialog(Adw.ApplicationWindow):
    __gtype_name__ = "MarmaladeServerAddDialog"

    DISCOVERY_PORT: int = 7359
    DISCOVERY_ENCODING: str = "utf-8"
    DISCOVERY_SEND_TIMEOUT_SECONDS: float = 5.0
    DISCOVERY_RECEIVE_TIMEOUT_SECONDS: float = 30.0
    DISCOVERY_BUFSIZE: int = 4096

    __manual_add_editable: Adw.EntryRow
    __detected_server_rows_group: Adw.PreferencesGroup
    __spinner_revealer: Gtk.Revealer
    __toast_overlay: Adw.ToastOverlay

    __tasks_cancellable: Gio.Cancellable
    __discover_subtasks_count: int
    __discover_subtasks_done_count: int
    __addresses: set[str]
    __discovered_addresses: set[str]

    @GObject.Signal(name="cancelled")
    def cancelled(self):
        """Signal emitted when the dialog is cancelled"""

    @GObject.Signal(name="server-picked", arg_types=[object])
    def server_picked(self, _server: ServerInfo):
        """Signal emitted when a server is picked"""

    def __init_widget(self):
        self.__spinner_revealer = build(
            Gtk.Revealer
            + Properties(
                reveal_child=True,
                transition_type=Gtk.RevealerTransitionType.CROSSFADE,
            )
            + Children(
                Gtk.Spinner
                + Properties(
                    spinning=True,
                )
            )
        )

        self.__manual_add_editable = build(
            Adw.EntryRow
            + Properties(title=_("Server address"))
            + TypedChild(
                "suffix",
                Gtk.Button
                + Handlers(clicked=self.__on_manual_button_clicked)
                + Properties(
                    valign=Gtk.Align.CENTER,
                    icon_name="list-add-symbolic",
                ),
            )
        )

        self.__detected_server_rows_group = build(
            Adw.PreferencesGroup
            + Properties(title=_("Discovered servers"))
            + TypedChild("header-suffix", self.__spinner_revealer)
        )

        self.__toast_overlay = build(
            Adw.ToastOverlay
            + Children(
                Gtk.ScrolledWindow
                + Children(
                    Adw.Clamp
                    + Properties(
                        margin_top=16,
                        margin_start=16,
                        margin_end=16,
                        margin_bottom=16,
                    )
                    + Children(
                        Gtk.Box
                        + Properties(orientation=Gtk.Orientation.VERTICAL)
                        + Children(
                            # Wrapping the manual add editable in a preferences group
                            # is necessary, else its corners will be sharp instead of
                            # rounded like the other rows.
                            Adw.PreferencesGroup
                            + Properties(margin_bottom=16)
                            + Children(self.__manual_add_editable),
                            self.__detected_server_rows_group,
                        )
                    )
                )
            )
        )

        header_bar = (
            Adw.HeaderBar
            + Properties(decoration_layout="")
            + TypedChild(
                "start",
                Gtk.Button
                + Handlers(clicked=self.__on_cancel_button_clicked)
                + Properties(label=_("Cancel")),
            )
        )

        self.set_default_size(width=600, height=300)
        self.set_modal(True)
        self.set_content(
            build(
                Adw.ToolbarView
                + TypedChild("top", header_bar)
                + TypedChild("content", self.__toast_overlay)
            )
        )

        pass

    def __init__(
        self, application: Adw.Application, addresses: Set[str], **kwargs
    ) -> None:
        super().__init__(application=application, **kwargs)
        self.__init_widget()

        self.__tasks_cancellable = Gio.Cancellable.new()
        self.__discover_subtasks_count = 0
        self.__discover_subtasks_done_count = 0
        self.__addresses = set(addresses)
        self.__discovered_addresses = set(addresses)
        discover_task = Task(
            main=self.discover,
            cancellable=self.__tasks_cancellable,
        )
        discover_task.run()

    def close(self) -> None:
        self.__tasks_cancellable.cancel()
        super().close()

    def discover(self) -> None:
        logging.debug("Discovering servers")
        for name, address_info_list in psutil.net_if_addrs().items():
            for address_info in address_info_list:
                if (
                    address_info.family not in (AF_INET, AF_INET6)
                    or address_info.broadcast is None
                ):
                    continue
                self.__discover_subtasks_count += 1
                subtask = Task(
                    main=self.discover_on_interface,
                    main_args=(name, address_info.family, address_info.broadcast),
                    callback=self.on_discover_subtask_finished,
                    cancellable=self.__tasks_cancellable,
                )
                subtask.run()

    def discover_on_interface(
        self,
        interface_name: str,
        address_family: socket.AddressFamily,  # pylint: disable=no-member
        broadcast_address: str,
    ) -> None:
        """Discover servers by UDP broadcasting on the given interface information"""

        with socket.socket(
            family=address_family, type=SOCK_DGRAM, proto=IPPROTO_UDP
        ) as sock:
            # Set socket up
            interface_name_buffer = bytearray(interface_name, encoding="utf-8")
            sock.setsockopt(SOL_SOCKET, SO_BINDTODEVICE, interface_name_buffer)
            sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

            # Broadcast
            try:
                self.discover_broadcast(sock, broadcast_address)
            except TimeoutError:
                logging.error("Server discovery broadcast send timed out")
                return

            # Listen for responses
            try:
                self.discover_listen(sock)
            except TimeoutError:
                logging.debug("Server discovery receive timeout")
                return

    def discover_broadcast(self, sock, address):
        """
        Broadcast a discover message on the socket.
        Changes the socket's timeout value.
        May raise TimeoutError.
        """
        logging.debug("Discovering servers on %s %d", address, self.DISCOVERY_PORT)
        sock.settimeout(self.DISCOVERY_SEND_TIMEOUT_SECONDS)
        message = bytearray("Who is JellyfinServer?", encoding=self.DISCOVERY_ENCODING)
        sock.sendto(message, (address, self.DISCOVERY_PORT))

    def discover_listen(self, sock):
        """
        Receive discover response messages from the socket.
        Changes the socket timeout value.
        May raise TimeoutError.
        """
        logging.debug("Listening for server responses")
        start = time.time()
        elapsed = 0
        while elapsed < self.DISCOVERY_RECEIVE_TIMEOUT_SECONDS:
            # Wait for a message
            sock.settimeout(self.DISCOVERY_RECEIVE_TIMEOUT_SECONDS - elapsed)
            (response, _address) = sock.recvfrom(self.DISCOVERY_BUFSIZE)
            # Process the message
            message = response.decode(encoding=self.DISCOVERY_ENCODING)
            try:
                server_info = json.loads(message)
                server = ServerInfo(
                    name=server_info["Name"],
                    address=server_info["Address"],
                    server_id=server_info["Id"],
                )
            except (json.JSONDecodeError, KeyError):
                # Response isn't JSON or contains invalid data
                continue
            # Add a server row in the main thread
            GLib.idle_add(self.add_discovered_server, server)
            elapsed = time.time() - start

    def add_discovered_server(self, server: ServerInfo) -> None:
        # Deduplicate servers
        if server.address in self.__discovered_addresses:
            return
        logging.debug("Discovered %s", str(server))
        self.__discovered_addresses.add(server.address)
        # Add the server row
        row = ServersListRow(server, "list-add-symbolic")
        row.connect("button-clicked", self.on_detected_row_button_clicked)
        self.__detected_server_rows_group.add(row)

    def on_discover_subtask_finished(self, _result):
        self.__discover_subtasks_done_count += 1
        if self.__discover_subtasks_count == self.__discover_subtasks_done_count:
            self.__spinner_revealer.set_reveal_child(False)

    def __on_cancel_button_clicked(self, _button) -> None:
        self.emit("cancelled")
        self.close()

    def on_detected_row_button_clicked(self, server_row: ServersListRow) -> None:
        self.emit("server-picked", server_row.server)
        self.close()

    def query_public_server_info(self, address: str) -> PublicSystemInfo:
        """Query a server address to check its validity and get its name"""
        try:
            client = JfClient(address)
            info = get_public_system_info.sync(client=client)
        except (RequestError, InvalidURL) as error:
            raise ValueError(_("Invalid server address")) from error
        if info is None:
            raise ValueError(_("Server has no public info"))
        return info

    def __on_manual_button_clicked(self, _button: Gtk.Widget) -> None:
        """Check server address then react to it"""

        def main(address: str):
            if address in self.__addresses:
                raise KnownAddressError()
            return self.query_public_server_info(address)

        def on_error(address: str, error: KnownAddressError | ValueError):
            toast = Adw.Toast()
            toast.set_priority(Adw.ToastPriority.HIGH)
            if isinstance(error, KnownAddressError):
                toast.set_title(_("Server address is already known"))
            else:
                toast.set_title(error.args[0])
                logging.error('Invalid server address "%s"', address, exc_info=error)
            self.__toast_overlay.add_toast(toast)

        def on_success(address: str, result: PublicSystemInfo):
            server = ServerInfo(
                name=result.server_name,  # type: ignore
                server_id=result.id,  # type: ignore
                address=address,
            )
            self.emit("server-picked", server)
            self.close()

        address = self.__manual_add_editable.get_text()
        task = Task(
            main=main,
            main_args=(address,),
            callback=on_success,
            callback_args=(address,),
            error_callback=on_error,
            error_callback_args=(address,),
            cancellable=self.__tasks_cancellable,
        )
        task.run()
