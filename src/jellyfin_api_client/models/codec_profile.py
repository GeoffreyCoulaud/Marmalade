from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.codec_type import CodecType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="CodecProfile")


@_attrs_define
class CodecProfile:
    """
    Attributes:
        type (Union[Unset, CodecType]):
        conditions (Union[Unset, None, List['ProfileCondition']]):
        apply_conditions (Union[Unset, None, List['ProfileCondition']]):
        codec (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
    """

    type: Union[Unset, CodecType] = UNSET
    conditions: Union[Unset, None, List["ProfileCondition"]] = UNSET
    apply_conditions: Union[Unset, None, List["ProfileCondition"]] = UNSET
    codec: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        conditions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            if self.conditions is None:
                conditions = None
            else:
                conditions = []
                for conditions_item_data in self.conditions:
                    conditions_item = conditions_item_data.to_dict()

                    conditions.append(conditions_item)

        apply_conditions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.apply_conditions, Unset):
            if self.apply_conditions is None:
                apply_conditions = None
            else:
                apply_conditions = []
                for apply_conditions_item_data in self.apply_conditions:
                    apply_conditions_item = apply_conditions_item_data.to_dict()

                    apply_conditions.append(apply_conditions_item)

        codec = self.codec
        container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if apply_conditions is not UNSET:
            field_dict["ApplyConditions"] = apply_conditions
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Union[Unset, CodecType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodecType(_type)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ProfileCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        apply_conditions = []
        _apply_conditions = d.pop("ApplyConditions", UNSET)
        for apply_conditions_item_data in _apply_conditions or []:
            apply_conditions_item = ProfileCondition.from_dict(apply_conditions_item_data)

            apply_conditions.append(apply_conditions_item)

        codec = d.pop("Codec", UNSET)

        container = d.pop("Container", UNSET)

        codec_profile = cls(
            type=type,
            conditions=conditions,
            apply_conditions=apply_conditions,
            codec=codec,
            container=container,
        )

        return codec_profile
