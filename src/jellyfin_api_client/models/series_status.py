from enum import Enum


class SeriesStatus(str, Enum):
    CONTINUING = "Continuing"
    ENDED = "Ended"

    def __str__(self) -> str:
        return str(self.value)
