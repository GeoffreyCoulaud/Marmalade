from gi.repository import Adw, GObject, Gtk

from src import build_constants


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/loading_view.ui")
class LoadingView(Gtk.Box):
    __gtype_name__ = "MarmaladeLoadingView"

    # fmt: off
    __spinner: Gtk.Spinner         = Gtk.Template.Child("spinner")
    __status_page: Adw.StatusPage  = Gtk.Template.Child("status_page")
    __child_bin: Adw.Bin           = Gtk.Template.Child("child_bin")
    # fmt: on

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connect("map", self.__on_mapped)
        self.connect("unmap", self.__on_unmapped)
        self.__hide_unused_status_page()

    def __hide_unused_status_page(self) -> None:
        title = self.__status_page.get_title()
        description = self.__status_page.get_description()
        self.__status_page.set_visible(title or description)

    def __on_mapped(self, *args) -> None:
        self.__spinner.set_spinning(self.get_animate())

    def __on_unmapped(self, *args) -> None:
        self.__spinner.set_spinning(False)

    # child property

    @GObject.Property(type=Gtk.Widget, default=None)
    def child(self) -> Gtk.Widget:
        return self.__child_bin.get_child()

    def get_child(self) -> Gtk.Widget:
        return self.get_property("child")

    @child.setter
    def child(self, value: Gtk.Widget) -> None:
        self.__child_bin.set_child(value)

    def set_child(self, value: Gtk.Widget):
        self.set_property("child", value)

    # title property

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.__status_page.get_title()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__status_page.set_title(value)
        self.__hide_unused_status_page()

    def set_title(self, value: str):
        self.set_property("title", value)

    # description property

    @GObject.Property(type=str, default="")
    def description(self) -> str:
        return self.__status_page.get_description()

    def get_description(self) -> str:
        return self.get_property("description")

    @description.setter
    def description(self, value: str) -> None:
        self.__status_page.set_description(value)
        self.__hide_unused_status_page()

    def set_description(self, value: str):
        self.set_property("description", value)

    # animate property

    __animate: bool

    @GObject.Property(type=bool, default=True)
    def animate(self) -> bool:
        return self.__animate

    def get_animate(self) -> bool:
        return self.get_property("animate")

    @animate.setter
    def animate(self, value: bool) -> None:
        self.__animate = value
        self.__spinner.set_spinning(self.__animate)

    def set_animate(self, value: bool):
        self.set_property("animate", value)
