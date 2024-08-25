from typing import Callable

from gi.repository import Adw, GObject, Gtk

from src import shared
from src.components.user_picker import UserPicker
from src.components.widget_builder import (
    Children,
    Handlers,
    Properties,
    TypedChild,
    build,
)
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

        self.__cancel_button = build(
            Gtk.Button
            + Properties(label=_("Cancel"))
            + Handlers(clicked=self.__on_cancel_button_clicked)
        )

        self.__user_picker = build(
            UserPicker
            + Properties(title=_("Resume Session"), columns=4, lines=1)
            + Handlers(user_picked=self.__on_quick_resume_picked)
        )

        def next_button_factory(clicked_handler: Callable) -> Gtk.Button:
            return build(
                Gtk.Button
                + Properties(valign=Gtk.Align.CENTER, icon_name="go-next-symbolic")
                + Handlers(clicked=clicked_handler)
            )

        self.__username_password_button = next_button_factory(
            clicked_handler=self.__on_credentials_clicked
        )
        self.__quick_connect_button = next_button_factory(
            clicked_handler=self.__on_quick_connect_clicked
        )

        def auth_method_row_factory(
            title: str,
            icon: str,
            activatable: Gtk.Widget,
        ) -> Adw.ActionRow:
            return build(
                Adw.ActionRow
                + Properties(title=title, activatable_widget=activatable)
                + TypedChild("suffix", activatable)
                + TypedChild(
                    "prefix",
                    Gtk.Image
                    + Properties(
                        margin_top=16,
                        margin_bottom=16,
                        margin_start=10,
                        margin_end=16,
                        icon_size=Gtk.IconSize.LARGE,
                        from_icon_name=icon,
                    ),
                )
            )

        header_bar = (
            Adw.HeaderBar
            + Properties(decoration_layout="")
            + TypedChild("start", self.__cancel_button)
        )

        content_auth_methods = (
            Adw.PreferencesGroup
            + Properties(
                title=_("Authenticate"),
                margin_start=48,
                margin_end=48,
            )
            + Children(
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
            )
        )

        content = (
            Adw.Clamp
            + Properties(
                margin_top=16,
                margin_bottom=16,
                margin_start=16,
                margin_end=16,
            )
            + Children(
                Gtk.Box
                + Properties(
                    orientation=Gtk.Orientation.VERTICAL,
                    spacing=16,
                )
                + Children(
                    self.__user_picker,
                    content_auth_methods,
                )
            )
        )

        self.set_title(_("Login Method"))
        self.set_can_pop(False)
        self.set_child(
            build(
                Adw.ToolbarView
                + TypedChild("top", header_bar)
                + TypedChild("content", content)
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

    def __on_cancel_button_clicked(self, _button) -> None:
        self.emit("cancelled")

    def __on_credentials_clicked(self, _button) -> None:
        self.emit("chose-username-password")

    def __on_quick_connect_clicked(self, _button) -> None:
        self.emit("chose-quick-connect")

    def __on_quick_resume_picked(self, _picker, user_id: str) -> None:
        self.emit("authenticated", user_id)
