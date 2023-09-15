from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.hardware_encoding_type import HardwareEncodingType
from ..models.transcode_reason import TranscodeReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodingInfo")


@_attrs_define
class TranscodingInfo:
    """
    Attributes:
        audio_codec (Union[Unset, None, str]):
        video_codec (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
        is_video_direct (Union[Unset, bool]):
        is_audio_direct (Union[Unset, bool]):
        bitrate (Union[Unset, None, int]):
        framerate (Union[Unset, None, float]):
        completion_percentage (Union[Unset, None, float]):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        audio_channels (Union[Unset, None, int]):
        hardware_acceleration_type (Union[Unset, None, HardwareEncodingType]): Enum HardwareEncodingType.
        transcode_reasons (Union[Unset, List[TranscodeReason]]):
    """

    audio_codec: Union[Unset, None, str] = UNSET
    video_codec: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET
    is_video_direct: Union[Unset, bool] = UNSET
    is_audio_direct: Union[Unset, bool] = UNSET
    bitrate: Union[Unset, None, int] = UNSET
    framerate: Union[Unset, None, float] = UNSET
    completion_percentage: Union[Unset, None, float] = UNSET
    width: Union[Unset, None, int] = UNSET
    height: Union[Unset, None, int] = UNSET
    audio_channels: Union[Unset, None, int] = UNSET
    hardware_acceleration_type: Union[Unset, None, HardwareEncodingType] = UNSET
    transcode_reasons: Union[Unset, List[TranscodeReason]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        audio_codec = self.audio_codec
        video_codec = self.video_codec
        container = self.container
        is_video_direct = self.is_video_direct
        is_audio_direct = self.is_audio_direct
        bitrate = self.bitrate
        framerate = self.framerate
        completion_percentage = self.completion_percentage
        width = self.width
        height = self.height
        audio_channels = self.audio_channels
        hardware_acceleration_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.hardware_acceleration_type, Unset):
            hardware_acceleration_type = (
                self.hardware_acceleration_type.value if self.hardware_acceleration_type else None
            )

        transcode_reasons: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transcode_reasons, Unset):
            transcode_reasons = []
            for transcode_reasons_item_data in self.transcode_reasons:
                transcode_reasons_item = transcode_reasons_item_data.value

                transcode_reasons.append(transcode_reasons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if container is not UNSET:
            field_dict["Container"] = container
        if is_video_direct is not UNSET:
            field_dict["IsVideoDirect"] = is_video_direct
        if is_audio_direct is not UNSET:
            field_dict["IsAudioDirect"] = is_audio_direct
        if bitrate is not UNSET:
            field_dict["Bitrate"] = bitrate
        if framerate is not UNSET:
            field_dict["Framerate"] = framerate
        if completion_percentage is not UNSET:
            field_dict["CompletionPercentage"] = completion_percentage
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if audio_channels is not UNSET:
            field_dict["AudioChannels"] = audio_channels
        if hardware_acceleration_type is not UNSET:
            field_dict["HardwareAccelerationType"] = hardware_acceleration_type
        if transcode_reasons is not UNSET:
            field_dict["TranscodeReasons"] = transcode_reasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        audio_codec = d.pop("AudioCodec", UNSET)

        video_codec = d.pop("VideoCodec", UNSET)

        container = d.pop("Container", UNSET)

        is_video_direct = d.pop("IsVideoDirect", UNSET)

        is_audio_direct = d.pop("IsAudioDirect", UNSET)

        bitrate = d.pop("Bitrate", UNSET)

        framerate = d.pop("Framerate", UNSET)

        completion_percentage = d.pop("CompletionPercentage", UNSET)

        width = d.pop("Width", UNSET)

        height = d.pop("Height", UNSET)

        audio_channels = d.pop("AudioChannels", UNSET)

        _hardware_acceleration_type = d.pop("HardwareAccelerationType", UNSET)
        hardware_acceleration_type: Union[Unset, None, HardwareEncodingType]
        if _hardware_acceleration_type is None:
            hardware_acceleration_type = None
        elif isinstance(_hardware_acceleration_type, Unset):
            hardware_acceleration_type = UNSET
        else:
            hardware_acceleration_type = HardwareEncodingType(_hardware_acceleration_type)

        transcode_reasons = []
        _transcode_reasons = d.pop("TranscodeReasons", UNSET)
        for transcode_reasons_item_data in _transcode_reasons or []:
            transcode_reasons_item = TranscodeReason(transcode_reasons_item_data)

            transcode_reasons.append(transcode_reasons_item)

        transcoding_info = cls(
            audio_codec=audio_codec,
            video_codec=video_codec,
            container=container,
            is_video_direct=is_video_direct,
            is_audio_direct=is_audio_direct,
            bitrate=bitrate,
            framerate=framerate,
            completion_percentage=completion_percentage,
            width=width,
            height=height,
            audio_channels=audio_channels,
            hardware_acceleration_type=hardware_acceleration_type,
            transcode_reasons=transcode_reasons,
        )

        return transcoding_info
