import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChapterInfo")


@_attrs_define
class ChapterInfo:
    """Class ChapterInfo.

    Attributes:
        start_position_ticks (Union[Unset, int]): Gets or sets the start position ticks.
        name (Union[Unset, None, str]): Gets or sets the name.
        image_path (Union[Unset, None, str]): Gets or sets the image path.
        image_date_modified (Union[Unset, datetime.datetime]):
        image_tag (Union[Unset, None, str]):
    """

    start_position_ticks: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    image_path: Union[Unset, None, str] = UNSET
    image_date_modified: Union[Unset, datetime.datetime] = UNSET
    image_tag: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_position_ticks = self.start_position_ticks
        name = self.name
        image_path = self.image_path
        image_date_modified: Union[Unset, str] = UNSET
        if not isinstance(self.image_date_modified, Unset):
            image_date_modified = self.image_date_modified.isoformat()

        image_tag = self.image_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks
        if name is not UNSET:
            field_dict["Name"] = name
        if image_path is not UNSET:
            field_dict["ImagePath"] = image_path
        if image_date_modified is not UNSET:
            field_dict["ImageDateModified"] = image_date_modified
        if image_tag is not UNSET:
            field_dict["ImageTag"] = image_tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_position_ticks = d.pop("StartPositionTicks", UNSET)

        name = d.pop("Name", UNSET)

        image_path = d.pop("ImagePath", UNSET)

        _image_date_modified = d.pop("ImageDateModified", UNSET)
        image_date_modified: Union[Unset, datetime.datetime]
        if isinstance(_image_date_modified, Unset):
            image_date_modified = UNSET
        else:
            image_date_modified = isoparse(_image_date_modified)

        image_tag = d.pop("ImageTag", UNSET)

        chapter_info = cls(
            start_position_ticks=start_position_ticks,
            name=name,
            image_path=image_path,
            image_date_modified=image_date_modified,
            image_tag=image_tag,
        )

        return chapter_info
