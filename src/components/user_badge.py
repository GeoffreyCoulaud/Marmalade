import logging
from http import HTTPStatus
from pathlib import Path

from gi.repository import Adw, GObject, Gtk
from jellyfin_api_client.errors import UnexpectedStatus

from src import build_constants, shared
from src.database.api import ServerInfo, UserInfo
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
    image_size: int

    server: ServerInfo
    user: UserInfo

    @GObject.Signal(name="clicked")
    def user_picked(self):
        """Signal emitted when the widget is clicked"""

    def __init__(self, *args, server: ServerInfo, user: UserInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        self.user = user
        self.image_dir = (
            shared.app_cache_dir
            / "servers"
            / self.server.server_id
            / "users"
            / self.user.user_id
            / "images"
        )
        self.image_path = self.image_dir / "profile.png"
        self.image_size = self.avatar.get_size()
        self.label.set_label(user.name)
        self.avatar.set_text(user.name)
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
            client = JellyfinClient(base_url=self.server.address, device_id="").get_httpx_client()
            url = f"/Users/{self.user.user_id}/Images/Profile"
            params = {
                "format": "Png",
                "width": self.image_size,
                # "height": self.image_size,
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

        def on_success(_result=None):
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
