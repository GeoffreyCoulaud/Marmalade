import logging
from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional

from gi.repository import Adw, Gdk, GLib, GObject, Gtk, Pango
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.image_type import ImageType

from src.components.widget_builder import Children, Properties, build
from src.jellyfin import JellyfinClient
from src.task import Task


class ImageDownloadError(UnexpectedStatus):
    """Error raised when an image cannot be downloaded"""


class NoImageError(ImageDownloadError):
    """Error raised when an item has no image of the requested type"""


@dataclass
class Size:
    width: int
    height: int


POSTER = Size(200, 300)
WIDE_SCREENSHOT = Size(200, 112)


class ItemCard(Adw.Bin):
    __gtype_name__ = "MarmaladeItemCard"

    __button: Gtk.Button
    __picture: Gtk.Picture
    __title_label: Gtk.Label
    __subtitle_label: Gtk.Label

    def __init_widget(self):

        self.__picture = build(
            Gtk.Picture
            + Properties(
                can_shrink=False,
                content_fit=Gtk.ContentFit.COVER,
            )
        )
        self.__title_label = build(
            Gtk.Label
            + Properties(
                css_classes=["heading"],
                ellipsize=Pango.EllipsizeMode.END,
                halign=Gtk.Align.START,
            )
        )
        self.__subtitle_label = build(
            Gtk.Label
            + Properties(
                css_classes=["dim-label"],
                ellipsize=Pango.EllipsizeMode.END,
                halign=Gtk.Align.START,
            )
        )
        self.__button = build(
            Gtk.Button
            + Properties(css_classes=["card"])
            + Children(
                Gtk.Box
                + Properties(orientation=Gtk.Orientation.VERTICAL)
                + Children(
                    self.__picture,
                    Gtk.Box
                    + Properties(
                        orientation=Gtk.Orientation.VERTICAL,
                        spacing=12,
                        margin_top=12,
                        margin_bottom=12,
                        margin_start=12,
                        margin_end=12,
                    )
                    + Children(
                        self.__title_label,
                        self.__subtitle_label,
                    ),
                )
            )
        )
        self.set_child(self.__button)

    # item_id property

    __item_id: str

    @GObject.Property(type=str)
    def item_id(self) -> str:
        return self.__item_id

    def get_item_id(self) -> str:
        return self.get_property("item_id")

    @item_id.setter
    def item_id_setter(self, value: str) -> None:
        self.__item_id = value

    def set_item_id(self, value: str):
        self.set_property("item_id", value)

    # image_size property

    __image_size: Size = POSTER

    @GObject.Property(type=object)
    def image_size(self) -> Size:
        return self.__image_size

    def get_image_size(self) -> Size:
        return self.get_property("image_size")

    @image_size.setter
    def image_size_setter(self, value: Size) -> None:
        self.__image_size = value
        self.__picture.set_size_request(value.width, value.height)

    def set_image_size(self, value: Size):
        self.set_property("image_size", value)

    # image_type property

    __image_type: ImageType = ImageType.PRIMARY

    @GObject.Property(type=str, default=ImageType.PRIMARY)
    def image_type(self) -> ImageType:
        return self.__image_type

    def get_image_type(self) -> ImageType:
        return self.get_property("image_type")

    @image_type.setter
    def image_type_setter(self, value: ImageType) -> None:
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
    def image_tag_setter(self, value: str) -> None:
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
    def title_setter(self, value: str) -> None:
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
    def subtitle_setter(self, value: str) -> None:
        self.__subtitle_label.set_label(value)
        self.__update_subtitle_visible()

    def set_subtitle(self, value: str):
        self.set_property("subtitle", value)

    # action_name property

    @GObject.Property(type=str, default="")
    def action_name(self) -> str | None:
        return self.__button.get_action_name()

    def get_action_name(self) -> str:
        return self.get_property("action_name")

    @action_name.setter
    def action_name_setter(self, value: str) -> None:
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
    def action_target_value_setter(self, value: Optional[GLib.Variant]) -> None:
        self.__button.set_action_target_value(value)

    def set_action_target_value(self, value: Optional[GLib.Variant]):
        self.set_property("action_target_value", value)

    # Private methods

    def __update_subtitle_visible(self, *_args) -> None:
        self.__subtitle_label.set_visible(bool(self.__subtitle_label.get_label()))

    # Public methods

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__init_widget()
        self.__update_subtitle_visible()

    def load_image(self, client: JellyfinClient) -> None:
        """Load the item's image from the server or the cache"""

        def download_image() -> Gdk.Texture:
            """Download the image in PNG format in the given file"""

            # Create query
            url = f"/Items/{self.get_item_id()}/Images/{self.get_image_type()}"
            image_size = self.get_image_size()
            params = {
                "format": "Png",
                "maxHeight": image_size.height,
                "maxWidth": image_size.width,
            }
            if tag := self.get_image_tag():
                params["tag"] = tag

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
            # TODO composite the image to be the exact image format
            return Gdk.Texture.new_from_bytes(GLib.Bytes.new(res.content))

        def on_download_success(paintable: Gdk.Texture):
            self.__picture.set_paintable(paintable)

        def on_download_error(error: Exception):
            match error:
                case NoImageError():
                    logging.debug("%s has no image", self.get_item_id())
                    # TODO set a fallback image
                case ImageDownloadError():
                    logging.error(
                        "Item %s image error %d", self.get_item_id(), error.status_code
                    )
                case _:
                    logging.error(
                        "Unexpected %s error", self.get_item_id(), exc_info=error
                    )

        # Download the image asynchronously
        # (Note that caching is done at the HTTP layer on the Client)
        task = Task(
            main=download_image,
            callback=on_download_success,
            error_callback=on_download_error,
        )
        task.run()
