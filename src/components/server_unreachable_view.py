from gi.repository import Adw, Gtk

from src import build_constants


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_unreachable_view.ui"
)
class ServerUnreachableView(Adw.Bin):
    __gtype_name__ = "MarmaladeServerUnreachableView"
