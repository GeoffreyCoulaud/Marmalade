from typing import Optional

from gi.repository import Adw, GObject

from src.components.shelf import Shelf
from src.components.user_badge import UserBadge
from src.database.api import ServerInfo, UserInfo


class UserPicker(Adw.Bin):
    """User picker widget"""

    __gtype_name__ = "MarmaladeUserPicker"

    __server: Optional[ServerInfo] = None
    __users: list[UserInfo]

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
        return self.__title

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title(self, value: str) -> None:
        self.__title = value

    def set_title(self, value: str):
        self.set_property("title", value)

    # is_navigation_visible property

    __is_navigation_visible: bool

    @GObject.Property(type=bool, default=False)
    def is_navigation_visible(self) -> bool:
        return self.__is_navigation_visible

    def get_is_navigation_visible(self) -> bool:
        return self.get_property("is_navigation_visible")

    # Private python methods

    def __on_user_clicked(self, _emitter, user_id: str) -> None:
        self.emit("user-picked", user_id)

    # Public python methods

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__users = []

        # HACK: Using a delegate Shelf widget, since PyGObject doesn't allow inheriting
        # from classes decorated with @Gtk.Template
        self.set_child(shelf := Shelf())

        # Bind read-only props
        flags = GObject.BindingFlags.SYNC_CREATE
        for prop in ("is_navigation_visible",):
            shelf.bind_property(prop, self, prop, flags)

        # Read-write props
        flags |= GObject.BindingFlags.BIDIRECTIONAL
        for prop in ("title", "lines", "columns"):
            shelf.bind_property(prop, self, prop, flags)

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

        shelf = self.get_child()
        for user in new_users:
            badge = UserBadge(server=self.__server, user=user)
            badge.connect("clicked", self.__on_user_clicked, user.user_id)
            shelf.append(badge)
