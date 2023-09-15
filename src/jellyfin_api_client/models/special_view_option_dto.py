from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpecialViewOptionDto")


@_attrs_define
class SpecialViewOptionDto:
    """Special view option dto.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets view option name.
        id (Union[Unset, None, str]): Gets or sets view option id.
    """

    name: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        id = d.pop("Id", UNSET)

        special_view_option_dto = cls(
            name=name,
            id=id,
        )

        return special_view_option_dto
