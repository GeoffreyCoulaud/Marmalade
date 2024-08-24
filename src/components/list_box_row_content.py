from gi.repository import GObject, Gtk, Pango

from src.components.widget_builder import Properties, WidgetBuilder, build


class ListBoxRowContent(Gtk.Box):
    __gtype_name__ = "MarmaladeListBoxRowContent"

    __image: Gtk.Image
    __label: Gtk.Label

    def __init_widget(self):
        self.__image = build(Gtk.Image)
        self.__label = build(
            Gtk.Label
            + Properties(
                wrap=True,
                wrap_mode=Pango.WrapMode.WORD,
            )
        )
        self.set_spacing(10)
        self.append(self.__image)
        self.append(self.__label)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__init_widget()

    # icon_name property

    @GObject.Property(type=str, default="")
    def icon_name(self) -> str | None:
        return self.__image.get_icon_name()

    def get_icon_name(self) -> str:
        return self.get_property("icon_name")

    @icon_name.setter
    def icon_name_setter(self, value: str) -> None:
        self.__image.set_from_icon_name(value)

    def set_icon_name(self, value: str):
        self.set_property("icon_name", value)

    # label property

    @GObject.Property(type=str, default="")
    def label(self) -> str:
        return self.__label.get_label()

    def get_label(self) -> str:
        return self.get_property("label")

    @label.setter
    def label_setter(self, value: str) -> None:
        self.__label.set_label(value)

    def set_label(self, value: str):
        self.set_property("label", value)
