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
        return self.__title_label.get_title()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__title_label.set_label(value)
        self.__title_label.set_visible(len(value) > 0)

    def set_title(self, value: str):
        self.set_property("title", value)

    # Init

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__next_button.connect("clicked", self.__on_next_button_clicked)
        self.__previous_button.connect("clicked", self.__on_previous_button_clicked)
        self.__carousel.connect("page-changed", self.__on_page_changed)
        self.__carousel.connect("notify::n-pages", self.__on_n_pages_changed)
        self.__update_navigation_visibility()

    # Navigation methods

    def __on_previous_button_clicked(self, _button) -> None:
        self._shift_carousel(-1)

    def __on_next_button_clicked(self, _button) -> None:
        self._shift_carousel(1)

    def __on_page_changed(self, _carousel, index) -> None:
        self.__next_button.set_sensitive(index < self.__carousel.get_n_pages() - 1)
        self.__previous_button.set_sensitive(index > 0)

    def __on_n_pages_changed(self, _carousel, _value) -> None:
        self.__update_navigation_visibility()
        self.notify("n_pages")

    def __update_navigation_visibility(self) -> None:
        has_multiple_pages = self._get_n_pages() > 1
        for widget in (
            self.__previous_button,
            self.__next_button,
            self.__dots,
        ):
            widget.set_visible(has_multiple_pages)

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

    def append(self, widget: Gtk.Widget) -> None:
        """
        Append an item to the shelf.
        Before appending, adds a page if none exists or the last one is full.
        """
        if self._get_n_pages() == 0:
            self.__carousel.append(ShelfPage())
        page = self._get_nth_page(-1)
        if len(page) >= self.get_columns() * self.get_lines():
            self.__carousel.append(page := ShelfPage())
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
