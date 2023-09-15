from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalUrl")


@_attrs_define
class ExternalUrl:
    """
    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        url (Union[Unset, None, str]): Gets or sets the type of the item.
    """

    name: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if url is not UNSET:
            field_dict["Url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        url = d.pop("Url", UNSET)

        external_url = cls(
            name=name,
            url=url,
        )

        return external_url
