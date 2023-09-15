from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaUpdateInfoPathDto")


@_attrs_define
class MediaUpdateInfoPathDto:
    """The media update info path.

    Attributes:
        path (Union[Unset, None, str]): Gets or sets media path.
        update_type (Union[Unset, None, str]): Gets or sets media update type.
            Created, Modified, Deleted.
    """

    path: Union[Unset, None, str] = UNSET
    update_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        update_type = self.update_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path
        if update_type is not UNSET:
            field_dict["UpdateType"] = update_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("Path", UNSET)

        update_type = d.pop("UpdateType", UNSET)

        media_update_info_path_dto = cls(
            path=path,
            update_type=update_type,
        )

        return media_update_info_path_dto
