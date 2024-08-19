from typing import Any, Callable, Sequence, TypeVar

from gi.repository import Gtk

from src.components.widget_builder import WidgetBuilder

WidgetType = TypeVar("WidgetType", bound=Gtk.Widget)
ChildWidgetType = TypeVar("ChildWidgetType", bound=Gtk.Widget)


def WidgetFactory(
    klass: type[WidgetType],
    arguments: None | dict[str, Any] = None,
    properties: None | dict[str, Any] = None,
    signal_handlers: None | dict[str, Callable] = None,
    children: None | ChildWidgetType | Sequence[None | ChildWidgetType] = None,
) -> WidgetType:
    """
    Create a widget from a given class and constructor arguments,
    set properties on it and compose it with optional children.

    Children may be a sequence or a single child widget for conciseness.
    """
    return (
        WidgetBuilder(klass, **(arguments if isinstance(arguments, dict) else {}))
        .set_properties(properties if isinstance(properties, dict) else {})
        .add_signal_handlers(
            signal_handlers if isinstance(signal_handlers, dict) else {}
        )
        .add_children(
            children
            if isinstance(children, Sequence)
            else (children,) if isinstance(children, Gtk.Widget) else tuple()
        )
        .build()
    )
