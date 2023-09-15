from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.control_response_headers import ControlResponseHeaders


T = TypeVar("T", bound="ControlResponse")


@_attrs_define
class ControlResponse:
    """
    Attributes:
        headers (Union[Unset, ControlResponseHeaders]):
        xml (Union[Unset, str]):
        is_successful (Union[Unset, bool]):
    """

    headers: Union[Unset, "ControlResponseHeaders"] = UNSET
    xml: Union[Unset, str] = UNSET
    is_successful: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        xml = self.xml
        is_successful = self.is_successful

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if headers is not UNSET:
            field_dict["Headers"] = headers
        if xml is not UNSET:
            field_dict["Xml"] = xml
        if is_successful is not UNSET:
            field_dict["IsSuccessful"] = is_successful

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.control_response_headers import ControlResponseHeaders

        d = src_dict.copy()
        _headers = d.pop("Headers", UNSET)
        headers: Union[Unset, ControlResponseHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ControlResponseHeaders.from_dict(_headers)

        xml = d.pop("Xml", UNSET)

        is_successful = d.pop("IsSuccessful", UNSET)

        control_response = cls(
            headers=headers,
            xml=xml,
            is_successful=is_successful,
        )

        return control_response
