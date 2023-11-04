from typing import Any

from gi.repository import GObject


class ListStoreItem(GObject.Object):
    """Wrapper object to store widgets of any type in a Gio.ListStore"""

    __gtype_name__ = "MarmaladeListStoreItem"

    value: Any

    def __init__(self, widget: Any, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.value = widget
