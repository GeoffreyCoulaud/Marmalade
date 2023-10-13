import logging
import time
from http import HTTPStatus

from gi.repository import Adw, GObject, Gtk
from httpx import TimeoutException
from jellyfin_api_client.api.user import get_public_users
from jellyfin_api_client.errors import UnexpectedStatus

from src import build_constants, shared
from src.components.user_picker import UserPicker
from src.database.api import ServerInfo, UserInfo
from src.jellyfin import JellyfinClient
from src.task import Task


class NoPublicUsers(Exception):
    """Error raised when the server doesn't provide public users"""


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_user_select_view.ui"
)
class AuthUserSelectView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthUserSelectView"

    user_picker_view_stack = Gtk.Template.Child()
    user_picker_error_status = Gtk.Template.Child()
    user_picker: UserPicker = Gtk.Template.Child()

    other_user_button = Gtk.Template.Child()

    dialog: Adw.Window
    server: ServerInfo

    @GObject.Signal(name="user-picked", arg_types=[str])
    def user_picked(self, _user_id: str):
        """Signal emitted when a user is picked"""

    @GObject.Signal(name="skipped")
    def skipped(self):
        """Signal emitted when the other user button is clicked"""

    def __init__(self, *args, dialog: Adw.Window, server: ServerInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.dialog = dialog
        self.server = server
        self.user_picker.set_server(self.server)
        self.user_picker.connect("user-picked", self.on_user_picked)
        self.other_user_button.connect("clicked", self.on_other_user_button_clicked)
        self.discover_users()

    def discover_users(self) -> None:
        """Discover users from the server asynchronously"""

        def main() -> list[UserInfo]:
            # Get a list of public users
            client = JellyfinClient(self.server.address)
            response = get_public_users.sync_detailed(client=client)
            if response.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(response.status_code, response.content)
            user_dtos = response.parsed
            if len(user_dtos) == 0:
                raise NoPublicUsers()
            public = [UserInfo(user_id=dto.id, name=dto.name) for dto in user_dtos]

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
            self.user_picker.clear()
            self.user_picker.append(*users)
            self.user_picker_view_stack.set_visible_child_name("users")

        def on_error(error: Exception) -> None:
            match error:
                case UnexpectedStatus():
                    logging.error("Couldn't discover users", exc_info=error)
                    pass
                case NoPublicUsers():
                    logging.debug("%s has no public users", self.server.name)
                    message = _("This server doesn't provide a list of public users")
                    self.user_picker_error_status.set_description(message)
                case TimeoutException():
                    logging.error(
                        "%s (%s) timed out",
                        self.server.name,
                        self.server.address,
                    )
                    message = _("Server timed out")
                    self.user_picker_error_status.set_description(message)
            self.user_picker_view_stack.set_visible_child_name("error")

        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
        )
        task.run()

    def on_user_picked(self, _picker, user_id: str) -> None:
        self.emit("user-picked", user_id)

    def on_other_user_button_clicked(self, _widget) -> None:
        self.emit("skipped")
