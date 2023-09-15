from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicSystemInfo")


@_attrs_define
class PublicSystemInfo:
    """
    Attributes:
        local_address (Union[Unset, None, str]): Gets or sets the local address.
        server_name (Union[Unset, None, str]): Gets or sets the name of the server.
        version (Union[Unset, None, str]): Gets or sets the server version.
        product_name (Union[Unset, None, str]): Gets or sets the product name. This is the AssemblyProduct name.
        operating_system (Union[Unset, None, str]): Gets or sets the operating system.
        id (Union[Unset, None, str]): Gets or sets the id.
        startup_wizard_completed (Union[Unset, None, bool]): Gets or sets a value indicating whether the startup wizard
            is completed.
    """

    local_address: Union[Unset, None, str] = UNSET
    server_name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    product_name: Union[Unset, None, str] = UNSET
    operating_system: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    startup_wizard_completed: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        local_address = self.local_address
        server_name = self.server_name
        version = self.version
        product_name = self.product_name
        operating_system = self.operating_system
        id = self.id
        startup_wizard_completed = self.startup_wizard_completed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if local_address is not UNSET:
            field_dict["LocalAddress"] = local_address
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if version is not UNSET:
            field_dict["Version"] = version
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if operating_system is not UNSET:
            field_dict["OperatingSystem"] = operating_system
        if id is not UNSET:
            field_dict["Id"] = id
        if startup_wizard_completed is not UNSET:
            field_dict["StartupWizardCompleted"] = startup_wizard_completed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        local_address = d.pop("LocalAddress", UNSET)

        server_name = d.pop("ServerName", UNSET)

        version = d.pop("Version", UNSET)

        product_name = d.pop("ProductName", UNSET)

        operating_system = d.pop("OperatingSystem", UNSET)

        id = d.pop("Id", UNSET)

        startup_wizard_completed = d.pop("StartupWizardCompleted", UNSET)

        public_system_info = cls(
            local_address=local_address,
            server_name=server_name,
            version=version,
            product_name=product_name,
            operating_system=operating_system,
            id=id,
            startup_wizard_completed=startup_wizard_completed,
        )

        return public_system_info
