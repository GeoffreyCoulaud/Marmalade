from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_option_info_dto import LibraryOptionInfoDto
    from ..models.library_type_options_dto import LibraryTypeOptionsDto


T = TypeVar("T", bound="LibraryOptionsResultDto")


@_attrs_define
class LibraryOptionsResultDto:
    """Library options result dto.

    Attributes:
        metadata_savers (Union[Unset, List['LibraryOptionInfoDto']]): Gets or sets the metadata savers.
        metadata_readers (Union[Unset, List['LibraryOptionInfoDto']]): Gets or sets the metadata readers.
        subtitle_fetchers (Union[Unset, List['LibraryOptionInfoDto']]): Gets or sets the subtitle fetchers.
        type_options (Union[Unset, List['LibraryTypeOptionsDto']]): Gets or sets the type options.
    """

    metadata_savers: Union[Unset, List["LibraryOptionInfoDto"]] = UNSET
    metadata_readers: Union[Unset, List["LibraryOptionInfoDto"]] = UNSET
    subtitle_fetchers: Union[Unset, List["LibraryOptionInfoDto"]] = UNSET
    type_options: Union[Unset, List["LibraryTypeOptionsDto"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metadata_savers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_savers, Unset):
            metadata_savers = []
            for metadata_savers_item_data in self.metadata_savers:
                metadata_savers_item = metadata_savers_item_data.to_dict()

                metadata_savers.append(metadata_savers_item)

        metadata_readers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_readers, Unset):
            metadata_readers = []
            for metadata_readers_item_data in self.metadata_readers:
                metadata_readers_item = metadata_readers_item_data.to_dict()

                metadata_readers.append(metadata_readers_item)

        subtitle_fetchers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subtitle_fetchers, Unset):
            subtitle_fetchers = []
            for subtitle_fetchers_item_data in self.subtitle_fetchers:
                subtitle_fetchers_item = subtitle_fetchers_item_data.to_dict()

                subtitle_fetchers.append(subtitle_fetchers_item)

        type_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.type_options, Unset):
            type_options = []
            for type_options_item_data in self.type_options:
                type_options_item = type_options_item_data.to_dict()

                type_options.append(type_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if metadata_savers is not UNSET:
            field_dict["MetadataSavers"] = metadata_savers
        if metadata_readers is not UNSET:
            field_dict["MetadataReaders"] = metadata_readers
        if subtitle_fetchers is not UNSET:
            field_dict["SubtitleFetchers"] = subtitle_fetchers
        if type_options is not UNSET:
            field_dict["TypeOptions"] = type_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.library_option_info_dto import LibraryOptionInfoDto
        from ..models.library_type_options_dto import LibraryTypeOptionsDto

        d = src_dict.copy()
        metadata_savers = []
        _metadata_savers = d.pop("MetadataSavers", UNSET)
        for metadata_savers_item_data in _metadata_savers or []:
            metadata_savers_item = LibraryOptionInfoDto.from_dict(metadata_savers_item_data)

            metadata_savers.append(metadata_savers_item)

        metadata_readers = []
        _metadata_readers = d.pop("MetadataReaders", UNSET)
        for metadata_readers_item_data in _metadata_readers or []:
            metadata_readers_item = LibraryOptionInfoDto.from_dict(metadata_readers_item_data)

            metadata_readers.append(metadata_readers_item)

        subtitle_fetchers = []
        _subtitle_fetchers = d.pop("SubtitleFetchers", UNSET)
        for subtitle_fetchers_item_data in _subtitle_fetchers or []:
            subtitle_fetchers_item = LibraryOptionInfoDto.from_dict(subtitle_fetchers_item_data)

            subtitle_fetchers.append(subtitle_fetchers_item)

        type_options = []
        _type_options = d.pop("TypeOptions", UNSET)
        for type_options_item_data in _type_options or []:
            type_options_item = LibraryTypeOptionsDto.from_dict(type_options_item_data)

            type_options.append(type_options_item)

        library_options_result_dto = cls(
            metadata_savers=metadata_savers,
            metadata_readers=metadata_readers,
            subtitle_fetchers=subtitle_fetchers,
            type_options=type_options,
        )

        return library_options_result_dto
