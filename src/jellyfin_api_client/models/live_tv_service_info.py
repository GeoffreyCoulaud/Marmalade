from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.live_tv_service_status import LiveTvServiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveTvServiceInfo")


@_attrs_define
class LiveTvServiceInfo:
    """Class ServiceInfo.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        home_page_url (Union[Unset, None, str]): Gets or sets the home page URL.
        status (Union[Unset, LiveTvServiceStatus]):
        status_message (Union[Unset, None, str]): Gets or sets the status message.
        version (Union[Unset, None, str]): Gets or sets the version.
        has_update_available (Union[Unset, bool]): Gets or sets a value indicating whether this instance has update
            available.
        is_visible (Union[Unset, bool]): Gets or sets a value indicating whether this instance is visible.
        tuners (Union[Unset, None, List[str]]):
    """

    name: Union[Unset, None, str] = UNSET
    home_page_url: Union[Unset, None, str] = UNSET
    status: Union[Unset, LiveTvServiceStatus] = UNSET
    status_message: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    has_update_available: Union[Unset, bool] = UNSET
    is_visible: Union[Unset, bool] = UNSET
    tuners: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        home_page_url = self.home_page_url
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message
        version = self.version
        has_update_available = self.has_update_available
        is_visible = self.is_visible
        tuners: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tuners, Unset):
            if self.tuners is None:
                tuners = None
            else:
                tuners = self.tuners

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if home_page_url is not UNSET:
            field_dict["HomePageUrl"] = home_page_url
        if status is not UNSET:
            field_dict["Status"] = status
        if status_message is not UNSET:
            field_dict["StatusMessage"] = status_message
        if version is not UNSET:
            field_dict["Version"] = version
        if has_update_available is not UNSET:
            field_dict["HasUpdateAvailable"] = has_update_available
        if is_visible is not UNSET:
            field_dict["IsVisible"] = is_visible
        if tuners is not UNSET:
            field_dict["Tuners"] = tuners

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        home_page_url = d.pop("HomePageUrl", UNSET)

        _status = d.pop("Status", UNSET)
        status: Union[Unset, LiveTvServiceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LiveTvServiceStatus(_status)

        status_message = d.pop("StatusMessage", UNSET)

        version = d.pop("Version", UNSET)

        has_update_available = d.pop("HasUpdateAvailable", UNSET)

        is_visible = d.pop("IsVisible", UNSET)

        tuners = cast(List[str], d.pop("Tuners", UNSET))

        live_tv_service_info = cls(
            name=name,
            home_page_url=home_page_url,
            status=status,
            status_message=status_message,
            version=version,
            has_update_available=has_update_available,
            is_visible=is_visible,
            tuners=tuners,
        )

        return live_tv_service_info
