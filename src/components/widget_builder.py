import logging
from typing import Any, Generic, Never, Self, Sequence, TypeVar, cast

from gi.repository import Adw, Gtk

WidgetType = TypeVar("WidgetType", bound=Gtk.Widget)
ChildWidgetType = TypeVar("ChildWidgetType", bound=Gtk.Widget)


class WidgetBuilder(Generic[WidgetType]):
    """Builder pattern to sequentially create Gtk Widget subclasses"""

    __widget: WidgetType

    def __init__(
        self, widget_class: type[WidgetType], **arguments: dict[str, Any]
    ) -> None:
        self.__widget = widget_class(**arguments)  # type: ignore

    @property
    def __widget_class_name(self) -> str:
        return self.__widget.__class__.__name__

    def set_properties(self, properties: dict[str, Any]) -> Self:
        """Add properties to set on the widget"""
        for key, value in properties.items():
            clean_key = key.replace("-", "_")
            setter_name = f"set_{clean_key}"
            if not callable(setter := getattr(self.__widget, setter_name)):
                raise AttributeError(
                    "Widget type %s doesn't have a setter for property %s"
                    % (self.__widget_class_name, key)
                )
            if key != clean_key:
                logging.warning("Consider using underscores for property %s", key)
            setter(value)
        return self

    def __check_no_null_children(self, children: Sequence[Gtk.Widget | None]) -> None:
        for child in children:
            if child is None:
                raise ValueError(
                    f"Widget type ${self.__widget_class_name} may not receive None children"
                )

    def __check_n_children(self, n: int, children: Sequence[Gtk.Widget | None]) -> None:
        if len(children) != n:
            raise ValueError(
                "Widget type %s may only receive %d children, passed %d"
                % (self.__widget_class_name, n, len(children))
            )

    def add_children(self, children: Sequence[Gtk.Widget | None]) -> Self:
        """Add children to the widget"""

        if not children:
            pass

        # Gtk.Box
        elif isinstance(self.__widget, Gtk.Box):
            self.__check_no_null_children(children)
            for child in (child for child in children if child is not None):
                self.__widget.append(child)

        # Adw.PreferencesGroup
        elif isinstance(self.__widget, Adw.PreferencesGroup):
            self.__check_no_null_children(children)
            for child in children:
                self.__widget.add(cast(Gtk.Widget, child))

        # Adw.ApplicationWindow
        elif isinstance(self.__widget, Adw.ApplicationWindow):
            self.__check_n_children(1, children)
            self.__widget.set_content(children[0])

        # Adw.ToolbarView
        elif isinstance(self.__widget, Adw.ToolbarView):
            self.__check_n_children(3, children)
            start, title, end = children
            if isinstance(start, Gtk.Widget):
                self.__widget.add_top_bar(start)
            if isinstance(end, Gtk.Widget):
                self.__widget.add_bottom_bar(end)
            self.__widget.set_content(title)

        # Adw.HeaderBar
        elif isinstance(self.__widget, Adw.HeaderBar):
            self.__check_n_children(3, children)
            start, title, end = children
            if isinstance(start, Gtk.Widget):
                self.__widget.pack_start(start)
            if isinstance(end, Gtk.Widget):
                self.__widget.pack_end(end)
            self.__widget.set_title_widget(title)

        # Any widget with "set_child"
        elif getattr(self.__widget, "set_child", None) is not None:
            self.__check_n_children(1, children)
            self.__widget.set_child(children[0])  # type: ignore

        # Cannot set children
        else:
            raise TypeError(
                f"Widgets ${self.__widget_class_name} may not receive children"
            )

        return self

    def build(self) -> WidgetType:
        """Build the widget according to the instructions"""
        return self.__widget
