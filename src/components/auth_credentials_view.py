import logging
from http import HTTPStatus

from gi.repository import Adw, GObject, Gtk
from jellyfin_api_client.api.user import authenticate_user_by_name
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.authenticate_user_by_name import AuthenticateUserByName
from jellyfin_api_client.models.authentication_result import AuthenticationResult

from src import build_constants, shared
from src.database.api import ServerInfo, UserInfo
from src.jellyfin import JellyfinClient
from src.task import Task


class InvalidCredentialsError(Exception):
    """Error raised when the user cannot be authenticated"""


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_credentials_view.ui"
)
class AuthCredentialsView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthCredentialsView"

    # fmt: off
    __log_in_button     = Gtk.Template.Child("log_in_button")
    __username_editable = Gtk.Template.Child("username_editable")
    __password_editable = Gtk.Template.Child("password_editable")
    __toast_overlay     = Gtk.Template.Child("toast_overlay")
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
        self.__log_in_button.connect("clicked", self.__on_log_in_request)

    def __on_log_in_request(self, _widget) -> None:
        """Try to authenticate the user with the given credentials"""

        def main(username: str, password: str) -> AuthenticationResult:
            client = JellyfinClient(self.__server.address)
            response = authenticate_user_by_name.sync_detailed(
                client=client,
                json_body=AuthenticateUserByName(username=username, pw=password),
            )
            if response.status_code == HTTPStatus.OK:
                return response.parsed
            if response.status_code == HTTPStatus.UNAUTHORIZED:
                raise InvalidCredentialsError()
            raise UnexpectedStatus(response.status_code, response.content)

        def on_success(result: AuthenticationResult) -> None:
            logging.debug(
                "Authenticated %s on %s", result.user.name, self.__server.address
            )
            self.__log_in_button.set_sensitive(True)
            shared.settings.add_users(
                self.__server.address,
                UserInfo(user_id=result.user.id, name=result.user.name),
            )
            shared.settings.add_active_token(
                self.__server.address,
                result.user.id,
                result.access_token,
            )
            self.emit("authenticated", result.user.id)

        def on_error(error: Exception):
            self.__log_in_button.set_sensitive(True)
            toast = Adw.Toast()
            match error:
                case InvalidCredentialsError():
                    logging.error("Invalid credentials")
                    toast.set_title(_("Invalid username or password"))
                case _:
                    logging.error("Credentials login error", exc_info=error)
                    toast.set_title(_("Autentication failed"))
                    toast.set_button_label(_("Details"))
                    toast.connect(
                        "button-clicked",
                        on_details,
                        _("Authentication Error"),
                        str(error),
                    )
            self.__toast_overlay.add_toast(toast)

        def on_details(_button, title: str, details: str) -> None:
            logging.debug("Credentials login error details requested")
            msg = Adw.MessageDialog()
            msg.add_response("close", _("Close"))
            msg.set_heading(title)
            msg.set_body(details)
            msg.set_transient_for(self.__dialog)
            msg.present()

        username = self.__username_editable.get_text()
        password = self.__password_editable.get_text()
        self.__log_in_button.set_sensitive(False)
        logging.debug("Authenticating %s on %s", username, self.__server.address)
        task = Task(
            main=main,
            main_args=(username, password),
            callback=on_success,
            error_callback=on_error,
        )
        task.run()

    def focus_password(self) -> None:
        """Focus the password row"""
        self.__password_editable.grab_focus_without_selecting()
