from typing import cast

from gi.repository import Gio, GObject, Gtk

from src.components.list_store_item import ListStoreItem


class ShelfPage(Gtk.FlowBox):
    __gtype_name__ = "MarmaladeShelfPage"

    __model: Gio.ListStore

    def __init_widget(self):
        self.set_selection_mode(Gtk.SelectionMode.NONE)
        self.set_column_spacing(8)
        self.set_row_spacing(8)
        self.set_margin_bottom(16)
        self.set_margin_top(16)
        self.set_margin_start(16)
        self.set_margin_end(16)
        self.set_homogeneous(True)
        self.set_halign(Gtk.Align.START)

    # lines property

    __lines: int

    @GObject.Property(type=int)
    def lines(self) -> int:
        return self.__lines

    def get_lines(self) -> int:
        return self.get_property("lines")

    @lines.setter
    def lines_setter(self, value: int) -> None:
        self.__lines = value

    def set_lines(self, value: int):
        self.set_property("lines", value)

    # columns property

    __columns: int

    @GObject.Property(type=int)
    def columns(self) -> int:
        return self.__columns

    def get_columns(self) -> int:
        return self.get_property("columns")

    @columns.setter
    def columns_setter(self, value: int) -> None:
        self.__columns = value

    def set_columns(self, value: int):
        self.set_property("columns", value)

    # Private python methods

    def __create_widget_func(self, item: ListStoreItem, *_args) -> Gtk.Widget:
        return item.value

    def __on_model_items_changed(self, *args):
        page_columns = min(self.get_columns(), self.__model.get_n_items())
        self.set_max_children_per_line(page_columns)
        self.set_min_children_per_line(page_columns)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_widget()

        # Create the inner list model
        self.__model = Gio.ListStore.new(ListStoreItem)
        self.__model.connect("items-changed", self.__on_model_items_changed)
        self.bind_model(self.__model, self.__create_widget_func, None, None)

    def __len__(self) -> int:
        return self.__model.get_n_items()

    def append(self, widget: Gtk.Widget) -> None:
        """Append a widget to the shelf page"""
        wrapper = ListStoreItem(widget)
        self.__model.append(wrapper)

    def pop(self) -> Gtk.Widget:
        """Pop the last widget of the page"""
        if (n_items := len(self)) == 0:
            raise IndexError()
        item = cast(ListStoreItem, self.__model.get_item(index := n_items - 1))
        self.__model.remove(index)
        return item.value

    @property
    def is_full(self) -> bool:
        return len(self) >= self.get_lines() * self.get_columns()
