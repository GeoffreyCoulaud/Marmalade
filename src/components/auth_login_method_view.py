from gi.repository import Adw, GObject, Gtk

from src import build_constants, shared
from src.components.user_picker import UserPicker
from src.database.api import ServerInfo


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_login_method_view.ui"
)
class AuthLoginMethodView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthLoginMethodView"

    cancel_button = Gtk.Template.Child()
    username_password_button = Gtk.Template.Child()
    quick_connect_button = Gtk.Template.Child()
    auth_method_group = Gtk.Template.Child()
    user_picker: UserPicker = Gtk.Template.Child()

    __server: ServerInfo
    __dialog: Adw.Window

    @GObject.Signal(name="cancelled")
    def user_picked(self):
        """Signal emitted when the user cancels the login process"""

    @GObject.Signal(name="chose-username-password")
    def chose_username_password(self):
        """Signal emitted when the user chooses to log in via username and password"""

    @GObject.Signal(name="chose-quick-connect")
    def chose_quick_connect(self):
        """Signal emitted when the user chooses to log in via quick connect"""

    @GObject.Signal(name="authenticated", arg_types=[str])
    def authenticated(self, _user_id: str):
        """Signal emitted when a user is authenticated via quick resume"""

    def __init__(self, *args, dialog: Adw.Window, server: ServerInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__dialog = dialog
        self.__server = server
        self.user_picker.set_server(self.__server)

        self.cancel_button.connect("clicked", self.on_cancel_button_clicked)
        self.username_password_button.connect("clicked", self.on_credentials_clicked)
        self.quick_connect_button.connect("clicked", self.on_quick_connect_clicked)
        self.user_picker.connect("user-picked", self.on_quick_resume_picked)

        self.discover_authenticated_users()

    def discover_authenticated_users(self) -> None:
        """Discover the authenticated users and display them"""
        users = shared.settings.get_authenticated_users(self.__server.address)
        has_users = len(users) > 0
        self.user_picker.set_visible(has_users)
        if not has_users:
            return
        self.user_picker.clear()
        self.user_picker.append(*users)
        if self.user_picker.get_n_pages() > 1:
            self.auth_method_group.set_margin_start(48)
            self.auth_method_group.set_margin_end(48)

    def on_cancel_button_clicked(self, _button) -> None:
        self.emit("cancelled")

    def on_credentials_clicked(self, _button) -> None:
        self.emit("chose-username-password")

    def on_quick_connect_clicked(self, _button) -> None:
        self.emit("chose-quick-connect")

    def on_quick_resume_picked(self, _picker, user_id: str) -> None:
        self.emit("authenticated", user_id)
