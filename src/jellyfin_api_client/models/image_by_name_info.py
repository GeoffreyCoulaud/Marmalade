from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageByNameInfo")


@_attrs_define
class ImageByNameInfo:
    """
    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        theme (Union[Unset, None, str]): Gets or sets the theme.
        context (Union[Unset, None, str]): Gets or sets the context.
        file_length (Union[Unset, int]): Gets or sets the length of the file.
        format_ (Union[Unset, None, str]): Gets or sets the format.
    """

    name: Union[Unset, None, str] = UNSET
    theme: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET
    file_length: Union[Unset, int] = UNSET
    format_: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        theme = self.theme
        context = self.context
        file_length = self.file_length
        format_ = self.format_

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if theme is not UNSET:
            field_dict["Theme"] = theme
        if context is not UNSET:
            field_dict["Context"] = context
        if file_length is not UNSET:
            field_dict["FileLength"] = file_length
        if format_ is not UNSET:
            field_dict["Format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        theme = d.pop("Theme", UNSET)

        context = d.pop("Context", UNSET)

        file_length = d.pop("FileLength", UNSET)

        format_ = d.pop("Format", UNSET)

        image_by_name_info = cls(
            name=name,
            theme=theme,
            context=context,
            file_length=file_length,
            format_=format_,
        )

        return image_by_name_info
