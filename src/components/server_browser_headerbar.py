from gi.repository import Adw, GObject, Gtk

from src import build_constants


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_browser_headerbar.ui"
)
class ServerBrowserHeaderbar(Gtk.HeaderBar):
    __gtype_name__ = "MarmaladeServerBrowserHeaderbar"

    # fmt: off
    __back_button                  = Gtk.Template.Child("back_button")
    __disconnect_button            = Gtk.Template.Child("disconnect_button")
    __filter_button_revealer       = Gtk.Template.Child("filter_button_revealer")
    __search_button                = Gtk.Template.Child("search_button")
    __search_button_revealer       = Gtk.Template.Child("search_button_revealer")
    __sidebar_show_button          = Gtk.Template.Child("sidebar_show_button")
    __sidebar_show_button_revealer = Gtk.Template.Child("sidebar_show_button_revealer")
    __title                        = Gtk.Template.Child("title")
    # TODO Expose signals and methods instead many public attributes
    filter_button                  = Gtk.Template.Child()
    header_center_stack            = Gtk.Template.Child()
    header_left_stack              = Gtk.Template.Child()
    path_bar                       = Gtk.Template.Child()
    preferences_button             = Gtk.Template.Child()
    search_bar                     = Gtk.Template.Child()
    # fmt: on

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__back_button.connect("clicked", self.__on_back_clicked)
        self.__disconnect_button.connect("clicked", self.__on_disconnect_clicked)
        self.__sidebar_show_button.connect("clicked", self.__on_sidebar_show_clicked)
        self.__search_button.connect("toggled", self.__on_search_toggled)

    def __on_disconnect_clicked(self, *_args) -> None:
        self.emit("disconnect-request")

    def __on_back_clicked(self, *_args) -> None:
        self.emit("go-back-request")

    def __on_sidebar_show_clicked(self, *_args) -> None:
        self.emit("show-sidebar-request")

    def __on_search_toggled(self, *_args) -> None:
        name = "search" if self.__search_button.get_active() else "title"
        self.header_center_stack.set_visible_child_name(name)

    @GObject.Signal(name="disconnect-request")
    def disconnect_request(self):
        """Signal emitted when the user clicks the disconnect button"""

    @GObject.Signal(name="show-sidebar-request")
    def show_sidebar_request(self):
        """Signal emitted when the user clicks the show sidebar button"""

    @GObject.Signal(name="go-back-request")
    def go_back_request(self):
        """Signal emitted when the user clicks on the back button"""

    # title property

    def set_title(self, title: str):
        self.__title.set_title(title)

    def get_title(self) -> str:
        return self.__title.get_title()

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.get_title()

    @title.setter
    def title(self, value: str) -> None:
        self.set_title(value)

    # show_sidebar_button_visible property

    def set_show_sidebar_button_visible(self, visible: bool):
        self.__sidebar_show_button_revealer.set_reveal_child(visible)

    def get_show_sidebar_button_visible(self) -> bool:
        raise self.__sidebar_show_button_revealer.get_reveal_child()

    @GObject.Property(nick="show-sidebar-button-visible", type=bool, default=True)
    def show_sidebar_button_visible(self) -> bool:
        return self.get_show_sidebar_button_visible()

    @show_sidebar_button_visible.setter
    def show_sidebar_button_visible(self, value: bool) -> None:
        self.set_show_sidebar_button_visible(value)

    # filter_button_visible property

    def set_filter_button_visible(self, visible: bool):
        self.__filter_button_revealer.set_reveal_child(visible)

    def get_filter_button_visible(self) -> bool:
        return self.__filter_button_revealer.get_reveal_child()

    @GObject.Property(type=bool, default=True)
    def filter_button_visible(self) -> bool:
        return self.get_filter_button_visible()

    @filter_button_visible.setter
    def filter_button_visible(self, value: bool) -> None:
        self.set_filter_button_visible(value)

    # search_visible property

    def set_search_visible(self, visible: bool):
        self.__search_button_revealer.set_reveal_child(visible)
        if not visible:
            self.header_center_stack.set_visible_child_name("title")

    def get_search_visible(self) -> bool:
        return self.__search_button_revealer.get_reveal_child()

    @GObject.Property(type=bool, default=True)
    def search_visible(self) -> bool:
        return self.get_search_visible()

    @search_visible.setter
    def search_visible(self, value: bool) -> None:
        self.set_search_visible(value)
