from gi.repository import Adw, GObject, Gtk

from src import build_constants


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_login_method_view.ui"
)
class AuthLoginMethodView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthLoginMethodView"

    cancel_button = Gtk.Template.Child()
    username_password_button = Gtk.Template.Child()
    quick_connect_button = Gtk.Template.Child()

    dialog: Adw.Window

    @GObject.Signal(name="cancelled")
    def user_picked(self):
        """Signal emitted when the user cancels the login process"""

    @GObject.Signal(name="chose-username-password")
    def chose_username_password(self):
        """Signal emitted when the user chooses to log in via username and password"""

    @GObject.Signal(name="chose-quick-connect")
    def chose_quick_connect(self):
        """Signal emitted when the user chooses to log in via quick connect"""

    def __init__(self, *args, dialog: Adw.Window, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.dialog = dialog
        self.cancel_button.connect("clicked", self.on_cancel_button_clicked)
        self.username_password_button.connect(
            "clicked", self.on_username_password_button_clicked
        )
        self.quick_connect_button.connect(
            "clicked", self.on_quick_connect_button_clicked
        )

    def on_cancel_button_clicked(self, _button) -> None:
        self.emit("cancelled")

    def on_username_password_button_clicked(self, _button) -> None:
        self.emit("chose-username-password")

    def on_quick_connect_button_clicked(self, _button) -> None:
        self.emit("chose-quick-connect")
