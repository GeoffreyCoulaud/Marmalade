from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryOptionInfoDto")


@_attrs_define
class LibraryOptionInfoDto:
    """Library option info dto.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets name.
        default_enabled (Union[Unset, bool]): Gets or sets a value indicating whether default enabled.
    """

    name: Union[Unset, None, str] = UNSET
    default_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        default_enabled = self.default_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if default_enabled is not UNSET:
            field_dict["DefaultEnabled"] = default_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        default_enabled = d.pop("DefaultEnabled", UNSET)

        library_option_info_dto = cls(
            name=name,
            default_enabled=default_enabled,
        )

        return library_option_info_dto
