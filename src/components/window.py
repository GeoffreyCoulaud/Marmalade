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

from gi.repository import Adw

from src import shared
from src.components.server_browser_view import ServerBrowserView
from src.components.servers_list_view import ServersListView
from src.components.widget_builder import WidgetBuilder
from src.jellyfin import JellyfinClient


class BadToken(Exception):
    """Exception raised when a token is invalid"""


class UserNotFound(Exception):
    """Error raised when a user_id is not found"""


class MarmaladeWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MarmaladeWindow"

    navigation: Adw.NavigationView

    def __init_widget(self):
        self.navigation = (
            WidgetBuilder(Adw.NavigationView)
            .set_properties(pop_on_escape=False)
            .build()
        )
        self.set_default_size(800, 600)
        self.set_content(self.navigation)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__init_widget()

        # Add servers list
        self.navigation.add(ServersListView())

        # Try to get the active token to resume navigation on the server
        info = shared.settings.get_active_token()
        if info is not None:
            logging.debug("Resuming where we left off")
            address, user_id, (device_id, token) = info
            client = JellyfinClient(address, device_id=device_id, token=token)
            self.navigation.push(ServerBrowserView(client=client, user_id=user_id))
