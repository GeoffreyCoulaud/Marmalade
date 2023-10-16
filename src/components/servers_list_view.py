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

from src import build_constants, shared
from src.components.marmalade_navigation_page import MarmaladeNavigationPage
from src.components.server_add_dialog import ServerAddDialog
from src.components.server_row import ServerRow
from src.database.api import DataHandler, ServerInfo


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/servers_list_view.ui")
class ServersListView(MarmaladeNavigationPage):
    """
    Servers list view navigation page.

    This is the page that is shown to the user when they aren't connected to a server.

    In charge of:
    - Adding servers
    - Deleting servers
    - Starting the login process on a server
    """

    __gtype_name__ = "MarmaladeServersListView"

    edit_button = Gtk.Template.Child()
    add_button = Gtk.Template.Child()
    add_button_revealer = Gtk.Template.Child()
    remove_selected_button = Gtk.Template.Child()
    remove_selected_button_revealer = Gtk.Template.Child()
    server_rows_group = Gtk.Template.Child()
    servers_view_stack = Gtk.Template.Child()
    status_add_button = Gtk.Template.Child()
    toast_overlay = Gtk.Template.Child()

    __rows: set[ServerRow]
    __servers_trash: set[ServerInfo]
    __edit_mode: bool
    __edit_toggled_id: int

    @GObject.Signal(name="server-added", arg_types=[object])
    def server_added(self, _server: ServerInfo):
        """Signal emitted when a server is added"""

    @GObject.Signal(name="server-removed", arg_types=[str])
    def server_removed(self, _address: str):
        """Signal emitted when a server is removed"""

    @GObject.Signal(name="server-connect-request", arg_types=[object])
    def server_connect_request(self, _server: ServerInfo):
        """Signal emitted when a server is connected"""

    def __init__(self, *args, **kwargs):
        """Create a server list view"""

        super().__init__(*args, **kwargs)
        self.__rows = set()
        self.__servers_trash = set()
        self.__edit_mode = False

        # Initial content
        self.refresh_servers()

        # React to user inputs
        self.add_button.connect("clicked", self.on_add_button_clicked)
        self.status_add_button.connect("clicked", self.on_add_button_clicked)
        self.remove_selected_button.connect(
            "clicked", self.on_remove_selected_button_clicked
        )
        self.__edit_toggled_id = self.edit_button.connect(
            "toggled", self.on_edit_button_toggled
        )

    def refresh_servers(self) -> None:
        """Refresh the server list from the database"""
        # Empty the view
        for row in set(self.__rows):
            self.__rows.remove(row)
            self.server_rows_group.remove(row)
        # Refill it
        servers = shared.settings.get_servers()
        for server in servers:
            self.add_server(server, False)

    def add_server(self, server: ServerInfo, add_to_settings: bool = True) -> None:
        # Add to the settings database
        if add_to_settings:
            shared.settings.add_server(server)
        # Create visible row
        row = ServerRow(server)
        row.connect("button-clicked", self.on_server_connect_request)
        self.__rows.add(row)
        self.server_rows_group.add(row)
        self.servers_view_stack.set_visible_child_name("servers")

    def on_add_button_clicked(self, _button) -> None:
        addresses = {row.server.address for row in self.__rows}
        dialog = ServerAddDialog(addresses=addresses)
        dialog.connect("server-picked", self.on_add_dialog_picked)
        dialog.set_transient_for(shared.window)
        dialog.set_modal(True)
        dialog.present()

    def on_add_dialog_picked(self, _dialog, server: ServerInfo) -> None:
        self.add_server(server)

    def toggle_edit_mode(self) -> None:
        self.__edit_mode = not self.__edit_mode
        self.add_button_revealer.set_reveal_child(not self.__edit_mode)
        self.remove_selected_button_revealer.set_reveal_child(self.__edit_mode)
        for server_row in self.__rows:
            server_row.edit_mode = self.__edit_mode

    def on_edit_button_toggled(self, _button) -> None:
        self.toggle_edit_mode()

    def create_removed_toast(self) -> None:
        toast = Adw.Toast()
        match len(self.__servers_trash):
            case 0:
                # Nothing removed
                return
            case 1:
                # Single server removed
                toast.set_title(_("1 server removed"))
            case n:
                # Multiple servers removed
                toast.set_title(_("%d servers removed") % n)
        toast.set_button_label(_("Undo"))
        toast.connect("button-clicked", self.on_removed_toast_undo)
        self.__toast_overlay.add_toast(toast)

    def on_remove_selected_button_clicked(self, _button) -> None:
        selected = [row for row in self.__rows if row.is_selected]
        self.__servers_trash.clear()
        for row in selected:
            self.server_rows_group.remove(row)
            self.__rows.remove(row)
            self.__servers_trash.add(row.server)
            shared.settings.remove_server(row.server.address)
        if len(self.__rows) == 0:
            self.servers_view_stack.set_visible_child_name("no-server")
        with self.edit_button.freeze_notify(self.__edit_toggled_id):
            self.toggle_edit_mode()
        self.create_removed_toast()

    def on_removed_toast_undo(self, _toast) -> None:
        for server in self.__servers_trash:
            self.add_server(server)
        self.__servers_trash.clear()

    def on_server_connect_request(self, row: ServerRow) -> None:
        self.emit("server-connect-request", row.server)
