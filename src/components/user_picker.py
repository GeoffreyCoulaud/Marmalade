from typing import Optional

from gi.repository import GObject, Gtk

from src import build_constants
from src.components.user_badge import UserBadge
from src.components.user_picker_page import UserPickerPage
from src.database.api import ServerInfo, UserInfo


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/user_picker.ui")
class UserPicker(Gtk.Box):
    __gtype_name__ = "MarmaladeUserPicker"

    @GObject.Signal(name="user-picked", arg_types=[str])
    def user_picked(self, _user_id: str):
        """Signal emitted when a user is picked"""

    # lines property

    __lines: int = 1

    @GObject.Property(type=int)
    def lines(self) -> int:
        return self.__lines

    @lines.setter
    def lines(self, value: int) -> None:
        self.__lines = value
        self.__recreate_pages()

    def get_lines(self) -> int:
        return self.get_property("lines")

    def set_lines(self, value: int) -> None:
        self.set_property("lines", value)

    # columns property

    __columns: int = 4

    @GObject.Property(type=int)
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, value: int) -> None:
        self.__columns = value
        self.__recreate_pages()

    def get_columns(self) -> int:
        return self.get_property("columns")

    def set_columns(self, value: int) -> None:
        self.set_property("columns", value)

    # title property

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.title_label.get_label()

    @title.setter
    def title(self, text: str) -> None:
        self.title_label.set_label(text)
        self.title_revealer.set_reveal_child(len(text) > 0)

    def get_title(self) -> str:
        return self.get_property("title")

    def set_title(self, value: str) -> None:
        self.set_property("title", value)

    # n_pages property

    @GObject.Property(type=int)
    def n_pages(self) -> int:
        return self.carousel.get_n_pages()

    def get_n_pages(self) -> int:
        return self.get_property("n_pages")

    # server setter

    __server: Optional[ServerInfo] = None

    def set_server(self, server: ServerInfo) -> None:
        self.__server = server

    title_label = Gtk.Template.Child()
    title_revealer = Gtk.Template.Child()
    carousel = Gtk.Template.Child()
    previous_button = Gtk.Template.Child()
    next_button = Gtk.Template.Child()
    dots = Gtk.Template.Child()

    __users: list[UserInfo]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__users = []
        self.__server = None
        self.previous_button.connect("clicked", self.on_previous_clicked)
        self.next_button.connect("clicked", self.on_next_clicked)
        self.carousel.connect("page-changed", self.on_page_changed)

    def __clear_pages(self) -> None:
        for _i in range(self.carousel.get_n_pages()):
            page = self.carousel.get_nth_page(0)
            self.carousel.remove(page)

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
                badge.connect("clicked", self.on_user_clicked, user.user_id)
                page.append(badge)
            self.carousel.append(page)

    def __update_navigation(self) -> None:
        has_multiple_pages = self.carousel.get_n_pages() > 1
        navigation_widgets = [self.dots, self.previous_button, self.next_button]
        for widget in navigation_widgets:
            widget.set_visible(has_multiple_pages)
        self.on_page_changed(self.carousel, 0)

    def __recreate_pages(self) -> None:
        self.__clear_pages()
        self.__create_pages()
        self.__update_navigation()

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

    def clear(self) -> None:
        """Remove all users from the user picker"""
        self.__users.clear()
        self.__clear_pages()
        self.__update_navigation()

    def __shift_carousel(self, offset: int = 1, animate: bool = True) -> None:
        """Navigate the carousel relatively"""
        page = self.carousel.get_nth_page(self.carousel.get_position() + offset)
        self.carousel.scroll_to(page, animate=animate)

    def on_previous_clicked(self, _button) -> None:
        self.__shift_carousel(-1)

    def on_next_clicked(self, _button) -> None:
        self.__shift_carousel(1)

    def on_page_changed(self, _carousel, index) -> None:
        self.next_button.set_sensitive(index < self.carousel.get_n_pages() - 1)
        self.previous_button.set_sensitive(index > 0)

    def on_user_clicked(self, _emitter, user_id: str) -> None:
        self.emit("user-picked", user_id)
