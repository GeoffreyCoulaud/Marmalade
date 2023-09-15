from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultDirectoryBrowserInfoDto")


@_attrs_define
class DefaultDirectoryBrowserInfoDto:
    """Default directory browser info.

    Attributes:
        path (Union[Unset, None, str]): Gets or sets the path.
    """

    path: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("Path", UNSET)

        default_directory_browser_info_dto = cls(
            path=path,
        )

        return default_directory_browser_info_dto
