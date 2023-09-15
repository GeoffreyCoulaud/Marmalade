from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryInfo")


@_attrs_define
class RepositoryInfo:
    """Class RepositoryInfo.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        url (Union[Unset, None, str]): Gets or sets the URL.
        enabled (Union[Unset, bool]): Gets or sets a value indicating whether the repository is enabled.
    """

    name: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        url = self.url
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if url is not UNSET:
            field_dict["Url"] = url
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        url = d.pop("Url", UNSET)

        enabled = d.pop("Enabled", UNSET)

        repository_info = cls(
            name=name,
            url=url,
            enabled=enabled,
        )

        return repository_info
