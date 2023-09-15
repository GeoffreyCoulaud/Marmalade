from enum import Enum


class HeaderMatchType(str, Enum):
    EQUALS = "Equals"
    REGEX = "Regex"
    SUBSTRING = "Substring"

    def __str__(self) -> str:
        return str(self.value)
