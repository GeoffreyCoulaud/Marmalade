from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceOptionsDto")


@_attrs_define
class DeviceOptionsDto:
    """A dto representing custom options for a device.

    Attributes:
        id (Union[Unset, int]): Gets or sets the id.
        device_id (Union[Unset, None, str]): Gets or sets the device id.
        custom_name (Union[Unset, None, str]): Gets or sets the custom name.
    """

    id: Union[Unset, int] = UNSET
    device_id: Union[Unset, None, str] = UNSET
    custom_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        device_id = self.device_id
        custom_name = self.custom_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if custom_name is not UNSET:
            field_dict["CustomName"] = custom_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        device_id = d.pop("DeviceId", UNSET)

        custom_name = d.pop("CustomName", UNSET)

        device_options_dto = cls(
            id=id,
            device_id=device_id,
            custom_name=custom_name,
        )

        return device_options_dto
