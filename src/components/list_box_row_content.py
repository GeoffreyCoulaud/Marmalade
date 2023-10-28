from gi.repository import Adw, GObject, Gtk

from src import build_constants


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/list_box_row_content.ui"
)
class ListBoxRowContent(Gtk.Box):
    __gtype_name__ = "MarmaladeListBoxRowContent"

    # fmt: off
    __image: Gtk.Image = Gtk.Template.Child("image")
    __label: Gtk.Label = Gtk.Template.Child("label")
    # fmt: on

    # icon_name property

    @GObject.Property(type=str, default="")
    def icon_name(self) -> str:
        return self.__image.get_icon_name()

    def get_icon_name(self) -> str:
        return self.get_property("icon_name")

    @icon_name.setter
    def icon_name(self, value: str) -> None:
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
    def label(self, value: str) -> None:
        self.__label.set_label(value)

    def set_label(self, value: str):
        self.set_property("label", value)
