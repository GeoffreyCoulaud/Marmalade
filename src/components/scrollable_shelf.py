from gi.repository import Adw, GObject, Gtk

from src import build_constants


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/scrollable_shelf.ui")
class ScrollableShelf(Adw.Bin):
    __gtype_name__ = "MarmaladeScrollableShelf"

    # fmt: off
    __label: Gtk.Label = Gtk.Template.Child("label")
    __box: Gtk.Box = Gtk.Template.Child("box")
    # fmt: on

    # title property

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.__label.get_label()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__label.set_label(value)
        self.__update_title_visibility()

    def set_title(self, value: str):
        self.set_property("title", value)

    # Private methods

    def __update_title_visibility(self, *_args) -> None:
        visible = bool(self.get_title())
        self.__label.set_visible(visible)

    # Public methods

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__update_title_visibility()

    def append(self, widget: Gtk.Widget) -> None:
        self.__box.append(widget)

    def remove(self, widget: Gtk.Widget) -> None:
        self.__box.remove(widget)
