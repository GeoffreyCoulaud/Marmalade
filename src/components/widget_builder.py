from typing import Any, Generic, Self, Sequence, TypeVar

from gi.repository import Gtk

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
            if not callable(setter := getattr(self.__widget, f"set_{key}")):
                raise AttributeError(
                    "Widget type %s doesn't have a setter for property %s"
                    % (self.__widget_class_name, key)
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
            self.__widget.set_child(children[0])  # type: ignore
        else:
            # Cannot set children
            raise TypeError(
                f"Widgets ${self.__widget_class_name} may not receive children"
            )
        return self

    def build(self) -> WidgetType:
        """Build the widget according to the instructions"""
        return self.__widget
