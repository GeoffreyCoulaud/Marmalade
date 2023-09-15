import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_capabilities import ClientCapabilities


T = TypeVar("T", bound="DeviceInfo")


@_attrs_define
class DeviceInfo:
    """
    Attributes:
        name (Union[Unset, None, str]):
        access_token (Union[Unset, None, str]): Gets or sets the access token.
        id (Union[Unset, None, str]): Gets or sets the identifier.
        last_user_name (Union[Unset, None, str]): Gets or sets the last name of the user.
        app_name (Union[Unset, None, str]): Gets or sets the name of the application.
        app_version (Union[Unset, None, str]): Gets or sets the application version.
        last_user_id (Union[Unset, str]): Gets or sets the last user identifier.
        date_last_activity (Union[Unset, datetime.datetime]): Gets or sets the date last modified.
        capabilities (Union[Unset, None, ClientCapabilities]):
        icon_url (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    access_token: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    last_user_name: Union[Unset, None, str] = UNSET
    app_name: Union[Unset, None, str] = UNSET
    app_version: Union[Unset, None, str] = UNSET
    last_user_id: Union[Unset, str] = UNSET
    date_last_activity: Union[Unset, datetime.datetime] = UNSET
    capabilities: Union[Unset, None, "ClientCapabilities"] = UNSET
    icon_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        access_token = self.access_token
        id = self.id
        last_user_name = self.last_user_name
        app_name = self.app_name
        app_version = self.app_version
        last_user_id = self.last_user_id
        date_last_activity: Union[Unset, str] = UNSET
        if not isinstance(self.date_last_activity, Unset):
            date_last_activity = self.date_last_activity.isoformat()

        capabilities: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict() if self.capabilities else None

        icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if id is not UNSET:
            field_dict["Id"] = id
        if last_user_name is not UNSET:
            field_dict["LastUserName"] = last_user_name
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if last_user_id is not UNSET:
            field_dict["LastUserId"] = last_user_id
        if date_last_activity is not UNSET:
            field_dict["DateLastActivity"] = date_last_activity
        if capabilities is not UNSET:
            field_dict["Capabilities"] = capabilities
        if icon_url is not UNSET:
            field_dict["IconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_capabilities import ClientCapabilities

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        access_token = d.pop("AccessToken", UNSET)

        id = d.pop("Id", UNSET)

        last_user_name = d.pop("LastUserName", UNSET)

        app_name = d.pop("AppName", UNSET)

        app_version = d.pop("AppVersion", UNSET)

        last_user_id = d.pop("LastUserId", UNSET)

        _date_last_activity = d.pop("DateLastActivity", UNSET)
        date_last_activity: Union[Unset, datetime.datetime]
        if isinstance(_date_last_activity, Unset):
            date_last_activity = UNSET
        else:
            date_last_activity = isoparse(_date_last_activity)

        _capabilities = d.pop("Capabilities", UNSET)
        capabilities: Union[Unset, None, ClientCapabilities]
        if _capabilities is None:
            capabilities = None
        elif isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = ClientCapabilities.from_dict(_capabilities)

        icon_url = d.pop("IconUrl", UNSET)

        device_info = cls(
            name=name,
            access_token=access_token,
            id=id,
            last_user_name=last_user_name,
            app_name=app_name,
            app_version=app_version,
            last_user_id=last_user_id,
            date_last_activity=date_last_activity,
            capabilities=capabilities,
            icon_url=icon_url,
        )

        return device_info
