from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.database.api import ServerInfo


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_credentials_view.ui"
)
class AuthCredentialsView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthCredentialsView"

    log_in_button = Gtk.Template.Child()
    username_editable = Gtk.Template.Child()
    password_editable = Gtk.Template.Child()

    dialog: Adw.Window
    server: ServerInfo

    @GObject.Signal(name="authenticated", arg_types=[object, str, str])
    def authenticated(self, server: ServerInfo, _user_id: str, _token: str):
        """Signal emitted when the user is authenticated"""

    def __init__(
        self, *args, dialog: Adw.Window, server: ServerInfo, username: str, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        self.dialog = dialog
        self.username_editable.set_text(username)

    def on_log_in_request(self, _widget) -> None:
        # TODO implement logging in with username and password
        pass
