import logging
from collections.abc import Sequence
from operator import call
from typing import Any, Callable, Generic, Self, TypeVar

from gi.repository import Adw, Gtk
from gi.repository.Gtk import Widget

_BuiltWidgetType = TypeVar("_BuiltWidgetType", bound=Widget)
_WidgetProducer = Callable[[], Widget]
_ResolvedWidgetBuilderChild = Widget | None
_WidgetBuilderChild = _WidgetProducer | _ResolvedWidgetBuilderChild

class Properties(dict[str, Any]):
    """A dict of properties to pass to a builder object"""

    def __init__(self, **properties: Any) -> None:
        super().__init__(properties)


class Handlers(dict[str, Any]):
    """A dict of signal handlers to pass to a builder object"""

    def __init__(self, **handlers: Callable) -> None:
        super().__init__(handlers)


class Children(list[_WidgetBuilderChild]):
    """A list of children to pass to a builder object"""

    def __init__(self, *children: _WidgetBuilderChild) -> None:
        super().__init__(children)


class WidgetBuilder(Generic[_BuiltWidgetType]):
    """
    Builder pattern to sequentially create Gtk Widget subclasses

    `WidgetBuilder`s may be added as children to other `WidgetBuilder`s as they
    are callables that return `Widget`.
    """

    __widget: _BuiltWidgetType

    def __init__(
        self, constructor: Callable[..., _BuiltWidgetType], **arguments: dict[str, Any]
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

    def __check_no_null_children(
        self, children: Sequence[_ResolvedWidgetBuilderChild]
    ) -> Sequence[Widget]:
        """Helper function to check that the passed children contains no None"""
        for child in children:
            if child is None:
                raise ValueError(
                    "Widget type %s may not receive None children"
                    % self.__widget_class_name
                )
        return children  # type: ignore

    def __check_n_children(
        self, n: int, children: Sequence[_ResolvedWidgetBuilderChild]
    ) -> None:
        """Helper function to check that the passed children are of length `n`"""
        if len(children) != n:
            raise ValueError(
                "Widget type %s may only receive %d children, passed %d"
                % (self.__widget_class_name, n, len(children))
            )

    def __resolve_children(
        self, children: Sequence[_WidgetBuilderChild]
    ) -> Sequence[_ResolvedWidgetBuilderChild]:
        """Resolve `WidgetProducer` children by calling them and producing their `Widget`"""
        return [(call(child) if callable(child) else child) for child in children]

    def add_children(self, *children: _WidgetBuilderChild) -> Self:  # type: ignore
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

        # Resolve children from producers
        resolved = self.__resolve_children(children)

        # Short circuit
        if not resolved:
            pass

        # Gtk.Box
        elif isinstance(self.__widget, Gtk.Box):
            non_null = self.__check_no_null_children(resolved)
            for child in non_null:
                self.__widget.append(child)

        # Adw.PreferencesGroup
        elif isinstance(self.__widget, Adw.PreferencesGroup):
            non_null = self.__check_no_null_children(resolved)
            for child in non_null:
                self.__widget.add(child)

        # Adw.ApplicationWindow
        elif isinstance(self.__widget, Adw.ApplicationWindow):
            self.__check_n_children(1, resolved)
            self.__widget.set_content(resolved[0])

        # Adw.ToolbarView
        elif isinstance(self.__widget, Adw.ToolbarView):
            self.__check_n_children(3, resolved)
            start, title, end = resolved
            if isinstance(start, Widget):
                self.__widget.add_top_bar(start)
            if isinstance(end, Widget):
                self.__widget.add_bottom_bar(end)
            self.__widget.set_content(title)

        # Adw.HeaderBar
        elif isinstance(self.__widget, Adw.HeaderBar):
            self.__check_n_children(3, resolved)
            start, title, end = resolved
            if isinstance(start, Widget):
                self.__widget.pack_start(start)
            if isinstance(end, Widget):
                self.__widget.pack_end(end)
            self.__widget.set_title_widget(title)

        # Adw.ActionRow
        elif isinstance(self.__widget, Adw.ActionRow):
            self.__check_n_children(2, resolved)
            prefix, suffix = resolved
            if isinstance(prefix, Widget):
                self.__widget.add_prefix(prefix)
            if isinstance(suffix, Widget):
                self.__widget.add_suffix(suffix)

        # Adw.ViewStack
        elif isinstance(self.__widget, Adw.ViewStack):
            non_null = self.__check_no_null_children(resolved)
            for child in non_null:
                self.__widget.add(child)

        # Any widget with "set_child"
        elif getattr(self.__widget, "set_child", None) is not None:
            self.__check_n_children(1, resolved)
            self.__widget.set_child(resolved[0])  # type: ignore

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

    def build(self) -> _BuiltWidgetType:
        """Get the built widget"""
        return self.__widget

    def __call__(self) -> _BuiltWidgetType:
        """
        Alias for `build()`

        Needed to pass `WidgetBuilder` instances to `WidgetBuilder.add_children()`
        """
        return self.build()

    def __or__(
        self,
        # fmt: off
        other: (
            Properties 
            | Handlers 
            | _WidgetBuilderChild 
            | Sequence[_WidgetBuilderChild]
        ),
        # fmt: on
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

        # Single child
        elif isinstance(other, Widget) or callable(other):
            self.add_children(other)
        elif other is None:
            # fmt: off
            logging.warning("While syntactically valid, adding a single None child to a WidgetBuilder is a no-op. Please avoid doing so.")
            # fmt: on
            pass

        # Multiple children
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
