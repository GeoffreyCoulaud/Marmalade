import logging
from http import HTTPStatus
from threading import Thread
from typing import Any, Sequence

from gi.repository import Adw, GLib, Gtk
from httpx import Response
from jellyfin_api_client.api.user_views import get_user_views
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.base_item_dto import BaseItemDto

from src import build_constants
from src.components.loading_view import LoadingView
from src.components.server_browser import ServerBrowser
from src.components.server_page import ServerPage
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
    __content_view                    = Gtk.Template.Child("content_view")
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
            # TODO Display the error in the status page
            # self.__view_stack.set_visible_child_name("error")

        def on_libraries_success(items: Sequence[BaseItemDto]) -> None:
            # TODO Create the "Item Shelf" component
            # TODO Add the "resume watching" shelf
            # TODO Add the "up next" shelf
            # TODO Add the library shelves
            self.__view_stack.set_visible_child_name("content")
            # TODO Get every shelf's content in tasks

        def query_shelf_items(name: str) -> None:
            # TODO Get the shelf's content
            pass

        def on_shelf_items_error(error: Exception, widget) -> None:
            # TODO Handle shelf content error
            pass

        def on_shelf_items_success(result) -> None:
            # TODO Create the "Item Card" component
            # TODO add shelf content
            pass

        self.__view_stack.set_visible_child_name("loading")

        # Spawn the home content thread
        Task(
            main=query_libraries,
            main_args=(self.get_browser(),),
            callback=on_libraries_success,
            error_callback=on_libraries_error,
        ).run()
