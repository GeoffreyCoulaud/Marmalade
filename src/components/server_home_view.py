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
from src.components.marmalade_navigation_page import MarmaladeNavigationPage
from src.jellyfin import JellyfinClient


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_home_view.ui")
class ServerHomeView(MarmaladeNavigationPage):
    """
    Server home view navigation page.

    This is the page that is shown to the user when they connect to a server.
    """

    __gtype_name__ = "MarmaladeServerHomeView"

    @GObject.Signal(name="log-out", arg_types=[str, str])
    def log_out(self, _address: str, _user_id: str):
        """Signal emitted when the user logs out of the server (discard the token)"""

    @GObject.Signal(name="log-off", arg_types=[str])
    def log_off(self, _address: str):
        """
        Signal emitted when the user logs off the server.
        Should also be emitted alongside log-out.
        """

    disconnect_button = Gtk.Template.Child()
    search_button = Gtk.Template.Child()
    collection_filter_button = Gtk.Template.Child()
    preferences_button = Gtk.Template.Child()
    label: Gtk.Label = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()

    __client: JellyfinClient
    __user_id: str

    def __init__(self, *args, client: JellyfinClient, user_id: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.__client = client
        self.__user_id = user_id
        shared.settings.update_connected_timestamp(address=self.__client._base_url)
        self.disconnect_button.connect("clicked", self.on_disconnect_button_clicked)

        # TODO server connectivity check (switch to status pages if needed)

        self.set_title(_("Server Home"))
        self.label.set_label(
            "\n".join(
                (
                    f"Address: {self.__client._base_url}",
                    f"User ID: {self.__user_id}",
                    f"Token: {self.__client._token}",
                )
            )
        )

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
        self.navigation.pop_to_tag("servers-view")

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
        self.navigation.pop_to_tag("servers-view")
