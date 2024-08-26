from gi.repository import Adw, GObject, Gtk

from src.components.widget_builder import Children, Handlers, Properties, build
from src.database.api import ServerInfo


class ServersListRow(Adw.ActionRow):
    __gtype_name__ = "MarmaladeServersListRow"

    __button: Gtk.Button
    __button_revealer: Gtk.Revealer
    __tick: Gtk.CheckButton
    __tick_revealer: Gtk.Revealer

    @GObject.Signal(name="button-clicked")
    def button_clicked(self):
        """Signal emitted when the row button is clicked"""

    @GObject.Signal(name="selected-changed", arg_types=[bool])
    def selected_changed(self, _is_selected: bool):
        """Signal emitted when the tick is check or unchecked"""

    def __on_button_clicked(self, _button) -> None:
        self.emit("button-clicked")

    def __on_tick_toggled(self, _tick) -> None:
        self.emit("selected-changed", self.get_selected())

    def __init_widget(self):
        self.__button = build(
            Gtk.Button
            + Handlers(clicked=self.__on_button_clicked)
            + Properties(
                valign=Gtk.Align.CENTER,
            )
        )
        self.__button_revealer = build(
            Gtk.Revealer
            + Children(self.__button)
            + Properties(
                reveal_child=True,
                transition_type=Gtk.RevealerTransitionType.CROSSFADE,
            )
        )
        self.__tick = build(
            Gtk.CheckButton
            + Handlers(toggled=self.__on_tick_toggled)
            + Properties(
                css_classes=["selection-mode"],
                valign=Gtk.Align.CENTER,
            )
        )
        self.__tick_revealer = build(
            Gtk.Revealer
            + Children(self.__tick)
            + Properties(
                reveal_child=False,
                transition_type=Gtk.RevealerTransitionType.SLIDE_LEFT,
            )
        )
        self.set_selectable(False)
        self.set_activatable_widget(self.__button)
        self.add_suffix(self.__button_revealer)
        self.add_prefix(self.__tick_revealer)

    # selectable property

    @GObject.Property(type=bool, default=False)
    def selectable(self) -> bool:
        return self.__tick_revealer.get_reveal_child()

    def get_selectable(self) -> bool:
        return self.get_property("selectable")

    @selectable.setter
    def selectable_setter(self, selectable: bool) -> None:
        if selectable:
            self.__tick.set_active(False)
        self.__tick_revealer.set_reveal_child(selectable)
        self.__button_revealer.set_reveal_child(not selectable)
        self.set_activatable_widget(self.__tick if selectable else self.__button)

    def set_selectable(self, value: bool):
        self.set_property("selectable", value)

    # selected property

    @GObject.Property(type=bool, default=False)
    def selected(self) -> bool:
        return self.__tick.get_active()

    def get_selected(self) -> bool:
        return self.get_property("selected")

    @selected.setter
    def selected_setter(self, value: bool) -> None:
        self.__tick.set_active(value)

    def set_selected(self, value: bool):
        self.set_property("selected", value)

    # server property

    __server: ServerInfo

    @GObject.Property(type=object)
    def server(self) -> ServerInfo:
        return self.__server

    def get_server(self) -> ServerInfo:
        return self.get_property("server")

    @server.setter
    def server_setter(self, value: ServerInfo) -> None:
        self.__server = value

    def set_server(self, value: ServerInfo):
        self.set_property("server", value)

    # Public methods

    def __init__(
        self,
        server: ServerInfo,
        icon_name: str = "go-next-symbolic",
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.__init_widget()

        self.__server = server
        self.__button.set_icon_name(icon_name)
        self.set_title(server.name)
        self.set_subtitle(server.address)
