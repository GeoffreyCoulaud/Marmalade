from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.server import Server
from src.task import Task


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_user_select_view.ui"
)
class AuthUserSelectView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthUserSelectView"

    other_user_button = Gtk.Template.Child()
    user_picker_wrapper = Gtk.Template.Child()
    server: Server

    @GObject.Signal(name="user-picked", arg_types=[str])
    def user_picked(self, _username: str):
        """Signal emitted when a user is picked"""

    def __init__(self, server: Server, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        self.other_user_button.connect("clicked", self.on_other_user_button_clicked)
        discover_task = Task(main=self.discover)
        discover_task.run()

    def discover(self) -> None:
        # TODO get public users from the server
        # TODO create the user picker
        pass

    def on_user_picked(self, _picker, username: str) -> None:
        self.emit("user-picked", username)

    def on_other_user_button_clicked(self, _widget) -> None:
        self.emit("user-picked", "")
