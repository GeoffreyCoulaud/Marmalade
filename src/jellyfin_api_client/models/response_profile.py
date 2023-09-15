from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="ResponseProfile")


@_attrs_define
class ResponseProfile:
    """
    Attributes:
        container (Union[Unset, None, str]):
        audio_codec (Union[Unset, None, str]):
        video_codec (Union[Unset, None, str]):
        type (Union[Unset, DlnaProfileType]):
        org_pn (Union[Unset, None, str]):
        mime_type (Union[Unset, None, str]):
        conditions (Union[Unset, None, List['ProfileCondition']]):
    """

    container: Union[Unset, None, str] = UNSET
    audio_codec: Union[Unset, None, str] = UNSET
    video_codec: Union[Unset, None, str] = UNSET
    type: Union[Unset, DlnaProfileType] = UNSET
    org_pn: Union[Unset, None, str] = UNSET
    mime_type: Union[Unset, None, str] = UNSET
    conditions: Union[Unset, None, List["ProfileCondition"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        container = self.container
        audio_codec = self.audio_codec
        video_codec = self.video_codec
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        org_pn = self.org_pn
        mime_type = self.mime_type
        conditions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            if self.conditions is None:
                conditions = None
            else:
                conditions = []
                for conditions_item_data in self.conditions:
                    conditions_item = conditions_item_data.to_dict()

                    conditions.append(conditions_item)

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
        if org_pn is not UNSET:
            field_dict["OrgPn"] = org_pn
        if mime_type is not UNSET:
            field_dict["MimeType"] = mime_type
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

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

        org_pn = d.pop("OrgPn", UNSET)

        mime_type = d.pop("MimeType", UNSET)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ProfileCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        response_profile = cls(
            container=container,
            audio_codec=audio_codec,
            video_codec=video_codec,
            type=type,
            org_pn=org_pn,
            mime_type=mime_type,
            conditions=conditions,
        )

        return response_profile
