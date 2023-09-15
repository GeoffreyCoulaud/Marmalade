from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.country_info import CountryInfo
    from ..models.culture_dto import CultureDto
    from ..models.external_id_info import ExternalIdInfo
    from ..models.name_value_pair import NameValuePair
    from ..models.parental_rating import ParentalRating


T = TypeVar("T", bound="MetadataEditorInfo")


@_attrs_define
class MetadataEditorInfo:
    """
    Attributes:
        parental_rating_options (Union[Unset, List['ParentalRating']]):
        countries (Union[Unset, List['CountryInfo']]):
        cultures (Union[Unset, List['CultureDto']]):
        external_id_infos (Union[Unset, List['ExternalIdInfo']]):
        content_type (Union[Unset, None, str]):
        content_type_options (Union[Unset, List['NameValuePair']]):
    """

    parental_rating_options: Union[Unset, List["ParentalRating"]] = UNSET
    countries: Union[Unset, List["CountryInfo"]] = UNSET
    cultures: Union[Unset, List["CultureDto"]] = UNSET
    external_id_infos: Union[Unset, List["ExternalIdInfo"]] = UNSET
    content_type: Union[Unset, None, str] = UNSET
    content_type_options: Union[Unset, List["NameValuePair"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        parental_rating_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parental_rating_options, Unset):
            parental_rating_options = []
            for parental_rating_options_item_data in self.parental_rating_options:
                parental_rating_options_item = parental_rating_options_item_data.to_dict()

                parental_rating_options.append(parental_rating_options_item)

        countries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = []
            for countries_item_data in self.countries:
                countries_item = countries_item_data.to_dict()

                countries.append(countries_item)

        cultures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cultures, Unset):
            cultures = []
            for cultures_item_data in self.cultures:
                cultures_item = cultures_item_data.to_dict()

                cultures.append(cultures_item)

        external_id_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.external_id_infos, Unset):
            external_id_infos = []
            for external_id_infos_item_data in self.external_id_infos:
                external_id_infos_item = external_id_infos_item_data.to_dict()

                external_id_infos.append(external_id_infos_item)

        content_type = self.content_type
        content_type_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.content_type_options, Unset):
            content_type_options = []
            for content_type_options_item_data in self.content_type_options:
                content_type_options_item = content_type_options_item_data.to_dict()

                content_type_options.append(content_type_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if parental_rating_options is not UNSET:
            field_dict["ParentalRatingOptions"] = parental_rating_options
        if countries is not UNSET:
            field_dict["Countries"] = countries
        if cultures is not UNSET:
            field_dict["Cultures"] = cultures
        if external_id_infos is not UNSET:
            field_dict["ExternalIdInfos"] = external_id_infos
        if content_type is not UNSET:
            field_dict["ContentType"] = content_type
        if content_type_options is not UNSET:
            field_dict["ContentTypeOptions"] = content_type_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.country_info import CountryInfo
        from ..models.culture_dto import CultureDto
        from ..models.external_id_info import ExternalIdInfo
        from ..models.name_value_pair import NameValuePair
        from ..models.parental_rating import ParentalRating

        d = src_dict.copy()
        parental_rating_options = []
        _parental_rating_options = d.pop("ParentalRatingOptions", UNSET)
        for parental_rating_options_item_data in _parental_rating_options or []:
            parental_rating_options_item = ParentalRating.from_dict(parental_rating_options_item_data)

            parental_rating_options.append(parental_rating_options_item)

        countries = []
        _countries = d.pop("Countries", UNSET)
        for countries_item_data in _countries or []:
            countries_item = CountryInfo.from_dict(countries_item_data)

            countries.append(countries_item)

        cultures = []
        _cultures = d.pop("Cultures", UNSET)
        for cultures_item_data in _cultures or []:
            cultures_item = CultureDto.from_dict(cultures_item_data)

            cultures.append(cultures_item)

        external_id_infos = []
        _external_id_infos = d.pop("ExternalIdInfos", UNSET)
        for external_id_infos_item_data in _external_id_infos or []:
            external_id_infos_item = ExternalIdInfo.from_dict(external_id_infos_item_data)

            external_id_infos.append(external_id_infos_item)

        content_type = d.pop("ContentType", UNSET)

        content_type_options = []
        _content_type_options = d.pop("ContentTypeOptions", UNSET)
        for content_type_options_item_data in _content_type_options or []:
            content_type_options_item = NameValuePair.from_dict(content_type_options_item_data)

            content_type_options.append(content_type_options_item)

        metadata_editor_info = cls(
            parental_rating_options=parental_rating_options,
            countries=countries,
            cultures=cultures,
            external_id_infos=external_id_infos,
            content_type=content_type,
            content_type_options=content_type_options,
        )

        return metadata_editor_info
