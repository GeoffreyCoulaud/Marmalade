import logging
from http import HTTPStatus

from gi.repository import Adw, Gio, GObject, Gtk
from jellyfin_api_client.api.quick_connect import initiate as initiate_quick_connect
from jellyfin_api_client.api.user import authenticate_with_quick_connect
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.quick_connect_dto import QuickConnectDto
from jellyfin_api_client.models.quick_connect_result import QuickConnectResult

from src import build_constants, shared
from src.database.api import ServerInfo
from src.jellyfin import JellyfinClient
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

    refresh_button = Gtk.Template.Child()
    connect_button = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()
    code_state_stack = Gtk.Template.Child()
    code_label = Gtk.Template.Child()

    dialog: Adw.Window
    server: ServerInfo
    __secret: str
    __cancellable: Gio.Cancellable

    @GObject.Signal(name="authenticated", arg_types=[str])
    def authenticated(self, _user_id: str):
        """Signal emitted when the user is authenticated"""

    def __init__(self, *args, dialog: Adw.Window, server: ServerInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.dialog = dialog
        self.server = server
        self.refresh_button.connect("clicked", self.on_refresh_requested)
        self.connect_button.connect("clicked", self.on_connect_requested)
        self.__cancellable = Gio.Cancellable()
        self.__secret = ""
        self.on_refresh_requested(None)

    def on_refresh_requested(self, _button) -> None:
        logging.debug("Requested a new Quick Connect code")
        self.refresh()

    def refresh(self) -> None:
        def main() -> QuickConnectResult:
            client = JellyfinClient(base_url=self.server.address)
            response = initiate_quick_connect.sync_detailed(client=client)
            if response.status_code == HTTPStatus.OK:
                return response.parsed
            if HTTPStatus.UNAUTHORIZED:
                raise QuickConnectDisabledError()
            raise UnexpectedStatus(response.status_code, response.content)

        def on_success(result: QuickConnectResult):
            self.__secret = result.secret
            label_markup = f'<span size="xx-large">{result.code}</span>'
            self.code_label.set_label(label_markup)
            self.code_state_stack.set_visible_child_name("code")
            self.connect_button.set_sensitive(True)

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
                args = (_("Unexpected Quick Connect Error"), str(error))
                toast.connect("button-clicked", self.on_error_details, *args)
            self.toast_overlay.add_toast(toast)
            self.code_state_stack.set_visible_child_name("error")
            self.connect_button.set_sensitive(False)

        self.__cancellable.cancel()
        self.__cancellable.reset()
        self.code_state_stack.set_visible_child_name("loading")
        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
            cancellable=self.__cancellable,
            return_on_cancel=True,
        )
        task.run()

    def on_error_details(self, _widget, title: str, details: str) -> None:
        logging.debug("Quick Connect error details requested")
        msg = Adw.MessageDialog()
        msg.add_response("close", _("Close"))
        msg.set_heading(title)
        msg.set_body(details)
        msg.set_transient_for(self.dialog)
        msg.present()

    def on_connect_requested(self, _widget) -> None:
        def main() -> tuple[str, str]:
            client = JellyfinClient(base_url=self.server.address)
            response = authenticate_with_quick_connect.sync_detailed(
                client=client,
                json_body=QuickConnectDto(secret=self.__secret),
            )
            if response.status_code == HTTPStatus.OK:
                return (response.parsed.user.id, response.parsed.access_token)
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise UnauthorizedQuickConnect()
            else:
                raise UnexpectedStatus(response.status_code)

        def on_success(result: tuple[str, str]) -> None:
            logging.debug("Authenticated via quick connect")
            user_id, token = result
            shared.settings.add_active_token(
                address=self.server.address,
                user_id=user_id,
                token=token,
            )
            self.emit("authenticated", user_id)

        def on_error(error: Exception) -> None:
            toast = Adw.Toast()
            if isinstance(error, UnauthorizedQuickConnect):
                logging.error("Quick connect not authorized yet")
                toast.set_title(_("Code hasn't been verified yet"))
            else:
                toast.set_timeout(0)
                logging.error("Unexpected Quick Connect error", exc_info=error)
                toast.set_title(_("An unexpected error occured"))
                toast.set_button_label(_("Details"))
                args = (_("Unexpected Quick Connect Error"), str(error))
                toast.connect("button-clicked", self.on_error_details, *args)
                self.code_state_stack.set_visible_child_name("error")
                self.connect_button.set_sensitive(False)
            self.toast_overlay.add_toast(toast)

        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
            return_on_cancel=True,
        )
        task.run()
