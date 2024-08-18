import logging
from http import HTTPStatus

from gi.repository import Adw, GLib, GObject, Gtk
from jellyfin_api_client.api.user import authenticate_user_by_name
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.authenticate_user_by_name import AuthenticateUserByName
from jellyfin_api_client.models.authentication_result import AuthenticationResult

from src import shared
from src.components.widget_factory import WidgetFactory
from src.database.api import ServerInfo, UserInfo
from src.jellyfin import JellyfinClient, make_device_id
from src.task import Task


class InvalidCredentialsError(Exception):
    """Error raised when the user cannot be authenticated"""


class AuthCredentialsView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthCredentialsView"

    __log_in_button: Gtk.Button
    __username_editable: Adw.EntryRow
    __password_editable: Adw.EntryRow
    __toast_overlay: Adw.ToastOverlay

    __dialog: Adw.Window  # TODO remove if unused
    __server: ServerInfo

    @GObject.Signal(name="authenticated", arg_types=[str])
    def authenticated(self, _user_id: str):
        """Signal emitted when the user is authenticated"""

    def __init_widget(self):
        self.__log_in_button = WidgetFactory(
            klass=Gtk.Button,
            properties={"css_classes": "suggested-action", "label": _("Log In")},
        )
        self.__username_editable = WidgetFactory(
            klass=Adw.EntryRow,
            properties={"title": _("Username")},
        )
        self.__password_editable = WidgetFactory(
            klass=Adw.EntryRow,
            properties={"title": _("Password")},
        )
        self.__toast_overlay = WidgetFactory(
            klass=Adw.ToastOverlay,
            children=WidgetFactory(
                klass=Adw.Clamp,
                properties={
                    "margin_top": 16,
                    "margin_bottom": 16,
                    "margin_start": 16,
                    "margin_end": 16,
                },
                children=WidgetFactory(
                    klass=Adw.PreferencesGroup,
                    children=[
                        self.__username_editable,
                        self.__password_editable,
                    ],
                ),
            ),
        )
        self.set_title(_("Credentials"))
        self.set_tag("credentials")
        self.set_child(
            WidgetFactory(
                klass=Adw.ToolbarView,
                children=[
                    WidgetFactory(
                        klass=Adw.HeaderBar,
                        properties={"decoration_layout": ""},
                        children=[None, None, self.__log_in_button],
                    ),
                    self.__toast_overlay,
                    None,
                ],
            )
        )

    def __init__(
        self, *args, dialog: Adw.Window, server: ServerInfo, username: str, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__init_widget()
        self.__server = server
        self.__dialog = dialog
        self.__username_editable.set_text(username)
        self.__log_in_button.connect("clicked", self.__on_log_in_request)
        self.connect("map", self.__on_mapped)

    def __on_mapped(self, _page) -> None:
        """Callback executed when the page is about to be shown"""
        if self.__username_editable.get_text():
            self.__password_editable.grab_focus_without_selecting()

    def __on_log_in_request(self, _widget) -> None:
        """Try to authenticate the user with the given credentials"""

        def main(username: str, password: str) -> AuthenticationResult:
            device_id = make_device_id()
            client = JellyfinClient(base_url=self.__server.address, device_id=device_id)
            response = authenticate_user_by_name.sync_detailed(
                client=client,
                json_body=AuthenticateUserByName(username=username, pw=password),  # type: ignore
            )
            if response.status_code == HTTPStatus.OK:
                return response.parsed
            if response.status_code == HTTPStatus.UNAUTHORIZED:
                raise InvalidCredentialsError()
            raise UnexpectedStatus(response.status_code, response.content)

        def on_success(result: AuthenticationResult) -> None:
            logging.debug(
                "Authenticated %s on %s",
                result.user.name,  # type: ignore
                self.__server.address,
            )
            self.__log_in_button.set_sensitive(True)
            shared.settings.add_users(
                self.__server.address,
                UserInfo(
                    user_id=result.user.id,  # type: ignore
                    name=result.user.name,  # type: ignore
                ),
            )
            shared.settings.add_token(
                address=self.__server.address,
                user_id=result.user.id,  # type: ignore
                token=result.access_token,  # type: ignore
                device_id=result.session_info.device_id,  # type: ignore
            )
            self.emit(
                "authenticated",
                result.user.id,  # type: ignore
            )

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
                    toast.set_action_name("app.error-details")
                    toast.set_action_target_value(
                        GLib.Variant.new_strv([_("Authentication Error"), str(error)])
                    )
            self.__toast_overlay.add_toast(toast)

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
