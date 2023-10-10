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
import socket
from http import HTTPStatus

from gi.repository import Adw, Gtk
from jellyfin_api_client.api.user import get_user_by_id
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.user_dto import UserDto

from src import build_constants
from src.components.auth_dialog import AuthDialog
from src.components.server_connected_view import ServerConnectedView
from src.components.servers_list_view import ServersListView
from src.database.api import DataHandler, ServerInfo
from src.jellyfin import JellyfinClient
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

    __settings: DataHandler

    def __init__(self, *args, settings: DataHandler, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__settings = settings

        # Add servers list
        view = ServersListView(
            window=self,
            toast_overlay=self.toast_overlay,
            settings=self.__settings,
        )
        view.connect("server-connect-request", self.on_server_connect_request)
        self.views.add(view)

        # Try to get the active token to resume navigation on the server
        active_token_info = self.__settings.get_active_token()
        if active_token_info is not None:
            server, user_id, token = active_token_info
            logging.debug("Resuming where we left off")
            self.navigate_to_server(server=server, user_id=user_id, token=token)

    def on_server_connect_request(self, _emitter, server: ServerInfo) -> None:
        """Handle a request to connect to a server"""
        dialog = AuthDialog(server)
        dialog.connect("authenticated", self.on_authenticated)
        dialog.set_transient_for(self)
        dialog.set_modal(True)
        dialog.present()

    def on_authenticated(
        self, _widget, server: ServerInfo, user_id: str, token: str
    ) -> None:
        logging.debug("Authenticated on %s", server.name)
        # Update access token store, bookmark server and user
        self.__settings.add_active_token(
            address=server.address,
            user_id=user_id,
            token=token,
        )
        self.navigate_to_server(server=server, user_id=user_id, token=token)

    def navigate_to_server(self, server: ServerInfo, user_id: str, token: str) -> None:
        """Navigate to the server with the given authentication token"""

        def main(address: str, user_id: str, token: str) -> UserDto:
            # Get token info to pass it to home view
            client = JellyfinClient(base_url=address, device_id="-", token=token)
            response = get_user_by_id.sync_detailed(user_id, client=client)
            match response.status_code:
                case HTTPStatus.OK:
                    return response.parsed
                case HTTPStatus.UNAUTHORIZED | HTTPStatus.FORBIDDEN:
                    raise BadToken()
                case HTTPStatus.NOT_FOUND:
                    raise UserNotFound()
                case _:
                    raise UnexpectedStatus(response.status_code)

        def on_error(
            server: ServerInfo,
            error: BadToken | UserNotFound | UnexpectedStatus,
        ) -> None:
            # Handler user info error
            toast = Adw.Toast()
            toast.set_priority(Adw.ToastPriority.HIGH)
            if isinstance(error, UserNotFound):
                # Bad user
                toast.set_title(_("User not found"))
            if isinstance(error, BadToken):
                # Inform user that the token is invalid
                toast.set_title(_("Bad authentication token"))
                toast.set_button_label(_("Log in"))
                toast.connect("button-clicked", self.on_server_connect_request, server)
            else:
                # Other unexpected error
                toast.set_title(_("Unexpected error when connecting"))
                toast.set_button_label(_("Details"))
                toast.connect("button-clicked", on_error_details, str(error))
            self.toast_overlay.add_toast(toast)

        def on_error_details(_widget, details: str) -> None:
            # Show error details message
            logging.debug("Connection error details requested")
            msg = Adw.MessageDialog()
            msg.add_response("close", _("Close"))
            msg.set_heading(_("Unexpected Connection Error"))
            msg.set_body(details)
            msg.set_transient_for(self)
            msg.present()

        def on_success(result: UserDto) -> None:
            # Navigate to server connected view
            view = ServerConnectedView(
                window=self,
                toast_overlay=self.toast_overlay,
                settings=self.__settings,
                server=server,
                user=result,
                token=token,
            )
            view.connect("log-off", self.on_server_log_off)
            view.connect("log-out", self.on_server_log_out)
            self.views.push(view)

        task = Task(
            main=main,
            main_args=(server.address, user_id, token),
            callback=on_success,
            error_callback=on_error,
            error_callback_args=(server,),
        )
        task.run()

    def on_server_log_out(self, _widget, address: str, user_id: str) -> None:
        self.__settings.remove_token(address=address, user_id=user_id)
        self.views.pop()

    def on_server_log_off(self, _widget, _address: str) -> None:
        self.__settings.unset_active_token()
        self.views.pop()
