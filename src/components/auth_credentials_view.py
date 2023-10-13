import logging

from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.database.api import ServerInfo


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_credentials_view.ui"
)
class AuthCredentialsView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthCredentialsView"

    # fmt: off
    __log_in_button     = Gtk.Template.Child("log_in_button")
    __username_editable = Gtk.Template.Child("username_editable")
    __password_editable = Gtk.Template.Child("password_editable")
    # fmt: on

    __dialog: Adw.Window
    __server: ServerInfo

    @GObject.Signal(name="authenticated", arg_types=[str])
    def authenticated(self, _user_id: str):
        """Signal emitted when the user is authenticated"""

    def __init__(
        self, *args, dialog: Adw.Window, server: ServerInfo, username: str, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__server = server
        self.__dialog = dialog
        self.__username_editable.set_text(username)

    def focus_password(self) -> None:
        """Focus the password row"""
        self.__password_editable.grab_focus_without_selecting()

    def on_log_in_request(self, _widget) -> None:
        # TODO implement logging in with username and password
        # TODO add the user to the database if succeeds
        # TODO add the token to the database if succeeds
        pass
