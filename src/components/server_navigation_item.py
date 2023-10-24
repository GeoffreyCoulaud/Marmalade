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

    def set_icon_name(self, icon_name: str):
        self.__image.set_from_icon_name(icon_name)

    def get_icon_name(self) -> str:
        return self.__image.get_icon_name()

    @GObject.Property(type=str, default="")
    def icon_name(self) -> str:
        return self.get_icon_name()

    @icon_name.setter
    def icon_name(self, value: str) -> None:
        self.set_icon_name(value)

    # title property

    def set_title(self, title: str):
        self.__label.set_label(title)

    def get_title(self) -> str:
        return self.__label.get_label()

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.get_title()

    @title.setter
    def title(self, value: str) -> None:
        self.set_title(value)

    # destination property

    def set_destination(self, destination: str):
        variant = GLib.Variant.new_string(destination)
        self.set_action_target_value(variant)

    def get_destination(self) -> str:
        variant: GLib.Variant = self.get_action_target_value()
        return variant.get_string()

    @GObject.Property(type=str)
    def destination(self) -> str:
        return self.get_destination()

    @destination.setter
    def destination(self, value: str) -> None:
        self.set_destination(value)
