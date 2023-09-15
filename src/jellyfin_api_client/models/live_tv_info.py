from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_tv_service_info import LiveTvServiceInfo


T = TypeVar("T", bound="LiveTvInfo")


@_attrs_define
class LiveTvInfo:
    """
    Attributes:
        services (Union[Unset, List['LiveTvServiceInfo']]): Gets or sets the services.
        is_enabled (Union[Unset, bool]): Gets or sets a value indicating whether this instance is enabled.
        enabled_users (Union[Unset, List[str]]): Gets or sets the enabled users.
    """

    services: Union[Unset, List["LiveTvServiceInfo"]] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    enabled_users: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()

                services.append(services_item)

        is_enabled = self.is_enabled
        enabled_users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.enabled_users, Unset):
            enabled_users = self.enabled_users

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if services is not UNSET:
            field_dict["Services"] = services
        if is_enabled is not UNSET:
            field_dict["IsEnabled"] = is_enabled
        if enabled_users is not UNSET:
            field_dict["EnabledUsers"] = enabled_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.live_tv_service_info import LiveTvServiceInfo

        d = src_dict.copy()
        services = []
        _services = d.pop("Services", UNSET)
        for services_item_data in _services or []:
            services_item = LiveTvServiceInfo.from_dict(services_item_data)

            services.append(services_item)

        is_enabled = d.pop("IsEnabled", UNSET)

        enabled_users = cast(List[str], d.pop("EnabledUsers", UNSET))

        live_tv_info = cls(
            services=services,
            is_enabled=is_enabled,
            enabled_users=enabled_users,
        )

        return live_tv_info
