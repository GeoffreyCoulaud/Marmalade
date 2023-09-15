from enum import Enum


class PluginStatus(str, Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    DISABLED = "Disabled"
    MALFUNCTIONED = "Malfunctioned"
    NOTSUPPORTED = "NotSupported"
    RESTART = "Restart"
    SUPERCEDED = "Superceded"

    def __str__(self) -> str:
        return str(self.value)
