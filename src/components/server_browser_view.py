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

from gi.repository import Adw, GObject, Gtk

from src import build_constants, shared
from src.components.disconnect_dialog import DisconnectDialog
from src.components.server_loading_view import ServerLoadingView  # For .ui
from src.components.server_unreachable_view import ServerUnreachableView  # For .ui
from src.jellyfin import JellyfinClient


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_browser_view.ui"
)
class ServerBrowserView(Adw.NavigationPage):
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
    __back_button                  = Gtk.Template.Child("back_button")
    __content_view_stack           = Gtk.Template.Child("content_view_stack")
    __disconnect_button            = Gtk.Template.Child("disconnect_button")
    __filter_button                = Gtk.Template.Child("filter_button")
    __header_center_stack          = Gtk.Template.Child("header_center_stack")
    __header_left_stack            = Gtk.Template.Child("header_left_stack")
    __home_link                    = Gtk.Template.Child("home_link")
    __libraries_links              = Gtk.Template.Child("libraries_links")
    __navigation                   = Gtk.Template.Child("navigation")
    __overlay_split_view           = Gtk.Template.Child("overlay_split_view")
    __path_bar                     = Gtk.Template.Child("path_bar")
    __preferences_button           = Gtk.Template.Child("preferences_button")
    __search_bar                   = Gtk.Template.Child("search_bar")
    __search_button                = Gtk.Template.Child("search_button")
    __server_links                 = Gtk.Template.Child("server_links")
    __sidebar_hide_button          = Gtk.Template.Child("sidebar_hide_button")
    __sidebar_hide_button_revealer = Gtk.Template.Child("sidebar_hide_button_revealer")
    __sidebar_show_button          = Gtk.Template.Child("sidebar_show_button")
    __sidebar_show_button_revealer = Gtk.Template.Child("sidebar_show_button_revealer")
    __sidebar_title                = Gtk.Template.Child("sidebar_title")
    __title                        = Gtk.Template.Child("title")
    __toast_overlay                = Gtk.Template.Child("toast_overlay")
    # fmt: on

    __client: JellyfinClient
    __user_id: str

    def __init__(self, *args, client: JellyfinClient, user_id: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.__client = client
        self.__user_id = user_id
        shared.settings.update_connected_timestamp(address=self.__client._base_url)
        self.__disconnect_button.connect("clicked", self.__on_disconnect_button_clicked)

        # Sidebar
        self.__sidebar_show_button.connect("clicked", self.__toggle_sidebar, True)
        self.__sidebar_hide_button.connect("clicked", self.__toggle_sidebar, False)
        self.__overlay_split_view.connect(
            "notify::show-sidebar", self.__on_sidebar_shown_changed
        )

        # Browser state
        self.__content_view_stack.set_visible_child_name("loading")

        # TODO server connectivity check (switch to status pages if needed)

        # Reactive headerbar title
        self.__content_view_stack.connect(
            "notify::visible-child", self.__on_content_stack_page_changed
        )
        self.__navigation.connect(
            "notify::visible-page", self.__on_navigation_page_changed
        )
        self.connect("map", self.__on_mapped)

    def __on_mapped(self, *_args) -> None:
        self.__on_content_stack_page_changed()

    def __on_content_stack_page_changed(self, *_args) -> None:
        child = self.__content_view_stack.get_visible_child()
        view: Adw.ViewStackPage = self.__content_view_stack.get_page(child)
        match view.get_name():
            case "navigation":
                self.__on_navigation_page_changed()
            case _:
                title = view.get_title()
                self.__title.set_label(title)

    def __on_navigation_page_changed(self, *_args) -> None:
        view: Adw.NavigationPage = self.__navigation.get_visible_page()
        title = view.get_title()
        self.__title.set_label(title)

    def __on_sidebar_shown_changed(self, *_args) -> None:
        shown = self.__overlay_split_view.get_show_sidebar()
        self.__sidebar_hide_button_revealer.set_reveal_child(shown)
        self.__sidebar_show_button_revealer.set_reveal_child(not shown)

    def __toggle_sidebar(self, _widget, shown: bool = True) -> None:
        """Toggle the navigation sidebar's visibility"""
        self.__overlay_split_view.set_show_sidebar(shown)

    def __on_disconnect_button_clicked(self, *_args) -> None:
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
        logging.debug("Logging off %s", self.__client._base_url)
        shared.settings.unset_active_token()
        navigation = self.get_parent()
        navigation.pop_to_tag("servers-view")

    def log_out(self) -> None:
        """Disconnect from the server, deleting the access token"""
        logging.debug(
            "Logging %s out of %s",
            self.__user_id,
            self.__client._base_url,
        )
        shared.settings.remove_token(
            address=self.__client._base_url,
            user_id=self.__user_id,
        )
        navigation = self.get_parent()
        navigation.pop_to_tag("servers-view")
