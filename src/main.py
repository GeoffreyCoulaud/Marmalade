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
import time
from typing import Callable

from gi.repository import Gio, Adw

from src import build_constants
from src.components.server_home_view import ServerHomeView
from src.components.server_row import ServerRow
from src.components.servers_view import ServersView
from src.reactive_set import ReactiveSet
from src.server import Server
from src.components.window import MarmaladeWindow


class MarmaladeApplication(Adw.Application):
    """The main application singleton class."""

    servers: ReactiveSet[Server]

    def __init__(self):
        super().__init__(
            application_id=build_constants.APP_ID,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.servers = ReactiveSet()
        self.create_action("quit", lambda *_: self.quit(), ["<primary>q"])
        self.create_action("about", self.on_about_action)

    def create_window(self) -> MarmaladeWindow:
        win = MarmaladeWindow(application=self)
        servers_view = ServersView(self.servers)
        server_home_view = ServerHomeView()
        win.add_view(servers_view, "servers")
        win.add_view(server_home_view, "server_home")
        win.set_visible_view("servers")
        return win

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = self.create_window()
        win.present()

    def on_about_action(self, widget, _):
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


def main(version):
    """The application's entry point."""
    app = MarmaladeApplication()
    return app.run(sys.argv)
