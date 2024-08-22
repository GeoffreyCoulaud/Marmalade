from gi.repository import Adw, GObject

from src import shared
from src.components.auth_credentials_view import AuthCredentialsView
from src.components.auth_login_method_view import AuthLoginMethodView
from src.components.auth_quick_connect_view import AuthQuickConnectView
from src.components.auth_user_select_view import AuthUserSelectView
from src.components.widget_builder import WidgetBuilder, build
from src.database.api import ServerInfo


class AuthDialog(Adw.ApplicationWindow):
    __gtype_name__ = "MarmaladeAuthDialog"

    views: Adw.NavigationView

    server: ServerInfo

    @GObject.Signal(name="authenticated", arg_types=[str, str])
    def authenticated(self, _address: str, _user_id: str):
        """Signal emitted when the user is authenticated"""

    @GObject.Signal(name="cancelled")
    def cancelled(self):
        """Signal emitted when the login process is cancelled"""

    def __init_widget(self):
        self.views = build(WidgetBuilder(Adw.NavigationView))
        self.set_default_size(width=600, height=400)
        self.set_content(self.views)

    def __init__(
        self, application: Adw.Application, server: ServerInfo, **kwargs
    ) -> None:
        super().__init__(application=application, **kwargs)
        self.__init_widget()

        self.server = server

        # Create the login method / quick resume view
        view = AuthLoginMethodView(server=server)
        view.connect("chose-username-password", self.on_username_password_chosen)
        view.connect("chose-quick-connect", self.on_quick_connect_chosen)
        view.connect("authenticated", self.on_authenticated)
        view.connect("cancelled", self.on_cancelled)
        self.views.add(view)

    def on_cancelled(self, _widget) -> None:
        self.emit("cancelled")
        self.close()

    def on_quick_connect_chosen(self, _widget) -> None:
        view = AuthQuickConnectView(server=self.server)
        view.connect("authenticated", self.on_authenticated)
        self.views.push(view)

    def on_username_password_chosen(self, _widget) -> None:
        view = AuthUserSelectView(server=self.server)
        view.connect("user-picked", self.on_user_picked)
        view.connect("skipped", self.on_user_picked)
        self.views.push(view)

    def on_user_picked(self, _widget, user_id: str = ""):
        # Check if we have a token for that user
        token = shared.settings.get_token(address=self.server.address, user_id=user_id)
        if token is not None:
            self.on_authenticated(None, user_id)
            return
        # If not, display the credentials view
        user = shared.settings.get_user(address=self.server.address, user_id=user_id)
        username = "" if user is None else user.name
        view = AuthCredentialsView(server=self.server, username=username)
        view.connect("authenticated", self.on_authenticated)
        self.views.push(view)

    def on_authenticated(self, _widget, user_id: str) -> None:
        self.emit("authenticated", self.server.address, user_id)
        self.close()
