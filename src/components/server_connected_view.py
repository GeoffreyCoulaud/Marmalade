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
from jellyfin_api_client.models.user_dto import UserDto

from src import build_constants, shared
from src.components.disconnect_dialog import DisconnectDialog
from src.database.api import ServerInfo


@Gtk.Template(
    resource_path=build_constants.PREFIX + "/templates/server_connected_view.ui"
)
class ServerConnectedView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeServerConnectedView"

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

    __toast_overlay: Adw.ToastOverlay
    __server: ServerInfo
    __user: UserDto
    __token: str

    def __init__(
        self,
        *args,
        toast_overlay: Adw.ToastOverlay,
        server: ServerInfo,
        user: UserDto,
        token: str,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.__toast_overlay = toast_overlay
        self.__server = server
        self.__user = user
        self.__token = token

        # Variable is the server's name
        self.set_title(_("%s Home") % self.__server.name)

        # React to user input
        self.disconnect_button.connect("clicked", self.on_disconnect_button_clicked)

        # TODO implement content
        label = "\n".join(
            (
                f"Server: {self.__server.name}",
                f"Address: {self.__server.address}",
                f"Token: {self.__token}",
            )
        )
        self.label.set_label(label)

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
                    self.__server.address,
                )
                self.emit("log-off", self.__server.address)
            case "log-out":
                logging.debug(
                    "Logging user id %s out of %s",
                    self.__user.id,
                    self.__server.address,
                )
                self.emit("log-out", self.__server.address, self.__user.id)
