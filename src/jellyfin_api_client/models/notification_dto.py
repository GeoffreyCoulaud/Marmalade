import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.notification_level import NotificationLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationDto")


@_attrs_define
class NotificationDto:
    """The notification DTO.

    Attributes:
        id (Union[Unset, str]): Gets or sets the notification ID. Defaults to an empty string.
        user_id (Union[Unset, str]): Gets or sets the notification's user ID. Defaults to an empty string.
        date (Union[Unset, datetime.datetime]): Gets or sets the notification date.
        is_read (Union[Unset, bool]): Gets or sets a value indicating whether the notification has been read. Defaults
            to false.
        name (Union[Unset, str]): Gets or sets the notification's name. Defaults to an empty string.
        description (Union[Unset, str]): Gets or sets the notification's description. Defaults to an empty string.
        url (Union[Unset, str]): Gets or sets the notification's URL. Defaults to an empty string.
        level (Union[Unset, NotificationLevel]):
    """

    id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    is_read: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    level: Union[Unset, NotificationLevel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        is_read = self.is_read
        name = self.name
        description = self.description
        url = self.url
        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if date is not UNSET:
            field_dict["Date"] = date
        if is_read is not UNSET:
            field_dict["IsRead"] = is_read
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if url is not UNSET:
            field_dict["Url"] = url
        if level is not UNSET:
            field_dict["Level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        user_id = d.pop("UserId", UNSET)

        _date = d.pop("Date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        is_read = d.pop("IsRead", UNSET)

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        url = d.pop("Url", UNSET)

        _level = d.pop("Level", UNSET)
        level: Union[Unset, NotificationLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = NotificationLevel(_level)

        notification_dto = cls(
            id=id,
            user_id=user_id,
            date=date,
            is_read=is_read,
            name=name,
            description=description,
            url=url,
            level=level,
        )

        return notification_dto
