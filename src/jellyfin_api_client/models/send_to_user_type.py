from enum import Enum


class SendToUserType(str, Enum):
    ADMINS = "Admins"
    ALL = "All"
    CUSTOM = "Custom"

    def __str__(self) -> str:
        return str(self.value)
