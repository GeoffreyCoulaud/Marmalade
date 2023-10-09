from gi.repository import Adw, Gtk

from src import build_constants


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/disconnect_dialog.ui")
class DisconnectDialog(Adw.MessageDialog):
    __gtype_name__ = "MarmaladeDisconnectDialog"
