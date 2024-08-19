import logging
from typing import Any, Callable, Generic, Never, Self, Sequence, TypeVar, cast

from gi.repository import Adw, Gtk

WidgetType = TypeVar("WidgetType", bound=Gtk.Widget)
ChildWidgetType = TypeVar("ChildWidgetType", bound=Gtk.Widget)


class WidgetBuilder(Generic[WidgetType]):
    """Builder pattern to sequentially create Gtk Widget subclasses"""

    __widget: WidgetType

    def __init__(
        self, constructor: Callable[..., WidgetType], **arguments: dict[str, Any]
    ) -> None:
        self.__widget = constructor(**arguments)  # type: ignore

    @property
    def __widget_class_name(self) -> str:
        return self.__widget.__class__.__name__

    def set_properties(self, **properties: Any) -> Self:
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

    def add_children(
        self, *children: "None | WidgetBuilder | Gtk.Widget"  # type: ignore
    ) -> Self:
        """Add children to the widget"""

        # Convert WidgetBuilder children to Widget
        children: Sequence[Gtk.Widget | None] = [
            (child.build() if isinstance(child, WidgetBuilder) else child)
            for child in children
        ]

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

        # Adw.ActionRow
        elif isinstance(self.__widget, Adw.ActionRow):
            self.__check_n_children(2, children)
            prefix, suffix = children
            if isinstance(prefix, Gtk.Widget):
                self.__widget.add_prefix(prefix)
            if isinstance(suffix, Gtk.Widget):
                self.__widget.add_suffix(suffix)

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

    def add_signal_handlers(self, **signal_handlers: Callable) -> Self:
        """Add signal handlers to the built widget"""
        for signal, handler in signal_handlers.items():
            self.__widget.connect(signal, handler)
        return self

    def build(self) -> WidgetType:
        """Build the widget according to the instructions"""
        return self.__widget
