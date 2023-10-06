from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.components.auth_credentials_view import AuthCredentialsView
from src.components.auth_login_method_view import AuthLoginMethodView
from src.components.auth_quick_connect_view import AuthQuickConnectView
from src.components.auth_user_select_view import AuthUserSelectView
from src.server import Server


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/auth_dialog.ui")
class AuthDialog(Adw.Window):
    __gtype_name__ = "MarmaladeAuthDialog"

    views = Gtk.Template.Child()

    server: Server

    @GObject.Signal(name="authenticated", arg_types=[object, str, str])
    def authenticated(self, _server: Server, _user_id: str, _token: str):
        """Signal emitted when the user is authenticated"""

    @GObject.Signal(name="cancelled")
    def cancelled(self):
        """Signal emitted when the login process is cancelled"""

    def __init__(self, server: Server, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        view = AuthLoginMethodView(dialog=self)
        view.connect("chose-username-password", self.on_username_password_chosen)
        view.connect("chose-quick-connect", self.on_quick_connect_chosen)
        view.connect("cancelled", self.on_cancelled)
        self.views.add(view)

    def on_cancelled(self, _widget) -> None:
        self.emit("cancelled")
        self.close()

    def on_quick_connect_chosen(self, _widget) -> None:
        view = AuthQuickConnectView(dialog=self, server=self.server)
        view.connect("authenticated", self.on_authenticated)
        self.views.push(view)

    def on_username_password_chosen(self, _widget) -> None:
        view = AuthUserSelectView(dialog=self, server=self.server)
        view.connect("user-picked", self.on_user_picked)
        self.views.push(view)

    def on_user_picked(self, _widget, username: str):
        view = AuthCredentialsView(dialog=self, server=self.server, username=username)
        view.connect("authenticated", self.on_authenticated)
        self.views.push(view)

    def on_authenticated(
        self, _widget, server: Server, user_id: str, token: str
    ) -> None:
        self.emit("authenticated", server, user_id, token)
        self.close()
