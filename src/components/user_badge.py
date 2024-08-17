import logging
from http import HTTPStatus
from pathlib import Path

from gi.repository import Adw, GObject, Gtk  # type: ignore
from jellyfin_api_client.errors import UnexpectedStatus

from src import shared
from src.components.utils import widget_factory
from src.database.api import ServerInfo, UserInfo
from src.jellyfin import JellyfinClient
from src.task import Task


class ImageDownloadError(UnexpectedStatus):
    """Error raised when a user image cannot be downloaded"""


class NoUserImageError(ImageDownloadError):
    """Error raised when a user has no image"""


class UserBadge(Adw.Bin):
    __gtype_name__ = "MarmaladeUserBadge"

    __button: Gtk.Button
    __avatar: Adw.Avatar
    __label: Gtk.Label

    __image_dir: Path
    __image_path: Path
    __image_size: int

    __server: ServerInfo
    __user: UserInfo

    @GObject.Signal(name="clicked")
    def clicked_signal(self, *_args):
        """Signal emitted when the widget is clicked"""

    def __init_widget(self) -> None:
        """Create the widget structure"""

        self.__avatar = widget_factory(
            klass=Adw.Avatar,
            properties={
                "icon_name": "avatar-default-symbolic",
                "valign": Gtk.Align.CENTER,
                "margin_bottom": 8,
                "size": 128,
            },
        )
        self.__label = widget_factory(
            klass=Gtk.Label,
            properties={
                "css_classes": ["dim-label", "heading"],
                "justify": Gtk.Justification.CENTER,
                "valign": Gtk.Align.CENTER,
                "wrap": True,
            },
        )
        self.__button = widget_factory(
            klass=Gtk.Button,
            properties={"css_classes": ["flat"]},
            children=widget_factory(
                klass=Gtk.Box,
                properties={"orientation": Gtk.Orientation.VERTICAL},
                children=(self.__avatar, self.__label),
            ),
        )
        self.__button.connect("clicked", self.clicked_signal)
        self.set_child(self.__button)

    def __init__(self, *args, server: ServerInfo, user: UserInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__init_widget()
        self.__server = server
        self.__user = user
        self.__image_dir = (
            shared.app_cache_dir
            / "servers"
            / self.__server.server_id
            / "users"
            / self.__user.user_id
            / "images"
        )
        self.__image_path = self.__image_dir / "profile.png"
        self.__image_size = self.__avatar.get_size()
        self.__label.set_label(user.name)
        self.__avatar.set_text(user.name)
        self.load_image()

    def load_image(self) -> None:
        """
        Load the user image from disk or from the server.

        - If the image is on disk, will use it
        - Else downloads from the server and uses that (unless an error happened)
        """

        def download_image():
            client = JellyfinClient(
                base_url=self.__server.address, device_id=""
            ).get_httpx_client()
            url = f"/Users/{self.__user.user_id}/Images/Profile"
            params = {
                "format": "Png",
                "width": self.__image_size,
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
            self.__image_dir.mkdir(parents=True, exist_ok=True)
            with self.__image_path.open("wb") as file:
                file.write(response.content)
            return

        def on_error(error: Exception):
            match error:
                case NoUserImageError():
                    logging.debug("%s has no user image", self.__user.name)
                case _:
                    logging.debug(
                        "Couldn't download %s's profile image",
                        self.__user.name,
                        exc_info=error,
                    )

        def on_success(_result=None):
            picture: Gtk.Picture = Gtk.Picture.new_for_filename(str(self.__image_path))  # type: ignore
            paintable = picture.get_paintable()
            self.__avatar.set_custom_image(paintable)

        # Use the local image if present
        if self.__image_path.is_file():
            on_success()
            return

        # Download the image asynchronously
        task = Task(
            main=download_image,
            callback=on_success,
            error_callback=on_error,
        )
        task.run()
