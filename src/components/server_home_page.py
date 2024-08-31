import logging
from http import HTTPStatus
from typing import Sequence

from gi.repository import Adw, GLib, Gtk
from jellyfin_api_client.api.items import get_resume_items
from jellyfin_api_client.api.tv_shows import get_next_up
from jellyfin_api_client.api.user_library import get_latest_media
from jellyfin_api_client.api.user_views import get_user_views
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.base_item_dto import BaseItemDto
from jellyfin_api_client.models.image_type import ImageType
from jellyfin_api_client.types import UNSET

from src.components.item_card import POSTER, WIDE_SCREENSHOT, ItemCard
from src.components.loading_view import LoadingView
from src.components.server_page import ServerPage
from src.components.shelf import Shelf
from src.components.widget_builder import Children, Properties, build
from src.task import Task

# TODO make sure that the loading view stays up until
# all the startup requests are done.


class ServerHomePage(ServerPage):
    __gtype_name__ = "MarmaladeServerHomePage"

    __toast_overlay: Adw.ToastOverlay
    __view_stack: Adw.ViewStack
    __loading_view: LoadingView
    __error_view: Adw.StatusPage
    __content_view: Gtk.ScrolledWindow
    __content_box: Gtk.Box
    __resume_shelf: Shelf
    __next_up_shelf: Shelf

    def __init_widget(self) -> None:
        self.__next_up_shelf = build(
            Shelf
            + Properties(
                title=_("Next Up"),
                columns=3,
                lines=1,
            )
        )
        self.__resume_shelf = build(
            Shelf
            + Properties(
                title=_("Resume Watching"),
                columns=3,
                lines=1,
            )
        )
        self.__content_box = build(
            Gtk.Box
            + Properties(
                orientation=Gtk.Orientation.VERTICAL,
                margin_start=25,
                margin_end=25,
                margin_bottom=25,
                margin_top=25,
                spacing=24,
            )
            + Children(
                self.__resume_shelf,
                self.__next_up_shelf,
            )
        )
        self.__content_view = build(
            Gtk.ScrolledWindow
            + Children(
                Adw.Clamp
                + Properties(maximum_size=1240)
                + Children(
                    self.__content_box,
                )
            )
        )
        self.__loading_view = build(LoadingView)
        self.__error_view = build(
            Adw.StatusPage
            + Properties(
                title=_("Error"),
                description=_("An error occurred while getting the server's home"),
                icon_name="dialog-error-symbolic",
            )
        )
        self.__view_stack = build(
            Adw.ViewStack
            + Children(
                self.__loading_view,
                self.__error_view,
                self.__content_view,
            )
        )
        self.__toast_overlay = build(
            Adw.ToastOverlay
            + Children(
                self.__view_stack,
            )
        )
        self.set_is_root(True)
        self.set_is_filterable(True)
        self.set_title(_("Home"))
        self.set_child(self.__toast_overlay)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__init_widget()

    def load(self) -> None:
        """Load the home page content"""

        browser = self.get_browser()
        user_id = browser.get_user_id()
        client = browser.get_client()

        def query_libraries() -> Sequence[BaseItemDto]:
            """Query user libraries"""
            logging.debug("Querying libraries")
            res = get_user_views.sync_detailed(client=client, user_id=user_id)  # type: ignore
            if res.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(res.status_code, res.content)
            return res.parsed.items  # type: ignore

        def on_libraries_error(error: Exception) -> None:
            logging.error("Error while loading user libraries", exc_info=error)
            toast = Adw.Toast(title=_("Could not load user libraries"))
            toast.set_timeout(0)
            toast.set_button_label(_("Reload Page"))
            toast.set_action_name("browser.reload")
            self.__toast_overlay.add_toast(toast)

        def on_libraries_success(items: Sequence[BaseItemDto]) -> None:
            # Add the library shelves
            logging.debug("Home libraries: %s", str([item.name for item in items]))
            included_types = {"books", "movies", "music", "tvshows", UNSET}
            for item in items:
                if item.collection_type not in included_types:
                    continue

                # Create the shelf
                title = _("Latest in {library}").format(library=item.name)
                shelf = Shelf(title=title, columns=6, lines=1)
                self.__content_box.append(shelf)

                # Query shelf content in a task
                task = Task(
                    main=query_library_items,
                    main_args=(item.id,),
                    callback=on_shelf_items_success,
                    callback_args=(shelf,),
                    error_callback=on_shelf_items_error,
                    error_callback_args=(shelf,),
                )
                task.run()

        def query_library_items(library_id: str) -> Sequence[BaseItemDto]:
            logging.debug("Querying items for library %s", library_id)
            res = get_latest_media.sync_detailed(
                client=client,  # type: ignore
                user_id=user_id,
                parent_id=library_id,
            )
            if res.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(res.status_code, res.content)
            return res.parsed  # type: ignore

        def query_resume_items() -> Sequence[BaseItemDto]:
            logging.debug("Querying resume items")
            res = get_resume_items.sync_detailed(
                client=client,  # type: ignore
                user_id=user_id,
            )
            if res.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(res.status_code, res.content)
            return res.parsed.items  # type: ignore

        def query_next_up_items() -> Sequence[BaseItemDto]:
            logging.debug("Querying next up items")
            res = get_next_up.sync_detailed(
                client=client,  # type: ignore
                user_id=user_id,
            )
            if res.status_code != HTTPStatus.OK:
                raise UnexpectedStatus(res.status_code, res.content)
            return res.parsed.items  # type: ignore

        def on_shelf_items_error(shelf: Shelf, error: Exception) -> None:
            logging.error("Couldn't get %s items", shelf.get_title(), exc_info=error)
            toast = Adw.Toast(title=_("Could not load shelf items"))
            toast.set_button_label(_("Details"))
            toast.set_action_name("app.error-details")
            toast.set_action_target_value(
                GLib.Variant.new_strv([_("Shelf Items Error"), str(error)])
            )
            self.__toast_overlay.add_toast(toast)
            self.__content_box.remove(shelf)

        def on_shelf_items_success(shelf: Shelf, result: Sequence[BaseItemDto]) -> None:
            logging.debug('Shelf "%s": %d items', shelf.get_title(), len(result))
            client = self.get_browser().get_client()
            for item in result:
                card = build(
                    ItemCard
                    + Properties(
                        item_id=item.id,
                        title=item.name,
                        image_type=ImageType.PRIMARY,
                        image_size=POSTER,
                    )
                )
                shelf.append(card)
                card.load_image(client)
                # TODO Properly handle the subtitle
                # TODO Set the card action

        self.__view_stack.set_visible_child(self.__content_view)

        # Spawn content query tasks
        logging.debug("Spawning homepage loading tasks")
        for task in (
            Task(
                main=query_libraries,
                callback=on_libraries_success,
                error_callback=on_libraries_error,
            ),
            Task(
                main=query_resume_items,
                callback=on_shelf_items_success,
                callback_args=(self.__resume_shelf,),
                error_callback=on_shelf_items_error,
                error_callback_args=(self.__resume_shelf,),
            ),
            Task(
                main=query_next_up_items,
                callback=on_shelf_items_success,
                callback_args=(self.__next_up_shelf,),
                error_callback=on_shelf_items_error,
                error_callback_args=(self.__next_up_shelf,),
            ),
        ):
            task.run()
