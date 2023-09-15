import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchHint")


@_attrs_define
class SearchHint:
    """Class SearchHintResult.

    Attributes:
        item_id (Union[Unset, str]): Gets or sets the item id.
        id (Union[Unset, str]):
        name (Union[Unset, None, str]): Gets or sets the name.
        matched_term (Union[Unset, None, str]): Gets or sets the matched term.
        index_number (Union[Unset, None, int]): Gets or sets the index number.
        production_year (Union[Unset, None, int]): Gets or sets the production year.
        parent_index_number (Union[Unset, None, int]): Gets or sets the parent index number.
        primary_image_tag (Union[Unset, None, str]): Gets or sets the image tag.
        thumb_image_tag (Union[Unset, None, str]): Gets or sets the thumb image tag.
        thumb_image_item_id (Union[Unset, None, str]): Gets or sets the thumb image item identifier.
        backdrop_image_tag (Union[Unset, None, str]): Gets or sets the backdrop image tag.
        backdrop_image_item_id (Union[Unset, None, str]): Gets or sets the backdrop image item identifier.
        type (Union[Unset, None, str]): Gets or sets the type.
        is_folder (Union[Unset, None, bool]):
        run_time_ticks (Union[Unset, None, int]): Gets or sets the run time ticks.
        media_type (Union[Unset, None, str]): Gets or sets the type of the media.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        series (Union[Unset, None, str]): Gets or sets the series.
        status (Union[Unset, None, str]):
        album (Union[Unset, None, str]): Gets or sets the album.
        album_id (Union[Unset, str]):
        album_artist (Union[Unset, None, str]): Gets or sets the album artist.
        artists (Union[Unset, None, List[str]]): Gets or sets the artists.
        song_count (Union[Unset, None, int]): Gets or sets the song count.
        episode_count (Union[Unset, None, int]): Gets or sets the episode count.
        channel_id (Union[Unset, str]): Gets or sets the channel identifier.
        channel_name (Union[Unset, None, str]): Gets or sets the name of the channel.
        primary_image_aspect_ratio (Union[Unset, None, float]): Gets or sets the primary image aspect ratio.
    """

    item_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    matched_term: Union[Unset, None, str] = UNSET
    index_number: Union[Unset, None, int] = UNSET
    production_year: Union[Unset, None, int] = UNSET
    parent_index_number: Union[Unset, None, int] = UNSET
    primary_image_tag: Union[Unset, None, str] = UNSET
    thumb_image_tag: Union[Unset, None, str] = UNSET
    thumb_image_item_id: Union[Unset, None, str] = UNSET
    backdrop_image_tag: Union[Unset, None, str] = UNSET
    backdrop_image_item_id: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    is_folder: Union[Unset, None, bool] = UNSET
    run_time_ticks: Union[Unset, None, int] = UNSET
    media_type: Union[Unset, None, str] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    series: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    album: Union[Unset, None, str] = UNSET
    album_id: Union[Unset, str] = UNSET
    album_artist: Union[Unset, None, str] = UNSET
    artists: Union[Unset, None, List[str]] = UNSET
    song_count: Union[Unset, None, int] = UNSET
    episode_count: Union[Unset, None, int] = UNSET
    channel_id: Union[Unset, str] = UNSET
    channel_name: Union[Unset, None, str] = UNSET
    primary_image_aspect_ratio: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id
        id = self.id
        name = self.name
        matched_term = self.matched_term
        index_number = self.index_number
        production_year = self.production_year
        parent_index_number = self.parent_index_number
        primary_image_tag = self.primary_image_tag
        thumb_image_tag = self.thumb_image_tag
        thumb_image_item_id = self.thumb_image_item_id
        backdrop_image_tag = self.backdrop_image_tag
        backdrop_image_item_id = self.backdrop_image_item_id
        type = self.type
        is_folder = self.is_folder
        run_time_ticks = self.run_time_ticks
        media_type = self.media_type
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        series = self.series
        status = self.status
        album = self.album
        album_id = self.album_id
        album_artist = self.album_artist
        artists: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.artists, Unset):
            if self.artists is None:
                artists = None
            else:
                artists = self.artists

        song_count = self.song_count
        episode_count = self.episode_count
        channel_id = self.channel_id
        channel_name = self.channel_name
        primary_image_aspect_ratio = self.primary_image_aspect_ratio

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if matched_term is not UNSET:
            field_dict["MatchedTerm"] = matched_term
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if production_year is not UNSET:
            field_dict["ProductionYear"] = production_year
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if thumb_image_tag is not UNSET:
            field_dict["ThumbImageTag"] = thumb_image_tag
        if thumb_image_item_id is not UNSET:
            field_dict["ThumbImageItemId"] = thumb_image_item_id
        if backdrop_image_tag is not UNSET:
            field_dict["BackdropImageTag"] = backdrop_image_tag
        if backdrop_image_item_id is not UNSET:
            field_dict["BackdropImageItemId"] = backdrop_image_item_id
        if type is not UNSET:
            field_dict["Type"] = type
        if is_folder is not UNSET:
            field_dict["IsFolder"] = is_folder
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if series is not UNSET:
            field_dict["Series"] = series
        if status is not UNSET:
            field_dict["Status"] = status
        if album is not UNSET:
            field_dict["Album"] = album
        if album_id is not UNSET:
            field_dict["AlbumId"] = album_id
        if album_artist is not UNSET:
            field_dict["AlbumArtist"] = album_artist
        if artists is not UNSET:
            field_dict["Artists"] = artists
        if song_count is not UNSET:
            field_dict["SongCount"] = song_count
        if episode_count is not UNSET:
            field_dict["EpisodeCount"] = episode_count
        if channel_id is not UNSET:
            field_dict["ChannelId"] = channel_id
        if channel_name is not UNSET:
            field_dict["ChannelName"] = channel_name
        if primary_image_aspect_ratio is not UNSET:
            field_dict["PrimaryImageAspectRatio"] = primary_image_aspect_ratio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("ItemId", UNSET)

        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        matched_term = d.pop("MatchedTerm", UNSET)

        index_number = d.pop("IndexNumber", UNSET)

        production_year = d.pop("ProductionYear", UNSET)

        parent_index_number = d.pop("ParentIndexNumber", UNSET)

        primary_image_tag = d.pop("PrimaryImageTag", UNSET)

        thumb_image_tag = d.pop("ThumbImageTag", UNSET)

        thumb_image_item_id = d.pop("ThumbImageItemId", UNSET)

        backdrop_image_tag = d.pop("BackdropImageTag", UNSET)

        backdrop_image_item_id = d.pop("BackdropImageItemId", UNSET)

        type = d.pop("Type", UNSET)

        is_folder = d.pop("IsFolder", UNSET)

        run_time_ticks = d.pop("RunTimeTicks", UNSET)

        media_type = d.pop("MediaType", UNSET)

        _start_date = d.pop("StartDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("EndDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        series = d.pop("Series", UNSET)

        status = d.pop("Status", UNSET)

        album = d.pop("Album", UNSET)

        album_id = d.pop("AlbumId", UNSET)

        album_artist = d.pop("AlbumArtist", UNSET)

        artists = cast(List[str], d.pop("Artists", UNSET))

        song_count = d.pop("SongCount", UNSET)

        episode_count = d.pop("EpisodeCount", UNSET)

        channel_id = d.pop("ChannelId", UNSET)

        channel_name = d.pop("ChannelName", UNSET)

        primary_image_aspect_ratio = d.pop("PrimaryImageAspectRatio", UNSET)

        search_hint = cls(
            item_id=item_id,
            id=id,
            name=name,
            matched_term=matched_term,
            index_number=index_number,
            production_year=production_year,
            parent_index_number=parent_index_number,
            primary_image_tag=primary_image_tag,
            thumb_image_tag=thumb_image_tag,
            thumb_image_item_id=thumb_image_item_id,
            backdrop_image_tag=backdrop_image_tag,
            backdrop_image_item_id=backdrop_image_item_id,
            type=type,
            is_folder=is_folder,
            run_time_ticks=run_time_ticks,
            media_type=media_type,
            start_date=start_date,
            end_date=end_date,
            series=series,
            status=status,
            album=album,
            album_id=album_id,
            album_artist=album_artist,
            artists=artists,
            song_count=song_count,
            episode_count=episode_count,
            channel_id=channel_id,
            channel_name=channel_name,
            primary_image_aspect_ratio=primary_image_aspect_ratio,
        )

        return search_hint
