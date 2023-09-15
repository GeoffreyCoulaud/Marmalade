from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IgnoreWaitRequestDto")


@_attrs_define
class IgnoreWaitRequestDto:
    """Class IgnoreWaitRequestDto.

    Attributes:
        ignore_wait (Union[Unset, bool]): Gets or sets a value indicating whether the client should be ignored.
    """

    ignore_wait: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ignore_wait = self.ignore_wait

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ignore_wait is not UNSET:
            field_dict["IgnoreWait"] = ignore_wait

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ignore_wait = d.pop("IgnoreWait", UNSET)

        ignore_wait_request_dto = cls(
            ignore_wait=ignore_wait,
        )

        return ignore_wait_request_dto
