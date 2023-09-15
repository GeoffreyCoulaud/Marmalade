import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artist_info_provider_ids import ArtistInfoProviderIds
    from ..models.song_info import SongInfo


T = TypeVar("T", bound="ArtistInfo")


@_attrs_define
class ArtistInfo:
    """
    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        original_title (Union[Unset, None, str]): Gets or sets the original title.
        path (Union[Unset, None, str]): Gets or sets the path.
        metadata_language (Union[Unset, None, str]): Gets or sets the metadata language.
        metadata_country_code (Union[Unset, None, str]): Gets or sets the metadata country code.
        provider_ids (Union[Unset, None, ArtistInfoProviderIds]): Gets or sets the provider ids.
        year (Union[Unset, None, int]): Gets or sets the year.
        index_number (Union[Unset, None, int]):
        parent_index_number (Union[Unset, None, int]):
        premiere_date (Union[Unset, None, datetime.datetime]):
        is_automated (Union[Unset, bool]):
        song_infos (Union[Unset, List['SongInfo']]):
    """

    name: Union[Unset, None, str] = UNSET
    original_title: Union[Unset, None, str] = UNSET
    path: Union[Unset, None, str] = UNSET
    metadata_language: Union[Unset, None, str] = UNSET
    metadata_country_code: Union[Unset, None, str] = UNSET
    provider_ids: Union[Unset, None, "ArtistInfoProviderIds"] = UNSET
    year: Union[Unset, None, int] = UNSET
    index_number: Union[Unset, None, int] = UNSET
    parent_index_number: Union[Unset, None, int] = UNSET
    premiere_date: Union[Unset, None, datetime.datetime] = UNSET
    is_automated: Union[Unset, bool] = UNSET
    song_infos: Union[Unset, List["SongInfo"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        original_title = self.original_title
        path = self.path
        metadata_language = self.metadata_language
        metadata_country_code = self.metadata_country_code
        provider_ids: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_ids, Unset):
            provider_ids = self.provider_ids.to_dict() if self.provider_ids else None

        year = self.year
        index_number = self.index_number
        parent_index_number = self.parent_index_number
        premiere_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.premiere_date, Unset):
            premiere_date = self.premiere_date.isoformat() if self.premiere_date else None

        is_automated = self.is_automated
        song_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.song_infos, Unset):
            song_infos = []
            for song_infos_item_data in self.song_infos:
                song_infos_item = song_infos_item_data.to_dict()

                song_infos.append(song_infos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if original_title is not UNSET:
            field_dict["OriginalTitle"] = original_title
        if path is not UNSET:
            field_dict["Path"] = path
        if metadata_language is not UNSET:
            field_dict["MetadataLanguage"] = metadata_language
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if provider_ids is not UNSET:
            field_dict["ProviderIds"] = provider_ids
        if year is not UNSET:
            field_dict["Year"] = year
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if premiere_date is not UNSET:
            field_dict["PremiereDate"] = premiere_date
        if is_automated is not UNSET:
            field_dict["IsAutomated"] = is_automated
        if song_infos is not UNSET:
            field_dict["SongInfos"] = song_infos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.artist_info_provider_ids import ArtistInfoProviderIds
        from ..models.song_info import SongInfo

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        original_title = d.pop("OriginalTitle", UNSET)

        path = d.pop("Path", UNSET)

        metadata_language = d.pop("MetadataLanguage", UNSET)

        metadata_country_code = d.pop("MetadataCountryCode", UNSET)

        _provider_ids = d.pop("ProviderIds", UNSET)
        provider_ids: Union[Unset, None, ArtistInfoProviderIds]
        if _provider_ids is None:
            provider_ids = None
        elif isinstance(_provider_ids, Unset):
            provider_ids = UNSET
        else:
            provider_ids = ArtistInfoProviderIds.from_dict(_provider_ids)

        year = d.pop("Year", UNSET)

        index_number = d.pop("IndexNumber", UNSET)

        parent_index_number = d.pop("ParentIndexNumber", UNSET)

        _premiere_date = d.pop("PremiereDate", UNSET)
        premiere_date: Union[Unset, None, datetime.datetime]
        if _premiere_date is None:
            premiere_date = None
        elif isinstance(_premiere_date, Unset):
            premiere_date = UNSET
        else:
            premiere_date = isoparse(_premiere_date)

        is_automated = d.pop("IsAutomated", UNSET)

        song_infos = []
        _song_infos = d.pop("SongInfos", UNSET)
        for song_infos_item_data in _song_infos or []:
            song_infos_item = SongInfo.from_dict(song_infos_item_data)

            song_infos.append(song_infos_item)

        artist_info = cls(
            name=name,
            original_title=original_title,
            path=path,
            metadata_language=metadata_language,
            metadata_country_code=metadata_country_code,
            provider_ids=provider_ids,
            year=year,
            index_number=index_number,
            parent_index_number=parent_index_number,
            premiere_date=premiere_date,
            is_automated=is_automated,
            song_infos=song_infos,
        )

        return artist_info
