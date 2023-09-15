from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.device_profile_type import DeviceProfileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceProfileInfo")


@_attrs_define
class DeviceProfileInfo:
    """
    Attributes:
        id (Union[Unset, None, str]): Gets or sets the identifier.
        name (Union[Unset, None, str]): Gets or sets the name.
        type (Union[Unset, DeviceProfileType]):
    """

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    type: Union[Unset, DeviceProfileType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, DeviceProfileType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DeviceProfileType(_type)

        device_profile_info = cls(
            id=id,
            name=name,
            type=type,
        )

        return device_profile_info
