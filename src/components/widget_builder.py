import logging
from collections.abc import Sequence
from typing import Any, Callable, Generic, Self, TypeVar

from gi.repository import Adw, Gtk
from gi.repository.Gtk import Widget

_BuiltWidget = TypeVar("_BuiltWidget", bound=Widget)


class WidgetBuilder(Generic[_BuiltWidget]):
    """
    Builder pattern to sequentially create Gtk Widget subclasses

    `WidgetBuilder`s may be added as children to other `WidgetBuilder`s as they
    are callables that return `Widget`.
    """

    __widget_class: type[_BuiltWidget]
    __arguments: dict[str, Any]
    __handlers: dict[str, Any]
    __properties: dict[str, Any]
    __children: list["WidgetBuilder | Widget | None"]

    def __init__(self, widget_class: None | type[_BuiltWidget] = None) -> None:
        super().__init__()
        if widget_class is not None:
            self.set_widget_class(widget_class)
        self.__arguments = {}
        self.__handlers = {}
        self.__properties = {}
        self.__children = []

    # Adders / Setters

    def set_widget_class(self, widget_class: type[_BuiltWidget]) -> Self:
        self.__widget_class = widget_class
        return self

    def add_arguments(self, **arguments: Any) -> Self:
        self.__arguments |= arguments
        return self

    def add_properties(self, **properties: Any) -> Self:
        self.__properties |= properties
        return self

    def add_handlers(self, **signal_handlers: Callable) -> Self:
        self.__handlers |= signal_handlers
        return self

    def add_children(self, *children: "WidgetBuilder | Widget | None") -> Self:
        """
        Add children to the widget.

        Children may be `Widget` instances, or any callable producing them.
        This includes `WidgetBuilder`, as calling it is an alias for `build()`.

        Cases depending on the built widget:
        - Receives a single child: Passing multiple will raise a ValueError.
        - Receives a finite number of children: Children will be added, `None` may be used to fill empty spaces
            (eg. the start and title of a `Adw.HeaderBar` when only the end is to be set)
        - Receives many children: all of them will be added.
        """
        self.__children.extend(children)
        return self

    # Getters

    def get_widget_class(self) -> type[_BuiltWidget]:
        return self.__widget_class

    def get_arguments(self) -> dict[str, Any]:
        return self.__arguments

    def get_properties(self) -> dict[str, Any]:
        return self.__properties

    def get_handlers(self) -> dict[str, Any]:
        return self.__handlers

    def get_children(self) -> list["WidgetBuilder | Widget | None"]:
        return self.__children

    # Build helpers

    def __apply_properties(self, widget: _BuiltWidget) -> None:
        """Apply a set of properties to a widget"""
        for key, value in self.__properties.items():
            clean_key = key.replace("-", "_")
            setter_name = f"set_{clean_key}"
            if not callable(setter := getattr(widget, setter_name)):
                raise AttributeError(
                    "Widget type %s doesn't have a setter for property %s"
                    % (widget.__class__.__name__, key)
                )
            if key != clean_key:
                logging.warning("Consider using underscores for property %s", key)
            setter(value)

    def __apply_handlers(self, widget: Widget) -> None:
        for signal, handler in self.__handlers.items():
            widget.connect(signal, handler)

    def __check_no_null_children(
        self, widget: Widget, children: Sequence[Widget | None]
    ) -> Sequence[Widget]:
        """Helper function to check that the passed children contains no None"""
        for child in children:
            if child is None:
                raise ValueError(
                    "WidgetBuilder may not receive None children for %s"
                    % widget.__class__.__name__
                )
        return children  # type: ignore

    def __check_n_children(
        self, widget: Widget, n: int, children: Sequence[Widget | None]
    ) -> None:
        """Helper function to check that the passed children are of length `n`"""
        if len(children) != n:
            raise ValueError(
                "Widget %s may only receive %d children, passed %d for this widget type"
                % (widget.__class__.__name__, n, len(children))
            )

    def __resolve_children(
        self, children: Sequence["WidgetBuilder | Widget | None"]
    ) -> Sequence[Widget | None]:
        """Resolve `WidgetProducer` children by calling them and producing their `Widget`"""
        return [
            (build(child) if isinstance(child, WidgetBuilder) else child)
            for child in children
        ]

    def __apply_children(self, widget: Widget) -> None:

        # Resolve children from producers
        resolved = self.__resolve_children(self.__children)

        # Short circuit
        if not resolved:
            pass

        # Gtk.Box
        elif isinstance(widget, Gtk.Box):
            non_null = self.__check_no_null_children(widget, resolved)
            for child in non_null:
                widget.append(child)

        # Adw.PreferencesGroup
        elif isinstance(widget, Adw.PreferencesGroup):
            non_null = self.__check_no_null_children(widget, resolved)
            for child in non_null:
                widget.add(child)

        # Adw.ApplicationWindow
        elif isinstance(widget, Adw.ApplicationWindow):
            self.__check_n_children(widget, 1, resolved)
            widget.set_content(resolved[0])

        # Adw.ToolbarView
        elif isinstance(widget, Adw.ToolbarView):
            self.__check_n_children(widget, 3, resolved)
            start, title, end = resolved
            if isinstance(start, Widget):
                widget.add_top_bar(start)
            if isinstance(end, Widget):
                widget.add_bottom_bar(end)
            widget.set_content(title)

        # Adw.HeaderBar
        elif isinstance(widget, Adw.HeaderBar):
            self.__check_n_children(widget, 3, resolved)
            start, title, end = resolved
            if isinstance(start, Widget):
                widget.pack_start(start)
            if isinstance(end, Widget):
                widget.pack_end(end)
            widget.set_title_widget(title)

        # Adw.ActionRow
        elif isinstance(widget, Adw.ActionRow):
            self.__check_n_children(widget, 2, resolved)
            prefix, suffix = resolved
            if isinstance(prefix, Widget):
                widget.add_prefix(prefix)
            if isinstance(suffix, Widget):
                widget.add_suffix(suffix)

        # Adw.ViewStack
        elif isinstance(widget, Adw.ViewStack):
            non_null = self.__check_no_null_children(widget, resolved)
            for child in non_null:
                widget.add(child)

        # Any widget with "set_child"
        elif getattr(widget, "set_child", None) is not None:
            self.__check_n_children(widget, 1, resolved)
            widget.set_child(resolved[0])  # type: ignore

        # Cannot set children
        else:
            raise TypeError(
                'Widgets of type "%s" cannot receive children'
                % widget.__class__.__name__
            )

    def build(self) -> _BuiltWidget:
        """Build the widget"""
        if not callable(self.__widget_class):
            raise ValueError("Cannot build without a widget class")
        widget = self.__widget_class(**self.__arguments)
        self.__apply_handlers(widget)
        self.__apply_properties(widget)
        self.__apply_children(widget)
        return widget

    def __add__(self, other: "WidgetBuilder") -> "WidgetBuilder":
        new_builder = (
            WidgetBuilder()
            .set_widget_class(self.get_widget_class())
            # Add data from self
            .add_arguments(**self.get_arguments())
            .add_handlers(**self.get_handlers())
            .add_properties(**self.get_properties())
            .add_children(*self.get_children())
            # Add data from other
            .add_arguments(**other.get_arguments())
            .add_handlers(**other.get_handlers())
            .add_properties(**other.get_properties())
            .add_children(*other.get_children())
        )

        return new_builder

    def __radd__(self, other: type[Widget]) -> "WidgetBuilder":
        """
        Applies to a Widget class to return a new WidgetBuilder
        Enables the following syntax:

        Gtk.Button | Properties(css_classes=["suggested-action"])
        """

        # Other is a widget class,
        # Makes it into a WidgetBuilder and recurse
        if issubclass(other, Widget):
            builder = WidgetBuilder()
            builder.set_widget_class(other)
            return builder + self

        return NotImplemented


class Arguments(WidgetBuilder):
    """A dict of constructor arguments to pass to a builder object"""

    def __init__(self, **arguments: Any) -> None:
        super().__init__()
        self.add_arguments(**arguments)


class Properties(WidgetBuilder):
    """A dict of properties to pass to a builder object"""

    def __init__(self, **properties: Any) -> None:
        super().__init__()
        self.add_properties(**properties)


class Handlers(WidgetBuilder):
    """A dict of signal handlers to pass to a builder object"""

    def __init__(self, **handlers: Callable) -> None:
        super().__init__()
        self.add_handlers(**handlers)


class Children(WidgetBuilder):
    """A list of children to pass to a builder object"""

    def __init__(self, *children: "WidgetBuilder | Widget | None") -> None:
        super().__init__()
        self.add_children(*children)


def build(builder: WidgetBuilder[_BuiltWidget]) -> _BuiltWidget:
    """
    Function that builds a `WidgetBuilder`.

    This is just syntactic sugar around `WidgetBuilder.build()`
    """
    return builder.build()
