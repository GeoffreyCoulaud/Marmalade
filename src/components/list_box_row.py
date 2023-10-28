from gi.repository import GLib, GObject, Gtk


class ListBoxRow(Gtk.ListBoxRow):
    """
    Simple extension of the Gtk.ListBoxRow, with an easier to set action target

    Adds a convenience `action-target-string` property to easily get and set the
    `Gtk.Actionnable.action-target` value as a string.
    Also exposes getter and setter methods for that property.
    """

    __gtype_name__ = "MarmaladeListBoxRow"

    # action_target_string property

    @GObject.Property(type=str)
    def action_target_string(self) -> str:
        return self.get_action_target_value().get_string()

    def get_action_target_string(self) -> str:
        return self.get_property("action_target_string")

    @action_target_string.setter
    def action_target_string(self, value: str) -> None:
        self.set_action_target_value(GLib.Variant.new_string(value))

    def set_action_target_string(self, value: str):
        self.set_property("action_target_string", value)
