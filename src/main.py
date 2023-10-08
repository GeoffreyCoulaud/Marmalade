# main.py
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
import sys
from pathlib import Path
from typing import Callable

from gi.repository import Adw, Gio, GLib

# pylint: disable=no-name-in-module
from src import build_constants
from src.components.auth_dialog import AuthDialog
from src.components.server_connected_view import ServerConnectedView
from src.components.servers_list_view import ServersListView
from src.components.window import MarmaladeWindow
from src.database.api import DataHandler, ServerInfo
from src.logging.setup import log_system_info, setup_logging


class MarmaladeApplication(Adw.Application):
    """The main application singleton class."""

    app_data_dir: Path
    app_cache_dir: Path
    app_config_dir: Path

    settings: DataHandler

    window: MarmaladeWindow

    def __init__(self):
        super().__init__(
            application_id=build_constants.APP_ID,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.init_app_dirs()
        self.init_logging()

        database_file = self.app_data_dir / "marmalade.db"
        self.settings = DataHandler(file=database_file)
        self.window = None

        self.create_action("quit", lambda *_: self.quit(), ["<primary>q"])
        self.create_action("about", self.on_about_action)

    def init_app_dirs(self) -> None:
        self.app_data_dir = Path(GLib.get_user_data_dir()) / "marmalade"
        self.app_cache_dir = Path(GLib.get_user_cache_dir()) / "marmalade"
        self.app_config_dir = Path(GLib.get_user_config_dir()) / "marmalade"
        self.app_data_dir.mkdir(parents=True, exist_ok=True)
        self.app_cache_dir.mkdir(parents=True, exist_ok=True)
        self.app_config_dir.mkdir(parents=True, exist_ok=True)

    def init_logging(self) -> None:
        """Set the logging system up"""
        log_file = self.app_cache_dir / "marmalade.log"
        setup_logging(log_file)
        log_system_info()

    def on_server_connect_request(self, _emitter, server: ServerInfo) -> None:
        """Handle a request to connect to a server"""
        dialog = AuthDialog(server)
        dialog.connect("authenticated", self.on_authenticated)
        dialog.set_transient_for(self.window)
        dialog.set_modal(True)
        dialog.present()

    def on_authenticated(
        self, _widget, server: ServerInfo, user_id: str, token: str
    ) -> None:
        logging.debug("Authenticated on %s", server.name)
        # Update access token store, bookmark server and user
        self.settings.add_active_token(
            address=server.address,
            user_id=user_id,
            token=token,
        )
        self.navigate_to_server(server=server, token=token)

    def navigate_to_server(self, server: ServerInfo, token: str) -> None:
        home = ServerConnectedView(window=self.window, server=server, token=token)
        home.connect("log-off", self.on_server_log_off)
        home.connect("log-out", self.on_server_log_out)
        self.window.views.push(home)

    def on_server_log_out(self, _widget, server: ServerInfo, user_id: str) -> None:
        self.settings.remove_token(address=server.address, user_id=user_id)
        # TODO pop server home

    def on_server_log_off(self, _widget, _server: ServerInfo) -> None:
        self.settings.unset_active_token()
        # TODO pop server home

    def create_window(self):
        self.window = MarmaladeWindow(application=self)
        servers = ServersListView(window=self.window, settings=self.settings)
        servers.connect("server-connect-request", self.on_server_connect_request)
        self.window.views.add(servers)
        # Try to get the active token to resume navigation on the server
        active_token_info = self.settings.get_active_token()
        if active_token_info is not None:
            server, token = active_token_info
            logging.debug("Resuming where we left off")
            self.navigate_to_server(server=server, token=token)

    def do_activate(self):
        if not self.window:
            self.create_window()
        self.window.present()

    def on_about_action(self, _widget, _):
        """Callback handling the about action"""
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name="Marmalade",
            application_icon=build_constants.APP_ID,
            developer_name="Geoffrey Coulaud",
            version="0.1.0",
            developers=["Geoffrey Coulaud"],
            copyright="© 2023 Geoffrey Coulaud",
        )
        about.present()

    def create_action(self, name: str, callback: Callable, shortcuts=None):
        """Create an action with a name, handler and optional shortcuts"""
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(_version):
    """The application's entry point."""
    app = MarmaladeApplication()
    return app.run(sys.argv)
