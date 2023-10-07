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

from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.server import Server


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_home_view.ui")
class ServerHomeView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeServerHomeView"

    @GObject.Signal(name="log-out", arg_types=[object, str])
    def log_out(self, _server: Server, _token: str):
        """Signal emitted when the user logs out of the server (discard the token)"""

    @GObject.Signal(name="log-off", arg_types=[object])
    def log_off(self, _server: Server):
        """
        Signal emitted when the user logs off the server.
        Should also be emitted alongside log-out.
        """

    label: Gtk.Label = Gtk.Template.Child()

    window: Gtk.Window
    server: Server
    token: str

    def __init__(
        self,
        *args,
        window: Gtk.Window,
        server: Server,
        token: str,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.window = window
        self.server = server
        self.token = token

        # Variable is the server's name
        self.set_title(_("%s Home") % self.server.name)

        # TODO implement
        label = "\n".join(
            (
                f"Server: {self.server.name}",
                f"Address: {self.server.address}",
                f"Token: {self.token}",
            )
        )
        self.label.set_label(label)
