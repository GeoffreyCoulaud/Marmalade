from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.database.api import ServerInfo


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/servers_list_row.ui")
class ServersListRow(Adw.ActionRow):
    __gtype_name__ = "MarmaladeServersListRow"

    button = Gtk.Template.Child()
    button_revealer = Gtk.Template.Child()
    tick = Gtk.Template.Child()
    tick_revealer = Gtk.Template.Child()
    server: ServerInfo

    __edit_mode: bool

    @GObject.Signal(name="button-clicked")
    def button_clicked(self):
        """Signal emitted when the row button is clicked"""

    @GObject.Signal(name="selected-changed", arg_types=[bool])
    def selected_changed(self, _is_selected: bool):
        """Signal emitted when the tick is check or unchecked"""

    @property
    def edit_mode(self) -> bool:
        return self.__edit_mode

    @edit_mode.setter
    def edit_mode(self, edit_mode: bool) -> None:
        self.__edit_mode = edit_mode
        if edit_mode:
            self.tick.set_active(False)
        self.tick_revealer.set_reveal_child(edit_mode)
        self.button_revealer.set_reveal_child(not edit_mode)
        self.set_activatable_widget(self.tick if edit_mode else self.button)

    @property
    def is_selected(self):
        return self.tick.get_active()

    def __init__(
        self,
        server: ServerInfo,
        icon_name: str = "go-next-symbolic",
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.__edit_mode = False
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

    def on_tick_toggled(self, _tick) -> None:
        self.emit("selected-changed", self.is_selected)
