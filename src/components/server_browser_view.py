# servers_home_view.py
#
# Copyright 2023 Geoffrey Coulaud
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
from http import HTTPStatus
from typing import Optional

from gi.repository import Adw, GObject, Gtk
from jellyfin_api_client.api.user import get_current_user
from jellyfin_api_client.api.user_views import get_user_views
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.base_item_dto import BaseItemDto
from jellyfin_api_client.models.base_item_dto_query_result import BaseItemDtoQueryResult

from src import build_constants, shared
from src.components.disconnect_dialog import DisconnectDialog
from src.components.server_browser import ServerBrowser
from src.components.server_browser_headerbar import ServerBrowserHeaderbar
from src.components.server_home_page import ServerHomePage
from src.components.server_navigation_item import ServerNavigationItem
from src.components.server_page import ServerPage
from src.jellyfin import JellyfinClient
from src.task import Task


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_browser_view.ui"
)
class ServerBrowserView(Adw.NavigationPage, ServerBrowser):
    """
    Server browser page.

    This is the page that is shown to the user when they connect to a server.
    """

    __gtype_name__ = "MarmaladeServerBrowserView"

    @GObject.Signal(name="log-out", arg_types=[str, str])
    def log_out(self, _address: str, _user_id: str):
        """Signal emitted when the user logs out of the server (discard the token)"""

    @GObject.Signal(name="log-off", arg_types=[str])
    def log_off(self, _address: str):
        """
        Signal emitted when the user logs off the server.
        Should also be emitted alongside log-out.
        """

    # fmt: off
    __navigation                   = Gtk.Template.Child("navigation")
    __overlay_split_view           = Gtk.Template.Child("overlay_split_view")
    __sidebar_hide_button          = Gtk.Template.Child("sidebar_hide_button")
    __sidebar_hide_button_revealer = Gtk.Template.Child("sidebar_hide_button_revealer")
    __sidebar_title                = Gtk.Template.Child("sidebar_title")
    __server_links                 = Gtk.Template.Child("server_links")
    __libraries_links              = Gtk.Template.Child("libraries_links")
    __home_link                    = Gtk.Template.Child("home_link")
    __user_settings_link           = Gtk.Template.Child("user_settings_link")
    __admin_dashboard_link         = Gtk.Template.Child("admin_dashboard_link")
    __headerbar: ServerBrowserHeaderbar = Gtk.Template.Child("headerbar")
    # fmt: on

    def __init__(self, *args, client: JellyfinClient, user_id: str, **kwargs):
        super().__init__(*args, client=client, user_id=user_id, **kwargs)
        shared.settings.update_connected_timestamp(address=self.client._base_url)
        self.__headerbar.connect("disconnect-request", self.__on_disconnect_request)

        # Sidebar
        self.__headerbar.connect("show-sidebar-request", self.__toggle_sidebar, True)
        self.__sidebar_hide_button.connect("clicked", self.__toggle_sidebar, False)
        self.__overlay_split_view.connect(
            "notify::show-sidebar", self.__on_sidebar_shown_changed
        )

        # Reactive headerbar title
        self.__navigation.connect(
            "notify::visible-page", self.__on_navigation_page_changed
        )
        self.connect("map", self.__on_mapped)

    def __on_mapped(self, *_args) -> None:
        """Callback executed when this view is about to be shown"""
        self.__on_sidebar_shown_changed()
        self.__on_navigation_page_changed()
        self.__init_navigation_sidebar()
        # Navigate to server home page
        page = ServerHomePage(browser=self, headerbar=self.__headerbar)
        navigation: Adw.NavigationView = self.__navigation
        navigation.replace([page])

    def __init_navigation_sidebar(self) -> None:
        """Asynchronously initialize the navigation sidebar's content"""

        def query_admin():
            res = get_current_user.sync_detailed(client=self.client)
            if res.status_code == HTTPStatus.OK:
                return res.parsed.policy.is_administrator
            raise UnexpectedStatus(res.status_code, res.content)

        def on_admin_success(is_admin: bool) -> None:
            logging.debug("Loaded user admin status: %s", str(is_admin))
            self.__admin_dashboard_link.set_visible(is_admin)

        def query_libraries():
            res = get_user_views.sync_detailed(self.user_id, client=self.client)
            if res.status_code == HTTPStatus.OK:
                return res.parsed
            raise UnexpectedStatus(res.status_code, res.content)

        def on_libraries_success(result: BaseItemDtoQueryResult) -> None:
            logging.debug("Loaded user libraries")
            items: list[BaseItemDto] = result.items
            icon_map = {
                "tvshows": "tv-symbolic",
                "movies": "folder-videos-symbolic",
                "music": "folder-music-symbolic",
                "books": "open-book-symbolic",
            }
            self.__libraries_links.remove_all()
            for item in items:
                logging.debug("Adding library %s to navigation", item.name)
                link = ServerNavigationItem(
                    title=item.name,
                    icon_name=icon_map.get(item.collection_type, "folder-symbolic"),
                )
                # TODO connect link item navigation
                self.__libraries_links.append(link)
            pass

        for task in (
            Task(main=query_admin, callback=on_admin_success),
            Task(main=query_libraries, callback=on_libraries_success),
        ):
            task.run()

    def __on_navigation_page_changed(self, *_args) -> None:
        """Callback executed when the navigation view changes the current page"""
        page: Optional[ServerPage] = self.__navigation.get_visible_page()
        if page is None:
            return
        self.__headerbar.set_filter_button_visible(page.get_is_filterable())
        self.__headerbar.set_search_visible(page.get_is_searchable())
        self.__headerbar.set_title(page.get_title())

    def __on_sidebar_shown_changed(self, *_args) -> None:
        shown = self.__overlay_split_view.get_show_sidebar()
        self.__sidebar_hide_button_revealer.set_reveal_child(shown)
        self.__headerbar.set_show_sidebar_button_visible(not shown)

    def __toggle_sidebar(self, _widget, shown: bool = True) -> None:
        """Toggle the navigation sidebar's visibility"""
        self.__overlay_split_view.set_show_sidebar(shown)

    def __on_disconnect_request(self, *_args) -> None:
        dialog = DisconnectDialog()
        dialog.connect("response", self.__on_disconnect_dialog_response)
        dialog.set_transient_for(self.get_root())
        dialog.set_modal(True)
        dialog.present()

    def __on_disconnect_dialog_response(self, _widget, response: str) -> None:
        match response:
            case "log-off":
                self.log_off()
            case "log-out":
                self.log_out()

    def log_off(self) -> None:
        """Disconnect from the server"""
        logging.debug("Logging off %s", self.client._base_url)
        shared.settings.unset_active_token()
        navigation = self.get_parent()
        navigation.pop_to_tag("servers-view")

    def log_out(self) -> None:
        """Disconnect from the server, deleting the access token"""
        logging.debug(
            "Logging %s out of %s",
            self.user_id,
            self.client._base_url,
        )
        shared.settings.remove_token(
            address=self.client._base_url,
            user_id=self.user_id,
        )
        navigation = self.get_parent()
        navigation.pop_to_tag("servers-view")
