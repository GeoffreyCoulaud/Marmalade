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
from src.components.marmalade_navigation_page import MarmaladeNavigationPage
from src.components.disconnect_dialog import DisconnectDialog


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

    __address: str
    __user_id: str
    __device_id: str
    __token: str

    def __init__(
        self,
        *args,
        address: str,
        user_id: str,
        device_id: str,
        token: str,
        **kwargs,
    ):
        """Create a server home view"""

        super().__init__(*args, **kwargs)
        self.__address = address
        self.__device_id = device_id
        self.__user_id = user_id
        self.__token = token

        # React to user input
        self.disconnect_button.connect("clicked", self.on_disconnect_button_clicked)

        # TODO server connectivity check (switch to status pages if needed)

        self.set_title(_("Server Home"))
        self.label.set_label(
            "\n".join(
                (
                    f"Address: {self.__address}",
                    f"User ID: {self.__user_id}",
                    f"Token: {self.__token}",
                )
            )
        )

    def on_disconnect_button_clicked(self, _button) -> None:
        dialog = DisconnectDialog()
        dialog.connect("response", self.on_disconnect_dialog_response)
        dialog.set_transient_for(shared.window)
        dialog.set_modal(True)
        dialog.present()

    def on_disconnect_dialog_response(self, _dialog, response: str) -> None:
        match response:
            case "log-off":
                logging.debug(
                    "Logging off %s",
                    self.__address,
                )
                self.emit("log-off", self.__address)
            case "log-out":
                logging.debug(
                    "Logging user id %s out of %s",
                    self.__user_id,
                    self.__address,
                )
                self.emit("log-out", self.__address, self.__user_id)
