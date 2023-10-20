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

import logging

from gi.repository import Adw, Gtk

from src import build_constants, shared
from src.components.auth_dialog import AuthDialog
from src.components.server_add_dialog import ServerAddDialog
from src.components.server_browser_view import ServerBrowserView
from src.components.server_row import ServerRow
from src.database.api import ServerInfo
from src.jellyfin import JellyfinClient


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/servers_list_view.ui")
class ServersListView(Adw.NavigationPage):
    """
    Servers list view navigation page.

    This is the page that is shown to the user when they aren't connected to a server.

    In charge of:
    - Adding servers
    - Deleting servers
    - Starting the login process on a server
    """

    __gtype_name__ = "MarmaladeServersListView"

    # fmt: off
    __edit_button            = Gtk.Template.Child("edit_button")
    __add_button             = Gtk.Template.Child("add_button")
    __add_button_revealer    = Gtk.Template.Child("add_button_revealer")
    __delete_button          = Gtk.Template.Child("delete_button")
    __delete_button_revealer = Gtk.Template.Child("delete_button_revealer")
    __server_rows_group      = Gtk.Template.Child("server_rows_group")
    __servers_view_stack     = Gtk.Template.Child("servers_view_stack")
    __status_add_button      = Gtk.Template.Child("status_add_button")
    __toast_overlay          = Gtk.Template.Child("toast_overlay")
    # fmt: on

    __rows: set[ServerRow]
    __servers_trash: set[ServerInfo]
    __edit_mode: bool

    def __init__(self, *args, **kwargs):
        """Create a server list view"""

        super().__init__(*args, **kwargs)
        self.__rows = set()
        self.__servers_trash = set()
        self.__edit_mode = False

        # Initial content
        self.refresh_servers()

        # React to user inputs
        self.__add_button.connect("clicked", self.on_add_button_clicked)
        self.__status_add_button.connect("clicked", self.on_add_button_clicked)
        self.__delete_button.connect("clicked", self.on_delete_button_clicked)
        self.__edit_button.connect("toggled", self.on_edit_button_toggled)
        self.connect("map", self.__on_mapped)

    def __on_mapped(self, _page) -> None:
        self.refresh_servers()

    def refresh_servers(self) -> None:
        """Refresh the server list from the database"""
        logging.debug("Refreshing servers view")
        # Empty the view
        for row in set(self.__rows):
            self.__rows.remove(row)
            self.__server_rows_group.remove(row)
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
        self.__server_rows_group.add(row)
        self.__servers_view_stack.set_visible_child_name("servers")

    def on_add_button_clicked(self, _button) -> None:
        addresses = {row.server.address for row in self.__rows}
        dialog = ServerAddDialog(addresses=addresses)
        dialog.connect("server-picked", self.on_add_dialog_picked)
        dialog.set_transient_for(self.get_root())
        dialog.set_modal(True)
        dialog.present()

    def on_add_dialog_picked(self, _dialog, server: ServerInfo) -> None:
        self.add_server(server)

    def toggle_edit_mode(self) -> None:
        self.__edit_mode = not self.__edit_mode
        self.__add_button_revealer.set_reveal_child(not self.__edit_mode)
        self.__delete_button_revealer.set_reveal_child(self.__edit_mode)
        for server_row in self.__rows:
            server_row.edit_mode = self.__edit_mode

    def on_edit_button_toggled(self, _button) -> None:
        self.toggle_edit_mode()

    def on_delete_button_clicked(self, _button) -> None:
        selected = [row for row in self.__rows if row.is_selected]
        self.__servers_trash.clear()
        for row in selected:
            self.__server_rows_group.remove(row)
            self.__rows.remove(row)
            self.__servers_trash.add(row.server)
            shared.settings.remove_server(row.server.address)
        if len(self.__rows) == 0:
            self.__servers_view_stack.set_visible_child_name("no-server")
        with self.__edit_button.freeze_notify():
            self.toggle_edit_mode()
        self.create_removed_toast()

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

    def on_removed_toast_undo(self, _toast) -> None:
        for server in self.__servers_trash:
            self.add_server(server)
        self.__servers_trash.clear()

    def on_server_connect_request(self, row: ServerRow) -> None:
        dialog = AuthDialog(row.server)
        dialog.connect("authenticated", self.on_authenticated)
        dialog.set_transient_for(self.get_root())
        dialog.set_modal(True)
        dialog.present()

    def on_authenticated(self, _widget, address: str, user_id: str) -> None:
        shared.settings.set_active_token(address=address, user_id=user_id)
        info = shared.settings.get_token(address=address, user_id=user_id)
        client = JellyfinClient(address, device_id=info.device_id, token=info.token)
        server_home_view = ServerBrowserView(client=client, user_id=user_id)
        navigation = self.get_parent()
        navigation.push(server_home_view)
