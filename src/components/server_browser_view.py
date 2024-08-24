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

import logging
from http import HTTPStatus
from typing import Callable, cast
from urllib.parse import parse_qsl, urlparse

from gi.repository import Adw, Gio, GLib, GObject, Gtk
from jellyfin_api_client.api.user import get_current_user
from jellyfin_api_client.api.user_views import get_user_views
from jellyfin_api_client.errors import UnexpectedStatus
from jellyfin_api_client.models.base_item_dto import BaseItemDto
from jellyfin_api_client.models.base_item_dto_query_result import BaseItemDtoQueryResult
from jellyfin_api_client.types import UNSET

from src import shared
from src.components.disconnect_dialog import DisconnectDialog
from src.components.list_box_row import ListBoxRow
from src.components.list_box_row_content import ListBoxRowContent
from src.components.server_browser import ServerBrowser
from src.components.server_browser_headerbar import ServerBrowserHeaderbar
from src.components.server_home_page import ServerHomePage
from src.components.server_page import ServerPage
from src.components.widget_builder import (
    Arguments,
    Children,
    Handlers,
    Properties,
    build,
)
from src.jellyfin import JellyfinClient
from src.task import Task


class ServerBrowserView(ServerBrowser):
    """
    Server browser page.

    This is the page that is shown to the user when they connect to a server.

    It is in charge of handling the `navigate` action.
    In that case, it is passed a destination string and optional parameters.
    """

    __gtype_name__ = "MarmaladeServerBrowserView"

    @GObject.Signal(name="log-out", arg_types=[str, str])
    def log_out_signal(self, _address: str, _user_id: str):
        """Signal emitted when the user logs out of the server (discard the token)"""

    @GObject.Signal(name="log-off", arg_types=[str])
    def log_off_signal(self, _address: str):
        """
        Signal emitted when the user logs off the server.
        Should also be emitted alongside log-out.
        """

    __admin_dashboard_link: Gtk.ListBoxRow
    __content_header_bar: ServerBrowserHeaderbar
    __libraries_list_box: Gtk.ListBox
    __navigation_view: Adw.NavigationView
    __search_bar: Gtk.SearchBar
    __server_links: Gtk.ListBox
    __sidebar_hide_button_revealer: Gtk.Revealer
    __overlay_split_view: Adw.OverlaySplitView
    __breakpoint_bin: Adw.BreakpointBin

    __actions: Gio.SimpleActionGroup
    __search_action: Gio.PropertyAction

    def __init_widget(self):
        self.__content_header_bar = build(ServerBrowserHeaderbar)

        self.__navigation_view = build(
            Adw.NavigationView
            + Handlers(**{"notify::visible-page": self.__on_page_changed})
        )

        search_entry = build(Gtk.SearchEntry + Properties(placeholder_text=_("Search")))

        self.__search_bar = build(
            Gtk.SearchBar + Children(Adw.Clamp + Children(search_entry))
        )
        self.__search_bar.connect_entry(search_entry)

        self.__admin_dashboard_link = build(
            ListBoxRow
            + Properties(
                action_name="browser.navigate",
                action_target_string="admin-dashboard",
                visible=False,
            )
            + Children(
                ListBoxRowContent
                + Properties(
                    icon_name="emblem-system-symbolic",
                    label=_("Administration dashboard"),
                )
            )
        )

        self.__libraries_list_box = build(
            Gtk.ListBox
            + Properties(
                css_classes=["navigation-sidebar"],
                selection_mode=Gtk.SelectionMode.NONE,
            )
        )

        def server_link_factory(
            icon_name: str,
            label: str,
            action_name: str,
            action_target_string: str | None = None,
        ) -> ListBoxRow:
            builder = (
                ListBoxRow
                + Properties(action_name=action_name)
                + Children(
                    ListBoxRowContent
                    + Properties(
                        icon_name=icon_name,
                        label=label,
                    )
                )
            )
            if action_target_string is not None:
                builder += Properties(action_target_string=action_target_string)
            return build(builder)

        self.__server_links = build(
            Gtk.ListBox
            + Properties(
                css_classes=["navigation-sidebar"],
                selection_mode=Gtk.SelectionMode.NONE,
            )
            + Children(
                server_link_factory(
                    icon_name="go-home-symbolic",
                    label=_("Home"),
                    action_name="browser.navigate",
                    action_target_string="home",
                ),
                server_link_factory(
                    icon_name="avatar-default-symbolic",
                    label=_("User settings"),
                    action_name="browser.navigate",
                    action_target_string="user-settings",
                ),
                self.__admin_dashboard_link,
                server_link_factory(
                    icon_name="system-log-out-symbolic",
                    label=_("Exit server"),
                    action_name="browser.disconnect",
                ),
            )
        )
        self.__sidebar_hide_button_revealer = build(
            Gtk.Revealer
            + Properties(
                transition_type=Gtk.RevealerTransitionType.SLIDE_RIGHT,
                reveal_child=False,
            )
            + Children(
                Gtk.Button
                + Properties(
                    icon_name="sidebar-show-symbolic",
                    action_name="browser.hide-sidebar",
                    margin_end=8,
                )
            )
        )

        sidebar_header = (
            Adw.HeaderBar
            + Properties(show_back_button=False)
            + Children(
                self.__sidebar_hide_button_revealer,
                Gtk.Label
                + Properties(
                    css_classes=["heading"],
                    label=_("Navigation"),
                ),
                None,
            )
        )
        sidebar_content = (
            Gtk.ScrolledWindow
            + Properties(propagate_natural_width=True)
            + Children(
                Gtk.Box
                + Properties(orientation=Gtk.Orientation.VERTICAL)
                + Children(
                    self.__server_links,
                    Gtk.ListBox
                    + Properties(
                        css_classes=["navigation-sidebar"],
                        selection_mode=Gtk.SelectionMode.NONE,
                    )
                    + Children(
                        ListBoxRow
                        + Properties(activatable=False)
                        + Children(
                            Gtk.Label
                            + Properties(
                                css_classes=["heading"],
                                label=_("Libraries"),
                                halign=Gtk.Align.START,
                            )
                        )
                    ),
                    self.__libraries_list_box,
                )
            )
        )

        self.__overlay_split_view = build(
            Adw.OverlaySplitView
            + Handlers(**{"notify::show-sidebar": self.__on_sidebar_toggled})
            + Properties(show_sidebar=False, pin_sidebar=True)
            + Children(
                # Sidebar
                Adw.ToolbarView
                + Children(
                    sidebar_header,
                    sidebar_content,
                    None,
                ),
                # Content
                Adw.ToolbarView
                + Children(
                    Gtk.Box
                    + Properties(orientation=Gtk.Orientation.VERTICAL)
                    + Children(
                        self.__content_header_bar,
                        self.__search_bar,
                    ),
                    self.__navigation_view,
                    None,
                ),
            )
        )

        self.__breakpoint_bin = build(
            Adw.BreakpointBin
            + Arguments(width_request=360, height_request=400)
            # TODO set_size_request seems to be broken
            # + Properties(size_request=(360, 400))
            + Children(self.__overlay_split_view)
        )

        # Auto-collapse the sidebar when there is not enough space
        bp = Adw.Breakpoint(condition=Adw.BreakpointCondition.parse("max-width: 675sp"))
        bp.add_setter(self.__overlay_split_view, "collapsed", True)
        self.__breakpoint_bin.add_breakpoint(bp)

        self.set_child(self.__breakpoint_bin)

    def __init__(self, *args, client: JellyfinClient, user_id: str, **kwargs):
        super().__init__(*args, client=client, user_id=user_id, **kwargs)
        self.__init_widget()

        # Actions
        self.__actions = Gio.SimpleActionGroup()
        self.insert_action_group("browser", self.__actions)
        for args in (
            ("disconnect", None, self.__on_disconnect),
            ("show-sidebar", None, self.__on_sidebar_toggle_request, True),
            ("hide-sidebar", None, self.__on_sidebar_toggle_request, False),
            ("navigate", "s", self.__on_navigate),
            ("reload", None, self.__on_reload),
        ):
            self.__create_simple_action(*args)  # type: ignore
        self.__search_action = self.__create_prop_action(
            "search", self.__search_bar, "search-mode-enabled"
        )

        # Children signals
        self.connect("map", self.__on_mapped)

        # Navigate to the home page
        self.activate_action("browser.navigate", GLib.Variant.new_string("home"))

    def __create_simple_action(
        self, name: str, type_str: None | str, callback: Callable, *args
    ) -> Gio.SimpleAction:
        """Add a simple action and connect it to a callback with optional arguments"""
        variant_type = None if type_str is None else GLib.VariantType(type_str)
        action = Gio.SimpleAction.new(name, variant_type)
        action.connect("activate", callback, *args)
        self.__actions.add_action(action)
        return action

    def __create_prop_action(
        self, name: str, obj: GObject.Object, property_name: str
    ) -> Gio.PropertyAction:
        action = Gio.PropertyAction.new(name, obj, property_name)
        self.__actions.add_action(action)
        return action

    def __on_mapped(self, *_args) -> None:
        """Callback executed when this view is about to be shown"""
        shared.settings.update_connected_timestamp(address=self.client._base_url)
        self.__on_sidebar_toggled()
        self.__on_page_changed()
        self.__init_navigation_sidebar()

    def __init_navigation_sidebar(self) -> None:
        """Asynchronously initialize the navigation sidebar's content"""

        def query_admin():
            res = get_current_user.sync_detailed(client=self.client)
            if res.status_code == HTTPStatus.OK:
                return res.parsed.policy.is_administrator  # type: ignore
            raise UnexpectedStatus(res.status_code, res.content)

        def on_admin_success(is_admin: bool) -> None:
            logging.debug("Loaded user admin status: %s", str(is_admin))
            self.__admin_dashboard_link.set_visible(is_admin)

        def query_libraries():
            res = get_user_views.sync_detailed(client=self.client, user_id=self.user_id)
            if res.status_code == HTTPStatus.OK:
                return res.parsed
            raise UnexpectedStatus(res.status_code, res.content)

        def on_libraries_success(result: BaseItemDtoQueryResult) -> None:
            logging.debug("Loaded user libraries")
            items: list[BaseItemDto] = result.items  # type: ignore
            default_icon = "library-unknown-symbolic"
            icon_map = {
                "books": "library-books-symbolic",
                "boxsets": "library-collections-symbolic",
                "homevideos": "library-images-symbolic",
                "movies": "library-movies-symbolic",
                "music": "library-music-symbolic",
                "tvshows": "library-shows-symbolic",
                UNSET: "library-unknown-symbolic",
            }
            self.__libraries_list_box.remove_all()
            for item in items:
                logging.debug(
                    "Adding library %s (%s) to navigation",
                    item.name,
                    item.collection_type,
                )
                library_link = build(
                    ListBoxRow
                    + Properties(
                        action_name="browser.navigate",
                        action_target_string=f"library?id={item.id}",
                    )
                    + Children(
                        ListBoxRowContent
                        + Properties(
                            icon_name=icon_map.get(item.collection_type, default_icon),
                            label=item.name,
                        )
                    )
                )
                self.__libraries_list_box.append(library_link)
            pass

        for task in (
            Task(main=query_admin, callback=on_admin_success),
            Task(main=query_libraries, callback=on_libraries_success),
        ):
            task.run()

    __current_uri: str

    def __on_navigate(self, _widget, variant: GLib.Variant) -> None:
        """
        Handle the `navigate` action

        Will change the inner Adw.NavigationView to the requested page.
        Additional parameters are passed as kwargs to the page constructor.
        """

        # Parse the destination
        uri = variant.get_string()
        parsed = urlparse(url=uri)
        name = parsed.path
        kwargs = {}
        for key, value in parse_qsl(parsed.query):
            kwargs[key] = value

        logging.debug('Navigating to "%s", kwargs: %s', name, kwargs)

        # Handle the "back" destination name
        if name == "back":
            self.__navigation_view.pop()
            return

        # Create the page from the destination and args
        page_name_map = {
            "home": ServerHomePage,
            "user-settings": None,  # TODO implement user settings page
            "admin-dashboard": None,  # TODO implement admin dashboard page
            "library": None,  # TODO implement library page
        }
        try:
            klass = page_name_map[name]
            if klass is None:
                raise NotImplementedError()
        except KeyError:
            logging.error("Invalid destination %s", name)
            return
        except NotImplementedError:
            logging.error("Destination %s is not implemented", name)
            return
        page: ServerPage = klass(
            browser=self, headerbar=self.__content_header_bar, **kwargs
        )
        self.__current_uri = uri

        # Update the view
        if page.get_is_root():
            self.__navigation_view.replace([page])
        else:
            self.__navigation_view.push(page)
        page.load()

    def __on_page_changed(self, *_args) -> None:
        """Callback executed when the navigation view changes the current page"""

        # Get current navigation state
        page: None | Adw.NavigationPage = self.__navigation_view.get_visible_page()
        if page is None:
            return
        previous_page = self.__navigation_view.get_previous_page(page)

        # Update controls from navigation state
        self.__content_header_bar.toggle_back_button(previous_page is not None)

        # Bind controls properties to the page properties
        flags = GObject.BindingFlags.SYNC_CREATE
        page.bind_property("title", self.__content_header_bar, "title", flags)
        page.bind_property(
            "is_filterable", self.__content_header_bar, "filter_button_visible", flags
        )

    def __on_sidebar_toggle_request(self, *args) -> None:
        *_rest, shown = args
        self.__overlay_split_view.set_show_sidebar(shown)

    def __on_sidebar_toggled(self, *_args) -> None:
        shown = self.__overlay_split_view.get_show_sidebar()
        self.__sidebar_hide_button_revealer.set_reveal_child(shown)
        self.__content_header_bar.set_show_sidebar_button_visible(not shown)

    def __on_disconnect(self, *_args) -> None:
        dialog = DisconnectDialog()
        dialog.connect("response", self.__on_disconnect_dialog_response)
        dialog.set_transient_for(self.get_root())  # type: ignore
        dialog.set_modal(True)
        dialog.present()

    def __on_disconnect_dialog_response(self, _widget, response: str) -> None:
        match response:
            case "log-off":
                self.log_off()
            case "log-out":
                self.log_out()

    def __on_reload(self, *_args) -> None:
        """handle the reload action"""
        self.activate_action(
            "browser.navigate", GLib.Variant.new_string(self.__current_uri)
        )

    def log_off(self) -> None:
        """Disconnect from the server"""
        logging.debug("Logging off %s", self.client._base_url)
        shared.settings.unset_active_token()
        navigation = cast(Adw.NavigationView, self.get_parent())
        navigation.pop_to_tag("servers-view")

    def log_out(self) -> None:
        """Disconnect from the server, deleting the access token"""
        logging.debug(
            "Logging %s out of %s",
            self.user_id,
            self.client._base_url,
        )
        shared.settings.remove_token(
            address=self.client._base_url,
            user_id=self.user_id,
        )
        navigation = cast(Adw.NavigationView, self.get_parent())
        navigation.pop_to_tag("servers-view")
