import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickConnectResult")


@_attrs_define
class QuickConnectResult:
    """Stores the state of an quick connect request.

    Attributes:
        authenticated (Union[Unset, bool]): Gets or sets a value indicating whether this request is authorized.
        secret (Union[Unset, str]): Gets the secret value used to uniquely identify this request. Can be used to
            retrieve authentication information.
        code (Union[Unset, str]): Gets the user facing code used so the user can quickly differentiate this request from
            others.
        device_id (Union[Unset, str]): Gets the requesting device id.
        device_name (Union[Unset, str]): Gets the requesting device name.
        app_name (Union[Unset, str]): Gets the requesting app name.
        app_version (Union[Unset, str]): Gets the requesting app version.
        date_added (Union[Unset, datetime.datetime]): Gets or sets the DateTime that this request was created.
    """

    authenticated: Union[Unset, bool] = UNSET
    secret: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    app_version: Union[Unset, str] = UNSET
    date_added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        authenticated = self.authenticated
        secret = self.secret
        code = self.code
        device_id = self.device_id
        device_name = self.device_name
        app_name = self.app_name
        app_version = self.app_version
        date_added: Union[Unset, str] = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["Authenticated"] = authenticated
        if secret is not UNSET:
            field_dict["Secret"] = secret
        if code is not UNSET:
            field_dict["Code"] = code
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if device_name is not UNSET:
            field_dict["DeviceName"] = device_name
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if date_added is not UNSET:
            field_dict["DateAdded"] = date_added

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authenticated = d.pop("Authenticated", UNSET)

        secret = d.pop("Secret", UNSET)

        code = d.pop("Code", UNSET)

        device_id = d.pop("DeviceId", UNSET)

        device_name = d.pop("DeviceName", UNSET)

        app_name = d.pop("AppName", UNSET)

        app_version = d.pop("AppVersion", UNSET)

        _date_added = d.pop("DateAdded", UNSET)
        date_added: Union[Unset, datetime.datetime]
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        quick_connect_result = cls(
            authenticated=authenticated,
            secret=secret,
            code=code,
            device_id=device_id,
            device_name=device_name,
            app_name=app_name,
            app_version=app_version,
            date_added=date_added,
        )

        return quick_connect_result
