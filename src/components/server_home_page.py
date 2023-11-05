import logging
from http import HTTPStatus
from typing import Callable, Sequence

from gi.repository import Adw, GLib, Gtk
from httpx import Response
from jellyfin_api_client.api.items import get_resume_items
from jellyfin_api_client.api.tv_shows import get_next_up
from jellyfin_api_client.api.user_library import get_latest_media
from jellyfin_api_client.api.user_views import get_user_views
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.base_item_dto import BaseItemDto

from src import build_constants
from src.components.loading_view import LoadingView
from src.components.server_browser import ServerBrowser
from src.components.server_page import ServerPage
from src.components.shelf import Shelf
from src.jellyfin import JellyfinClient
from src.task import Task


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_home_page.ui")
class ServerHomePage(ServerPage):
    __gtype_name__ = "MarmaladeServerHomePage"

    # fmt: off
    __toast_overlay: Adw.ToastOverlay = Gtk.Template.Child("toast_overlay")
    __view_stack: Adw.ViewStack       = Gtk.Template.Child("view_stack")
    __loading_view: LoadingView       = Gtk.Template.Child("loading_view")
    __error_view: Adw.StatusPage      = Gtk.Template.Child("error_view")
    __content_view: Gtk.Box           = Gtk.Template.Child("content_view")
    __resume_watching_shelf: Shelf    = Gtk.Template.Child("resume_watching_shelf")
    __next_up_shelf: Shelf            = Gtk.Template.Child("next_up_shelf")
    # fmt: on

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__load_contents()

    def __load_contents(self) -> None:
        """Load the page contents asynchronously"""

        def query_libraries(browser: ServerBrowser) -> Sequence[BaseItemDto]:
            """Query user libraries"""
            response = get_user_views.sync_detailed(
                browser.get_user_id(), client=browser.get_client()
            )
            if response.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(response.status_code, response.content)
            return response.parsed.items

        def on_libraries_error(error: Exception) -> None:
            logging.error("Error while loading user libraries", exc_info=error)
            toast = Adw.Toast(title=_("Could not load user libraries"))
            toast.set_timeout(0)
            toast.set_button_label(_("Details"))
            toast.set_action_name("app.error-details")
            toast.set_action_target_value(
                GLib.Variant.new_strv([_("User Libraries Error"), str(error)])
            )
            self.__toast_overlay.add_toast(toast)

        def on_libraries_success(items: Sequence[BaseItemDto]) -> None:
            # Add the library shelves
            for item in items:
                # TODO filter out collection libraries (and maybe others?)
                shelf = Shelf()
                shelf.set_title(_("Latest in {library}").format(library=item.name))
                self.__content_view.append(shelf)
                # TODO query library shelf content in a task

        def query_shelf_items(shelf: Shelf, request_func: Callable) -> None:
            response: Response = request_func()
            if response.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(response.status_code, response.content)
            return response.parsed.items

        def on_shelf_items_error(shelf: Shelf, error: Exception) -> None:
            # TODO Handle shelf content error
            pass

        def on_shelf_items_success(shelf: Shelf, result: Sequence[BaseItemDto]) -> None:
            # TODO Create the "Item Card" component
            # TODO add shelf content
            pass

        self.__view_stack.set_visible_child_name("content")

        # Spawn content query tasks
        tasks = (
            Task(
                main=query_libraries,
                main_args=(self.get_browser(),),
                callback=on_libraries_success,
                error_callback=on_libraries_error,
            ),
            # TODO Add "resume watching" shelf content task
            # TODO Add "up next" shelf content task
        )
        for task in tasks:
            task.run()
