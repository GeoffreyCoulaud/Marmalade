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

import sys
from pathlib import Path
from typing import Callable

from gi.repository import Adw, Gio, GLib

# pylint: disable=no-name-in-module
from src import build_constants
from src.components.window import MarmaladeWindow
from src.database.api import DataHandler
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
        self.window = None
        self.init_app_dirs()
        self.init_logging()
        database_file = self.app_data_dir / "marmalade.db"
        self.settings = DataHandler(file=database_file)
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

    def do_activate(self):
        if not self.window:
            self.window = MarmaladeWindow(
                application=self,
                settings=self.settings,
            )
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
