from typing import Optional

from gi.repository import GObject, Gtk

from src import build_constants
from src.components.user_badge import UserBadge
from src.components.user_picker_page import UserPickerPage
from src.database.api import ServerInfo, UserInfo


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/user_picker.ui")
class UserPicker(Gtk.Box):
    __gtype_name__ = "MarmaladeUserPicker"

    # fmt: off
    __carousel        = Gtk.Template.Child("carousel")
    __dots            = Gtk.Template.Child("dots")
    __next_button     = Gtk.Template.Child("next_button")
    __previous_button = Gtk.Template.Child("previous_button")
    __title_label     = Gtk.Template.Child("title_label")
    # fmt: on

    __server: Optional[ServerInfo] = None
    __users: list[UserInfo]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__users = []
        self.__next_button.connect("clicked", self.__on_next_button_clicked)
        self.__previous_button.connect("clicked", self.__on_previous_button_clicked)
        self.__carousel.connect("page-changed", self.__on_page_changed)
        self.__carousel.connect("notify::n-pages", self.__on_n_pages_changed)

    @GObject.Signal(name="user-picked", arg_types=[str])
    def user_picked(self, _user_id: str):
        """Signal emitted when a user is picked"""

    # lines property

    __lines: int

    @GObject.Property(type=int, default=1)
    def lines(self) -> int:
        return self.__lines

    def get_lines(self) -> int:
        return self.get_property("lines")

    @lines.setter
    def lines(self, value: int) -> None:
        self.__lines = value

    def set_lines(self, value: int):
        self.set_property("lines", value)

    # columns property

    __columns: int

    @GObject.Property(type=int, default=4)
    def columns(self) -> int:
        return self.__columns

    def get_columns(self) -> int:
        return self.get_property("columns")

    @columns.setter
    def columns(self, value: int) -> None:
        self.__columns = value

    def set_columns(self, value: int):
        self.set_property("columns", value)

    # title property

    __title: str

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.__title_label.get_title()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__title_label.set_title(value)
        self.__title_label.set_visible(len(value) > 0)

    def set_title(self, value: str):
        self.set_property("title", value)

    # n_pages property

    @GObject.Property(
        type=int,
        flags=GObject.ParamFlags.READABLE | GObject.ParamFlags.EXPLICIT_NOTIFY,
    )
    def n_pages(self) -> int:
        return self.__carousel.get_n_pages()

    def get_n_pages(self) -> int:
        return self.get_property("n_pages")

    # Callbacks

    def __on_previous_button_clicked(self, _button) -> None:
        self.__shift_carousel(-1)

    def __on_next_button_clicked(self, _button) -> None:
        self.__shift_carousel(1)

    def __on_page_changed(self, _carousel, index) -> None:
        self.__next_button.set_sensitive(index < self.__carousel.get_n_pages() - 1)
        self.__previous_button.set_sensitive(index > 0)

    def __on_n_pages_changed(self, _carousel, _value) -> None:
        self.__update_navigation()
        self.notify("n_pages")

    def __on_user_clicked(self, _emitter, user_id: str) -> None:
        self.emit("user-picked", user_id)

    # Python-side methods

    def __clear_pages(self) -> None:
        for _i in range(self.__carousel.get_n_pages()):
            page = self.__carousel.get_nth_page(0)
            self.__carousel.remove(page)

    def __create_pages(self) -> None:
        users_per_page = self.__lines * self.__columns
        for i in range(0, len(self.__users), users_per_page):
            page_users = self.__users[i : i + users_per_page]
            page = UserPickerPage()
            page_columns = min(self.__columns, len(page_users))
            page.set_max_children_per_line(page_columns)
            page.set_min_children_per_line(page_columns)
            for user in page_users:
                badge = UserBadge(server=self.__server, user=user)
                badge.connect("clicked", self.__on_user_clicked, user.user_id)
                page.append(badge)
            self.__carousel.append(page)

    def __update_navigation(self) -> None:
        has_multiple_pages = self.get_n_pages() > 1
        for widget in (
            self.__previous_button,
            self.__next_button,
            self.__dots,
        ):
            widget.set_visible(has_multiple_pages)

    def __recreate_pages(self) -> None:
        self.__clear_pages()
        self.__create_pages()
        self.__update_navigation()

    def __shift_carousel(self, offset: int = 1, animate: bool = True) -> None:
        """Navigate the carousel relatively"""
        position = self.__carousel.get_position()
        destination = max(0, min(self.get_n_pages() - 1, position + offset))
        destination_page = self.__carousel.get_nth_page(destination)
        self.__carousel.scroll_to(destination_page, animate=animate)

    def clear(self) -> None:
        """Remove all users from the user picker"""
        self.__users.clear()
        self.__clear_pages()
        self.__update_navigation()

    def set_server(self, server: ServerInfo) -> None:
        self.__server = server

    def append(self, *users: UserInfo, allow_duplicates: bool = False) -> None:
        """
        Append users to the user picker.

        Adding users befort calling set_server is prohibited.
        Duplicate users will not be added unless explicitely specified.
        """

        # Check that server is set
        # (Will be needed by the user badges)
        assert self.__server is not None, "Cannot append users when server is None"

        # Add new users
        new_users = []
        if allow_duplicates:
            new_users.extend(users)
        else:
            current_users_set = set(self.__users)
            new_users_set = set()
            for user in users:
                is_duplicate = user in current_users_set or user in new_users_set
                if not allow_duplicates and is_duplicate:
                    continue
                new_users_set.add(user)
                new_users.append(user)
        self.__users.extend(new_users)

        # Display
        self.__clear_pages()
        self.__create_pages()
        self.__update_navigation()
