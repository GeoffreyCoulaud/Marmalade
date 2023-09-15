from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_header_info import HttpHeaderInfo


T = TypeVar("T", bound="DeviceIdentification")


@_attrs_define
class DeviceIdentification:
    """
    Attributes:
        friendly_name (Union[Unset, str]): Gets or sets the name of the friendly.
        model_number (Union[Unset, str]): Gets or sets the model number.
        serial_number (Union[Unset, str]): Gets or sets the serial number.
        model_name (Union[Unset, str]): Gets or sets the name of the model.
        model_description (Union[Unset, str]): Gets or sets the model description.
        model_url (Union[Unset, str]): Gets or sets the model URL.
        manufacturer (Union[Unset, str]): Gets or sets the manufacturer.
        manufacturer_url (Union[Unset, str]): Gets or sets the manufacturer URL.
        headers (Union[Unset, List['HttpHeaderInfo']]): Gets or sets the headers.
    """

    friendly_name: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    model_name: Union[Unset, str] = UNSET
    model_description: Union[Unset, str] = UNSET
    model_url: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    manufacturer_url: Union[Unset, str] = UNSET
    headers: Union[Unset, List["HttpHeaderInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        friendly_name = self.friendly_name
        model_number = self.model_number
        serial_number = self.serial_number
        model_name = self.model_name
        model_description = self.model_description
        model_url = self.model_url
        manufacturer = self.manufacturer
        manufacturer_url = self.manufacturer_url
        headers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()

                headers.append(headers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if friendly_name is not UNSET:
            field_dict["FriendlyName"] = friendly_name
        if model_number is not UNSET:
            field_dict["ModelNumber"] = model_number
        if serial_number is not UNSET:
            field_dict["SerialNumber"] = serial_number
        if model_name is not UNSET:
            field_dict["ModelName"] = model_name
        if model_description is not UNSET:
            field_dict["ModelDescription"] = model_description
        if model_url is not UNSET:
            field_dict["ModelUrl"] = model_url
        if manufacturer is not UNSET:
            field_dict["Manufacturer"] = manufacturer
        if manufacturer_url is not UNSET:
            field_dict["ManufacturerUrl"] = manufacturer_url
        if headers is not UNSET:
            field_dict["Headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_header_info import HttpHeaderInfo

        d = src_dict.copy()
        friendly_name = d.pop("FriendlyName", UNSET)

        model_number = d.pop("ModelNumber", UNSET)

        serial_number = d.pop("SerialNumber", UNSET)

        model_name = d.pop("ModelName", UNSET)

        model_description = d.pop("ModelDescription", UNSET)

        model_url = d.pop("ModelUrl", UNSET)

        manufacturer = d.pop("Manufacturer", UNSET)

        manufacturer_url = d.pop("ManufacturerUrl", UNSET)

        headers = []
        _headers = d.pop("Headers", UNSET)
        for headers_item_data in _headers or []:
            headers_item = HttpHeaderInfo.from_dict(headers_item_data)

            headers.append(headers_item)

        device_identification = cls(
            friendly_name=friendly_name,
            model_number=model_number,
            serial_number=serial_number,
            model_name=model_name,
            model_description=model_description,
            model_url=model_url,
            manufacturer=manufacturer,
            manufacturer_url=manufacturer_url,
            headers=headers,
        )

        return device_identification
