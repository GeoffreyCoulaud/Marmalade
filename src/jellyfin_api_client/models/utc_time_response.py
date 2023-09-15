import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtcTimeResponse")


@_attrs_define
class UtcTimeResponse:
    """Class UtcTimeResponse.

    Attributes:
        request_reception_time (Union[Unset, datetime.datetime]): Gets the UTC time when request has been received.
        response_transmission_time (Union[Unset, datetime.datetime]): Gets the UTC time when response has been sent.
    """

    request_reception_time: Union[Unset, datetime.datetime] = UNSET
    response_transmission_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        request_reception_time: Union[Unset, str] = UNSET
        if not isinstance(self.request_reception_time, Unset):
            request_reception_time = self.request_reception_time.isoformat()

        response_transmission_time: Union[Unset, str] = UNSET
        if not isinstance(self.response_transmission_time, Unset):
            response_transmission_time = self.response_transmission_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if request_reception_time is not UNSET:
            field_dict["RequestReceptionTime"] = request_reception_time
        if response_transmission_time is not UNSET:
            field_dict["ResponseTransmissionTime"] = response_transmission_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _request_reception_time = d.pop("RequestReceptionTime", UNSET)
        request_reception_time: Union[Unset, datetime.datetime]
        if isinstance(_request_reception_time, Unset):
            request_reception_time = UNSET
        else:
            request_reception_time = isoparse(_request_reception_time)

        _response_transmission_time = d.pop("ResponseTransmissionTime", UNSET)
        response_transmission_time: Union[Unset, datetime.datetime]
        if isinstance(_response_transmission_time, Unset):
            response_transmission_time = UNSET
        else:
            response_transmission_time = isoparse(_response_transmission_time)

        utc_time_response = cls(
            request_reception_time=request_reception_time,
            response_transmission_time=response_transmission_time,
        )

        return utc_time_response
