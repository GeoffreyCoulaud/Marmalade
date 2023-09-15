from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.media_path_info import MediaPathInfo


T = TypeVar("T", bound="UpdateMediaPathRequestDto")


@_attrs_define
class UpdateMediaPathRequestDto:
    """Update library options dto.

    Attributes:
        name (str): Gets or sets the library name.
        path_info (MediaPathInfo):
    """

    name: str
    path_info: "MediaPathInfo"

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        path_info = self.path_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "Name": name,
                "PathInfo": path_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_path_info import MediaPathInfo

        d = src_dict.copy()
        name = d.pop("Name")

        path_info = MediaPathInfo.from_dict(d.pop("PathInfo"))

        update_media_path_request_dto = cls(
            name=name,
            path_info=path_info,
        )

        return update_media_path_request_dto
