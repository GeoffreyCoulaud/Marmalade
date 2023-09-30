from gi.repository import Adw, Gtk, GObject
from src.server import Server
from src import build_constants


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_row.ui")
class ServerRow(Adw.ActionRow):
    __gtype_name__ = "MarmaladeServerRow"

    button = Gtk.Template.Child()
    button_content = Gtk.Template.Child()
    server: Server

    @GObject.Signal(name="button-clicked")
    def button_clicked(self):
        """Signal emitted when the row button is clicked"""

    def __init__(
        self,
        server: Server,
        icon_name: str = "go-next-symbolic",
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.server = server
        self.button_content.set_icon_name(icon_name)
        self.button.connect("clicked", self.on_button_clicked)
        self.update_from_server()

    def on_button_clicked(self, _button) -> None:
        self.emit("button-clicked")

    def update_from_server(self) -> None:
        self.set_title(self.server.name)
        self.set_subtitle(self.server.address)
