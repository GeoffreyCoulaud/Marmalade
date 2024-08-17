from typing import Any, Self, Sequence

from gi.repository import Gtk


class WidgetBuilder:
    """Builder pattern to sequentially create Gtk Widget subclasses"""

    __widget: Gtk.Widget

    def __init__(
        self, widget_class: type[Gtk.Widget], **arguments: dict[str, Any]
    ) -> None:
        self.__widget = widget_class(**arguments)

    @property
    def __widget_class_name(self) -> str:
        return self.__widget.__class__.__name__

    def set_properties(self, props: dict[str, Any]) -> Self:
        """Add properties to set on the widget"""
        for key, value in props:
            if not callable(setter := getattr(self.__widget, f"set_{key}")):
                raise AttributeError(
                    f"Widget type ${self.__widget_class_name} doesn't have a setter for property ${key}"
                )
            setter(value)
        return self

    def add_children(self, children: Sequence[Gtk.Widget]) -> Self:
        """Add children to the widget"""
        if not children:
            # Short circuit, do nothing if no children passed
            pass
        elif isinstance(self.__widget, Gtk.Box):
            # Case "Gtk.Box"
            for child in children:
                self.__widget.append(child)
        elif getattr(self.__widget, "set_child") is not None:
            # Any other case where there is a "set_child" method
            if len(children) > 1:
                raise ValueError(
                    f"Widget type ${self.__widget_class_name} may only receive one child"
                )
            self.__widget.set_child()
        else:
            # Cannot set children
            raise TypeError(
                f"Widgets ${self.__widget_class_name} may not receive children"
            )
        return self

    def build(self) -> Gtk.Widget:
        """Build the widget according to the instructions"""
        return self.__widget


def widget_factory(
    klass: type[Gtk.Widget],
    arguments: None | dict[str, Any] = None,
    properties: None | dict[str, Any] = None,
    children: None | Gtk.Widget | Sequence[Gtk.Widget] = None,
) -> Gtk.Widget:
    """
    Create a widget from a given class and constructor arguments,
    set properties on it and compose it with optional children.

    Children may be a sequence or a single child widget for conciseness.
    """
    return (
        WidgetBuilder(klass, **(arguments if arguments is not None else {}))
        .set_properties(properties if properties is not None else {})
        .add_children(
            tuple()
            if children is None
            else (children,) if isinstance(children, Gtk.Widget) else children
        )
        .build()
    )
