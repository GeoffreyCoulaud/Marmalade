from gi.repository import Adw, GObject, Gtk

from src.components.widget_builder import Arguments, Children, Properties, build


class LoadingView(Gtk.Box):
    # Inheriting from Box to be able to override the "child" property,
    # which would not be possible using a widget that has it,
    # like for example Adw.Bin or Adw.Clamp

    __gtype_name__ = "MarmaladeLoadingView"

    __spinner: Gtk.Spinner
    __status_page: Adw.StatusPage
    __child_bin: Adw.Bin

    def __init_widget(self):
        self.__status_page = build(Adw.StatusPage)
        self.__child_bin = build(Adw.Bin)
        self.__spinner = build(
            Gtk.Spinner
            + Arguments(height_request=64, width_request=64)
            + Properties(halign=Gtk.Align.CENTER, spinning=False)
        )
        self.set_valign(Gtk.Align.CENTER)
        self.set_halign(Gtk.Align.CENTER)
        self.append(
            build(
                Adw.Clamp
                + Children(
                    Gtk.Box
                    + Properties(orientation=Gtk.Orientation.VERTICAL)
                    + Children(
                        self.__spinner,
                        self.__status_page,
                        self.__child_bin,
                    )
                )
            )
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_widget()

        self.connect("map", self.__on_mapped)
        self.connect("unmap", self.__on_unmapped)
        self.__hide_unused_status_page()

    def __hide_unused_status_page(self) -> None:
        title = self.__status_page.get_title()
        description = self.__status_page.get_description()
        self.__status_page.set_visible(bool(title or description))

    def __on_mapped(self, *args) -> None:
        self.__spinner.set_spinning(self.get_animate())

    def __on_unmapped(self, *args) -> None:
        self.__spinner.set_spinning(False)

    # child property

    @GObject.Property(type=Gtk.Widget, default=None)
    def child(self) -> Gtk.Widget | None:
        return self.__child_bin.get_child()

    def get_child(self) -> Gtk.Widget:
        return self.get_property("child")

    @child.setter
    def child_setter(self, value: Gtk.Widget) -> None:
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
    def title_setter(self, value: str) -> None:
        self.__status_page.set_title(value)
        self.__hide_unused_status_page()

    def set_title(self, value: str):
        self.set_property("title", value)

    # description property

    @GObject.Property(type=str, default="")
    def description(self) -> str | None:
        return self.__status_page.get_description()

    def get_description(self) -> str:
        return self.get_property("description")

    @description.setter
    def description_setter(self, value: str) -> None:
        self.__status_page.set_description(value)
        self.__hide_unused_status_page()

    def set_description(self, value: str):
        self.set_property("description", value)

    # animate property

    __animate: bool = True

    @GObject.Property(type=bool, default=True)
    def animate(self) -> bool:
        return self.__animate

    def get_animate(self) -> bool:
        return self.get_property("animate")

    @animate.setter
    def animate_setter(self, value: bool) -> None:
        self.__animate = value
        self.__spinner.set_spinning(self.__animate)

    def set_animate(self, value: bool):
        self.set_property("animate", value)
