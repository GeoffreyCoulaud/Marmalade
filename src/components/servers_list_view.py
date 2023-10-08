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

from gi.repository import Adw, GObject, Gtk

from src import build_constants
from src.components.server_add_dialog import ServerAddDialog
from src.components.server_row import ServerRow
from src.reactive_set import ReactiveSet
from src.server import Server


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/servers_list_view.ui")
class ServersListView(Adw.NavigationPage):
    __gtype_name__ = "MarmaladeServersListView"

    edit_button = Gtk.Template.Child()
    add_button = Gtk.Template.Child()
    add_button_revealer = Gtk.Template.Child()
    remove_selected_button = Gtk.Template.Child()
    remove_selected_button_revealer = Gtk.Template.Child()
    server_rows_group = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()
    servers_view_stack = Gtk.Template.Child()
    status_add_button = Gtk.Template.Child()

    window: Gtk.Window
    server_rows_mapping: dict[Server, ServerRow]
    servers: ReactiveSet[Server]
    servers_trash: set[Server]

    edit_mode: bool

    @GObject.Signal(name="server-connect-request", arg_types=[object])
    def server_connect_request(self, _server: Server):
        """Signal emitted when a server is connected"""

    def __init__(
        self,
        *args,
        window: Gtk.Window,
        servers: ReactiveSet[Server],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.edit_mode = False
        self.server_rows_mapping = {}
        self.servers_trash = set()
        self.window = window
        self.servers = servers

        # Initial content
        for server in self.servers:
            self.create_server_row(server)
        self.on_servers_changed(None)

        # React to content change / user inputs
        self.servers.emitter.connect("changed", self.on_servers_changed)
        self.servers.emitter.connect("item-added", self.on_server_added)
        self.servers.emitter.connect("item-removed", self.on_server_removed)
        self.add_button.connect("clicked", self.on_add_button_clicked)
        self.status_add_button.connect("clicked", self.on_add_button_clicked)
        self.edit_button.connect("clicked", self.on_edit_button_clicked)
        self.remove_selected_button.connect(
            "clicked", self.on_remove_selected_button_clicked
        )

    def create_server_row(self, server: Server) -> None:
        row = ServerRow(server)
        row.connect("button-clicked", self.on_server_connect_request)
        self.server_rows_mapping[server] = row
        self.server_rows_group.add(row)

    def remove_server_row(self, server: Server):
        row = self.server_rows_mapping[server]
        del self.server_rows_mapping[server]
        self.server_rows_group.remove(row)

    def on_servers_changed(self, _emitter) -> None:
        self.servers_view_stack.set_visible_child_name(
            "no-server" if len(self.servers) == 0 else "servers"
        )

    def on_server_added(self, _emitter, server: Server) -> None:
        self.create_server_row(server)

    def on_server_removed(self, _emitter, server: Server) -> None:
        self.remove_server_row(server)

    def on_add_button_clicked(self, _button) -> None:
        dialog = ServerAddDialog()
        dialog.connect("server-picked", self.on_add_server_dialog_picked)
        dialog.set_transient_for(self.window)
        dialog.set_modal(True)
        dialog.present()

    def on_add_server_dialog_picked(self, _dialog, server: Server) -> None:
        self.servers.add(server)

    def toggle_edit_mode(self) -> None:
        self.edit_mode = not self.edit_mode
        self.add_button_revealer.set_reveal_child(not self.edit_mode)
        self.remove_selected_button_revealer.set_reveal_child(self.edit_mode)
        self.edit_button.set_css_classes(["raised"] if self.edit_mode else ["flat"])
        for server_row in self.server_rows_mapping.values():
            server_row.edit_mode = self.edit_mode

    def on_edit_button_clicked(self, _button) -> None:
        self.toggle_edit_mode()

    def create_removed_toast(self) -> None:
        n_removed = len(self.servers_trash)
        toast = Adw.Toast()
        toast.set_title(
            (
                _("%d server removed")  # Single server removed
                if n_removed == 1
                else _("%d servers removed")  # Multiple servers removed
            )
            % n_removed,
        )
        toast.set_button_label(_("Undo"))
        toast.connect("button-clicked", self.on_removed_toast_undo)
        self.toast_overlay.add_toast(toast)

    def on_remove_selected_button_clicked(self, _button) -> None:
        rows = self.server_rows_mapping.values()
        servers = [row.server for row in rows if row.is_selected]
        self.servers_trash.clear()
        self.servers_trash.update(servers)
        self.servers.difference_update(servers)
        self.toggle_edit_mode()
        self.create_removed_toast()

    def on_removed_toast_undo(self, _toast) -> None:
        self.servers.update(self.servers_trash)
        self.servers_trash.clear()

    def on_server_connect_request(self, row: ServerRow) -> None:
        server = row.server
        self.emit("server-connect-request", server)
