from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewGroupRequestDto")


@_attrs_define
class NewGroupRequestDto:
    """Class NewGroupRequestDto.

    Attributes:
        group_name (Union[Unset, str]): Gets or sets the group name.
    """

    group_name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_name = self.group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["GroupName"] = group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_name = d.pop("GroupName", UNSET)

        new_group_request_dto = cls(
            group_name=group_name,
        )

        return new_group_request_dto
