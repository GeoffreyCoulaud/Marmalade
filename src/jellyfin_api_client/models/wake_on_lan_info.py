from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WakeOnLanInfo")


@_attrs_define
class WakeOnLanInfo:
    """Provides the MAC address and port for wake-on-LAN functionality.

    Attributes:
        mac_address (Union[Unset, None, str]): Gets the MAC address of the device.
        port (Union[Unset, int]): Gets or sets the wake-on-LAN port.
    """

    mac_address: Union[Unset, None, str] = UNSET
    port: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        mac_address = self.mac_address
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if mac_address is not UNSET:
            field_dict["MacAddress"] = mac_address
        if port is not UNSET:
            field_dict["Port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mac_address = d.pop("MacAddress", UNSET)

        port = d.pop("Port", UNSET)

        wake_on_lan_info = cls(
            mac_address=mac_address,
            port=port,
        )

        return wake_on_lan_info
