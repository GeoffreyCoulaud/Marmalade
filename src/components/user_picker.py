from math import ceil
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

    title = Gtk.Template.Child()
    title_revealer = Gtk.Template.Child()
    carousel = Gtk.Template.Child()
    previous_button = Gtk.Template.Child()
    next_button = Gtk.Template.Child()
    dots = Gtk.Template.Child()

    n_pages: int = 0

    __server: ServerInfo

    def __init__(
        self,
        *args,
        server: ServerInfo,
        users: list[UserInfo],
        lines: int = 1,
        columns: int = 4,
        title: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Create a user picker widget"""
        super().__init__(*args, **kwargs)

        # TODO allow creating an empty picker then adding users
        if len(users) == 0:
            raise AssertionError("User picker cannot be empty")

        self.__server = server

        self.previous_button.connect("clicked", self.on_previous_clicked)
        self.next_button.connect("clicked", self.on_next_clicked)
        self.carousel.connect("page-changed", self.on_page_changed)

        # Picker title
        if title:
            self.title.set_label(title)
            self.title_revealer.set_reveal_child(True)

        # Fill in the carousel
        max_users_per_page = lines * columns
        self.n_pages = ceil(len(users) / max_users_per_page)
        for i in range(0, len(users), max_users_per_page):
            page_users = users[i : i + max_users_per_page]
            page = UserPickerPage()
            page_columns = min(columns, len(page_users))
            page.set_max_children_per_line(page_columns)
            page.set_min_children_per_line(page_columns)
            for user in page_users:
                badge = UserBadge(server=self.__server, user=user)
                badge.connect("clicked", self.on_user_clicked, user.user_id)
                page.append(badge)
            self.carousel.append(page)

        # Hide or show the navigation controls
        has_multiple_pages = self.n_pages > 1
        navigation_widgets = [self.dots, self.previous_button, self.next_button]
        for widget in navigation_widgets:
            widget.set_visible(has_multiple_pages)

        # Update navigation
        self.on_page_changed(self.carousel, 0)

    def __shift_carousel(self, offset: int = 1, animate: bool = True) -> None:
        """Navigate the carousel relatively"""
        page = self.carousel.get_nth_page(self.carousel.get_position() + offset)
        self.carousel.scroll_to(page, animate=animate)

    def on_previous_clicked(self, _button) -> None:
        self.__shift_carousel(-1)

    def on_next_clicked(self, _button) -> None:
        self.__shift_carousel(1)

    def on_page_changed(self, _carousel, index) -> None:
        """Toggle previous / next buttons if necessary"""
        self.next_button.set_sensitive(index < self.carousel.get_n_pages() - 1)
        self.previous_button.set_sensitive(index > 0)

    def on_user_clicked(self, _emitter, user_id: str) -> None:
        self.emit("user-picked", user_id)
