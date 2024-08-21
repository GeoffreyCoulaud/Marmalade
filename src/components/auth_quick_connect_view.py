import logging
from http import HTTPStatus
from operator import call
from typing import cast, no_type_check

from gi.repository import Adw, Gio, GLib, GObject, Gtk, Pango
from jellyfin_api_client.api.quick_connect import initiate_quick_connect
from jellyfin_api_client.api.user import authenticate_with_quick_connect
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.authentication_result import AuthenticationResult
from jellyfin_api_client.models.quick_connect_dto import QuickConnectDto
from jellyfin_api_client.models.quick_connect_result import QuickConnectResult

from src import shared
from src.components.widget_builder import Children, Handlers, Properties, WidgetBuilder
from src.database.api import ServerInfo, UserInfo
from src.jellyfin import JellyfinClient, make_device_id
from src.task import Task


class QuickConnectDisabledError(Exception):
    """Exception raised when quick connect is not enabled on the server"""


class UnauthorizedQuickConnect(Exception):
    """Exception raised when a quick connect secret is tried while not yet authorized"""


class AuthQuickConnectView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthQuickConnectView"

    __toast_overlay: Adw.ToastOverlay
    __refresh_button: Gtk.Button
    __connect_button: Gtk.Button

    # State stack containing the quick connect code
    # when everything goes as planned
    __state_view_stack: Adw.ViewStack
    __state_loading_view: Gtk.Spinner
    __state_error_view: Gtk.Image
    __state_ok_view: Gtk.Label

    __server: ServerInfo
    __secret: str
    __cancellable: Gio.Cancellable

    @GObject.Signal(name="authenticated", arg_types=[str])
    def authenticated(self, _user_id: str):
        """Signal emitted when the user is authenticated"""

    def __init_widget(self):
        self.__refresh_button = call(
            WidgetBuilder(Gtk.Button)
            | Handlers(clicked=self.on_refresh_requested)
            | Properties(icon_name="view-refresh-symbolic")
        )
        self.__connect_button = call(
            WidgetBuilder(Gtk.Button)
            | Handlers(clicked=self.on_connect_requested)
            | Properties(
                css_classes=["suggested-action"],
                label=_("Connect"),
                sensitive=False,
            )
        )
        self.__state_ok_view = call(
            WidgetBuilder(Gtk.Label)
            | Properties(
                css_classes=["title-1"],
                halign=Gtk.Align.CENTER,
                use_markup=True,
                selectable=True,
            )
        )
        self.__state_loading_view = call(
            WidgetBuilder(Gtk.Spinner)
            | Properties(
                spinning=True,
            )
        )
        self.__state_error_view = call(
            WidgetBuilder(Gtk.Image)
            | Properties(
                from_icon_name="computer-fail-symbolic",
                icon_size=Gtk.IconSize.LARGE,
            )
        )
        self.__state_view_stack = call(
            WidgetBuilder(Adw.ViewStack)
            | Properties(
                margin_top=32,
                margin_bottom=32,
                margin_start=32,
                margin_end=32,
            )
            | Children(
                self.__state_loading_view,
                self.__state_error_view,
                self.__state_ok_view,
            )
        )
        self.__toast_overlay = call(
            WidgetBuilder(Adw.ToastOverlay)
            | Children(
                WidgetBuilder(Adw.Clamp)
                | Properties(
                    margin_top=16,
                    margin_bottom=16,
                    margin_start=16,
                    margin_end=16,
                )
                | Children(
                    WidgetBuilder(Gtk.Box)
                    | Properties(orientation=Gtk.Orientation.VERTICAL)
                    | Children(
                        # Code state box
                        WidgetBuilder(Adw.Bin)
                        | Properties(
                            css_classes=["card", "view", "frame"],
                            margin_top=16,
                            margin_bottom=16,
                        )
                        | Children(self.__state_view_stack),
                        # Explaination title
                        WidgetBuilder(Gtk.Label)
                        | Properties(
                            css_classes=["heading"],
                            margin_bottom=8,
                            halign=Gtk.Align.START,
                            label=_("How to use quick connect?"),
                        ),
                        # Explaination
                        WidgetBuilder(Gtk.Label)
                        | Properties(
                            halign=Gtk.Align.START,
                            wrap=True,
                            wrap_mode=Pango.WrapMode.WORD_CHAR,
                            natural_wrap_mode=Gtk.WrapMode.WORD,
                            label=_(
                                "Quick connect permits logging into a new device without entering a password.\nUsing an already logged-in Jellyfin client, navigate to the settings to enter the quick connect code displayed above."
                            ),
                        ),
                    )
                ),
            )
        )
        self.set_title(_("Quick Connect"))
        self.set_tag("quick-connect")
        self.set_child(
            call(
                WidgetBuilder(Adw.ToolbarView)
                | Children(
                    # Header bar
                    WidgetBuilder(Adw.HeaderBar)
                    | Properties(decoration_layout="")
                    | Children(self.__refresh_button, None, self.__connect_button),
                    # Content
                    self.__toast_overlay,
                    # Bottom bar
                    None,
                )
            )
        )

    def __init__(self, *args, server: ServerInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__init_widget()

        self.__server = server
        self.__cancellable = Gio.Cancellable()
        self.__secret = ""

        self.on_refresh_requested(None)

    def on_refresh_requested(self, _button) -> None:
        logging.debug("Requested a new Quick Connect code")
        self.refresh()

    def refresh(self) -> None:
        def main() -> QuickConnectResult:
            client = JellyfinClient(base_url=self.__server.address)
            response = initiate_quick_connect.sync_detailed(client=client)
            if response.status_code == HTTPStatus.OK:
                return cast(QuickConnectResult, response.parsed)
            if HTTPStatus.UNAUTHORIZED:
                raise QuickConnectDisabledError()
            raise UnexpectedStatus(response.status_code, response.content)

        def on_success(result: QuickConnectResult):
            self.__secret = cast(str, result.secret)
            label_markup = f'<span size="xx-large">{result.code}</span>'
            self.__state_ok_view.set_label(label_markup)
            self.__state_view_stack.set_visible_child(self.__state_ok_view)
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
            self.__state_view_stack.set_visible_child(self.__state_error_view)

        self.__connect_button.set_sensitive(False)
        self.__cancellable.cancel()
        self.__cancellable.reset()
        self.__state_view_stack.set_visible_child(self.__state_loading_view)
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
                body=QuickConnectDto(secret=self.__secret),
            )
            if response.status_code == HTTPStatus.OK:
                return cast(AuthenticationResult, response.parsed)
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise UnauthorizedQuickConnect()
            raise UnexpectedStatus(response.status_code, response.content)

        @no_type_check
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
                self.__state_view_stack.set_visible_child(self.__state_error_view)
            self.__toast_overlay.add_toast(toast)

        self.__connect_button.set_sensitive(False)
        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
            return_on_cancel=True,
        )
        task.run()
