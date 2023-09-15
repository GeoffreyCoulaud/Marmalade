from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectPlayProfile")


@_attrs_define
class DirectPlayProfile:
    """
    Attributes:
        container (Union[Unset, None, str]):
        audio_codec (Union[Unset, None, str]):
        video_codec (Union[Unset, None, str]):
        type (Union[Unset, DlnaProfileType]):
    """

    container: Union[Unset, None, str] = UNSET
    audio_codec: Union[Unset, None, str] = UNSET
    video_codec: Union[Unset, None, str] = UNSET
    type: Union[Unset, DlnaProfileType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        container = self.container
        audio_codec = self.audio_codec
        video_codec = self.video_codec
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if container is not UNSET:
            field_dict["Container"] = container
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        container = d.pop("Container", UNSET)

        audio_codec = d.pop("AudioCodec", UNSET)

        video_codec = d.pop("VideoCodec", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, DlnaProfileType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DlnaProfileType(_type)

        direct_play_profile = cls(
            container=container,
            audio_codec=audio_codec,
            video_codec=video_codec,
            type=type,
        )

        return direct_play_profile
