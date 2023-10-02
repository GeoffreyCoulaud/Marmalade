import logging
import time
import psutil
from gi.repository import Gtk, Adw, GObject
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
    detected_servers_spinner = Gtk.Template.Child()

    detected_servers: ReactiveSet[Server]

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
        self.detected_servers = ReactiveSet()
        self.detected_servers.emitter.connect(
            "item-added", self.on_detected_server_added
        )
        # TODO run async
        self.detect_servers_thread_func()

    def detect_servers_thread_func(self) -> None:
        for name, address_info_list in psutil.net_if_addrs().items():
            for address_info in address_info_list:
                if (
                    address_info.family not in (AF_INET, AF_INET6)
                    or address_info.broadcast is None
                ):
                    continue
                # TODO Run async
                self.discover_servers(name, address_info.family, address_info.broadcast)

    def discover_servers(
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
                    logging.info("Server discovery receive timed out")
                    return
                msg = data.decode(encoding=self.DISCOVERY_ENCODING)
                # TODO handle response properly
                logging.debug("Response from %s: %s", address_info, msg)
                elapsed = time.time() - start

    def on_detected_server_added(self, _emitter, server: Server) -> None:
        row = ServerRow(server, "list-add-symbolic")
        row.connect("button-clicked", self.on_detected_row_button_clicked)
        self.detected_server_rows_group.add(row)

    def on_cancel_button_clicked(self, _button) -> None:
        self.emit("cancelled")
        self.close()

    def on_manual_button_clicked(self, _button: Gtk.Widget) -> None:
        address = self.manual_add_editable.get_text()
        # TODO test the address (notify failure visually)
        # TODO get the server name
        name = "TODO: Check server address + query its name"
        server = Server(name, address)
        self.emit("server-picked", server)
        self.close()

    def on_detected_row_button_clicked(self, server_row: ServerRow) -> None:
        self.emit("server-picked", server_row.server)
        self.close()
