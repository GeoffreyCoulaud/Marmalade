import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationInfo")


@_attrs_define
class AuthenticationInfo:
    """
    Attributes:
        id (Union[Unset, int]): Gets or sets the identifier.
        access_token (Union[Unset, None, str]): Gets or sets the access token.
        device_id (Union[Unset, None, str]): Gets or sets the device identifier.
        app_name (Union[Unset, None, str]): Gets or sets the name of the application.
        app_version (Union[Unset, None, str]): Gets or sets the application version.
        device_name (Union[Unset, None, str]): Gets or sets the name of the device.
        user_id (Union[Unset, str]): Gets or sets the user identifier.
        is_active (Union[Unset, bool]): Gets or sets a value indicating whether this instance is active.
        date_created (Union[Unset, datetime.datetime]): Gets or sets the date created.
        date_revoked (Union[Unset, None, datetime.datetime]): Gets or sets the date revoked.
        date_last_activity (Union[Unset, datetime.datetime]):
        user_name (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    access_token: Union[Unset, None, str] = UNSET
    device_id: Union[Unset, None, str] = UNSET
    app_name: Union[Unset, None, str] = UNSET
    app_version: Union[Unset, None, str] = UNSET
    device_name: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_revoked: Union[Unset, None, datetime.datetime] = UNSET
    date_last_activity: Union[Unset, datetime.datetime] = UNSET
    user_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        access_token = self.access_token
        device_id = self.device_id
        app_name = self.app_name
        app_version = self.app_version
        device_name = self.device_name
        user_id = self.user_id
        is_active = self.is_active
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_revoked: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_revoked, Unset):
            date_revoked = self.date_revoked.isoformat() if self.date_revoked else None

        date_last_activity: Union[Unset, str] = UNSET
        if not isinstance(self.date_last_activity, Unset):
            date_last_activity = self.date_last_activity.isoformat()

        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if device_name is not UNSET:
            field_dict["DeviceName"] = device_name
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if is_active is not UNSET:
            field_dict["IsActive"] = is_active
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_revoked is not UNSET:
            field_dict["DateRevoked"] = date_revoked
        if date_last_activity is not UNSET:
            field_dict["DateLastActivity"] = date_last_activity
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        access_token = d.pop("AccessToken", UNSET)

        device_id = d.pop("DeviceId", UNSET)

        app_name = d.pop("AppName", UNSET)

        app_version = d.pop("AppVersion", UNSET)

        device_name = d.pop("DeviceName", UNSET)

        user_id = d.pop("UserId", UNSET)

        is_active = d.pop("IsActive", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_revoked = d.pop("DateRevoked", UNSET)
        date_revoked: Union[Unset, None, datetime.datetime]
        if _date_revoked is None:
            date_revoked = None
        elif isinstance(_date_revoked, Unset):
            date_revoked = UNSET
        else:
            date_revoked = isoparse(_date_revoked)

        _date_last_activity = d.pop("DateLastActivity", UNSET)
        date_last_activity: Union[Unset, datetime.datetime]
        if isinstance(_date_last_activity, Unset):
            date_last_activity = UNSET
        else:
            date_last_activity = isoparse(_date_last_activity)

        user_name = d.pop("UserName", UNSET)

        authentication_info = cls(
            id=id,
            access_token=access_token,
            device_id=device_id,
            app_name=app_name,
            app_version=app_version,
            device_name=device_name,
            user_id=user_id,
            is_active=is_active,
            date_created=date_created,
            date_revoked=date_revoked,
            date_last_activity=date_last_activity,
            user_name=user_name,
        )

        return authentication_info
