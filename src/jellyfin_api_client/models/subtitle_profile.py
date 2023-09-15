from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.subtitle_delivery_method import SubtitleDeliveryMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubtitleProfile")


@_attrs_define
class SubtitleProfile:
    """
    Attributes:
        format_ (Union[Unset, None, str]):
        method (Union[Unset, SubtitleDeliveryMethod]): Delivery method to use during playback of a specific subtitle
            format.
        didl_mode (Union[Unset, None, str]):
        language (Union[Unset, None, str]):
        container (Union[Unset, None, str]):
    """

    format_: Union[Unset, None, str] = UNSET
    method: Union[Unset, SubtitleDeliveryMethod] = UNSET
    didl_mode: Union[Unset, None, str] = UNSET
    language: Union[Unset, None, str] = UNSET
    container: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        didl_mode = self.didl_mode
        language = self.language
        container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["Format"] = format_
        if method is not UNSET:
            field_dict["Method"] = method
        if didl_mode is not UNSET:
            field_dict["DidlMode"] = didl_mode
        if language is not UNSET:
            field_dict["Language"] = language
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = d.pop("Format", UNSET)

        _method = d.pop("Method", UNSET)
        method: Union[Unset, SubtitleDeliveryMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = SubtitleDeliveryMethod(_method)

        didl_mode = d.pop("DidlMode", UNSET)

        language = d.pop("Language", UNSET)

        container = d.pop("Container", UNSET)

        subtitle_profile = cls(
            format_=format_,
            method=method,
            didl_mode=didl_mode,
            language=language,
            container=container,
        )

        return subtitle_profile
