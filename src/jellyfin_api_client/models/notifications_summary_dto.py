from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.notification_level import NotificationLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationsSummaryDto")


@_attrs_define
class NotificationsSummaryDto:
    """The notification summary DTO.

    Attributes:
        unread_count (Union[Unset, int]): Gets or sets the number of unread notifications.
        max_unread_notification_level (Union[Unset, None, NotificationLevel]):
    """

    unread_count: Union[Unset, int] = UNSET
    max_unread_notification_level: Union[Unset, None, NotificationLevel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unread_count = self.unread_count
        max_unread_notification_level: Union[Unset, None, str] = UNSET
        if not isinstance(self.max_unread_notification_level, Unset):
            max_unread_notification_level = (
                self.max_unread_notification_level.value if self.max_unread_notification_level else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unread_count is not UNSET:
            field_dict["UnreadCount"] = unread_count
        if max_unread_notification_level is not UNSET:
            field_dict["MaxUnreadNotificationLevel"] = max_unread_notification_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unread_count = d.pop("UnreadCount", UNSET)

        _max_unread_notification_level = d.pop("MaxUnreadNotificationLevel", UNSET)
        max_unread_notification_level: Union[Unset, None, NotificationLevel]
        if _max_unread_notification_level is None:
            max_unread_notification_level = None
        elif isinstance(_max_unread_notification_level, Unset):
            max_unread_notification_level = UNSET
        else:
            max_unread_notification_level = NotificationLevel(_max_unread_notification_level)

        notifications_summary_dto = cls(
            unread_count=unread_count,
            max_unread_notification_level=max_unread_notification_level,
        )

        return notifications_summary_dto
