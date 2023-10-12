import logging
from http import HTTPStatus
from http.client import HTTPException
from pathlib import Path

from gi.repository import Adw, GObject, Gtk
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.user_dto import UserDto

from src import build_constants, shared
from src.database.api import ServerInfo
from src.jellyfin import JellyfinClient
from src.task import Task


class ImageDownloadError(UnexpectedStatus):
    """Error raised when a user image cannot be downloaded"""


class NoUserImageError(ImageDownloadError):
    """Error raised when a user has no image"""


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
        self.avatar.set_size(self.image_size[0])
        self.button.connect("clicked", self.on_button_clicked)
        self.load_image()

    def on_button_clicked(self, _button):
        self.emit("clicked")

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
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise NoUserImageError(
                    status_code=response.status_code,
                    content=response.content,
                )
            elif response.status_code != HTTPStatus.OK:
                raise ImageDownloadError(
                    status_code=response.status_code,
                    content=response.content,
                )
            self.image_dir.mkdir(parents=True, exist_ok=True)
            with self.image_path.open("wb") as file:
                file.write(response.content)
            return

        def on_error(error: Exception):
            match error:
                case NoUserImageError():
                    logging.debug("%s has no user image", self.user.name)
                case _:
                    logging.debug(
                        "Couldn't download %s's profile image",
                        self.user.name,
                        exc_info=error,
                    )

        def on_success():
            picture = Gtk.Picture.new_for_filename(str(self.image_path))
            paintable = picture.get_paintable()
            self.avatar.set_custom_image(paintable)

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
