from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_dto import NotificationDto


T = TypeVar("T", bound="NotificationResultDto")


@_attrs_define
class NotificationResultDto:
    """A list of notifications with the total record count for pagination.

    Attributes:
        notifications (Union[Unset, List['NotificationDto']]): Gets or sets the current page of notifications.
        total_record_count (Union[Unset, int]): Gets or sets the total number of notifications.
    """

    notifications: Union[Unset, List["NotificationDto"]] = UNSET
    total_record_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        notifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.to_dict()

                notifications.append(notifications_item)

        total_record_count = self.total_record_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if notifications is not UNSET:
            field_dict["Notifications"] = notifications
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_dto import NotificationDto

        d = src_dict.copy()
        notifications = []
        _notifications = d.pop("Notifications", UNSET)
        for notifications_item_data in _notifications or []:
            notifications_item = NotificationDto.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        total_record_count = d.pop("TotalRecordCount", UNSET)

        notification_result_dto = cls(
            notifications=notifications,
            total_record_count=total_record_count,
        )

        return notification_result_dto
