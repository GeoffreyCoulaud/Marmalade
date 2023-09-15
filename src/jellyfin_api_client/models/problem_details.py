from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemDetails")


@_attrs_define
class ProblemDetails:
    """
    Attributes:
        type (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        status (Union[Unset, None, int]):
        detail (Union[Unset, None, str]):
        instance (Union[Unset, None, str]):
    """

    type: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, int] = UNSET
    detail: Union[Unset, None, str] = UNSET
    instance: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        title = self.title
        status = self.status
        detail = self.detail
        instance = self.instance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        status = d.pop("status", UNSET)

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        problem_details = cls(
            type=type,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
        )

        problem_details.additional_properties = d
        return problem_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
