from enum import Enum


class MediaStreamType(str, Enum):
    AUDIO = "Audio"
    DATA = "Data"
    EMBEDDEDIMAGE = "EmbeddedImage"
    SUBTITLE = "Subtitle"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)
