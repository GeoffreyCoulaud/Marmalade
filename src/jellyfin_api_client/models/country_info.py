from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CountryInfo")


@_attrs_define
class CountryInfo:
    """Class CountryInfo.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        display_name (Union[Unset, None, str]): Gets or sets the display name.
        two_letter_iso_region_name (Union[Unset, None, str]): Gets or sets the name of the two letter ISO region.
        three_letter_iso_region_name (Union[Unset, None, str]): Gets or sets the name of the three letter ISO region.
    """

    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    two_letter_iso_region_name: Union[Unset, None, str] = UNSET
    three_letter_iso_region_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        display_name = self.display_name
        two_letter_iso_region_name = self.two_letter_iso_region_name
        three_letter_iso_region_name = self.three_letter_iso_region_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if two_letter_iso_region_name is not UNSET:
            field_dict["TwoLetterISORegionName"] = two_letter_iso_region_name
        if three_letter_iso_region_name is not UNSET:
            field_dict["ThreeLetterISORegionName"] = three_letter_iso_region_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        two_letter_iso_region_name = d.pop("TwoLetterISORegionName", UNSET)

        three_letter_iso_region_name = d.pop("ThreeLetterISORegionName", UNSET)

        country_info = cls(
            name=name,
            display_name=display_name,
            two_letter_iso_region_name=two_letter_iso_region_name,
            three_letter_iso_region_name=three_letter_iso_region_name,
        )

        return country_info
