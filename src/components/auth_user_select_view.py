import logging
import time
from http import HTTPStatus

from gi.repository import Adw, GObject, Gtk
from httpx import TimeoutException
from jellyfin_api_client.api.user import get_public_users
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.user_dto import UserDto

from src import build_constants
from src.components.user_picker import UserPicker
from src.database.api import ServerInfo
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
    user_picker_bin = Gtk.Template.Child()

    other_user_button = Gtk.Template.Child()

    dialog: Adw.Window
    server: ServerInfo

    @GObject.Signal(name="user-picked", arg_types=[str, str])
    def user_picked(self, _username: str, _user_id: str):
        """Signal emitted when a user is picked"""

    @GObject.Signal(name="skipped")
    def skipped(self):
        """Signal emitted when the other user button is clicked"""

    def __init__(self, *args, dialog: Adw.Window, server: ServerInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.dialog = dialog
        self.server = server
        self.other_user_button.connect("clicked", self.on_other_user_button_clicked)
        self.discover_users()

    def discover_users(self) -> None:
        """Discover users from the server asynchronously"""

        def main() -> list[UserDto]:
            client = JellyfinClient(self.server.address)
            response = get_public_users.sync_detailed(client=client)
            if response.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(response.status_code, response.content)
            # TODO get public users from the server
            return response.parsed

        def on_success(users: list[UserDto]) -> None:
            picker = UserPicker(server=self.server, users=users)
            picker.connect("user-picked", self.on_user_picked)
            self.user_picker_bin.set_child(picker)
            self.user_picker_view_stack.set_visible_child_name("users")

        def on_error(error: Exception) -> None:
            logging.error("Couldn't discover users", exc_info=error)
            match error:
                case UnexpectedStatus():
                    pass
                case NoPublicUsers():
                    message = _("Server doesn't provide a list of public users")
                    self.user_picker_error_status.set_description(message)
                case TimeoutException():
                    message = _("Server timed out")
                    self.user_picker_error_status.set_description(message)
            self.user_picker_view_stack.set_visible_child_name("error")

        task = Task(
            main=main,
            callback=on_success,
            error_callback=on_error,
        )
        task.run()

    def on_user_picked(self, _picker, username: str, user_id: str) -> None:
        self.emit("user-picked", username, user_id)

    def on_other_user_button_clicked(self, _widget) -> None:
        self.emit("skipped")
