from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_path_info import MediaPathInfo


T = TypeVar("T", bound="MediaPathDto")


@_attrs_define
class MediaPathDto:
    """Media Path dto.

    Attributes:
        name (str): Gets or sets the name of the library.
        path (Union[Unset, None, str]): Gets or sets the path to add.
        path_info (Union[Unset, None, MediaPathInfo]):
    """

    name: str
    path: Union[Unset, None, str] = UNSET
    path_info: Union[Unset, None, "MediaPathInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        path = self.path
        path_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.path_info, Unset):
            path_info = self.path_info.to_dict() if self.path_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
            }
        )
        if path is not UNSET:
            field_dict["Path"] = path
        if path_info is not UNSET:
            field_dict["PathInfo"] = path_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_path_info import MediaPathInfo

        d = src_dict.copy()
        name = d.pop("Name")

        path = d.pop("Path", UNSET)

        _path_info = d.pop("PathInfo", UNSET)
        path_info: Union[Unset, None, MediaPathInfo]
        if _path_info is None:
            path_info = None
        elif isinstance(_path_info, Unset):
            path_info = UNSET
        else:
            path_info = MediaPathInfo.from_dict(_path_info)

        media_path_dto = cls(
            name=name,
            path=path,
            path_info=path_info,
        )

        return media_path_dto
