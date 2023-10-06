import logging
import time

from gi.repository import Adw, Gio, GObject, Gtk

from src import build_constants
from src.server import Server
from src.task import Task


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/auth_quick_connect_view.ui"
)
class AuthQuickConnectView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthQuickConnectView"

    refresh_button = Gtk.Template.Child()
    connect_button = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()
    code_state_stack = Gtk.Template.Child()
    code_label = Gtk.Template.Child()

    server: Server
    __secret: str
    __cancellable: Gio.Cancellable

    @GObject.Signal(name="authenticated", arg_types=[object, str, str])
    def authenticated(self, _server: Server, _user_id: str, _token: str):
        """Signal emitted when the user is authenticated"""

    def __init__(self, server: Server, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.server = server
        self.refresh_button.connect("clicked", self.on_refresh_requested)
        self.connect_button.connect("clicked", self.on_connect_requested)
        self.__cancellable = Gio.Cancellable()
        self.__secret = ""
        self.on_refresh_requested(None)

    def on_refresh_requested(self, _button) -> None:
        logging.debug("Requested a new Quick Connect code")
        self.__cancellable.cancel()
        self.__cancellable.reset()
        self.code_state_stack.set_visible_child_name("loading")
        refresh_task = Task(
            main=self.refresh,
            cancellable=self.__cancellable,
            return_on_cancel=True,
        )
        refresh_task.run()

    def refresh(self) -> None:
        # TODO implement requesting a new quick connect code
        time.sleep(2)
        self.__secret = ""
        code = 123456
        label_markup = f'<span size="xx-large">{code}</span>'
        self.code_label.set_label(label_markup)
        self.code_state_stack.set_visible_child_name("code")

    def on_connect_requested(self, _widget) -> None:
        # TODO implement trying to connect with a quick connect code
        print(self.__secret)
