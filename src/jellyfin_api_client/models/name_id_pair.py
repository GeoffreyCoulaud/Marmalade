from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameIdPair")


@_attrs_define
class NameIdPair:
    """
    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        id (Union[Unset, None, str]): Gets or sets the identifier.
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

        name_id_pair = cls(
            name=name,
            id=id,
        )

        return name_id_pair
