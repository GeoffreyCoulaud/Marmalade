from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.profile_condition_type import ProfileConditionType
from ..models.profile_condition_value import ProfileConditionValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileCondition")


@_attrs_define
class ProfileCondition:
    """
    Attributes:
        condition (Union[Unset, ProfileConditionType]):
        property_ (Union[Unset, ProfileConditionValue]):
        value (Union[Unset, None, str]):
        is_required (Union[Unset, bool]):
    """

    condition: Union[Unset, ProfileConditionType] = UNSET
    property_: Union[Unset, ProfileConditionValue] = UNSET
    value: Union[Unset, None, str] = UNSET
    is_required: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        condition: Union[Unset, str] = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.value

        property_: Union[Unset, str] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.value

        value = self.value
        is_required = self.is_required

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if condition is not UNSET:
            field_dict["Condition"] = condition
        if property_ is not UNSET:
            field_dict["Property"] = property_
        if value is not UNSET:
            field_dict["Value"] = value
        if is_required is not UNSET:
            field_dict["IsRequired"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _condition = d.pop("Condition", UNSET)
        condition: Union[Unset, ProfileConditionType]
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = ProfileConditionType(_condition)

        _property_ = d.pop("Property", UNSET)
        property_: Union[Unset, ProfileConditionValue]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = ProfileConditionValue(_property_)

        value = d.pop("Value", UNSET)

        is_required = d.pop("IsRequired", UNSET)

        profile_condition = cls(
            condition=condition,
            property_=property_,
            value=value,
            is_required=is_required,
        )

        return profile_condition
