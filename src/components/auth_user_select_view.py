import logging
from http import HTTPStatus
from typing import cast

from gi.repository import Adw, GObject, Gtk
from httpx import TimeoutException
from jellyfin_api_client.api.user import get_public_users
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models import UserDto

from src import shared
from src.components.loading_view import LoadingView
from src.components.user_picker import UserPicker
from src.components.widget_builder import (
    Children,
    Handlers,
    Properties,
    WidgetBuilder,
    build,
)
from src.database.api import ServerInfo, UserInfo
from src.jellyfin import JellyfinClient
from src.task import Task


class NoPublicUsers(Exception):
    """Error raised when the server doesn't provide public users"""


class AuthUserSelectView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthUserSelectView"

    __user_picker_view_stack: Adw.ViewStack
    __user_picker_error_status: Adw.StatusPage
    __user_picker_loading_status: LoadingView
    __user_picker: UserPicker
    __other_user_button: Gtk.Button

    server: ServerInfo

    @GObject.Signal(name="user-picked", arg_types=[str])
    def user_picked(self, _user_id: str):
        """Signal emitted when a user is picked"""

    @GObject.Signal(name="skipped")
    def skipped(self):
        """Signal emitted when the other user button is clicked"""

    def __init_widget(self) -> None:
        self.__user_picker = build(
            UserPicker
            + Handlers(user_picked=self.__on_user_picked)
            + Properties(columns=4, lines=2)
        )
        self.__other_user_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_other_user_button_clicked)
            + Properties(
                css_classes=["pill"],
                halign=Gtk.Align.CENTER,
                label=_("Log in as another user"),
            )
        )
        self.__user_picker_error_status = build(
            Adw.StatusPage
            + Properties(
                css_classes=["compact"],
                icon_name="user-info-symbolic",
                title=_("Couldn't Obtain Users"),
                description=_(
                    "An error occured when getting the public users from the servers"
                ),
            )
        )
        self.__user_picker_loading_status = build(WidgetBuilder(LoadingView))
        self.__user_picker_view_stack = build(
            Adw.ViewStack
            + Children(
                self.__user_picker_loading_status,
                self.__user_picker_error_status,
                self.__user_picker,
            )
        )
        self.set_title(_("User Selection"))
        self.set_tag("user-selection")
        self.set_child(
            build(
                Adw.ToolbarView
                + Children(
                    # Header bar
                    Adw.HeaderBar + Properties(decoration_layout=""),
                    # Content
                    Adw.Clamp
                    + Properties(
                        margin_top=16,
                        margin_bottom=16,
                        margin_start=16,
                        margin_end=16,
                    )
                    + Children(
                        Gtk.Box
                        + Properties(
                            orientation=Gtk.Orientation.VERTICAL,
                            spacing=24,
                        )
                        + Children(
                            self.__user_picker_view_stack,
                            self.__other_user_button,
                        )
                    ),
                    # No bottom bar
                    None,
                )
            )
        )

    def __init__(self, *args, server: ServerInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__init_widget()

        self.server = server
        self.__user_picker.set_server(self.server)

        self.discover_users()

    def discover_users(self) -> None:
        """Discover users from the server asynchronously"""

        def main() -> list[UserInfo]:
            # Get a list of public users
            client = JellyfinClient(self.server.address)
            response = get_public_users.sync_detailed(client=client)
            if response.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(response.status_code, response.content)
            user_dtos = cast(list[UserDto], response.parsed)
            if len(user_dtos) == 0:
                raise NoPublicUsers()
            public = [
                UserInfo(
                    user_id=cast(str, dto.id),
                    name=cast(str, dto.name),
                )
                for dto in user_dtos
            ]

            # Add public users to the database
            shared.settings.add_users(self.server.address, *public)

            # Order the authenticated users first
            others = []
            authenticated = shared.settings.get_authenticated_users(self.server.address)
            authenticated_set = set(authenticated)
            for user in public:
                if user in authenticated_set:
                    continue
                others.append(user)
            authenticated.extend(others)
            return authenticated

        def on_success(users: list[UserInfo]) -> None:
            self.__user_picker.append(*users)
            self.__user_picker_view_stack.set_visible_child(self.__user_picker)

        def on_error(error: Exception) -> None:
            match error:
                case UnexpectedStatus():
                    logging.error("Couldn't discover users", exc_info=error)
                    pass
                case NoPublicUsers():
                    logging.debug("%s has no public users", self.server.name)
                    message = _("This server doesn't provide a list of public users")
                    self.__user_picker_error_status.set_description(message)
                case TimeoutException():
                    logging.error(
                        "%s (%s) timed out",
                        self.server.name,
                        self.server.address,
                    )
                    message = _("Server timed out")
                    self.__user_picker_error_status.set_description(message)
            self.__user_picker_view_stack.set_visible_child(
                self.__user_picker_error_status
            )

        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
        )
        task.run()

    def __on_user_picked(self, _picker, user_id: str) -> None:
        self.emit("user-picked", user_id)

    def __on_other_user_button_clicked(self, _widget) -> None:
        self.emit("skipped")
