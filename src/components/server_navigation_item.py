from gi.repository import GLib, GObject, Gtk

from src import build_constants


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_navigation_item.ui"
)
class ServerNavigationItem(Gtk.ListBoxRow):
    __gtype_name__ = "MarmaladeServerNavigationItem"

    __image: Gtk.Image = Gtk.Template.Child("image")
    __label: Gtk.Label = Gtk.Template.Child("label")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_action_name("browser.navigate")

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

    # title property

    __title: str

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.__label.get_label()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__label.set_label(value)

    def set_title(self, value: str):
        self.set_property("title", value)

    # destination property

    @GObject.Property(type=str)
    def destination(self) -> str:
        return self.get_action_target_value().get_string()

    def get_destination(self) -> str:
        return self.get_property("destination")

    @destination.setter
    def destination(self, value: str) -> None:
        self.set_action_target_value(GLib.Variant.new_string(value))

    def set_destination(self, value: str):
        self.set_property("destination", value)
