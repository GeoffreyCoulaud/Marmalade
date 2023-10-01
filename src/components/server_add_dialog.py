from gi.repository import Gtk, Adw, GObject
from src import build_constants
from src.components.server_row import ServerRow
from src.reactive_set import ReactiveSet
from src.server import Server


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_add_dialog.ui")
class ServerAddDialog(Adw.Window):
    __gtype_name__ = "MarmaladeServerAddDialog"

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
        self.detect_servers()

    def detect_servers(self) -> None:
        # TODO implement
        self.detected_servers.update(
            (
                Server("An automatically detected server", "http://192.168.1.2:4000"),
                Server("A local server", "http://192.168.1.3:8096"),
            )
        )

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
