from gi.repository import Adw, Gtk, GObject
from src.server import Server
from src import build_constants


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_row.ui")
class ServerRow(Adw.ActionRow):
    __gtype_name__ = "MarmaladeServerRow"

    button = Gtk.Template.Child()
    button_revealer = Gtk.Template.Child()
    tick = Gtk.Template.Child()
    tick_revealer = Gtk.Template.Child()
    server: Server

    @property
    def is_selected(self):
        return self.tick.get_active()

    @GObject.Signal(name="button-clicked")
    def button_clicked(self):
        """Signal emitted when the row button is clicked"""

    @GObject.Signal(name="selected-changed", arg_types=[bool])
    def selected_changed(self, _is_selected: bool):
        """Signal emitted when the tick is check or unchecked"""

    def __init__(
        self,
        server: Server,
        icon_name: str = "go-next-symbolic",
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.server = server
        self.parent_selection_change_connection = None
        self.button.set_icon_name(icon_name)
        self.button.connect("clicked", self.on_button_clicked)
        self.tick.connect("toggled", self.on_tick_toggled)
        self.update_from_server()

    def on_button_clicked(self, _button) -> None:
        self.emit("button-clicked")

    def update_from_server(self) -> None:
        self.set_title(self.server.name)
        self.set_subtitle(self.server.address)

    def toggle_button_visible(self) -> None:
        is_revealed = self.button_revealer.get_reveal_child()
        self.button_revealer.set_reveal_child(not is_revealed)

    def toggle_tick_visible(self) -> None:
        is_revealed = self.tick_revealer.get_reveal_child()
        self.tick_revealer.set_reveal_child(not is_revealed)

    def on_tick_toggled(self, _tick) -> None:
        self.emit("selected-changed", self.is_selected)
