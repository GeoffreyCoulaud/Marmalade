from gi.repository import Adw, Gtk

from src import build_constants
from src.components.server_page import ServerPage


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_home_page.ui")
class ServerHomePage(Adw.NavigationPage, ServerPage):
    __gtype_name__ = "MarmaladeServerHomePage"

    # fmt: off
    __toast_overlay  = Gtk.Template.Child("toast_overlay")
    __view_stack     = Gtk.Template.Child("view_stack")
    __loading_status = Gtk.Template.Child("loading_status")
    __error_status   = Gtk.Template.Child("error_status")
    __content        = Gtk.Template.Child("content")
    # fmt: on

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_is_searchable(True)
        self.set_is_filterable(False)
        self.set_is_root(True)
        self.__load_contents()

    def __load_contents(self) -> None:
        """Load the page contents asynchronously"""
        self.__view_stack.set_visible_child_name("loading")
        # TODO load page content
