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
from typing import cast

from gi.repository import Adw, Gtk

from src import shared
from src.components.auth_dialog import AuthDialog
from src.components.server_add_dialog import ServerAddDialog
from src.components.server_browser_view import ServerBrowserView
from src.components.servers_list_row import ServersListRow
from src.components.widget_builder import (
    Children,
    Handlers,
    Properties,
    TypedChild,
    build,
)
from src.database.api import ServerInfo
from src.jellyfin import JellyfinClient


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

    __edit_button: Gtk.Button
    __add_button: Gtk.Button
    __add_button_revealer: Gtk.Revealer
    __delete_button: Gtk.Button
    __delete_button_revealer: Gtk.Revealer
    __server_rows_group: Adw.PreferencesGroup
    __servers_view_stack: Adw.ViewStack
    __status_add_button: Gtk.Button
    __toast_overlay: Adw.ToastOverlay

    __no_server_view: Gtk.Widget
    __servers_view: Gtk.Widget

    __rows: set[ServersListRow]
    __servers_trash: set[ServerInfo]
    __edit_mode: bool

    def __init_widget(self):
        self.__server_rows_group = build(
            Adw.PreferencesGroup + Properties(title=_("Servers"))
        )

        self.__no_server_view = build(
            Adw.StatusPage
            + Properties(
                title=_("No Servers Found"),
                description=_("Use the + button to discover or add a Jellyfin server"),
                icon_name="network-server-symbolic",
            )
            + Children(
                Gtk.Button
                + Properties(
                    css_classes=["pill", "suggested-action"],
                    halign=Gtk.Align.CENTER,
                    label=_("Add Jellyfin Server"),
                )
            )
        )

        self.__servers_view = build(Adw.Clamp + Children(self.__server_rows_group))

        self.__servers_view_stack = build(
            Adw.ViewStack
            + Properties(
                margin_top=16,
                margin_start=16,
                margin_end=16,
                margin_bottom=16,
            )
            + Children(
                self.__no_server_view,
                self.__servers_view,
            )
        )

        self.__toast_overlay = build(
            Adw.ToastOverlay + Children(self.__servers_view_stack)
        )

        self.__edit_button = build(
            Gtk.ToggleButton
            + Handlers(toggled=self.__on_edit_button_toggled)
            + Properties(
                icon_name="document-edit-symbolic",
                margin_end=4,
            )
        )

        self.__add_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_add_button_clicked)
            + Properties(icon_name="list-add-symbolic")
        )

        self.__add_button_revealer = build(
            Gtk.Revealer
            + Properties(
                reveal_child=True,
                transition_type=Gtk.RevealerTransitionType.SLIDE_RIGHT,
            )
            + Children(self.__add_button)
        )

        self.__delete_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_delete_button_clicked)
            + Properties(icon_name="user-trash-symbolic")
        )

        self.__delete_button_revealer = build(
            Gtk.Revealer
            + Properties(
                reveal_child=False,
                transition_type=Gtk.RevealerTransitionType.SLIDE_RIGHT,
            )
            + Children(self.__delete_button)
        )

        header_bar = (
            Adw.HeaderBar
            + TypedChild(
                "start",
                Gtk.Box
                + Children(
                    self.__edit_button,
                    self.__add_button_revealer,
                    self.__delete_button_revealer,
                ),
            )
            + TypedChild(
                "title",
                Adw.WindowTitle
                + Properties(
                    title=_(
                        "Marmalade",
                    )
                ),
            )
        )

        # The title property will not be show
        # since a Adw.WindowTitle is used instead
        self.set_title("servers-view")

        self.set_tag("servers-view")
        self.set_can_pop(False)
        self.set_child(
            build(
                Adw.ToolbarView
                + TypedChild("top", header_bar)
                + TypedChild("content", self.__toast_overlay)
            )
        )

    def __init__(self, *args, **kwargs):
        """Create a server list view"""

        super().__init__(*args, **kwargs)
        self.__init_widget()

        self.__rows = set()
        self.__servers_trash = set()
        self.__edit_mode = False
        self.connect("map", self.__on_mapped)

        self.refresh_servers()

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
        row = ServersListRow(server)
        row.connect("button-clicked", self.on_server_connect_request)
        self.__rows.add(row)
        self.__server_rows_group.add(row)
        self.__servers_view_stack.set_visible_child(self.__servers_view)

    def __on_add_button_clicked(self, _button) -> None:
        addresses = {row.server.address for row in self.__rows}
        window = cast(Adw.ApplicationWindow, self.get_root())
        application = cast(Adw.Application, window.get_application())
        dialog = ServerAddDialog(application=application, addresses=addresses)
        dialog.connect("server-picked", self.on_add_dialog_picked)
        dialog.set_transient_for(window)
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

    def __on_edit_button_toggled(self, _button) -> None:
        self.toggle_edit_mode()

    def __on_delete_button_clicked(self, _button) -> None:
        selected = [row for row in self.__rows if row.is_selected]
        self.__servers_trash.clear()
        for row in selected:
            self.__server_rows_group.remove(row)
            self.__rows.remove(row)
            self.__servers_trash.add(row.server)
            shared.settings.remove_server(row.server.address)
        if len(self.__rows) == 0:
            self.__servers_view_stack.set_visible_child(self.__no_server_view)
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

    def on_server_connect_request(self, row: ServersListRow) -> None:
        window = cast(Adw.ApplicationWindow, self.get_root())
        application = cast(Adw.Application, window.get_application())
        dialog = AuthDialog(application=application, server=row.server)
        dialog.connect("authenticated", self.on_authenticated)
        dialog.set_transient_for(window)
        dialog.set_modal(True)
        dialog.present()

    def on_authenticated(self, _widget, address: str, user_id: str) -> None:
        shared.settings.set_active_token(address=address, user_id=user_id)
        info = shared.settings.get_token(address=address, user_id=user_id)
        client = JellyfinClient(address, device_id=info.device_id, token=info.token)  # type: ignore
        server_home_view = ServerBrowserView(client=client, user_id=user_id)
        navigation = cast(Adw.NavigationView, self.get_parent())
        navigation.push(server_home_view)
