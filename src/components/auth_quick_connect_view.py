import logging
from http import HTTPStatus

from gi.repository import Adw, Gio, GObject, Gtk
from jellyfin_api_client.api.quick_connect import initiate as initiate_quick_connect
from jellyfin_api_client.api.user import authenticate_with_quick_connect
from jellyfin_api_client.client import Client as JfClient
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.quick_connect_result import QuickConnectResult

from src import build_constants
from src.server import Server
from src.task import Task


class QuickConnectDisabledError(Exception):
    """Exception raised when quick connect is not enabled on the server"""


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
    server: Server
    __secret: str
    __cancellable: Gio.Cancellable

    @GObject.Signal(name="authenticated", arg_types=[object, str, str])
    def authenticated(self, _server: Server, _user_id: str, _token: str):
        """Signal emitted when the user is authenticated"""

    def __init__(self, *args, dialog: Adw.Window, server: Server, **kwargs) -> None:
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
        def main(server: Server) -> QuickConnectResult:
            auth_data = {
                "Client": "Marmalade",
                "Version": "1.9.1",
                # TODO get device name
                "Device": "Dummy device :)",
                # TODO generate or get DeviceId
                "DeviceId": "me-dummy",
            }
            auth_data_list = [f'{key}="{value}"' for key, value in auth_data.items()]
            auth_header = "MediaBrowser " + ", ".join(auth_data_list)
            client = JfClient(
                base_url=server.address,
                headers={
                    "X-Emby-Authorization": auth_header,
                },
                raise_on_unexpected_status=True,
            )
            response = initiate_quick_connect.sync_detailed(client=client)
            if response.status_code == HTTPStatus.OK:
                return response.parsed
            if HTTPStatus.UNAUTHORIZED:
                raise QuickConnectDisabledError()

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
            if isinstance(error, UnexpectedStatus):
                logging.error("Unexpected Quick Connect error", exc_info=error)
                toast.set_title(_("An unexpected error occured"))
                toast.set_button_label(_("Details"))
                toast.connect(
                    "button-clicked",
                    self.on_error_details_requested,
                    _("Unexpected Quick Connect Error"),
                    str(error),
                )
            self.toast_overlay.add_toast(toast)
            self.code_state_stack.set_visible_child_name("error")
            self.connect_button.set_sensitive(False)

        self.__cancellable.cancel()
        self.__cancellable.reset()
        self.code_state_stack.set_visible_child_name("loading")
        refresh_task = Task(
            main=main,
            main_args=(self.server,),
            callback=on_success,
            error_callback=on_error,
            cancellable=self.__cancellable,
            return_on_cancel=True,
        )
        refresh_task.run()

    def on_error_details_requested(self, _widget, title: str, details: str) -> None:
        logging.debug("Quick Connect error details requested")
        msg = Adw.MessageDialog()
        msg.add_response("close", _("Close"))
        msg.set_heading(title)
        msg.set_body(details)
        msg.set_transient_for(self.dialog)
        msg.present()

    def on_connect_requested(self, _widget) -> None:
        # TODO implement trying to connect with a quick connect code
        print(self.__secret)
