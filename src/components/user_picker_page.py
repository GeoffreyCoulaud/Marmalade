from gi.repository import Gtk

from src import build_constants


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/user_picker_page.ui")
class UserPickerPage(Gtk.FlowBox):
    __gtype_name__ = "MarmaladeUserPickerPage"
