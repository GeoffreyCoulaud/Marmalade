from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaUrl")


@_attrs_define
class MediaUrl:
    """
    Attributes:
        url (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
    """

    url: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if url is not UNSET:
            field_dict["Url"] = url
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("Url", UNSET)

        name = d.pop("Name", UNSET)

        media_url = cls(
            url=url,
            name=name,
        )

        return media_url
