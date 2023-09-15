from enum import Enum


class FFmpegLocation(str, Enum):
    CUSTOM = "Custom"
    NOTFOUND = "NotFound"
    SETBYARGUMENT = "SetByArgument"
    SYSTEM = "System"

    def __str__(self) -> str:
        return str(self.value)
