from enum import Enum


class NotificationLevel(str, Enum):
    ERROR = "Error"
    NORMAL = "Normal"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
