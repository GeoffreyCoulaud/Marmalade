from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageOption")


@_attrs_define
class ImageOption:
    """
    Attributes:
        type (Union[Unset, ImageType]): Enum ImageType.
        limit (Union[Unset, int]): Gets or sets the limit.
        min_width (Union[Unset, int]): Gets or sets the minimum width.
    """

    type: Union[Unset, ImageType] = UNSET
    limit: Union[Unset, int] = UNSET
    min_width: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        limit = self.limit
        min_width = self.min_width

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if limit is not UNSET:
            field_dict["Limit"] = limit
        if min_width is not UNSET:
            field_dict["MinWidth"] = min_width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Union[Unset, ImageType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ImageType(_type)

        limit = d.pop("Limit", UNSET)

        min_width = d.pop("MinWidth", UNSET)

        image_option = cls(
            type=type,
            limit=limit,
            min_width=min_width,
        )

        return image_option
