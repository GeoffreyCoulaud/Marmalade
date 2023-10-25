from typing import Optional, Sequence

from gi.repository import GLib, GObject, Gtk

from src import build_constants


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_browser_headerbar.ui"
)
class ServerBrowserHeaderbar(Gtk.HeaderBar):
    __gtype_name__ = "MarmaladeServerBrowserHeaderbar"

    # fmt: off
    __back_button                  = Gtk.Template.Child("back_button")
    __disconnect_button            = Gtk.Template.Child("disconnect_button")
    __filter_button                = Gtk.Template.Child("filter_button")
    __filter_button_revealer       = Gtk.Template.Child("filter_button_revealer")
    __header_center_stack          = Gtk.Template.Child("header_center_stack")
    __header_left_stack            = Gtk.Template.Child("header_left_stack")
    __path_bar                     = Gtk.Template.Child("path_bar")
    __search_button_revealer       = Gtk.Template.Child("search_button_revealer")
    __sidebar_show_button          = Gtk.Template.Child("sidebar_show_button")
    __sidebar_show_button_revealer = Gtk.Template.Child("sidebar_show_button_revealer")
    __title                        = Gtk.Template.Child("title")
    # fmt: on

    # TODO Implement filter button

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__back_button.connect("clicked", self.__on_back_clicked)
        self.__disconnect_button.connect("clicked", self.__on_disconnect_clicked)
        self.__sidebar_show_button.connect("clicked", self.__on_sidebar_show_clicked)

    def __on_sidebar_show_clicked(self, *_args) -> None:
        self.activate_action("browser.hide-sidebar")

    def __on_disconnect_clicked(self, *_args) -> None:
        self.activate_action("browser.disconnect")

    def __on_back_clicked(self, *_args) -> None:
        self.activate_action("browser.navigate", GLib.Variant.new_string("back"))

    def toggle_back_button(self, back_button_shown: bool = True) -> None:
        name = "back" if back_button_shown else "disconnect"
        self.__header_left_stack.set_visible_child_name(name)

    # title property

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.__title.get_title()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__title.set_title(value)

    def set_title(self, value: str):
        self.set_property("title", value)

    # show_sidebar_button_visible property

    @GObject.Property(type=bool, default=True)
    def show_sidebar_button_visible(self) -> bool:
        return self.__sidebar_show_button_revealer.get_reveal_child()

    def get_show_sidebar_button_visible(self) -> bool:
        return self.get_property("show_sidebar_button_visible")

    @show_sidebar_button_visible.setter
    def show_sidebar_button_visible(self, value: bool) -> None:
        self.__sidebar_show_button_revealer.set_reveal_child(value)

    def set_show_sidebar_button_visible(self, value: bool):
        self.set_property("show_sidebar_button_visible", value)

    # filter_button_visible property

    @GObject.Property(type=bool, default=True)
    def filter_button_visible(self) -> bool:
        return self.__filter_button_revealer.get_reveal_child()

    def get_filter_button_visible(self) -> bool:
        return self.get_property("filter_button_visible")

    @filter_button_visible.setter
    def filter_button_visible(self, value: bool) -> None:
        self.__filter_button_revealer.set_reveal_child(value)

    def set_filter_button_visible(self, value: bool):
        self.set_property("filter_button_visible", value)

    # search_button_visible property

    @GObject.Property(type=bool, default=True)
    def search_button_visible(self) -> bool:
        return self.__search_button_revealer.get_reveal_child()

    def get_search_button_visible(self) -> bool:
        return self.get_property("search_button_visible")

    @search_button_visible.setter
    def search_button_visible(self, value: bool) -> None:
        self.__search_button_revealer.set_reveal_child(value)

    def set_search_button_visible(self, value: bool):
        self.set_property("search_button_visible", value)

    # ancestors property

    __ancestors: Optional[Sequence[tuple[str, str]]] = None

    @GObject.Property(type=object, default=None)
    def ancestors(self) -> Optional[Sequence[tuple[str, str]]]:
        # TODO get the ancestors from the pathbar
        return self.__ancestors

    def get_ancestors(self) -> Optional[Sequence[tuple[str, str]]]:
        return self.get_property("ancestors")

    @ancestors.setter
    def ancestors(self, value: Optional[Sequence[tuple[str, str]]]) -> None:
        # TODO implement pathbar widget (currently just a label)
        # TODO pass the ancestors to the pathbar
        self.__ancestors = value
        if has_path := value is not None and len(value) > 0:
            path = " / ".join((name for name, _uri in self.__ancestors))
            self.__path_bar.set_label(path)
        self.__header_center_stack.set_visible_child_name(
            "path" if has_path else "title"
        )

    def set_ancestors(self, value: Optional[Sequence[tuple[str, str]]]):
        self.set_property("ancestors", value)
