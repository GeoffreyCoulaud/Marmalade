import logging
from http import HTTPStatus
from typing import Optional

from gi.repository import Adw, Gdk, GLib, GObject, Gtk
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.image_type import ImageType

from src import build_constants
from src.components.loading_view import LoadingView
from src.jellyfin import JellyfinClient
from src.task import Task


class ImageDownloadError(UnexpectedStatus):
    """Error raised when an image cannot be downloaded"""


class NoImageError(ImageDownloadError):
    """Error raised when an item has no image of the requested type"""


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/item_card.ui")
class ItemCard(Adw.Bin):
    __gtype_name__ = "MarmaladeItemCard"

    # fmt: off
    __button: Gtk.Button = Gtk.Template.Child("button")
    __picture: Gtk.Picture = Gtk.Template.Child("picture")
    __title_label: Gtk.Label = Gtk.Template.Child("title_label")
    __subtitle_label: Gtk.Label = Gtk.Template.Child("subtitle_label")
    # fmt: on

    # item_id property

    __item_id: str

    @GObject.Property(type=str)
    def item_id(self) -> str:
        return self.__item_id

    def get_item_id(self) -> str:
        return self.get_property("item_id")

    @item_id.setter
    def item_id(self, value: str) -> None:
        self.__item_id = value

    def set_item_id(self, value: str):
        self.set_property("item_id", value)

    # image_width property

    __image_width: int

    @GObject.Property(type=int, default=-1)
    def image_width(self) -> int:
        return self.__image_width

    def get_image_width(self) -> int:
        return self.get_property("image_width")

    @image_width.setter
    def image_width(self, value: int) -> None:
        self.__image_width = value

    def set_image_width(self, value: int):
        self.set_property("image_width", value)

    # image_height property

    __image_height: int

    @GObject.Property(type=int, default=-1)
    def image_height(self) -> int:
        return self.__image_height

    def get_image_height(self) -> int:
        return self.get_property("image_height")

    @image_height.setter
    def image_height(self, value: int) -> None:
        self.__image_height = value

    def set_image_height(self, value: int):
        self.set_property("image_height", value)

    # image_type property

    __image_type: ImageType = ImageType.PRIMARY

    @GObject.Property(type=str, default=ImageType.PRIMARY)
    def image_type(self) -> ImageType:
        return self.__image_type

    def get_image_type(self) -> ImageType:
        return self.get_property("image_type")

    @image_type.setter
    def image_type(self, value: ImageType) -> None:
        self.__image_type = value

    def set_image_type(self, value: ImageType):
        self.set_property("image_type", value)

    # image_tag property

    __image_tag: str

    @GObject.Property(type=str)
    def image_tag(self) -> str:
        return self.__image_tag

    def get_image_tag(self) -> str:
        return self.get_property("image_tag")

    @image_tag.setter
    def image_tag(self, value: str) -> None:
        self.__image_tag = value

    def set_image_tag(self, value: str):
        self.set_property("image_tag", value)

    # title property

    @GObject.Property(type=str)
    def title(self) -> str:
        return self.__title_label.get_label()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__title_label.set_label(value)

    def set_title(self, value: str):
        self.set_property("title", value)

    # subtitle property

    @GObject.Property(type=str, default="")
    def subtitle(self) -> str:
        return self.__subtitle_label.get_label()

    def get_subtitle(self) -> str:
        return self.get_property("subtitle")

    @subtitle.setter
    def subtitle(self, value: str) -> None:
        self.__subtitle_label.set_label(value)
        self.__update_subtitle_visible()

    def set_subtitle(self, value: str):
        self.set_property("subtitle", value)

    # action_name property

    @GObject.Property(type=str, default="")
    def action_name(self) -> str:
        return self.__button.get_action_name()

    def get_action_name(self) -> str:
        return self.get_property("action_name")

    @action_name.setter
    def action_name(self, value: str) -> None:
        self.__button.set_action_name(value)

    def set_action_name(self, value: str):
        self.set_property("action_name", value)

    # action_target_value property

    @GObject.Property(type=object, default=None)
    def action_target_value(self) -> Optional[GLib.Variant]:
        return self.__button.get_action_target_value()

    def get_action_target_value(self) -> Optional[GLib.Variant]:
        return self.get_property("action_target_value")

    @action_target_value.setter
    def action_target_value(self, value: Optional[GLib.Variant]) -> None:
        self.__button.set_action_target_value(value)

    def set_action_target_value(self, value: Optional[GLib.Variant]):
        self.set_property("action_target_value", value)

    # Private methods

    def __update_subtitle_visible(self, *_args) -> None:
        self.__subtitle_label.set_visible(bool(self.__subtitle_label.get_label()))

    # Public methods

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__update_subtitle_visible()

    def load_image(self, client: JellyfinClient) -> None:
        """Load the item's image from the server or the cache"""

        def download_image() -> bytes:
            """Download the image in PNG format in the given file"""

            # Create query
            url = f"/Items/{self.get_item_id()}/Images/{self.get_image_type()}"
            params = {"format": "Png"}
            if (height := self.get_image_height()) > 0:
                params["fillHeight"] = height
            if (width := self.get_image_width()) > 0:
                params["fillWidth"] = width
            if tag := self.get_image_tag():
                params["tag"] = tag

            logging.debug(
                "Getting item %s image: %s %s", self.get_item_id(), url, str(params)
            )

            # Make the request
            httpx_client = client.get_httpx_client()
            res = httpx_client.get(url, params=params)
            match res.status_code:
                case HTTPStatus.OK:
                    pass
                case HTTPStatus.NOT_FOUND:
                    raise NoImageError(res.status_code, res.content)
                case _:
                    raise ImageDownloadError(res.status_code, res.content)

            # Wrap in a Gtk.Paintable
            return Gdk.Texture.new_from_bytes(GLib.Bytes.new(res.content))

        def on_download_success(paintable: Gdk.Texture):
            self.__picture.set_paintable(paintable)
            logging.debug("Displayed image for %s", self.get_item_id())

        def on_download_error(error: Exception):
            match error:
                case NoImageError():
                    logging.debug("%s has no image", self.get_item_id())
                    # TODO set a fallback image
                case ImageDownloadError():
                    logging.error(
                        "Item %s image error %d", self.get_item_id(), error.status_code
                    )

        # Download the image asynchronously
        # (Note that caching is done at the HTTP layer on the Client)
        task = Task(
            main=download_image,
            callback=on_download_success,
            error_callback=on_download_error,
        )
        task.run()
