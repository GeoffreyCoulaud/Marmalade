from typing import Optional

from gi.repository import Adw, Gio, GObject, Gtk

from src import build_constants
from src.components.list_store_item import ListStoreItem
from src.components.shelf_page import ShelfPage


class TypeOverrideError(Exception):
    """Error raised when overriding a shelf's item type"""


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/shelf.ui")
class Shelf(Gtk.Box):
    """A paginated item shelf with items of the same type"""

    __gtype_name__ = "MarmaladeShelf"

    # fmt: off
    __carousel: Adw.Carousel = Gtk.Template.Child("carousel")
    __dots: Adw.CarouselIndicatorDots = Gtk.Template.Child("dots")
    __next_button: Gtk.Button = Gtk.Template.Child("next_button")
    __previous_button: Gtk.Button = Gtk.Template.Child("previous_button")
    __title_label: Gtk.Label = Gtk.Template.Child("title_label")
    __view_stack: Adw.ViewStack = Gtk.Template.Child("view_stack")
    __empty_shelf_page: Adw.Bin = Gtk.Template.Child("empty_shelf_page")
    # fmt: on

    # lines property

    __lines: int

    @GObject.Property(type=int, default=1)
    def lines(self) -> int:
        return self.__lines

    def get_lines(self) -> int:
        return self.get_property("lines")

    @lines.setter
    def lines(self, value: int) -> None:
        self.__lines = value
        self._reflow_items()

    def set_lines(self, value: int):
        self.set_property("lines", value)

    # columns property

    __columns: int

    @GObject.Property(type=int, default=4)
    def columns(self) -> int:
        return self.__columns

    def get_columns(self) -> int:
        return self.get_property("columns")

    @columns.setter
    def columns(self, value: int) -> None:
        self.__columns = value
        self._reflow_items()

    def set_columns(self, value: int):
        self.set_property("columns", value)

    # title property

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.__title_label.get_label()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__title_label.set_label(value)
        self.__title_label.set_visible(len(value) > 0)

    def set_title(self, value: str):
        self.set_property("title", value)

    # empty_child property

    @GObject.Property(type=Gtk.Widget)
    def empty_child(self) -> Gtk.Widget:
        return self.__empty_shelf_page.get_child()

    def get_empty_child(self) -> Gtk.Widget:
        return self.get_property("empty_child")

    @empty_child.setter
    def empty_child(self, value: Gtk.Widget) -> None:
        self.__empty_shelf_page.set_child(value)

    def set_empty_child(self, value: Gtk.Widget):
        self.set_property("empty_child", value)

    # is_navigation_visible property

    @GObject.Property(type=bool, default=False, flags=GObject.ParamFlags.READABLE)
    def is_navigation_visible(self) -> bool:
        return self._get_n_pages() > 1

    def get_is_navigation_visible(self) -> bool:
        return self.get_property("is_navigation_visible")

    # Init

    def __init__(self, *args, **kwargs) -> None:
        """Create a new Shelf widget"""
        super().__init__(*args, **kwargs)
        self.__next_button.connect("clicked", self.__on_next_button_clicked)
        self.__previous_button.connect("clicked", self.__on_previous_button_clicked)
        self.__carousel.connect("page-changed", self.__update_navigation_controls)
        self.__carousel.connect("notify::n-pages", self.__on_n_pages_changed)
        self.__update_navigation_controls()
        self.__update_visible_stack_page()

    # Navigation methods

    def __on_previous_button_clicked(self, _button) -> None:
        self._shift_carousel(-1)

    def __on_next_button_clicked(self, _button) -> None:
        self._shift_carousel(1)

    def __on_n_pages_changed(self, _carousel, _value) -> None:
        self.__update_navigation_controls()
        self.__update_visible_stack_page()

    def __update_navigation_controls(self, *_args) -> None:
        has_multiple_pages = self.__carousel.get_n_pages() > 1
        self.__dots.set_visible(has_multiple_pages)
        index = self.__carousel.get_position()
        self.__next_button.set_sensitive(index < self.__carousel.get_n_pages() - 1)
        self.__previous_button.set_sensitive(index > 0)

    def __update_visible_stack_page(self) -> None:
        self.__view_stack.set_visible_child_name(
            "empty-shelf-page" if self._get_n_pages() == 0 else "carousel"
        )

    def _shift_carousel(self, offset: int = 1, animate: bool = True) -> None:
        """Navigate the carousel relatively"""
        position = self.__carousel.get_position()
        destination = max(0, min(self._get_n_pages() - 1, position + offset))
        destination_page = self.__carousel.get_nth_page(destination)
        self.__carousel.scroll_to(destination_page, animate=animate)

    # Content pagination methods

    def _get_n_pages(self) -> int:
        return self.__carousel.get_n_pages()

    def _get_nth_page(self, index: int) -> ShelfPage:
        n_pages = self._get_n_pages()
        index = index if index >= 0 else n_pages + index
        if index not in range(0, n_pages):
            raise IndexError()
        return self.__carousel.get_nth_page(index)

    def __create_page(self) -> None:
        page = ShelfPage()
        flags = GObject.BindingFlags.SYNC_CREATE
        for prop in ("columns", "lines"):
            self.bind_property(prop, page, prop, flags)
        self.__carousel.append(page)

    def append(self, widget: Gtk.Widget) -> None:
        """
        Append an item to the shelf.
        Before appending, adds a page if none exists or the last one is full.
        """
        if (self._get_n_pages() == 0) or (self._get_nth_page(-1).is_full):
            self.__create_page()
        page = self._get_nth_page(-1)
        page.append(widget)

    def pop(self) -> Gtk.Widget:
        """
        Pop the last shelf widget.
        Removes the widget's page if empty after popping.
        """
        if self._get_n_pages() == 0:
            raise IndexError()
        widget = (page := self._get_nth_page(-1)).pop()
        if len(page) == 0:
            self.__carousel.remove(page)
        return widget

    def _reflow_items(self) -> None:
        """
        Reflow the items in the different pages.
        Called when lines or columns changes to leave no gap and have no page overflow.
        """
        widgets = []
        while self._get_n_pages() > 0:
            widgets.append(self.pop())
        widgets.reverse()
        for widget in widgets:
            self.append(widget)

    # GTK.Buildable methods

    def add_child(self, builder=None, child=None, type=None) -> None:
        # TODO Check that this does work
        self.append(child)


Shelf.set_css_name("shelf")
