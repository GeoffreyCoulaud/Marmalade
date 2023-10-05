from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.server import Server


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_auth_dialog.ui")
class ServerAuthDialog(Adw.Window):
    __gtype_name__ = "MarmaladeServerAuthDialog"

    server: Server

    @GObject.Signal(name="authenticated", arg_types=[object, str, str])
    def authenticated(self, _server: Server, _user_id: str, _token: str):
        """Signal emitted when the user is authenticated"""

    def __init__(self, server: Server, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        # TODO implement
