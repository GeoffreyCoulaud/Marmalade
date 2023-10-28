from gi.repository import Adw, Gtk

from src import build_constants
from src.components.loading_view import LoadingView
from src.components.server_page import ServerPage


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_home_page.ui")
class ServerHomePage(ServerPage):
    __gtype_name__ = "MarmaladeServerHomePage"

    # fmt: off
    __toast_overlay: Adw.ToastOverlay = Gtk.Template.Child("toast_overlay")
    __view_stack: Adw.ViewStack       = Gtk.Template.Child("view_stack")
    __loading_view: LoadingView       = Gtk.Template.Child("loading_view")
    __error_view: Adw.StatusPage      = Gtk.Template.Child("error_view")
    __content_view                    = Gtk.Template.Child("content_view")
    # fmt: on

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__load_contents()

    def __load_contents(self) -> None:
        """Load the page contents asynchronously"""
        self.__view_stack.set_visible_child_name("loading")
        # TODO load page content
