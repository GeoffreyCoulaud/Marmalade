from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartupConfigurationDto")


@_attrs_define
class StartupConfigurationDto:
    """The startup configuration DTO.

    Attributes:
        ui_culture (Union[Unset, None, str]): Gets or sets UI language culture.
        metadata_country_code (Union[Unset, None, str]): Gets or sets the metadata country code.
        preferred_metadata_language (Union[Unset, None, str]): Gets or sets the preferred language for the metadata.
    """

    ui_culture: Union[Unset, None, str] = UNSET
    metadata_country_code: Union[Unset, None, str] = UNSET
    preferred_metadata_language: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ui_culture = self.ui_culture
        metadata_country_code = self.metadata_country_code
        preferred_metadata_language = self.preferred_metadata_language

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ui_culture is not UNSET:
            field_dict["UICulture"] = ui_culture
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ui_culture = d.pop("UICulture", UNSET)

        metadata_country_code = d.pop("MetadataCountryCode", UNSET)

        preferred_metadata_language = d.pop("PreferredMetadataLanguage", UNSET)

        startup_configuration_dto = cls(
            ui_culture=ui_culture,
            metadata_country_code=metadata_country_code,
            preferred_metadata_language=preferred_metadata_language,
        )

        return startup_configuration_dto
