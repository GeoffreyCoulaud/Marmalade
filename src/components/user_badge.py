import logging
from http import HTTPStatus
from http.client import HTTPException
from pathlib import Path

from gi.repository import Adw, GObject, Gtk
from jellyfin_api_client.models.user_dto import UserDto

from src import build_constants, shared
from src.database.api import ServerInfo
from src.jellyfin import JellyfinClient
from src.task import Task


class ImageDownloadError(HTTPException):
    """Error raised when a user image cannot be downloaded"""

    status: HTTPStatus
    message: str

    def __init__(self, *args: object, status: HTTPStatus, message: str) -> None:
        super().__init__(*args)
        self.status = status
        self.message = message

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.status}\n{self.message}"


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/user_badge.ui")
class UserBadge(Adw.Bin):
    __gtype_name__ = "MarmaladeUserBadge"

    button = Gtk.Template.Child()
    avatar = Gtk.Template.Child()
    label = Gtk.Template.Child()

    image_dir: Path
    image_path: Path
    image_size: tuple[int, int] = (128, 128)

    server: ServerInfo
    user: UserDto

    @GObject.Signal(name="clicked")
    def user_picked(self):
        """Signal emitted when the widget is clicked"""

    def __init__(self, *args, server: ServerInfo, user: UserDto, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        self.user = user
        self.image_dir = (
            shared.app_cache_dir
            / "servers"
            / self.server.server_id
            / "users"
            / self.user.id
            / "images"
        )
        self.image_path = self.image_dir / "profile.png"
        self.label.set_label(user.name)
        self.avatar.set_text(user.name)
        self.button.connect("clicked", self.on_button_clicked)
        self.load_image()

    def on_button_clicked(self, _button):
        self.emit("clicked", self.user.name, self.user.id)

    def load_image(self) -> None:
        """
        Load the user image from disk or from the server.

        - If the image is on disk, will use it
        - Else downloads from the server and uses that (unless an error happened)
        """

        def download_image():
            client = JellyfinClient(base_url=self.server.address).get_httpx_client()
            url = f"/Users/{self.user.id}/Images/Profile"
            params = {
                "tag": self.user.primary_image_tag,
                "format": "Png",
                "width": self.image_size[0],
                "height": self.image_size[1],
            }
            response = client.get(url, params=params)
            if response.status_code != HTTPStatus.OK:
                raise ImageDownloadError(
                    status=response.status_code,
                    message=str(response.content),
                )
            self.image_dir.mkdir(parents=True, exist_ok=True)
            with self.image_path.open("wb") as file:
                file.write(response.content)

        def on_error(error: Exception):
            logging.debug(
                "Couldn't download %s's profile image",
                self.user.name,
                exc_info=error,
            )

        def on_success():
            picture = Gtk.Picture.new_for_filename(str(self.image_path))
            self.avatar.set_custom_image(picture)

        # Use the local image if present
        if self.image_path.is_file():
            on_success()
            return

        # Download the image asynchronously
        task = Task(
            main=download_image,
            callback=on_success,
            error_callback=on_error,
        )
        task.run()
