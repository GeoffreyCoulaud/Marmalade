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
    __back_button         = Gtk.Template.Child("back_button")
    __disconnect_button   = Gtk.Template.Child("disconnect_button")
    __filter_button       = Gtk.Template.Child("filter_button")
    __header_center_stack = Gtk.Template.Child("header_center_stack")
    __header_left_stack   = Gtk.Template.Child("header_left_stack")
    __home_link           = Gtk.Template.Child("home_link")
    __libraries_links     = Gtk.Template.Child("libraries_links")
    __navigation          = Gtk.Template.Child("navigation")
    __overlay_split_view  = Gtk.Template.Child("overlay_split_view")
    __path_bar            = Gtk.Template.Child("path_bar")
    __preferences_button  = Gtk.Template.Child("preferences_button")
    __search_bar          = Gtk.Template.Child("search_bar")
    __search_button       = Gtk.Template.Child("search_button")
    __server_links        = Gtk.Template.Child("server_links")
    __sidebar_hide_button = Gtk.Template.Child("sidebar_hide_button")
    __sidebar_show_button = Gtk.Template.Child("sidebar_show_button")
    __sidebar_title       = Gtk.Template.Child("sidebar_title")
    __title               = Gtk.Template.Child("title")
    __toast_overlay       = Gtk.Template.Child("toast_overlay")
    # fmt: on

    __client: JellyfinClient
    __user_id: str

    def __init__(self, *args, client: JellyfinClient, user_id: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.__client = client
        self.__user_id = user_id
        shared.settings.update_connected_timestamp(address=self.__client._base_url)
        self.__disconnect_button.connect("clicked", self.on_disconnect_button_clicked)

        # TODO server connectivity check (switch to status pages if needed)

        self.__title.set_title("Placeholder title")
        # self.__label.set_label(
        #     "\n".join(
        #         (
        #             f"Address: {self.__client._base_url}",
        #             f"User ID: {self.__user_id}",
        #             f"Token: {self.__client._token}",
        #         )
        #     )
        # )

    def on_disconnect_button_clicked(self, _button) -> None:
        dialog = DisconnectDialog()
        dialog.connect("response", self.on_disconnect_dialog_response)
        dialog.set_transient_for(self.get_root())
        dialog.set_modal(True)
        dialog.present()

    def on_disconnect_dialog_response(self, _dialog, response: str) -> None:
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
