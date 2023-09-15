from enum import Enum


class HardwareEncodingType(str, Enum):
    AMF = "AMF"
    NVENC = "NVENC"
    QSV = "QSV"
    V4L2M2M = "V4L2M2M"
    VAAPI = "VAAPI"
    VIDEOTOOLBOX = "VideoToolBox"

    def __str__(self) -> str:
        return str(self.value)
