import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.log_level import LogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityLogEntry")


@_attrs_define
class ActivityLogEntry:
    """An activity log entry.

    Attributes:
        id (Union[Unset, int]): Gets or sets the identifier.
        name (Union[Unset, str]): Gets or sets the name.
        overview (Union[Unset, None, str]): Gets or sets the overview.
        short_overview (Union[Unset, None, str]): Gets or sets the short overview.
        type (Union[Unset, str]): Gets or sets the type.
        item_id (Union[Unset, None, str]): Gets or sets the item identifier.
        date (Union[Unset, datetime.datetime]): Gets or sets the date.
        user_id (Union[Unset, str]): Gets or sets the user identifier.
        user_primary_image_tag (Union[Unset, None, str]): Gets or sets the user primary image tag.
        severity (Union[Unset, LogLevel]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    overview: Union[Unset, None, str] = UNSET
    short_overview: Union[Unset, None, str] = UNSET
    type: Union[Unset, str] = UNSET
    item_id: Union[Unset, None, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET
    user_primary_image_tag: Union[Unset, None, str] = UNSET
    severity: Union[Unset, LogLevel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        overview = self.overview
        short_overview = self.short_overview
        type = self.type
        item_id = self.item_id
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        user_id = self.user_id
        user_primary_image_tag = self.user_primary_image_tag
        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if overview is not UNSET:
            field_dict["Overview"] = overview
        if short_overview is not UNSET:
            field_dict["ShortOverview"] = short_overview
        if type is not UNSET:
            field_dict["Type"] = type
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if date is not UNSET:
            field_dict["Date"] = date
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_primary_image_tag is not UNSET:
            field_dict["UserPrimaryImageTag"] = user_primary_image_tag
        if severity is not UNSET:
            field_dict["Severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        overview = d.pop("Overview", UNSET)

        short_overview = d.pop("ShortOverview", UNSET)

        type = d.pop("Type", UNSET)

        item_id = d.pop("ItemId", UNSET)

        _date = d.pop("Date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        user_id = d.pop("UserId", UNSET)

        user_primary_image_tag = d.pop("UserPrimaryImageTag", UNSET)

        _severity = d.pop("Severity", UNSET)
        severity: Union[Unset, LogLevel]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = LogLevel(_severity)

        activity_log_entry = cls(
            id=id,
            name=name,
            overview=overview,
            short_overview=short_overview,
            type=type,
            item_id=item_id,
            date=date,
            user_id=user_id,
            user_primary_image_tag=user_primary_image_tag,
            severity=severity,
        )

        return activity_log_entry
