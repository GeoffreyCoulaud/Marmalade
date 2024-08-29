from typing import Optional, Sequence

from gi.repository import Adw, Gio, GLib, GObject, Gtk, Pango

from src.components.widget_builder import Children, Handlers, Properties, build


class ServerBrowserHeaderbar(Gtk.HeaderBar):
    __gtype_name__ = "MarmaladeServerBrowserHeaderbar"

    __back_button: Gtk.Button
    __disconnect_button: Gtk.Button
    __filter_button: Gtk.Button
    __filter_button_revealer: Gtk.Revealer
    __sidebar_show_button: Gtk.Button
    __sidebar_show_button_revealer: Gtk.Revealer
    __search_button_revealer: Gtk.Revealer
    __header_center_stack: Adw.ViewStack
    __header_left_stack: Adw.ViewStack
    __title: Adw.WindowTitle
    __path_bar: Gtk.Label

    # TODO instead of having everything inside and having to toggle visibility
    # expose the properties and let the parent decide how to use them

    def __init_widget(self):
        self.__sidebar_show_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_sidebar_show_clicked)
            + Properties(
                icon_name="sidebar-show-symbolic",
                action_name="browser.show-sidebar",
                margin_end=8,
            )
        )
        self.__sidebar_show_button_revealer = build(
            Gtk.Revealer
            + Children(self.__sidebar_show_button)
            + Properties(
                reveal_child=True,
                transition_type=Gtk.RevealerTransitionType.SLIDE_RIGHT,
            )
        )
        self.__back_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_back_clicked)
            + Properties(icon_name="go-previous")
        )
        self.__disconnect_button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_disconnect_clicked)
            + Properties(icon_name="system-log-out-symbolic")
        )
        self.__header_left_stack = build(
            Adw.ViewStack
            + Children(
                self.__back_button,
                self.__disconnect_button,
            )
        )
        packed_start = build(
            Gtk.Box
            + Children(
                self.__sidebar_show_button_revealer,
                self.__header_left_stack,
            )
        )

        self.__title = build(
            Adw.WindowTitle
            + Properties(
                title=_("Browsing Server"),
            )
        )
        # TODO replace with pathbar widget
        self.__path_bar = build(
            Gtk.Label
            + Properties(
                ellipsize=Pango.EllipsizeMode.MIDDLE,
            )
        )
        self.__header_center_stack = build(
            Adw.ViewStack
            + Children(
                self.__title,
                self.__path_bar,
            )
        )

        self.__search_button_revealer = build(
            Gtk.Revealer
            + Properties(reveal_child=False)
            + Children(
                Gtk.ToggleButton
                + Properties(
                    icon_name="system-search-symbolic",
                    action_name="browser.search",
                )
            )
        )

        filter_menu = Gio.Menu()
        filter_menu_section1 = Gio.Menu()
        filter_menu_section1.append(_("Sort by"), None)
        filter_menu.append_section(None, filter_menu_section1)
        filter_menu_section2 = Gio.Menu()
        filter_menu_section2.append(_("Filters"), None)
        filter_menu_section2.append(_("Genres"), None)
        filter_menu_section2.append(_("Age rating"), None)
        filter_menu_section2.append(_("Tags"), None)
        filter_menu_section2.append(_("Year"), None)
        filter_menu.append_section(None, filter_menu_section2)

        self.__filter_button = build(
            Gtk.MenuButton
            + Properties(
                icon_name="view-sort-descending-symbolic",
                menu_model=filter_menu,
            )
        )

        self.__filter_button_revealer = build(
            Gtk.Revealer
            + Properties(reveal_child=False)
            + Children(self.__filter_button)
        )

        preferences_menu = Gio.Menu()
        preferences_menu.append(_("Preferences"), "app.preferences")
        preferences_menu.append(_("Keyboard Shortcuts"), "win.show-help-overlay")
        preferences_menu.append(_("About Marmalade"), "app.about")

        preferences_button = build(
            Gtk.MenuButton
            + Properties(
                icon_name="open-menu-symbolic",
                menu_model=preferences_menu,
            )
        )

        packed_end = build(
            Gtk.Box
            + Children(
                self.__search_button_revealer,
                self.__filter_button_revealer,
                preferences_button,
            )
        )

        self.pack_start(packed_start)
        self.pack_end(packed_end)
        self.set_title_widget(self.__header_center_stack)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_widget()

    def __on_sidebar_show_clicked(self, *_args) -> None:
        self.activate_action("browser.hide-sidebar")

    def __on_disconnect_clicked(self, *_args) -> None:
        self.activate_action("browser.disconnect")

    def __on_back_clicked(self, *_args) -> None:
        self.activate_action("browser.navigate", GLib.Variant.new_string("back"))

    def toggle_back_button(self, back_button_shown: bool = True) -> None:
        self.__header_left_stack.set_visible_child(
            self.__back_button if back_button_shown else self.__disconnect_button
        )

    # title property

    @GObject.Property(type=str, default="")
    def title(self) -> str:
        return self.__title.get_title()

    def get_title(self) -> str:
        return self.get_property("title")

    @title.setter
    def title_setter(self, value: str) -> None:
        self.__title.set_title(value)

    def set_title(self, value: str):
        self.set_property("title", value)

    # show_sidebar_button_visible property

    @GObject.Property(type=bool, default=True)
    def show_sidebar_button_visible(self) -> bool:
        return self.__sidebar_show_button_revealer.get_reveal_child()

    def get_show_sidebar_button_visible(self) -> bool:
        return self.get_property("show_sidebar_button_visible")

    @show_sidebar_button_visible.setter
    def show_sidebar_button_visible_setter(self, value: bool) -> None:
        self.__sidebar_show_button_revealer.set_reveal_child(value)

    def set_show_sidebar_button_visible(self, value: bool):
        self.set_property("show_sidebar_button_visible", value)

    # filter_button_visible property

    @GObject.Property(type=bool, default=True)
    def filter_button_visible(self) -> bool:
        return self.__filter_button_revealer.get_reveal_child()

    def get_filter_button_visible(self) -> bool:
        return self.get_property("filter_button_visible")

    @filter_button_visible.setter
    def filter_button_visible_setter(self, value: bool) -> None:
        self.__filter_button_revealer.set_reveal_child(value)

    def set_filter_button_visible(self, value: bool):
        self.set_property("filter_button_visible", value)

    # search_button_visible property

    @GObject.Property(type=bool, default=True)
    def search_button_visible(self) -> bool:
        return self.__search_button_revealer.get_reveal_child()

    def get_search_button_visible(self) -> bool:
        return self.get_property("search_button_visible")

    @search_button_visible.setter
    def search_button_visible_setter(self, value: bool) -> None:
        self.__search_button_revealer.set_reveal_child(value)

    def set_search_button_visible(self, value: bool):
        self.set_property("search_button_visible", value)

    # ancestors property

    __ancestors: Optional[Sequence[tuple[str, str]]]

    @GObject.Property(type=object, default=None)
    def ancestors(self) -> Optional[Sequence[tuple[str, str]]]:
        # TODO get the ancestors from the pathbar
        return self.__ancestors

    def get_ancestors(self) -> Optional[Sequence[tuple[str, str]]]:
        return self.get_property("ancestors")

    @ancestors.setter
    def ancestors_setter(self, value: Sequence[tuple[str, str]]) -> None:
        # TODO implement pathbar widget (currently just a label)
        # TODO pass the ancestors to the pathbar
        self.__ancestors = value
        if has_path := value is not None and len(value) > 0:
            path = " / ".join((name for name, _uri in self.__ancestors))
            self.__path_bar.set_label(path)
        self.__header_center_stack.set_visible_child_name(
            "path" if has_path else "title"
        )

    def set_ancestors(self, value: Optional[Sequence[tuple[str, str]]]):
        self.set_property("ancestors", value)
