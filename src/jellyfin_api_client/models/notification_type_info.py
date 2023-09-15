from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationTypeInfo")


@_attrs_define
class NotificationTypeInfo:
    """
    Attributes:
        type (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        enabled (Union[Unset, bool]):
        category (Union[Unset, None, str]):
        is_based_on_user_event (Union[Unset, bool]):
    """

    type: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    category: Union[Unset, None, str] = UNSET
    is_based_on_user_event: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name = self.name
        enabled = self.enabled
        category = self.category
        is_based_on_user_event = self.is_based_on_user_event

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if name is not UNSET:
            field_dict["Name"] = name
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if category is not UNSET:
            field_dict["Category"] = category
        if is_based_on_user_event is not UNSET:
            field_dict["IsBasedOnUserEvent"] = is_based_on_user_event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type", UNSET)

        name = d.pop("Name", UNSET)

        enabled = d.pop("Enabled", UNSET)

        category = d.pop("Category", UNSET)

        is_based_on_user_event = d.pop("IsBasedOnUserEvent", UNSET)

        notification_type_info = cls(
            type=type,
            name=name,
            enabled=enabled,
            category=category,
            is_based_on_user_event=is_based_on_user_event,
        )

        return notification_type_info
