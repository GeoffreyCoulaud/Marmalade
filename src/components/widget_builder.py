import logging
from collections.abc import Sequence
from operator import call
from typing import Any, Callable, Generic, Self, TypeVar, cast

from gi.repository import Adw, Gtk
from gi.repository.Gtk import Widget

WidgetProducer = Callable[[], Widget]
BuiltWidgetType = TypeVar("BuiltWidgetType", bound=Widget)


class Properties(dict[str, Any]):
    """A dict of properties to pass to a builder object"""


class Handlers(dict[str, Any]):
    """A dict of signal handlers to pass to a builder object"""


class Children(list["None | WidgetBuilder | Widget"]):
    """A list of children to pass to a builder object"""


class WidgetBuilder(Generic[BuiltWidgetType]):
    """
    Builder pattern to sequentially create Gtk Widget subclasses

    `WidgetBuilder`s may be added as children to other `WidgetBuilder`s as they
    are callables that return `Widget`.
    """

    __widget: BuiltWidgetType

    def __init__(
        self, constructor: Callable[..., BuiltWidgetType], **arguments: dict[str, Any]
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

    def __check_no_null_children(self, children: Sequence[Widget | None]) -> None:
        """Helper function to check that the passed children contains no None"""
        for child in children:
            if child is None:
                raise ValueError(
                    "Widget type %s may not receive None children"
                    % self.__widget_class_name
                )

    def __check_n_children(self, n: int, children: Sequence[Widget | None]) -> None:
        """Helper function to check that the passed children are of length `n`"""
        if len(children) != n:
            raise ValueError(
                "Widget type %s may only receive %d children, passed %d"
                % (self.__widget_class_name, n, len(children))
            )

    def add_children(
        self, *children: None | Callable[[], Widget] | Widget  # type: ignore
    ) -> Self:
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

        # Convert WidgetProducer children to Widget
        children: Sequence[Widget | None] = [
            (call(child) if callable(child) else child) for child in children
        ]

        # Short circuit
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
                self.__widget.add(cast(Widget, child))

        # Adw.ApplicationWindow
        elif isinstance(self.__widget, Adw.ApplicationWindow):
            self.__check_n_children(1, children)
            self.__widget.set_content(children[0])

        # Adw.ToolbarView
        elif isinstance(self.__widget, Adw.ToolbarView):
            self.__check_n_children(3, children)
            start, title, end = children
            if isinstance(start, Widget):
                self.__widget.add_top_bar(start)
            if isinstance(end, Widget):
                self.__widget.add_bottom_bar(end)
            self.__widget.set_content(title)

        # Adw.HeaderBar
        elif isinstance(self.__widget, Adw.HeaderBar):
            self.__check_n_children(3, children)
            start, title, end = children
            if isinstance(start, Widget):
                self.__widget.pack_start(start)
            if isinstance(end, Widget):
                self.__widget.pack_end(end)
            self.__widget.set_title_widget(title)

        # Adw.ActionRow
        elif isinstance(self.__widget, Adw.ActionRow):
            self.__check_n_children(2, children)
            prefix, suffix = children
            if isinstance(prefix, Widget):
                self.__widget.add_prefix(prefix)
            if isinstance(suffix, Widget):
                self.__widget.add_suffix(suffix)

        # Any widget with "set_child"
        elif getattr(self.__widget, "set_child", None) is not None:
            self.__check_n_children(1, children)
            self.__widget.set_child(children[0])  # type: ignore

        # Cannot set children
        else:
            raise TypeError(
                'Widgets of type "%s" cannot receive children'
                % self.__widget_class_name
            )

        return self

    def add_handlers(self, **signal_handlers: Callable) -> Self:
        """Add signal handlers to the built widget"""
        for signal, handler in signal_handlers.items():
            self.__widget.connect(signal, handler)
        return self

    def build(self) -> BuiltWidgetType:
        """Get the built widget"""
        return self.__widget

    def __call__(self) -> BuiltWidgetType:
        """
        Alias for `build()`

        Needed to pass `WidgetBuilder` instances to `WidgetBuilder.add_children()`
        """
        return self.build()

    def __or__(
        self,
        other: (
            Properties
            | Handlers
            | Widget
            | WidgetProducer
            | Sequence[None | Widget | WidgetProducer]
        ),
    ) -> Self:
        """
        Augment the widget builder with helper objects or children.

        This is just syntactic sugar on top of regular `WidgetBuilder` methods.
        """

        # Properties
        if isinstance(other, Properties):
            self.set_properties(**other)

        # Signal handlers
        elif isinstance(other, Handlers):
            self.add_handlers(**other)

        # Children
        elif isinstance(other, Widget):
            self.add_children(other)
        elif callable(other):
            self.add_children(other)

        # Valid sequences
        # - Contains None, Widget or callables that produce Widget
        elif isinstance(other, Sequence) and all(
            (child is None or isinstance(child, Widget) or callable(child))
            for child in other
        ):
            self.add_children(*other)

        # Unsupported
        else:
            return NotImplemented
        return self
