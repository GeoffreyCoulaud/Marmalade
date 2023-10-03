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

import psutil
from gi.repository import Adw, Gio, GObject, Gtk
from httpx import InvalidURL, RequestError
from jellyfin_api_client.api.system import get_public_system_info
from jellyfin_api_client.client import Client as JfClient
from jellyfin_api_client.models.public_system_info import PublicSystemInfo

from src import build_constants
from src.components.server_row import ServerRow
from src.reactive_set import ReactiveSet
from src.server import Server
from src.task import Task


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_add_dialog.ui")
class ServerAddDialog(Adw.Window):
    __gtype_name__ = "MarmaladeServerAddDialog"

    DISCOVERY_PORT: int = 7359
    DISCOVERY_ENCODING: str = "utf-8"
    DISCOVERY_SEND_TIMEOUT_SECONDS: float = 5.0
    DISCOVERY_RECEIVE_TIMEOUT_SECONDS: float = 30.0
    DISCOVERY_BUFSIZE: int = 4096

    cancel_button = Gtk.Template.Child()
    manual_add_button = Gtk.Template.Child()
    manual_add_editable = Gtk.Template.Child()
    detected_server_rows_group = Gtk.Template.Child()
    spinner = Gtk.Template.Child()
    spinner_revealer = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()

    discovered_servers: ReactiveSet[Server]
    __tasks_cancellable: Gio.Cancellable
    __n_discovery_tasks: int
    __n_discovery_tasks_done: int

    @GObject.Signal(name="cancelled")
    def cancelled(self):
        """Signal emitted when the dialog is cancelled"""

    @GObject.Signal(name="server-picked", arg_types=[object])
    def server_picked(self, _server: Server):
        """Signal emitted when a server is picked"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cancel_button.connect("clicked", self.on_cancel_button_clicked)
        self.manual_add_button.connect("clicked", self.on_manual_button_clicked)
        self.__tasks_cancellable = Gio.Cancellable.new()
        self.__n_discovery_tasks = 0
        self.__n_discovery_tasks_done = 0
        self.discovered_servers = ReactiveSet()
        self.discovered_servers.emitter.connect(
            "item-added", self.on_discovered_server_added
        )
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
                self.__n_discovery_tasks += 1
                subtask = Task(
                    main=self.discover_on_interface,
                    main_args=(name, address_info.family, address_info.broadcast),
                    callback=self.on_discovery_subtask_finished,
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
            # Broadcast
            logging.debug(
                "Discovering servers on %s (%s) %d",
                broadcast_address,
                address_family.name,
                self.DISCOVERY_PORT,
            )
            interface_name_buffer = bytearray(interface_name, encoding="utf-8")
            sock.setsockopt(SOL_SOCKET, SO_BINDTODEVICE, interface_name_buffer)
            sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            sock.settimeout(self.DISCOVERY_SEND_TIMEOUT_SECONDS)
            message = bytearray(
                "Who is JellyfinServer?", encoding=self.DISCOVERY_ENCODING
            )
            try:
                sock.sendto(message, (broadcast_address, self.DISCOVERY_PORT))
            except TimeoutError:
                logging.error("Server discovery broadcast send timed out")
                return

            # Listen for responses
            logging.debug("Listening for server responses")
            start = time.time()
            elapsed = 0
            while elapsed < self.DISCOVERY_RECEIVE_TIMEOUT_SECONDS:
                sock.settimeout(self.DISCOVERY_RECEIVE_TIMEOUT_SECONDS - elapsed)
                try:
                    (response, _addr_info) = sock.recvfrom(self.DISCOVERY_BUFSIZE)
                except TimeoutError:
                    logging.debug("Server discovery receive timed out")
                    return
                message = response.decode(encoding=self.DISCOVERY_ENCODING)
                try:
                    server_info = json.loads(message)
                    server = Server(server_info["Name"], server_info["Address"])
                except (json.JSONDecodeError, KeyError):
                    # Response isn't JSON or contains invalid data
                    continue
                else:
                    logging.debug("Discovered %s", str(server))
                    self.discovered_servers.add(server)
                elapsed = time.time() - start

    # pylint: disable=unused-argument
    def on_discovery_subtask_finished(self, *, result):
        self.__n_discovery_tasks_done += 1
        if self.__n_discovery_tasks == self.__n_discovery_tasks_done:
            self.spinner_revealer.set_reveal_child(False)

    def on_discovered_server_added(self, _emitter, server: Server) -> None:
        row = ServerRow(server, "list-add-symbolic")
        row.connect("button-clicked", self.on_detected_row_button_clicked)
        self.detected_server_rows_group.add(row)

    def on_cancel_button_clicked(self, _button) -> None:
        self.emit("cancelled")
        self.close()

    def on_detected_row_button_clicked(self, server_row: ServerRow) -> None:
        self.emit("server-picked", server_row.server)
        self.close()

    def query_public_server_info(self, address: str) -> PublicSystemInfo:
        """Query a server address to check its validity and get its name"""
        try:
            client = JfClient(address)
            info: PublicSystemInfo = get_public_system_info.sync(client=client)
        except (RequestError, InvalidURL) as error:
            raise ValueError(_("Invalid server address")) from error
        if info is None:
            raise ValueError(_("Server has no public info"))
        return info

    def on_manual_button_clicked(self, _button: Gtk.Widget) -> None:
        """Check server address then react to it"""

        def on_query_error(address: str, *, error: ValueError):
            logging.error('Invalid server address "%s"', address, exc_info=error)
            toast = Adw.Toast()
            toast.set_priority(Adw.ToastPriority.HIGH)
            toast.set_title(error.args[0])
            self.toast_overlay.add_toast(toast)

        def on_query_done(*, result: PublicSystemInfo):
            server = Server(result.server_name, result.local_address)
            self.emit("server-picked", server)
            self.close()

        address = self.manual_add_editable.get_text()
        task = Task(
            main=self.query_public_server_info,
            main_args=(address,),
            callback=on_query_done,
            error_callback=on_query_error,
            error_callback_args=(address,),
            cancellable=self.__tasks_cancellable,
        )
        task.run()
