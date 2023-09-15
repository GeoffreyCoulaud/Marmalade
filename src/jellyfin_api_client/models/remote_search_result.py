import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remote_search_result_provider_ids import RemoteSearchResultProviderIds


T = TypeVar("T", bound="RemoteSearchResult")


@_attrs_define
class RemoteSearchResult:
    """
    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name.
        provider_ids (Union[Unset, None, RemoteSearchResultProviderIds]): Gets or sets the provider ids.
        production_year (Union[Unset, None, int]): Gets or sets the year.
        index_number (Union[Unset, None, int]):
        index_number_end (Union[Unset, None, int]):
        parent_index_number (Union[Unset, None, int]):
        premiere_date (Union[Unset, None, datetime.datetime]):
        image_url (Union[Unset, None, str]):
        search_provider_name (Union[Unset, None, str]):
        overview (Union[Unset, None, str]):
        album_artist (Union[Unset, None, RemoteSearchResult]):
        artists (Union[Unset, None, List['RemoteSearchResult']]):
    """

    name: Union[Unset, None, str] = UNSET
    provider_ids: Union[Unset, None, "RemoteSearchResultProviderIds"] = UNSET
    production_year: Union[Unset, None, int] = UNSET
    index_number: Union[Unset, None, int] = UNSET
    index_number_end: Union[Unset, None, int] = UNSET
    parent_index_number: Union[Unset, None, int] = UNSET
    premiere_date: Union[Unset, None, datetime.datetime] = UNSET
    image_url: Union[Unset, None, str] = UNSET
    search_provider_name: Union[Unset, None, str] = UNSET
    overview: Union[Unset, None, str] = UNSET
    album_artist: Union[Unset, None, "RemoteSearchResult"] = UNSET
    artists: Union[Unset, None, List["RemoteSearchResult"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        provider_ids: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_ids, Unset):
            provider_ids = self.provider_ids.to_dict() if self.provider_ids else None

        production_year = self.production_year
        index_number = self.index_number
        index_number_end = self.index_number_end
        parent_index_number = self.parent_index_number
        premiere_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.premiere_date, Unset):
            premiere_date = self.premiere_date.isoformat() if self.premiere_date else None

        image_url = self.image_url
        search_provider_name = self.search_provider_name
        overview = self.overview
        album_artist: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.album_artist, Unset):
            album_artist = self.album_artist.to_dict() if self.album_artist else None

        artists: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.artists, Unset):
            if self.artists is None:
                artists = None
            else:
                artists = []
                for artists_item_data in self.artists:
                    artists_item = artists_item_data.to_dict()

                    artists.append(artists_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if provider_ids is not UNSET:
            field_dict["ProviderIds"] = provider_ids
        if production_year is not UNSET:
            field_dict["ProductionYear"] = production_year
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if index_number_end is not UNSET:
            field_dict["IndexNumberEnd"] = index_number_end
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if premiere_date is not UNSET:
            field_dict["PremiereDate"] = premiere_date
        if image_url is not UNSET:
            field_dict["ImageUrl"] = image_url
        if search_provider_name is not UNSET:
            field_dict["SearchProviderName"] = search_provider_name
        if overview is not UNSET:
            field_dict["Overview"] = overview
        if album_artist is not UNSET:
            field_dict["AlbumArtist"] = album_artist
        if artists is not UNSET:
            field_dict["Artists"] = artists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remote_search_result_provider_ids import RemoteSearchResultProviderIds

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        _provider_ids = d.pop("ProviderIds", UNSET)
        provider_ids: Union[Unset, None, RemoteSearchResultProviderIds]
        if _provider_ids is None:
            provider_ids = None
        elif isinstance(_provider_ids, Unset):
            provider_ids = UNSET
        else:
            provider_ids = RemoteSearchResultProviderIds.from_dict(_provider_ids)

        production_year = d.pop("ProductionYear", UNSET)

        index_number = d.pop("IndexNumber", UNSET)

        index_number_end = d.pop("IndexNumberEnd", UNSET)

        parent_index_number = d.pop("ParentIndexNumber", UNSET)

        _premiere_date = d.pop("PremiereDate", UNSET)
        premiere_date: Union[Unset, None, datetime.datetime]
        if _premiere_date is None:
            premiere_date = None
        elif isinstance(_premiere_date, Unset):
            premiere_date = UNSET
        else:
            premiere_date = isoparse(_premiere_date)

        image_url = d.pop("ImageUrl", UNSET)

        search_provider_name = d.pop("SearchProviderName", UNSET)

        overview = d.pop("Overview", UNSET)

        _album_artist = d.pop("AlbumArtist", UNSET)
        album_artist: Union[Unset, None, RemoteSearchResult]
        if _album_artist is None:
            album_artist = None
        elif isinstance(_album_artist, Unset):
            album_artist = UNSET
        else:
            album_artist = RemoteSearchResult.from_dict(_album_artist)

        artists = []
        _artists = d.pop("Artists", UNSET)
        for artists_item_data in _artists or []:
            artists_item = RemoteSearchResult.from_dict(artists_item_data)

            artists.append(artists_item)

        remote_search_result = cls(
            name=name,
            provider_ids=provider_ids,
            production_year=production_year,
            index_number=index_number,
            index_number_end=index_number_end,
            parent_index_number=parent_index_number,
            premiere_date=premiere_date,
            image_url=image_url,
            search_provider_name=search_provider_name,
            overview=overview,
            album_artist=album_artist,
            artists=artists,
        )

        return remote_search_result
