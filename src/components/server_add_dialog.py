import logging
import time
import jellyfin_api_client.client as jellyfin_client
from jellyfin_api_client.api.system import get_public_system_info
from jellyfin_api_client.models.public_system_info import PublicSystemInfo
from httpx import RequestError, InvalidURL
import psutil
from gi.repository import Gtk, Adw, GObject, Gio
import socket
from socket import (
    AF_INET,
    AF_INET6,
    SO_BINDTODEVICE,
    SO_BROADCAST,
    SOCK_DGRAM,
    IPPROTO_UDP,
    SOL_SOCKET,
)
from src import build_constants
from src.components.server_row import ServerRow
from src.reactive_set import ReactiveSet
from src.server import Server


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_add_dialog.ui")
class ServerAddDialog(Adw.Window):
    __gtype_name__ = "MarmaladeServerAddDialog"

    DISCOVERY_PORT: int = 7359
    DISCOVERY_ENCODING: str = "utf-8"
    DISCOVERY_SEND_TIMEOUT_SECONDS: float = 5.0
    # TODO use 30 seconds when not testing
    DISCOVERY_RECEIVE_TIMEOUT_SECONDS: float = 5.0
    DISCOVERY_BUFSIZE: int = 4096

    cancel_button = Gtk.Template.Child()
    manual_add_button = Gtk.Template.Child()
    manual_add_editable = Gtk.Template.Child()
    detected_server_rows_group = Gtk.Template.Child()
    spinner = Gtk.Template.Child()
    spinner_revealer = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()

    discovered_servers: ReactiveSet[Server]
    __n_discovery_tasks: int
    __n_discovery_tasks_done: int

    @GObject.Signal(name="cancelled")
    def cancelled(self):
        """Signal emitted when the dialog is cancelled"""

    @GObject.Signal(name="server-picked", arg_types=[object])
    def server_picked(self, _server: Server):
        """Signal emitted when a server is picked"""
        # FIXME cannot emit with GObject.Object descendant in the args it seems ???

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cancel_button.connect("clicked", self.on_cancel_button_clicked)
        self.manual_add_button.connect("clicked", self.on_manual_button_clicked)
        self.__n_discovery_tasks = 0
        self.__n_discovery_tasks_done = 0
        self.discovered_servers = ReactiveSet()
        self.discovered_servers.emitter.connect(
            "item-added", self.on_discovered_server_added
        )
        discover_task = Gio.Task.new(None, None, None, None)
        discover_task.run_in_thread(lambda *_args: self.discover())

    def discover(self) -> None:
        logging.debug("Discovering servers")
        for name, address_info_list in psutil.net_if_addrs().items():
            for address_info in address_info_list:
                if (
                    address_info.family not in (AF_INET, AF_INET6)
                    or address_info.broadcast is None
                ):
                    continue
                args = (name, address_info.family, address_info.broadcast)
                self.__n_discovery_tasks += 1
                subtask = Gio.Task.new(
                    None, None, self.on_discovery_subtask_finished, None
                )
                subtask.run_in_thread(
                    lambda *_args, args=args: self.discover_on_interface(*args)
                )

    def discover_on_interface(
        self,
        interface_name: str,
        address_family: socket.AddressFamily,
        broadcast_address: str,
    ) -> None:
        with socket.socket(
            family=address_family, type=SOCK_DGRAM, proto=IPPROTO_UDP
        ) as sock:
            # Broadcast
            logging.debug(
                "Discovering servers on %s %d", broadcast_address, self.DISCOVERY_PORT
            )
            interface_name_buffer = bytearray(interface_name, encoding="utf-8")
            sock.setsockopt(SOL_SOCKET, SO_BINDTODEVICE, interface_name_buffer)
            sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            sock.settimeout(self.DISCOVERY_SEND_TIMEOUT_SECONDS)
            msg = bytearray("Who is JellyfinServer?", encoding=self.DISCOVERY_ENCODING)
            try:
                sock.sendto(msg, (broadcast_address, self.DISCOVERY_PORT))
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
                    (data, address_info) = sock.recvfrom(self.DISCOVERY_BUFSIZE)
                except TimeoutError:
                    logging.debug("Server discovery receive timed out")
                    return
                msg = data.decode(encoding=self.DISCOVERY_ENCODING)
                # TODO handle response properly
                logging.debug("Response from %s: %s", address_info, msg)
                elapsed = time.time() - start

    def on_discovery_subtask_finished(self, *_args):
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

    def query_server_address(self, address: str) -> Server:
        """Query a server address to check its validity and get its name"""
        try:
            client = jellyfin_client.Client(address)
            info: PublicSystemInfo = get_public_system_info.sync(client=client)
        except (RequestError, InvalidURL) as error:
            raise ValueError(_("Invalid server address")) from error
        if info is None:
            raise ValueError(_("Server has no public info"))
        return Server(info.server_name, info.local_address)

    def on_manual_button_clicked(self, _button: Gtk.Widget) -> None:
        address = self.manual_add_editable.get_text()
        try:
            server = self.query_server_address(address)
        except ValueError as error:
            logging.error('Invalid server address "%s"', address, exc_info=error)
            toast = Adw.Toast()
            toast.set_priority(Adw.ToastPriority.HIGH)
            toast.set_title(error.args[0])
            self.toast_overlay.add_toast(toast)
        else:
            self.emit("server-picked", server)
            self.close()

    def on_detected_row_button_clicked(self, server_row: ServerRow) -> None:
        self.emit("server-picked", server_row.server)
        self.close()
