from typing import cast

from gi.repository import Adw, GObject, Gtk

from src.components.shelf_page import ShelfPage
from src.components.widget_builder import Children, Handlers, Properties, build


class TypeOverrideError(Exception):
    """Error raised when overriding a shelf's item type"""

class Shelf(Gtk.Box):
    """A paginated item shelf with items of the same type"""

    __gtype_name__ = "MarmaladeShelf"

    __title_label: Gtk.Label
    __previous_button: Gtk.Button
    __view_stack: Adw.ViewStack
    __carousel_view: Adw.Carousel
    __empty_view: Adw.Bin
    __next_button: Gtk.Button
    __dots: Adw.CarouselIndicatorDots

    def __init_widget(self):
        self.__title_label = build(
            Gtk.Label
            + Properties(
                css_classes=["title"],
                halign=Gtk.Align.START,
            )
        )
        self.__previous_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_previous_button_clicked)
            + Properties(
                css_classes=["flat"],
                icon_name="go-previous-symbolic",
                valign=Gtk.Align.CENTER,
                margin_start=8,
            )
        )
        self.__next_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_next_button_clicked)
            + Properties(
                css_classes=["flat"],
                icon_name="go-next-symbolic",
                valign=Gtk.Align.CENTER,
                margin_end=8,
            )
        )
        self.__carousel_view = build(
            Adw.Carousel
            + Handlers(
                **{
                    "page-changed": self.__update_navigation_controls,
                    "notify::n-pages": self.__on_n_pages_changed,
                }
            )
            + Properties(
                hexpand=True,
                halign=Gtk.Align.START,
            )
        )
        self.__dots = build(
            Adw.CarouselIndicatorDots
            + Properties(
                halign=Gtk.Align.CENTER,
                carousel=self.__carousel_view,
            )
        )
        self.__empty_view = build(
            Adw.Bin
            + Properties(
                name="shelf-placeholder-bin",
            )
        )
        self.__view_stack = build(
            Adw.ViewStack
            + Children(
                self.__empty_view,
                self.__carousel_view,
            )
        )

        center_box = (
            Gtk.Box
            + Properties(
                orientation=Gtk.Orientation.VERTICAL,
                spacing=14,
            )
            + Children(self.__title_label, self.__view_stack)
        )

        controls_and_content_box = build(
            Gtk.Box
            + Properties(
                orientation=Gtk.Orientation.HORIZONTAL,
                spacing=8,
            )
            + Children(
                self.__previous_button,
                center_box,
                self.__next_button,
            )
        )

        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_valign(Gtk.Align.START)
        self.set_hexpand(True)
        self.set_spacing(8)
        self.append(controls_and_content_box)
        self.append(self.__dots)

    # lines property

    __lines: int = 1

    @GObject.Property(type=int, default=1)
    def lines(self) -> int:
        return self.__lines

    def get_lines(self) -> int:
        return self.get_property("lines")

    @lines.setter
    def lines_setter(self, value: int) -> None:
        self.__lines = value
        self._reflow_items()

    def set_lines(self, value: int):
        self.set_property("lines", value)

    # columns property

    __columns: int = 4

    @GObject.Property(type=int, default=4)
    def columns(self) -> int:
        return self.__columns

    def get_columns(self) -> int:
        return self.get_property("columns")

    @columns.setter
    def columns_setter(self, value: int) -> None:
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
    def title_setter(self, value: str) -> None:
        self.__title_label.set_label(value)
        self.__title_label.set_visible(len(value) > 0)

    def set_title(self, value: str):
        self.set_property("title", value)

    # empty_child property

    @GObject.Property(type=Gtk.Widget)
    def empty_child(self) -> Gtk.Widget | None:
        return self.__empty_view.get_child()

    def get_empty_child(self) -> Gtk.Widget:
        return self.get_property("empty_child")

    @empty_child.setter
    def empty_child_setter(self, value: Gtk.Widget) -> None:
        self.__empty_view.set_child(value)

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
        self.__init_widget()

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
        has_multiple_pages = self.__carousel_view.get_n_pages() > 1
        self.__dots.set_visible(has_multiple_pages)
        index = self.__carousel_view.get_position()
        self.__next_button.set_sensitive(index < self.__carousel_view.get_n_pages() - 1)
        self.__previous_button.set_sensitive(index > 0)

    def __update_visible_stack_page(self) -> None:
        self.__view_stack.set_visible_child(
            self.__empty_view if self._get_n_pages() == 0 else self.__carousel_view
        )

    def _shift_carousel(self, offset: int = 1, animate: bool = True) -> None:
        """Navigate the carousel relatively"""
        position = self.__carousel_view.get_position()
        destination = round(max(0, min(self._get_n_pages() - 1, position + offset)))
        destination_page = self.__carousel_view.get_nth_page(destination)
        self.__carousel_view.scroll_to(destination_page, animate=animate)

    # Content pagination methods

    def _get_n_pages(self) -> int:
        return self.__carousel_view.get_n_pages()

    def _get_nth_page(self, index: int) -> ShelfPage:
        n_pages = self._get_n_pages()
        index = index if index >= 0 else n_pages + index
        if index not in range(0, n_pages):
            raise IndexError()
        return cast(ShelfPage, self.__carousel_view.get_nth_page(index))

    def __create_page(self) -> None:
        page = ShelfPage()
        flags = GObject.BindingFlags.SYNC_CREATE
        for prop in ("columns", "lines"):
            self.bind_property(prop, page, prop, flags)
        self.__carousel_view.append(page)

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
            self.__carousel_view.remove(page)
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


Shelf.set_css_name("shelf")  # type: ignore
