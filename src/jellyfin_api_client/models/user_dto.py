import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_configuration import UserConfiguration
    from ..models.user_policy import UserPolicy


T = TypeVar("T", bound="UserDto")


@_attrs_define
class UserDto:
    """Class UserDto.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        server_id (Union[Unset, None, str]): Gets or sets the server identifier.
        server_name (Union[Unset, None, str]): Gets or sets the name of the server.
            This is not used by the server and is for client-side usage only.
        id (Union[Unset, str]): Gets or sets the id.
        primary_image_tag (Union[Unset, None, str]): Gets or sets the primary image tag.
        has_password (Union[Unset, bool]): Gets or sets a value indicating whether this instance has password.
        has_configured_password (Union[Unset, bool]): Gets or sets a value indicating whether this instance has
            configured password.
        has_configured_easy_password (Union[Unset, bool]): Gets or sets a value indicating whether this instance has
            configured easy password.
        enable_auto_login (Union[Unset, None, bool]): Gets or sets whether async login is enabled or not.
        last_login_date (Union[Unset, None, datetime.datetime]): Gets or sets the last login date.
        last_activity_date (Union[Unset, None, datetime.datetime]): Gets or sets the last activity date.
        configuration (Union[Unset, None, UserConfiguration]): Class UserConfiguration.
        policy (Union[Unset, None, UserPolicy]):
        primary_image_aspect_ratio (Union[Unset, None, float]): Gets or sets the primary image aspect ratio.
    """

    name: Union[Unset, None, str] = UNSET
    server_id: Union[Unset, None, str] = UNSET
    server_name: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    primary_image_tag: Union[Unset, None, str] = UNSET
    has_password: Union[Unset, bool] = UNSET
    has_configured_password: Union[Unset, bool] = UNSET
    has_configured_easy_password: Union[Unset, bool] = UNSET
    enable_auto_login: Union[Unset, None, bool] = UNSET
    last_login_date: Union[Unset, None, datetime.datetime] = UNSET
    last_activity_date: Union[Unset, None, datetime.datetime] = UNSET
    configuration: Union[Unset, None, "UserConfiguration"] = UNSET
    policy: Union[Unset, None, "UserPolicy"] = UNSET
    primary_image_aspect_ratio: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        server_id = self.server_id
        server_name = self.server_name
        id = self.id
        primary_image_tag = self.primary_image_tag
        has_password = self.has_password
        has_configured_password = self.has_configured_password
        has_configured_easy_password = self.has_configured_easy_password
        enable_auto_login = self.enable_auto_login
        last_login_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_login_date, Unset):
            last_login_date = self.last_login_date.isoformat() if self.last_login_date else None

        last_activity_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_activity_date, Unset):
            last_activity_date = self.last_activity_date.isoformat() if self.last_activity_date else None

        configuration: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict() if self.configuration else None

        policy: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict() if self.policy else None

        primary_image_aspect_ratio = self.primary_image_aspect_ratio

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if id is not UNSET:
            field_dict["Id"] = id
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if has_password is not UNSET:
            field_dict["HasPassword"] = has_password
        if has_configured_password is not UNSET:
            field_dict["HasConfiguredPassword"] = has_configured_password
        if has_configured_easy_password is not UNSET:
            field_dict["HasConfiguredEasyPassword"] = has_configured_easy_password
        if enable_auto_login is not UNSET:
            field_dict["EnableAutoLogin"] = enable_auto_login
        if last_login_date is not UNSET:
            field_dict["LastLoginDate"] = last_login_date
        if last_activity_date is not UNSET:
            field_dict["LastActivityDate"] = last_activity_date
        if configuration is not UNSET:
            field_dict["Configuration"] = configuration
        if policy is not UNSET:
            field_dict["Policy"] = policy
        if primary_image_aspect_ratio is not UNSET:
            field_dict["PrimaryImageAspectRatio"] = primary_image_aspect_ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_configuration import UserConfiguration
        from ..models.user_policy import UserPolicy

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        server_id = d.pop("ServerId", UNSET)

        server_name = d.pop("ServerName", UNSET)

        id = d.pop("Id", UNSET)

        primary_image_tag = d.pop("PrimaryImageTag", UNSET)

        has_password = d.pop("HasPassword", UNSET)

        has_configured_password = d.pop("HasConfiguredPassword", UNSET)

        has_configured_easy_password = d.pop("HasConfiguredEasyPassword", UNSET)

        enable_auto_login = d.pop("EnableAutoLogin", UNSET)

        _last_login_date = d.pop("LastLoginDate", UNSET)
        last_login_date: Union[Unset, None, datetime.datetime]
        if _last_login_date is None:
            last_login_date = None
        elif isinstance(_last_login_date, Unset):
            last_login_date = UNSET
        else:
            last_login_date = isoparse(_last_login_date)

        _last_activity_date = d.pop("LastActivityDate", UNSET)
        last_activity_date: Union[Unset, None, datetime.datetime]
        if _last_activity_date is None:
            last_activity_date = None
        elif isinstance(_last_activity_date, Unset):
            last_activity_date = UNSET
        else:
            last_activity_date = isoparse(_last_activity_date)

        _configuration = d.pop("Configuration", UNSET)
        configuration: Union[Unset, None, UserConfiguration]
        if _configuration is None:
            configuration = None
        elif isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = UserConfiguration.from_dict(_configuration)

        _policy = d.pop("Policy", UNSET)
        policy: Union[Unset, None, UserPolicy]
        if _policy is None:
            policy = None
        elif isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = UserPolicy.from_dict(_policy)

        primary_image_aspect_ratio = d.pop("PrimaryImageAspectRatio", UNSET)

        user_dto = cls(
            name=name,
            server_id=server_id,
            server_name=server_name,
            id=id,
            primary_image_tag=primary_image_tag,
            has_password=has_password,
            has_configured_password=has_configured_password,
            has_configured_easy_password=has_configured_easy_password,
            enable_auto_login=enable_auto_login,
            last_login_date=last_login_date,
            last_activity_date=last_activity_date,
            configuration=configuration,
            policy=policy,
            primary_image_aspect_ratio=primary_image_aspect_ratio,
        )

        return user_dto
