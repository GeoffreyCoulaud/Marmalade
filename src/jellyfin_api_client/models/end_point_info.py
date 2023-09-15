from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndPointInfo")


@_attrs_define
class EndPointInfo:
    """
    Attributes:
        is_local (Union[Unset, bool]):
        is_in_network (Union[Unset, bool]):
    """

    is_local: Union[Unset, bool] = UNSET
    is_in_network: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_local = self.is_local
        is_in_network = self.is_in_network

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_local is not UNSET:
            field_dict["IsLocal"] = is_local
        if is_in_network is not UNSET:
            field_dict["IsInNetwork"] = is_in_network

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_local = d.pop("IsLocal", UNSET)

        is_in_network = d.pop("IsInNetwork", UNSET)

        end_point_info = cls(
            is_local=is_local,
            is_in_network=is_in_network,
        )

        return end_point_info
