import logging
from http import HTTPStatus

from gi.repository import Adw, Gio, GLib, GObject, Gtk
from jellyfin_api_client.api.quick_connect import initiate as initiate_quick_connect
from jellyfin_api_client.api.user import authenticate_with_quick_connect
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.authentication_result import AuthenticationResult
from jellyfin_api_client.models.quick_connect_dto import QuickConnectDto
from jellyfin_api_client.models.quick_connect_result import QuickConnectResult

from src import build_constants, shared
from src.database.api import ServerInfo, UserInfo
from src.jellyfin import JellyfinClient, make_device_id
from src.task import Task


class QuickConnectDisabledError(Exception):
    """Exception raised when quick connect is not enabled on the server"""


class UnauthorizedQuickConnect(Exception):
    """Exception raised when a quick connect secret is tried while not yet authorized"""


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_quick_connect_view.ui"
)
class AuthQuickConnectView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthQuickConnectView"

    # fmt: off
    __refresh_button   = Gtk.Template.Child("refresh_button")
    __connect_button   = Gtk.Template.Child("connect_button")
    __toast_overlay    = Gtk.Template.Child("toast_overlay")
    __code_state_stack = Gtk.Template.Child("code_state_stack")
    __code_label       = Gtk.Template.Child("code_label")
    # fmt: on

    __dialog: Adw.ApplicationWindow
    __server: ServerInfo
    __secret: str
    __cancellable: Gio.Cancellable

    @GObject.Signal(name="authenticated", arg_types=[str])
    def authenticated(self, _user_id: str):
        """Signal emitted when the user is authenticated"""

    def __init__(
        self, *args, dialog: Adw.ApplicationWindow, server: ServerInfo, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__dialog = dialog
        self.__server = server
        self.__cancellable = Gio.Cancellable()
        self.__secret = ""
        self.__refresh_button.connect("clicked", self.on_refresh_requested)
        self.__connect_button.connect("clicked", self.on_connect_requested)
        self.on_refresh_requested(None)

    def on_refresh_requested(self, _button) -> None:
        logging.debug("Requested a new Quick Connect code")
        self.refresh()

    def refresh(self) -> None:
        def main() -> QuickConnectResult:
            client = JellyfinClient(base_url=self.__server.address)
            response = initiate_quick_connect.sync_detailed(client=client)
            if response.status_code == HTTPStatus.OK:
                return response.parsed
            if HTTPStatus.UNAUTHORIZED:
                raise QuickConnectDisabledError()
            raise UnexpectedStatus(response.status_code, response.content)

        def on_success(result: QuickConnectResult):
            self.__secret = result.secret
            label_markup = f'<span size="xx-large">{result.code}</span>'
            self.__code_label.set_label(label_markup)
            self.__code_state_stack.set_visible_child_name("code")
            self.__connect_button.set_sensitive(True)

        def on_error(error: UnexpectedStatus | QuickConnectDisabledError):
            toast = Adw.Toast()
            toast.set_timeout(0)
            if isinstance(error, QuickConnectDisabledError):
                logging.error("Quick connect is not enabled")
                toast.set_title(_("Quick Connect is not enabled on this server"))
            else:
                logging.error("Unexpected Quick Connect error", exc_info=error)
                toast.set_title(_("An unexpected error occured"))
                toast.set_button_label(_("Details"))
                toast.set_action_name("app.error-details")
                toast.set_action_target_value(
                    GLib.Variant.new_strv([_("Quick Connect Error"), str(error)])
                )
            self.__toast_overlay.add_toast(toast)
            self.__code_state_stack.set_visible_child_name("error")

        self.__connect_button.set_sensitive(False)
        self.__cancellable.cancel()
        self.__cancellable.reset()
        self.__code_state_stack.set_visible_child_name("loading")
        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
            cancellable=self.__cancellable,
            return_on_cancel=True,
        )
        task.run()

    def on_connect_requested(self, _widget) -> None:
        """Try to authenticate with the server"""

        def main() -> AuthenticationResult:
            device_id = make_device_id()
            client = JellyfinClient(base_url=self.__server.address, device_id=device_id)
            response = authenticate_with_quick_connect.sync_detailed(
                client=client,
                json_body=QuickConnectDto(secret=self.__secret),
            )
            if response.status_code == HTTPStatus.OK:
                return response.parsed
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise UnauthorizedQuickConnect()
            raise UnexpectedStatus(response.status_code, response.content)

        def on_success(result: AuthenticationResult) -> None:
            logging.debug("Authenticated via quick connect")
            user_info = UserInfo(user_id=result.user.id, name=result.user.name)
            shared.settings.add_users(self.__server.address, user_info)
            shared.settings.add_token(
                address=self.__server.address,
                user_id=result.user.id,
                token=result.access_token,
                device_id=result.session_info.device_id,
            )
            self.emit("authenticated", result.user.id)

        def on_error(error: Exception) -> None:
            toast = Adw.Toast()
            if isinstance(error, UnauthorizedQuickConnect):
                logging.error("Quick connect not authorized yet")
                toast.set_title(_("Code hasn't been verified yet"))
                self.__connect_button.set_sensitive(True)
            else:
                toast.set_timeout(0)
                logging.error("Unexpected Quick Connect error", exc_info=error)
                toast.set_title(_("An unexpected error occured"))
                toast.set_button_label(_("Details"))
                toast.set_action_name("app.error-details")
                toast.set_action_target_value(
                    GLib.Variant.new_strv([_("Quick Connect Error"), str(error)])
                )
                self.__code_state_stack.set_visible_child_name("error")
            self.__toast_overlay.add_toast(toast)

        self.__connect_button.set_sensitive(False)
        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
            return_on_cancel=True,
        )
        task.run()
