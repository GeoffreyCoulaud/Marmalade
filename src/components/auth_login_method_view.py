from typing import Callable

from gi.repository import Adw, GObject, Gtk

from src import shared
from src.components.user_picker import UserPicker
from src.components.widget_factory import WidgetFactory
from src.database.api import ServerInfo


class AuthLoginMethodView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeAuthLoginMethodView"

    __cancel_button: Gtk.Button
    __username_password_button: Gtk.Button
    __quick_connect_button: Gtk.Button
    __user_picker: UserPicker

    __server: ServerInfo

    @GObject.Signal(name="cancelled")
    def user_picked(self):
        """Signal emitted when the user cancels the login process"""

    @GObject.Signal(name="chose-username-password")
    def chose_username_password(self):
        """Signal emitted when the user chooses to log in via username and password"""

    @GObject.Signal(name="chose-quick-connect")
    def chose_quick_connect(self):
        """Signal emitted when the user chooses to log in via quick connect"""

    @GObject.Signal(name="authenticated", arg_types=[str])
    def authenticated(self, _user_id: str):
        """Signal emitted when a user is authenticated via quick resume"""

    def __init_widget(self):

        self.__cancel_button = WidgetFactory(
            klass=Gtk.Button,
            signal_handlers={"clicked": self.on_cancel_button_clicked},
            properties={"label": _("Cancel")},
        )
        self.__user_picker = WidgetFactory(
            klass=UserPicker,
            signal_handlers={"user-picked": self.on_quick_resume_picked},
            properties={
                "title": _("Resume Session"),
                "columns": 4,
                "lines": 1,
            },
        )

        def next_button_factory(clicked_handler: Callable) -> Gtk.Button:
            return WidgetFactory(
                klass=Gtk.Button,
                signal_handlers={"clicked": clicked_handler},
                properties={
                    "valign": Gtk.Align.CENTER,
                    "icon_name": "go-next-symbolic",
                },
            )

        self.__username_password_button = next_button_factory(
            clicked_handler=self.on_credentials_clicked
        )
        self.__quick_connect_button = next_button_factory(
            clicked_handler=self.on_quick_connect_clicked
        )

        def auth_method_row_factory(
            title: str,
            icon: str,
            activatable: Gtk.Widget,
        ) -> Adw.ActionRow:
            return WidgetFactory(
                Adw.ActionRow,
                properties={"title": title, "activatable_widget": activatable},
                children=[
                    WidgetFactory(
                        Gtk.Image,
                        properties={
                            "margin_top": 16,
                            "margin_bottom": 16,
                            "margin_start": 10,
                            "margin_end": 16,
                            "icon_size": Gtk.IconSize.LARGE,
                            "from_icon_name": icon,
                        },
                    ),
                    activatable,
                ],
            )

        self.set_title(_("Login Method"))
        self.set_can_pop(False)
        self.set_child(
            WidgetFactory(
                klass=Adw.ToolbarView,
                children=[
                    WidgetFactory(
                        klass=Adw.HeaderBar,
                        properties={"decoration_layout": ""},
                        children=[
                            self.__cancel_button,
                            None,
                            None,
                        ],
                    ),
                    WidgetFactory(
                        klass=Adw.Clamp,
                        properties={
                            "margin_top": 16,
                            "margin_bottom": 16,
                            "margin_start": 16,
                            "margin_end": 16,
                        },
                        children=WidgetFactory(
                            klass=Gtk.Box,
                            properties={
                                "orientation": Gtk.Orientation.VERTICAL,
                                "spacing": 16,
                            },
                            children=[
                                self.__user_picker,
                                WidgetFactory(
                                    klass=Adw.PreferencesGroup,
                                    properties={
                                        "title": _("Authenticate"),
                                        "margin_start": 48,
                                        "margin_end": 48,
                                    },
                                    children=[
                                        auth_method_row_factory(
                                            title=_("Username &amp; Password"),
                                            icon="dialog-password-symbolic",
                                            activatable=self.__username_password_button,
                                        ),
                                        auth_method_row_factory(
                                            title=_("Quick Connect"),
                                            icon="phonelink-symbolic",
                                            activatable=self.__quick_connect_button,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    None,
                ],
            )
        )

    def __init__(self, *args, server: ServerInfo, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__init_widget()

        self.__server = server
        self.__user_picker.set_server(self.__server)

        self.discover_authenticated_users()

    def discover_authenticated_users(self) -> None:
        """Discover the authenticated users and display them"""
        users = shared.settings.get_authenticated_users(self.__server.address)
        has_users = len(users) > 0
        self.__user_picker.set_visible(has_users)
        if not has_users:
            return
        self.__user_picker.append(*users)

    def on_cancel_button_clicked(self, _button) -> None:
        self.emit("cancelled")

    def on_credentials_clicked(self, _button) -> None:
        self.emit("chose-username-password")

    def on_quick_connect_clicked(self, _button) -> None:
        self.emit("chose-quick-connect")

    def on_quick_resume_picked(self, _picker, user_id: str) -> None:
        self.emit("authenticated", user_id)
