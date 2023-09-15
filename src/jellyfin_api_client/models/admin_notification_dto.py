from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.notification_level import NotificationLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminNotificationDto")


@_attrs_define
class AdminNotificationDto:
    """The admin notification dto.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the notification name.
        description (Union[Unset, None, str]): Gets or sets the notification description.
        notification_level (Union[Unset, None, NotificationLevel]):
        url (Union[Unset, None, str]): Gets or sets the notification url.
    """

    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    notification_level: Union[Unset, None, NotificationLevel] = UNSET
    url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        notification_level: Union[Unset, None, str] = UNSET
        if not isinstance(self.notification_level, Unset):
            notification_level = self.notification_level.value if self.notification_level else None

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if notification_level is not UNSET:
            field_dict["NotificationLevel"] = notification_level
        if url is not UNSET:
            field_dict["Url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        _notification_level = d.pop("NotificationLevel", UNSET)
        notification_level: Union[Unset, None, NotificationLevel]
        if _notification_level is None:
            notification_level = None
        elif isinstance(_notification_level, Unset):
            notification_level = UNSET
        else:
            notification_level = NotificationLevel(_notification_level)

        url = d.pop("Url", UNSET)

        admin_notification_dto = cls(
            name=name,
            description=description,
            notification_level=notification_level,
            url=url,
        )

        return admin_notification_dto
