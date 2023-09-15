from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.send_to_user_type import SendToUserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationOption")


@_attrs_define
class NotificationOption:
    """
    Attributes:
        type (Union[Unset, None, str]):
        disabled_monitor_users (Union[Unset, List[str]]): Gets or sets user Ids to not monitor (it's opt out).
        send_to_users (Union[Unset, List[str]]): Gets or sets user Ids to send to (if SendToUserMode == Custom).
        enabled (Union[Unset, bool]): Gets or sets a value indicating whether this
            MediaBrowser.Model.Notifications.NotificationOption is enabled.
        disabled_services (Union[Unset, List[str]]): Gets or sets the disabled services.
        send_to_user_mode (Union[Unset, SendToUserType]):
    """

    type: Union[Unset, None, str] = UNSET
    disabled_monitor_users: Union[Unset, List[str]] = UNSET
    send_to_users: Union[Unset, List[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    disabled_services: Union[Unset, List[str]] = UNSET
    send_to_user_mode: Union[Unset, SendToUserType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        disabled_monitor_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disabled_monitor_users, Unset):
            disabled_monitor_users = self.disabled_monitor_users

        send_to_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.send_to_users, Unset):
            send_to_users = self.send_to_users

        enabled = self.enabled
        disabled_services: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disabled_services, Unset):
            disabled_services = self.disabled_services

        send_to_user_mode: Union[Unset, str] = UNSET
        if not isinstance(self.send_to_user_mode, Unset):
            send_to_user_mode = self.send_to_user_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if disabled_monitor_users is not UNSET:
            field_dict["DisabledMonitorUsers"] = disabled_monitor_users
        if send_to_users is not UNSET:
            field_dict["SendToUsers"] = send_to_users
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if disabled_services is not UNSET:
            field_dict["DisabledServices"] = disabled_services
        if send_to_user_mode is not UNSET:
            field_dict["SendToUserMode"] = send_to_user_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("Type", UNSET)

        disabled_monitor_users = cast(List[str], d.pop("DisabledMonitorUsers", UNSET))

        send_to_users = cast(List[str], d.pop("SendToUsers", UNSET))

        enabled = d.pop("Enabled", UNSET)

        disabled_services = cast(List[str], d.pop("DisabledServices", UNSET))

        _send_to_user_mode = d.pop("SendToUserMode", UNSET)
        send_to_user_mode: Union[Unset, SendToUserType]
        if isinstance(_send_to_user_mode, Unset):
            send_to_user_mode = UNSET
        else:
            send_to_user_mode = SendToUserType(_send_to_user_mode)

        notification_option = cls(
            type=type,
            disabled_monitor_users=disabled_monitor_users,
            send_to_users=send_to_users,
            enabled=enabled,
            disabled_services=disabled_services,
            send_to_user_mode=send_to_user_mode,
        )

        return notification_option
