# servers_view.py
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

from gi.repository import Gtk

from src import build_constants
from src.components.server_row import ServerRow
from src.reactive_set import ReactiveSet
from src.server import Server


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/servers_view.ui")
class ServersView(Gtk.Box):
    __gtype_name__ = "MarmaladeServersView"

    server_rows_group = Gtk.Template.Child()
    servers: ReactiveSet[Server]
    server_rows = dict[Server, ServerRow]

    def __init__(self, servers: set[Server], **kwargs):
        super().__init__(**kwargs)
        self.servers = servers
        self.create_server_rows(*servers)

    def create_server_rows(self, *servers: Server) -> None:
        for server in servers:
            row = ServerRow(server)
            self.server_rows_group.add(row)
            self.server_rows[server] = row

    def remove_server_rows(self, *servers: Server):
        for server in servers:
            row = self.server_rows[server]
            self.server_rows_group.remove(row)
