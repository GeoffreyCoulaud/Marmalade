from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CultureDto")


@_attrs_define
class CultureDto:
    """Class CultureDto.

    Attributes:
        name (Union[Unset, str]): Gets the name.
        display_name (Union[Unset, str]): Gets the display name.
        two_letter_iso_language_name (Union[Unset, str]): Gets the name of the two letter ISO language.
        three_letter_iso_language_name (Union[Unset, None, str]): Gets the name of the three letter ISO language.
        three_letter_iso_language_names (Union[Unset, List[str]]):
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    two_letter_iso_language_name: Union[Unset, str] = UNSET
    three_letter_iso_language_name: Union[Unset, None, str] = UNSET
    three_letter_iso_language_names: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        display_name = self.display_name
        two_letter_iso_language_name = self.two_letter_iso_language_name
        three_letter_iso_language_name = self.three_letter_iso_language_name
        three_letter_iso_language_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.three_letter_iso_language_names, Unset):
            three_letter_iso_language_names = self.three_letter_iso_language_names

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if two_letter_iso_language_name is not UNSET:
            field_dict["TwoLetterISOLanguageName"] = two_letter_iso_language_name
        if three_letter_iso_language_name is not UNSET:
            field_dict["ThreeLetterISOLanguageName"] = three_letter_iso_language_name
        if three_letter_iso_language_names is not UNSET:
            field_dict["ThreeLetterISOLanguageNames"] = three_letter_iso_language_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        two_letter_iso_language_name = d.pop("TwoLetterISOLanguageName", UNSET)

        three_letter_iso_language_name = d.pop("ThreeLetterISOLanguageName", UNSET)

        three_letter_iso_language_names = cast(List[str], d.pop("ThreeLetterISOLanguageNames", UNSET))

        culture_dto = cls(
            name=name,
            display_name=display_name,
            two_letter_iso_language_name=two_letter_iso_language_name,
            three_letter_iso_language_name=three_letter_iso_language_name,
            three_letter_iso_language_names=three_letter_iso_language_names,
        )

        return culture_dto
