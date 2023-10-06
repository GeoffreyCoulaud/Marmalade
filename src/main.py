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
from enum import IntEnum, auto
from http import HTTPStatus
from pathlib import Path
from typing import Callable

from gi.repository import Adw, Gio, GLib
from jellyfin_api_client.api.user import get_current_user
from jellyfin_api_client.client import AuthenticatedClient as JfAuthClient

# pylint: disable=no-name-in-module
from src import build_constants
from src.access_token_store import AccessTokenStore
from src.components.auth_dialog import AuthDialog
from src.components.server_home_view import ServerHomeView
from src.components.servers_view import ServersView
from src.components.window import MarmaladeWindow
from src.logging.setup import log_system_info, setup_logging
from src.server import Server
from src.server_store import ServerStore
from src.task import Task


class AppState(IntEnum):
    CREATED = auto()
    LOADED = auto()


class MarmaladeApplication(Adw.Application):
    """The main application singleton class."""

    app_data_dir: Path
    app_cache_dir: Path
    app_config_dir: Path
    servers_file: Path
    log_file: Path

    state: AppState
    servers_store: ServerStore
    access_token_store: AccessTokenStore

    window: MarmaladeWindow

    def __init__(self):
        super().__init__(
            application_id=build_constants.APP_ID,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.state = AppState.CREATED
        self.window = None

        self.app_data_dir = Path(GLib.get_user_data_dir()) / "marmalade"
        self.app_cache_dir = Path(GLib.get_user_cache_dir()) / "marmalade"
        self.app_config_dir = Path(GLib.get_user_config_dir()) / "marmalade"
        self.log_file = self.app_cache_dir / "marmalade.log"
        self.init_app_dirs()
        self.init_logging()

        servers_file_path = self.app_config_dir / "servers.json"
        self.servers_store = ServerStore(file_path=servers_file_path)
        self.servers_store.emitter.connect("changed", self.on_servers_changed)

        access_token_file = self.app_config_dir / "access_tokens.json"
        self.access_token_store = AccessTokenStore(file_path=access_token_file)

        self.create_action("quit", lambda *_: self.quit(), ["<primary>q"])
        self.create_action("about", self.on_about_action)
        self.state = AppState.LOADED

    def init_app_dirs(self) -> None:
        self.app_data_dir.mkdir(parents=True, exist_ok=True)
        self.app_cache_dir.mkdir(parents=True, exist_ok=True)
        self.app_config_dir.mkdir(parents=True, exist_ok=True)

    def init_logging(self) -> None:
        """Set the logging system up"""
        setup_logging(self.log_file)
        log_system_info()

    def on_servers_changed(self, _emitter) -> None:
        if self.state == AppState.CREATED:
            return
        self.servers_store.save()

    def on_server_connect_request(self, _emitter, server: Server) -> None:
        """Handle a request to connect to a server"""

        def query_bookmarked_token(server: Server) -> str:
            # Get a token from the store (may raise KeyError)
            tokens_bidict = self.access_token_store[server]
            token = tokens_bidict.get_bookmark()
            # Test the token with the server
            client = JfAuthClient(server.address, token)
            response = get_current_user.sync_detailed(client=client)
            if response.status_code in (HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN):
                tokens_bidict.unset_bookmark()
                del tokens_bidict[token]
                logging.warning("Removed invalid stored token: %s", token)
                raise ValueError("Invalid token")
            user_id = response.parsed.id
            return (user_id, token)

        def on_error(server: Server, *, error: Exception) -> None:
            # Handle bookmarked token errors
            if isinstance(error, KeyError):
                logging.debug("No bookmarked token")
            elif isinstance(error, ValueError):
                logging.debug("Invalid stored token")
            else:
                logging.debug("Error during token retrieval", exc_info=error)
            # Open auth dialog
            dialog = AuthDialog(server)
            dialog.connect("authenticated", self.on_server_authenticated)
            dialog.set_transient_for(self.window)
            dialog.set_modal(True)
            dialog.present()

        def on_valid(server: Server, *, result: tuple[str, str]) -> None:
            user_id, token = result
            self.on_server_authenticated(
                None,
                server=server,
                user_id=user_id,
                token=token,
            )

        task = Task(
            main=query_bookmarked_token,
            main_args=(server,),
            callback=on_valid,
            callback_args=(server,),
            error_callback=on_error,
            error_callback_args=(server,),
        )
        task.run()

    def on_server_authenticated(
        self,
        _widget,
        server: Server,
        user_id: str,
        token: str,
    ) -> None:
        logging.debug("Authenticated on %s (token: %s)", server.name, token)
        # Update access token store, bookmark server and user
        self.access_token_store[server][user_id] = token
        self.access_token_store.set_bookmark(server)
        self.access_token_store[server].set_bookmark(user_id)
        # Create server home view and navigate to it
        home = ServerHomeView(
            window=self.window, server=server, user_id=user_id, token=token
        )
        home.connect("log-off", self.on_server_log_off)
        home.connect("log-out", self.on_server_log_out)
        self.window.views.push(home)

    def on_server_log_out(self, _widget, server: Server, user_id: str) -> None:
        # Remove the user's token from the server
        self.access_token_store[server].unset_bookmark()
        del self.access_token_store[server][user_id]

    def on_server_log_off(self, _widget, _server: Server) -> None:
        # Unset the server bookmark but keep the token bookmark
        # (Enables instant login on the server)
        self.access_token_store.unset_bookmark()

    def create_window(self) -> MarmaladeWindow:
        window = MarmaladeWindow(application=self)
        servers = ServersView(window=window, servers=self.servers_store)
        servers.connect("server-connect-request", self.on_server_connect_request)
        window.views.add(servers)  # First page, servers, static
        try:
            server = self.access_token_store.get_bookmark()
            token = server.get_bookmark()
            user_id = server.inverse[token]
        except KeyError:
            # Just show the servers view
            pass
        else:
            # Navigate to latest server+user home view
            logging.debug("Resuming where we left off")
            self.on_server_authenticated(
                None,
                server=server,
                user_id=user_id,
                token=token,
            )
        return window

    def do_activate(self):
        if not self.window:
            self.window = self.create_window()
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
