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

import json
import logging
import sys
from enum import IntEnum, auto
from pathlib import Path
from typing import Callable

from gi.repository import Adw, Gio, GLib

from src import build_constants  # pylint: disable=no-name-in-module
from src.components.server_home_view import ServerHomeView
from src.components.servers_view import ServersView
from src.components.window import MarmaladeWindow
from src.logging.setup import log_system_info, setup_logging
from src.reactive_set import ReactiveSet
from src.server import Server


class AppState(IntEnum):
    CREATED = auto()
    LOADED = auto()


class MarmaladeApplication(Adw.Application):
    """The main application singleton class."""

    state: AppState

    app_data_dir: Path
    app_cache_dir: Path
    app_config_dir: Path
    servers_file: Path
    log_file: Path

    servers: ReactiveSet[Server]

    def __init__(self):
        super().__init__(
            application_id=build_constants.APP_ID,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.state = AppState.CREATED

        self.app_data_dir = Path(GLib.get_user_data_dir()) / "marmalade"
        self.app_cache_dir = Path(GLib.get_user_cache_dir()) / "marmalade"
        self.app_config_dir = Path(GLib.get_user_config_dir()) / "marmalade"
        self.servers_file = self.app_config_dir / "servers.json"
        self.log_file = self.app_cache_dir / "marmalade.log"

        self.servers = ReactiveSet()
        self.servers.emitter.connect("item-added", self.on_servers_changed)
        self.servers.emitter.connect("item-removed", self.on_servers_changed)

        self.create_action("quit", lambda *_: self.quit(), ["<primary>q"])
        self.create_action("about", self.on_about_action)

        self.init_app_dirs()
        self.init_logging()
        self.load_servers()

        self.state = AppState.LOADED

    def init_app_dirs(self) -> None:
        self.app_data_dir.mkdir(parents=True, exist_ok=True)
        self.app_cache_dir.mkdir(parents=True, exist_ok=True)
        self.app_config_dir.mkdir(parents=True, exist_ok=True)

    def init_logging(self) -> None:
        """Set the logging system up"""
        setup_logging(self.log_file)
        log_system_info()

    def save_servers(self) -> None:
        """Save servers to disk"""
        servers_dicts = [server._asdict() for server in self.servers]
        try:
            with open(self.servers_file, "w", encoding="utf-8") as file:
                json.dump(servers_dicts, file, indent=4)
        except OSError as error:
            logging.error("Couldn't save servers to disk", exc_info=error)

    def load_servers(self) -> None:
        """Load servers from disk"""
        try:
            with open(self.servers_file, "r", encoding="utf-8") as file:
                server_dicts = json.load(file)
        except FileNotFoundError:
            self.servers_file.touch()
            logging.info("Created servers file")
        except (OSError, json.JSONDecodeError) as error:
            logging.error("Couldn't load servers from disk", exc_info=error)
        else:
            servers = (Server(**server_dict) for server_dict in server_dicts)
            self.servers.update(servers)

    def on_servers_changed(self, _emitter, _server) -> None:
        if self.state == AppState.CREATED:
            return
        self.save_servers()

    def create_window(self) -> MarmaladeWindow:
        window = MarmaladeWindow(application=self)
        servers_view = ServersView(window, self.servers)
        servers_view.connect("server-connect-request", self.on_server_connect_request)
        server_home_view = ServerHomeView(window)
        window.add_view(servers_view, "servers")
        window.add_view(server_home_view, "server_home")
        window.set_visible_view("servers")
        return window

    def on_server_connect_request(self, _view, server: Server) -> None:
        logging.info("Requested to connect to %s", server)
        # TODO open connect window

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = self.create_window()
        win.present()

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
