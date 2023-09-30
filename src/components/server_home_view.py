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

from gi.repository import Adw
from gi.repository import Gtk

from src import build_constants


@Gtk.Template(resource_path=build_constants.PREFIX + "/templates/server_home_view.ui")
class ServerHomeView(Adw.Bin):
    __gtype_name__ = "MarmaladeServerHomeView"

    window: Gtk.Window

    def __init__(self, window: Gtk.Window, **kwargs):
        super().__init__(**kwargs)
        self.window = window
