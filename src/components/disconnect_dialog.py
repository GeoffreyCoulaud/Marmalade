from gi.repository import Adw, Gtk


class DisconnectDialog(Adw.MessageDialog):
    __gtype_name__ = "MarmaladeDisconnectDialog"

    def __init_widget(self):
        self.set_heading(_("Exit Server"))
        # fmt: off
        self.set_body(_("Disconnecting without logging out preserves the user session and avoids having to authenticate later."))
        # fmt: on

        for name, text, appearance in (
            ("cancel", _("Cancel"), Adw.ResponseAppearance.DEFAULT),
            ("log-off", _("Disconnect"), Adw.ResponseAppearance.SUGGESTED),
            ("log-out", _("Log Out"), Adw.ResponseAppearance.DESTRUCTIVE),
        ):
            self.add_response(name, text)
            self.set_response_appearance(name, appearance)

    def __init__(self):
        super().__init__()
        self.__init_widget()
