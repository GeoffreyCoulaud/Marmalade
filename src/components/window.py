# window.py
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

from gi.repository import Adw, Gtk

from src import build_constants, shared
from src.components.auth_dialog import AuthDialog
from src.components.server_home_view import ServerHomeView
from src.components.servers_list_view import ServersListView
from src.database.api import ServerInfo
from src.task import Task


class BadToken(Exception):
    """Exception raised when a token is invalid"""


class UserNotFound(Exception):
    """Error raised when a user_id is not found"""


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/window.ui")
class MarmaladeWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MarmaladeWindow"

    views = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()

    __servers_view: ServersListView

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Add servers list
        self.__servers_view = ServersListView(toast_overlay=self.toast_overlay)
        self.__servers_view.connect(
            "server-connect-request",
            self.on_server_connect_request,
        )
        self.views.add(self.__servers_view)

        # Try to get the active token to resume navigation on the server
        info = shared.settings.get_active_token()
        if info is not None:
            logging.debug("Resuming where we left off")
            self.navigate_to_server_home(
                address=info.address,
                user_id=info.user_id,
                device_id=info.token_info.device_id,
                token=info.token_info.token,
            )

    def on_server_connect_request(self, _emitter, server: ServerInfo) -> None:
        """Handle a request to connect to a server"""
        # TODO check server connectivity before showing auth dialog
        dialog = AuthDialog(server)
        dialog.connect("authenticated", self.on_user_authenticated)
        dialog.set_transient_for(self)
        dialog.set_modal(True)
        dialog.present()

    def on_user_authenticated(self, _widget, address: str, user_id: str) -> None:
        logging.debug("Authenticated on %s", address)
        info = shared.settings.get_token(address=address, user_id=user_id)
        self.navigate_to_server_home(
            address=address,
            user_id=user_id,
            device_id=info.device_id,
            token=info.token,
        )

    def navigate_to_server_home(
        self, address: str, user_id: str, device_id: str, token: str
    ) -> None:
        """Navigate to the server with the given authentication token"""
        shared.settings.set_active_token(address=address, user_id=user_id)
        shared.settings.update_connected_timestamp(address=address)
        view = ServerHomeView(
            navigation=self.views,
            address=address,
            user_id=user_id,
            device_id=device_id,
            token=token,
        )
        view.connect("log-off", self.on_server_log_off)
        view.connect("log-out", self.on_server_log_out)
        self.views.push(view)

    def on_server_log_out(self, _widget, address: str, user_id: str) -> None:
        shared.settings.remove_token(address=address, user_id=user_id)
        self.__servers_view.refresh_servers()
        self.views.pop()

    def on_server_log_off(self, _widget, _address: str) -> None:
        shared.settings.unset_active_token()
        self.__servers_view.refresh_servers()
        self.views.pop()
