from gi.repository import GObject, Gtk
from jellyfin_api_client.models.user_dto import UserDto

from src import build_constants
from src.components.user_badge import UserBadge
from src.components.user_picker_page import UserPickerPage
from src.database.api import ServerInfo


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/user_picker.ui")
class UserPicker(Gtk.Box):
    __gtype_name__ = "MarmaladeUserPicker"

    @GObject.Signal(name="user-picked", arg_types=[str, str])
    def user_picked(self, _username: str, _user_id: str):
        """Signal emitted when a user is picked"""

    carousel = Gtk.Template.Child()
    previous_page_button = Gtk.Template.Child()
    next_page_button = Gtk.Template.Child()

    __server: ServerInfo

    def __init__(
        self,
        *args,
        server: ServerInfo,
        users: list[UserDto],
        lines: int = 2,
        columns: int = 4,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__server = server

        self.previous_page_button.connect("clicked", self.on_previous_clicked)
        self.next_page_button.connect("clicked", self.on_next_clicked)
        self.carousel.connect("page-changed", self.on_page_changed)

        # Fill in the carousel
        max_users_per_page = lines * columns
        for i in range(0, len(users), max_users_per_page):
            page_users = users[i : i + max_users_per_page]
            page = UserPickerPage()
            page_columns = min(columns, len(page_users))
            page.set_max_children_per_line(page_columns)
            page.set_min_children_per_line(page_columns)
            for user in page_users:
                badge = UserBadge(server=self.__server, user=user)
                badge.connect("clicked", self.on_user_clicked, user.name, user.id)
                page.append(badge)
            self.carousel.append(page)
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
        self.next_page_button.set_sensitive(index < self.carousel.get_n_pages() - 1)
        self.previous_page_button.set_sensitive(index > 0)

    def on_user_clicked(self, _emitter, username: str, user_id: str) -> None:
        self.emit("user-picked", username, user_id)
