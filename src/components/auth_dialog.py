from gi.repository import Adw, GObject, Gtk

from src import build_constants, shared
from src.components.auth_credentials_view import AuthCredentialsView
from src.components.auth_login_method_view import AuthLoginMethodView
from src.components.auth_quick_connect_view import AuthQuickConnectView
from src.components.auth_user_select_view import AuthUserSelectView
from src.database.api import ServerInfo


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/auth_dialog.ui")
class AuthDialog(Adw.Window):
    __gtype_name__ = "MarmaladeAuthDialog"

    views = Gtk.Template.Child()

    server: ServerInfo

    @GObject.Signal(name="authenticated", arg_types=[object, str, str])
    def authenticated(self, _server: ServerInfo, _user_id: str, _token: str):
        """Signal emitted when the user is authenticated"""

    @GObject.Signal(name="cancelled")
    def cancelled(self):
        """Signal emitted when the login process is cancelled"""

    def __init__(self, server: ServerInfo, *args, **kwargs) -> None:
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
        view.connect("skipped", self.on_user_picked)
        self.views.push(view)

    def on_user_picked(self, _widget, username: str = "", user_id: str = ""):
        # Check if we have a token for that user
        token = shared.settings.get_token(address=self.server.address, user_id=user_id)
        if token is not None:
            self.on_authenticated(None, self.server, user_id, token)
            return
        # If not, display the credentials view
        view = AuthCredentialsView(dialog=self, server=self.server, username=username)
        view.connect("authenticated", self.on_authenticated)
        self.views.push(view)

    def on_authenticated(
        self, _widget, server: ServerInfo, user_id: str, token: str
    ) -> None:
        self.emit("authenticated", server, user_id, token)
        self.close()
