from gi.repository import Adw, Gtk

from src import build_constants


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_loading_view.ui"
)
class ServerLoadingView(Adw.Bin):
    __gtype_name__ = "MarmaladeServerLoadingView"
