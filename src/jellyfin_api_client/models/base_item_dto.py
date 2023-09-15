import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.base_item_kind import BaseItemKind
from ..models.channel_type import ChannelType
from ..models.day_of_week import DayOfWeek
from ..models.image_orientation import ImageOrientation
from ..models.iso_type import IsoType
from ..models.location_type import LocationType
from ..models.metadata_field import MetadataField
from ..models.play_access import PlayAccess
from ..models.program_audio import ProgramAudio
from ..models.video_3d_format import Video3DFormat
from ..models.video_type import VideoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto_image_blur_hashes import BaseItemDtoImageBlurHashes
    from ..models.base_item_dto_image_tags import BaseItemDtoImageTags
    from ..models.base_item_dto_provider_ids import BaseItemDtoProviderIds
    from ..models.base_item_person import BaseItemPerson
    from ..models.chapter_info import ChapterInfo
    from ..models.external_url import ExternalUrl
    from ..models.media_source_info import MediaSourceInfo
    from ..models.media_stream import MediaStream
    from ..models.media_url import MediaUrl
    from ..models.name_guid_pair import NameGuidPair
    from ..models.user_item_data_dto import UserItemDataDto


T = TypeVar("T", bound="BaseItemDto")


@_attrs_define
class BaseItemDto:
    """This is strictly used as a data transfer object from the api layer.
    This holds information about a BaseItem in a format that is convenient for the client.

        Attributes:
            name (Union[Unset, None, str]): Gets or sets the name.
            original_title (Union[Unset, None, str]):
            server_id (Union[Unset, None, str]): Gets or sets the server identifier.
            id (Union[Unset, str]): Gets or sets the id.
            etag (Union[Unset, None, str]): Gets or sets the etag.
            source_type (Union[Unset, None, str]): Gets or sets the type of the source.
            playlist_item_id (Union[Unset, None, str]): Gets or sets the playlist item identifier.
            date_created (Union[Unset, None, datetime.datetime]): Gets or sets the date created.
            date_last_media_added (Union[Unset, None, datetime.datetime]):
            extra_type (Union[Unset, None, str]):
            airs_before_season_number (Union[Unset, None, int]):
            airs_after_season_number (Union[Unset, None, int]):
            airs_before_episode_number (Union[Unset, None, int]):
            can_delete (Union[Unset, None, bool]):
            can_download (Union[Unset, None, bool]):
            has_subtitles (Union[Unset, None, bool]):
            preferred_metadata_language (Union[Unset, None, str]):
            preferred_metadata_country_code (Union[Unset, None, str]):
            supports_sync (Union[Unset, None, bool]): Gets or sets a value indicating whether [supports synchronize].
            container (Union[Unset, None, str]):
            sort_name (Union[Unset, None, str]): Gets or sets the name of the sort.
            forced_sort_name (Union[Unset, None, str]):
            video_3d_format (Union[Unset, None, Video3DFormat]):
            premiere_date (Union[Unset, None, datetime.datetime]): Gets or sets the premiere date.
            external_urls (Union[Unset, None, List['ExternalUrl']]): Gets or sets the external urls.
            media_sources (Union[Unset, None, List['MediaSourceInfo']]): Gets or sets the media versions.
            critic_rating (Union[Unset, None, float]): Gets or sets the critic rating.
            production_locations (Union[Unset, None, List[str]]):
            path (Union[Unset, None, str]): Gets or sets the path.
            enable_media_source_display (Union[Unset, None, bool]):
            official_rating (Union[Unset, None, str]): Gets or sets the official rating.
            custom_rating (Union[Unset, None, str]): Gets or sets the custom rating.
            channel_id (Union[Unset, None, str]): Gets or sets the channel identifier.
            channel_name (Union[Unset, None, str]):
            overview (Union[Unset, None, str]): Gets or sets the overview.
            taglines (Union[Unset, None, List[str]]): Gets or sets the taglines.
            genres (Union[Unset, None, List[str]]): Gets or sets the genres.
            community_rating (Union[Unset, None, float]): Gets or sets the community rating.
            cumulative_run_time_ticks (Union[Unset, None, int]): Gets or sets the cumulative run time ticks.
            run_time_ticks (Union[Unset, None, int]): Gets or sets the run time ticks.
            play_access (Union[Unset, None, PlayAccess]):
            aspect_ratio (Union[Unset, None, str]): Gets or sets the aspect ratio.
            production_year (Union[Unset, None, int]): Gets or sets the production year.
            is_place_holder (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is place
                holder.
            number (Union[Unset, None, str]): Gets or sets the number.
            channel_number (Union[Unset, None, str]):
            index_number (Union[Unset, None, int]): Gets or sets the index number.
            index_number_end (Union[Unset, None, int]): Gets or sets the index number end.
            parent_index_number (Union[Unset, None, int]): Gets or sets the parent index number.
            remote_trailers (Union[Unset, None, List['MediaUrl']]): Gets or sets the trailer urls.
            provider_ids (Union[Unset, None, BaseItemDtoProviderIds]): Gets or sets the provider ids.
            is_hd (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is HD.
            is_folder (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is folder.
            parent_id (Union[Unset, None, str]): Gets or sets the parent id.
            type (Union[Unset, BaseItemKind]): The base item kind.
            people (Union[Unset, None, List['BaseItemPerson']]): Gets or sets the people.
            studios (Union[Unset, None, List['NameGuidPair']]): Gets or sets the studios.
            genre_items (Union[Unset, None, List['NameGuidPair']]):
            parent_logo_item_id (Union[Unset, None, str]): Gets or sets wether the item has a logo, this will hold the Id of
                the Parent that has one.
            parent_backdrop_item_id (Union[Unset, None, str]): Gets or sets wether the item has any backdrops, this will
                hold the Id of the Parent that has one.
            parent_backdrop_image_tags (Union[Unset, None, List[str]]): Gets or sets the parent backdrop image tags.
            local_trailer_count (Union[Unset, None, int]): Gets or sets the local trailer count.
            user_data (Union[Unset, None, UserItemDataDto]): Class UserItemDataDto.
            recursive_item_count (Union[Unset, None, int]): Gets or sets the recursive item count.
            child_count (Union[Unset, None, int]): Gets or sets the child count.
            series_name (Union[Unset, None, str]): Gets or sets the name of the series.
            series_id (Union[Unset, None, str]): Gets or sets the series id.
            season_id (Union[Unset, None, str]): Gets or sets the season identifier.
            special_feature_count (Union[Unset, None, int]): Gets or sets the special feature count.
            display_preferences_id (Union[Unset, None, str]): Gets or sets the display preferences id.
            status (Union[Unset, None, str]): Gets or sets the status.
            air_time (Union[Unset, None, str]): Gets or sets the air time.
            air_days (Union[Unset, None, List[DayOfWeek]]): Gets or sets the air days.
            tags (Union[Unset, None, List[str]]): Gets or sets the tags.
            primary_image_aspect_ratio (Union[Unset, None, float]): Gets or sets the primary image aspect ratio, after image
                enhancements.
            artists (Union[Unset, None, List[str]]): Gets or sets the artists.
            artist_items (Union[Unset, None, List['NameGuidPair']]): Gets or sets the artist items.
            album (Union[Unset, None, str]): Gets or sets the album.
            collection_type (Union[Unset, None, str]): Gets or sets the type of the collection.
            display_order (Union[Unset, None, str]): Gets or sets the display order.
            album_id (Union[Unset, None, str]): Gets or sets the album id.
            album_primary_image_tag (Union[Unset, None, str]): Gets or sets the album image tag.
            series_primary_image_tag (Union[Unset, None, str]): Gets or sets the series primary image tag.
            album_artist (Union[Unset, None, str]): Gets or sets the album artist.
            album_artists (Union[Unset, None, List['NameGuidPair']]): Gets or sets the album artists.
            season_name (Union[Unset, None, str]): Gets or sets the name of the season.
            media_streams (Union[Unset, None, List['MediaStream']]): Gets or sets the media streams.
            video_type (Union[Unset, None, VideoType]): Enum VideoType.
            part_count (Union[Unset, None, int]): Gets or sets the part count.
            media_source_count (Union[Unset, None, int]):
            image_tags (Union[Unset, None, BaseItemDtoImageTags]): Gets or sets the image tags.
            backdrop_image_tags (Union[Unset, None, List[str]]): Gets or sets the backdrop image tags.
            screenshot_image_tags (Union[Unset, None, List[str]]): Gets or sets the screenshot image tags.
            parent_logo_image_tag (Union[Unset, None, str]): Gets or sets the parent logo image tag.
            parent_art_item_id (Union[Unset, None, str]): Gets or sets wether the item has fan art, this will hold the Id of
                the Parent that has one.
            parent_art_image_tag (Union[Unset, None, str]): Gets or sets the parent art image tag.
            series_thumb_image_tag (Union[Unset, None, str]): Gets or sets the series thumb image tag.
            image_blur_hashes (Union[Unset, None, BaseItemDtoImageBlurHashes]): Gets or sets the blurhashes for the image
                tags.
                Maps image type to dictionary mapping image tag to blurhash value.
            series_studio (Union[Unset, None, str]): Gets or sets the series studio.
            parent_thumb_item_id (Union[Unset, None, str]): Gets or sets the parent thumb item id.
            parent_thumb_image_tag (Union[Unset, None, str]): Gets or sets the parent thumb image tag.
            parent_primary_image_item_id (Union[Unset, None, str]): Gets or sets the parent primary image item identifier.
            parent_primary_image_tag (Union[Unset, None, str]): Gets or sets the parent primary image tag.
            chapters (Union[Unset, None, List['ChapterInfo']]): Gets or sets the chapters.
            location_type (Union[Unset, None, LocationType]): Enum LocationType.
            iso_type (Union[Unset, None, IsoType]): Enum IsoType.
            media_type (Union[Unset, None, str]): Gets or sets the type of the media.
            end_date (Union[Unset, None, datetime.datetime]): Gets or sets the end date.
            locked_fields (Union[Unset, None, List[MetadataField]]): Gets or sets the locked fields.
            trailer_count (Union[Unset, None, int]): Gets or sets the trailer count.
            movie_count (Union[Unset, None, int]): Gets or sets the movie count.
            series_count (Union[Unset, None, int]): Gets or sets the series count.
            program_count (Union[Unset, None, int]):
            episode_count (Union[Unset, None, int]): Gets or sets the episode count.
            song_count (Union[Unset, None, int]): Gets or sets the song count.
            album_count (Union[Unset, None, int]): Gets or sets the album count.
            artist_count (Union[Unset, None, int]):
            music_video_count (Union[Unset, None, int]): Gets or sets the music video count.
            lock_data (Union[Unset, None, bool]): Gets or sets a value indicating whether [enable internet providers].
            width (Union[Unset, None, int]):
            height (Union[Unset, None, int]):
            camera_make (Union[Unset, None, str]):
            camera_model (Union[Unset, None, str]):
            software (Union[Unset, None, str]):
            exposure_time (Union[Unset, None, float]):
            focal_length (Union[Unset, None, float]):
            image_orientation (Union[Unset, None, ImageOrientation]):
            aperture (Union[Unset, None, float]):
            shutter_speed (Union[Unset, None, float]):
            latitude (Union[Unset, None, float]):
            longitude (Union[Unset, None, float]):
            altitude (Union[Unset, None, float]):
            iso_speed_rating (Union[Unset, None, int]):
            series_timer_id (Union[Unset, None, str]): Gets or sets the series timer identifier.
            program_id (Union[Unset, None, str]): Gets or sets the program identifier.
            channel_primary_image_tag (Union[Unset, None, str]): Gets or sets the channel primary image tag.
            start_date (Union[Unset, None, datetime.datetime]): Gets or sets the start date of the recording, in UTC.
            completion_percentage (Union[Unset, None, float]): Gets or sets the completion percentage.
            is_repeat (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is repeat.
            episode_title (Union[Unset, None, str]): Gets or sets the episode title.
            channel_type (Union[Unset, None, ChannelType]): Enum ChannelType.
            audio (Union[Unset, None, ProgramAudio]):
            is_movie (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is movie.
            is_sports (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is sports.
            is_series (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is series.
            is_live (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is live.
            is_news (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is news.
            is_kids (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is kids.
            is_premiere (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is premiere.
            timer_id (Union[Unset, None, str]): Gets or sets the timer identifier.
            current_program (Union[Unset, None, BaseItemDto]): This is strictly used as a data transfer object from the api
                layer.
                This holds information about a BaseItem in a format that is convenient for the client.
    """

    name: Union[Unset, None, str] = UNSET
    original_title: Union[Unset, None, str] = UNSET
    server_id: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    etag: Union[Unset, None, str] = UNSET
    source_type: Union[Unset, None, str] = UNSET
    playlist_item_id: Union[Unset, None, str] = UNSET
    date_created: Union[Unset, None, datetime.datetime] = UNSET
    date_last_media_added: Union[Unset, None, datetime.datetime] = UNSET
    extra_type: Union[Unset, None, str] = UNSET
    airs_before_season_number: Union[Unset, None, int] = UNSET
    airs_after_season_number: Union[Unset, None, int] = UNSET
    airs_before_episode_number: Union[Unset, None, int] = UNSET
    can_delete: Union[Unset, None, bool] = UNSET
    can_download: Union[Unset, None, bool] = UNSET
    has_subtitles: Union[Unset, None, bool] = UNSET
    preferred_metadata_language: Union[Unset, None, str] = UNSET
    preferred_metadata_country_code: Union[Unset, None, str] = UNSET
    supports_sync: Union[Unset, None, bool] = UNSET
    container: Union[Unset, None, str] = UNSET
    sort_name: Union[Unset, None, str] = UNSET
    forced_sort_name: Union[Unset, None, str] = UNSET
    video_3d_format: Union[Unset, None, Video3DFormat] = UNSET
    premiere_date: Union[Unset, None, datetime.datetime] = UNSET
    external_urls: Union[Unset, None, List["ExternalUrl"]] = UNSET
    media_sources: Union[Unset, None, List["MediaSourceInfo"]] = UNSET
    critic_rating: Union[Unset, None, float] = UNSET
    production_locations: Union[Unset, None, List[str]] = UNSET
    path: Union[Unset, None, str] = UNSET
    enable_media_source_display: Union[Unset, None, bool] = UNSET
    official_rating: Union[Unset, None, str] = UNSET
    custom_rating: Union[Unset, None, str] = UNSET
    channel_id: Union[Unset, None, str] = UNSET
    channel_name: Union[Unset, None, str] = UNSET
    overview: Union[Unset, None, str] = UNSET
    taglines: Union[Unset, None, List[str]] = UNSET
    genres: Union[Unset, None, List[str]] = UNSET
    community_rating: Union[Unset, None, float] = UNSET
    cumulative_run_time_ticks: Union[Unset, None, int] = UNSET
    run_time_ticks: Union[Unset, None, int] = UNSET
    play_access: Union[Unset, None, PlayAccess] = UNSET
    aspect_ratio: Union[Unset, None, str] = UNSET
    production_year: Union[Unset, None, int] = UNSET
    is_place_holder: Union[Unset, None, bool] = UNSET
    number: Union[Unset, None, str] = UNSET
    channel_number: Union[Unset, None, str] = UNSET
    index_number: Union[Unset, None, int] = UNSET
    index_number_end: Union[Unset, None, int] = UNSET
    parent_index_number: Union[Unset, None, int] = UNSET
    remote_trailers: Union[Unset, None, List["MediaUrl"]] = UNSET
    provider_ids: Union[Unset, None, "BaseItemDtoProviderIds"] = UNSET
    is_hd: Union[Unset, None, bool] = UNSET
    is_folder: Union[Unset, None, bool] = UNSET
    parent_id: Union[Unset, None, str] = UNSET
    type: Union[Unset, BaseItemKind] = UNSET
    people: Union[Unset, None, List["BaseItemPerson"]] = UNSET
    studios: Union[Unset, None, List["NameGuidPair"]] = UNSET
    genre_items: Union[Unset, None, List["NameGuidPair"]] = UNSET
    parent_logo_item_id: Union[Unset, None, str] = UNSET
    parent_backdrop_item_id: Union[Unset, None, str] = UNSET
    parent_backdrop_image_tags: Union[Unset, None, List[str]] = UNSET
    local_trailer_count: Union[Unset, None, int] = UNSET
    user_data: Union[Unset, None, "UserItemDataDto"] = UNSET
    recursive_item_count: Union[Unset, None, int] = UNSET
    child_count: Union[Unset, None, int] = UNSET
    series_name: Union[Unset, None, str] = UNSET
    series_id: Union[Unset, None, str] = UNSET
    season_id: Union[Unset, None, str] = UNSET
    special_feature_count: Union[Unset, None, int] = UNSET
    display_preferences_id: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    air_time: Union[Unset, None, str] = UNSET
    air_days: Union[Unset, None, List[DayOfWeek]] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    primary_image_aspect_ratio: Union[Unset, None, float] = UNSET
    artists: Union[Unset, None, List[str]] = UNSET
    artist_items: Union[Unset, None, List["NameGuidPair"]] = UNSET
    album: Union[Unset, None, str] = UNSET
    collection_type: Union[Unset, None, str] = UNSET
    display_order: Union[Unset, None, str] = UNSET
    album_id: Union[Unset, None, str] = UNSET
    album_primary_image_tag: Union[Unset, None, str] = UNSET
    series_primary_image_tag: Union[Unset, None, str] = UNSET
    album_artist: Union[Unset, None, str] = UNSET
    album_artists: Union[Unset, None, List["NameGuidPair"]] = UNSET
    season_name: Union[Unset, None, str] = UNSET
    media_streams: Union[Unset, None, List["MediaStream"]] = UNSET
    video_type: Union[Unset, None, VideoType] = UNSET
    part_count: Union[Unset, None, int] = UNSET
    media_source_count: Union[Unset, None, int] = UNSET
    image_tags: Union[Unset, None, "BaseItemDtoImageTags"] = UNSET
    backdrop_image_tags: Union[Unset, None, List[str]] = UNSET
    screenshot_image_tags: Union[Unset, None, List[str]] = UNSET
    parent_logo_image_tag: Union[Unset, None, str] = UNSET
    parent_art_item_id: Union[Unset, None, str] = UNSET
    parent_art_image_tag: Union[Unset, None, str] = UNSET
    series_thumb_image_tag: Union[Unset, None, str] = UNSET
    image_blur_hashes: Union[Unset, None, "BaseItemDtoImageBlurHashes"] = UNSET
    series_studio: Union[Unset, None, str] = UNSET
    parent_thumb_item_id: Union[Unset, None, str] = UNSET
    parent_thumb_image_tag: Union[Unset, None, str] = UNSET
    parent_primary_image_item_id: Union[Unset, None, str] = UNSET
    parent_primary_image_tag: Union[Unset, None, str] = UNSET
    chapters: Union[Unset, None, List["ChapterInfo"]] = UNSET
    location_type: Union[Unset, None, LocationType] = UNSET
    iso_type: Union[Unset, None, IsoType] = UNSET
    media_type: Union[Unset, None, str] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    locked_fields: Union[Unset, None, List[MetadataField]] = UNSET
    trailer_count: Union[Unset, None, int] = UNSET
    movie_count: Union[Unset, None, int] = UNSET
    series_count: Union[Unset, None, int] = UNSET
    program_count: Union[Unset, None, int] = UNSET
    episode_count: Union[Unset, None, int] = UNSET
    song_count: Union[Unset, None, int] = UNSET
    album_count: Union[Unset, None, int] = UNSET
    artist_count: Union[Unset, None, int] = UNSET
    music_video_count: Union[Unset, None, int] = UNSET
    lock_data: Union[Unset, None, bool] = UNSET
    width: Union[Unset, None, int] = UNSET
    height: Union[Unset, None, int] = UNSET
    camera_make: Union[Unset, None, str] = UNSET
    camera_model: Union[Unset, None, str] = UNSET
    software: Union[Unset, None, str] = UNSET
    exposure_time: Union[Unset, None, float] = UNSET
    focal_length: Union[Unset, None, float] = UNSET
    image_orientation: Union[Unset, None, ImageOrientation] = UNSET
    aperture: Union[Unset, None, float] = UNSET
    shutter_speed: Union[Unset, None, float] = UNSET
    latitude: Union[Unset, None, float] = UNSET
    longitude: Union[Unset, None, float] = UNSET
    altitude: Union[Unset, None, float] = UNSET
    iso_speed_rating: Union[Unset, None, int] = UNSET
    series_timer_id: Union[Unset, None, str] = UNSET
    program_id: Union[Unset, None, str] = UNSET
    channel_primary_image_tag: Union[Unset, None, str] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    completion_percentage: Union[Unset, None, float] = UNSET
    is_repeat: Union[Unset, None, bool] = UNSET
    episode_title: Union[Unset, None, str] = UNSET
    channel_type: Union[Unset, None, ChannelType] = UNSET
    audio: Union[Unset, None, ProgramAudio] = UNSET
    is_movie: Union[Unset, None, bool] = UNSET
    is_sports: Union[Unset, None, bool] = UNSET
    is_series: Union[Unset, None, bool] = UNSET
    is_live: Union[Unset, None, bool] = UNSET
    is_news: Union[Unset, None, bool] = UNSET
    is_kids: Union[Unset, None, bool] = UNSET
    is_premiere: Union[Unset, None, bool] = UNSET
    timer_id: Union[Unset, None, str] = UNSET
    current_program: Union[Unset, None, "BaseItemDto"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        original_title = self.original_title
        server_id = self.server_id
        id = self.id
        etag = self.etag
        source_type = self.source_type
        playlist_item_id = self.playlist_item_id
        date_created: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat() if self.date_created else None

        date_last_media_added: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_last_media_added, Unset):
            date_last_media_added = self.date_last_media_added.isoformat() if self.date_last_media_added else None

        extra_type = self.extra_type
        airs_before_season_number = self.airs_before_season_number
        airs_after_season_number = self.airs_after_season_number
        airs_before_episode_number = self.airs_before_episode_number
        can_delete = self.can_delete
        can_download = self.can_download
        has_subtitles = self.has_subtitles
        preferred_metadata_language = self.preferred_metadata_language
        preferred_metadata_country_code = self.preferred_metadata_country_code
        supports_sync = self.supports_sync
        container = self.container
        sort_name = self.sort_name
        forced_sort_name = self.forced_sort_name
        video_3d_format: Union[Unset, None, str] = UNSET
        if not isinstance(self.video_3d_format, Unset):
            video_3d_format = self.video_3d_format.value if self.video_3d_format else None

        premiere_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.premiere_date, Unset):
            premiere_date = self.premiere_date.isoformat() if self.premiere_date else None

        external_urls: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.external_urls, Unset):
            if self.external_urls is None:
                external_urls = None
            else:
                external_urls = []
                for external_urls_item_data in self.external_urls:
                    external_urls_item = external_urls_item_data.to_dict()

                    external_urls.append(external_urls_item)

        media_sources: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media_sources, Unset):
            if self.media_sources is None:
                media_sources = None
            else:
                media_sources = []
                for media_sources_item_data in self.media_sources:
                    media_sources_item = media_sources_item_data.to_dict()

                    media_sources.append(media_sources_item)

        critic_rating = self.critic_rating
        production_locations: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.production_locations, Unset):
            if self.production_locations is None:
                production_locations = None
            else:
                production_locations = self.production_locations

        path = self.path
        enable_media_source_display = self.enable_media_source_display
        official_rating = self.official_rating
        custom_rating = self.custom_rating
        channel_id = self.channel_id
        channel_name = self.channel_name
        overview = self.overview
        taglines: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.taglines, Unset):
            if self.taglines is None:
                taglines = None
            else:
                taglines = self.taglines

        genres: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.genres, Unset):
            if self.genres is None:
                genres = None
            else:
                genres = self.genres

        community_rating = self.community_rating
        cumulative_run_time_ticks = self.cumulative_run_time_ticks
        run_time_ticks = self.run_time_ticks
        play_access: Union[Unset, None, str] = UNSET
        if not isinstance(self.play_access, Unset):
            play_access = self.play_access.value if self.play_access else None

        aspect_ratio = self.aspect_ratio
        production_year = self.production_year
        is_place_holder = self.is_place_holder
        number = self.number
        channel_number = self.channel_number
        index_number = self.index_number
        index_number_end = self.index_number_end
        parent_index_number = self.parent_index_number
        remote_trailers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.remote_trailers, Unset):
            if self.remote_trailers is None:
                remote_trailers = None
            else:
                remote_trailers = []
                for remote_trailers_item_data in self.remote_trailers:
                    remote_trailers_item = remote_trailers_item_data.to_dict()

                    remote_trailers.append(remote_trailers_item)

        provider_ids: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_ids, Unset):
            provider_ids = self.provider_ids.to_dict() if self.provider_ids else None

        is_hd = self.is_hd
        is_folder = self.is_folder
        parent_id = self.parent_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        people: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.people, Unset):
            if self.people is None:
                people = None
            else:
                people = []
                for people_item_data in self.people:
                    people_item = people_item_data.to_dict()

                    people.append(people_item)

        studios: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.studios, Unset):
            if self.studios is None:
                studios = None
            else:
                studios = []
                for studios_item_data in self.studios:
                    studios_item = studios_item_data.to_dict()

                    studios.append(studios_item)

        genre_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.genre_items, Unset):
            if self.genre_items is None:
                genre_items = None
            else:
                genre_items = []
                for genre_items_item_data in self.genre_items:
                    genre_items_item = genre_items_item_data.to_dict()

                    genre_items.append(genre_items_item)

        parent_logo_item_id = self.parent_logo_item_id
        parent_backdrop_item_id = self.parent_backdrop_item_id
        parent_backdrop_image_tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.parent_backdrop_image_tags, Unset):
            if self.parent_backdrop_image_tags is None:
                parent_backdrop_image_tags = None
            else:
                parent_backdrop_image_tags = self.parent_backdrop_image_tags

        local_trailer_count = self.local_trailer_count
        user_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_data, Unset):
            user_data = self.user_data.to_dict() if self.user_data else None

        recursive_item_count = self.recursive_item_count
        child_count = self.child_count
        series_name = self.series_name
        series_id = self.series_id
        season_id = self.season_id
        special_feature_count = self.special_feature_count
        display_preferences_id = self.display_preferences_id
        status = self.status
        air_time = self.air_time
        air_days: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.air_days, Unset):
            if self.air_days is None:
                air_days = None
            else:
                air_days = []
                for air_days_item_data in self.air_days:
                    air_days_item = air_days_item_data.value

                    air_days.append(air_days_item)

        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        primary_image_aspect_ratio = self.primary_image_aspect_ratio
        artists: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.artists, Unset):
            if self.artists is None:
                artists = None
            else:
                artists = self.artists

        artist_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.artist_items, Unset):
            if self.artist_items is None:
                artist_items = None
            else:
                artist_items = []
                for artist_items_item_data in self.artist_items:
                    artist_items_item = artist_items_item_data.to_dict()

                    artist_items.append(artist_items_item)

        album = self.album
        collection_type = self.collection_type
        display_order = self.display_order
        album_id = self.album_id
        album_primary_image_tag = self.album_primary_image_tag
        series_primary_image_tag = self.series_primary_image_tag
        album_artist = self.album_artist
        album_artists: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.album_artists, Unset):
            if self.album_artists is None:
                album_artists = None
            else:
                album_artists = []
                for album_artists_item_data in self.album_artists:
                    album_artists_item = album_artists_item_data.to_dict()

                    album_artists.append(album_artists_item)

        season_name = self.season_name
        media_streams: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media_streams, Unset):
            if self.media_streams is None:
                media_streams = None
            else:
                media_streams = []
                for media_streams_item_data in self.media_streams:
                    media_streams_item = media_streams_item_data.to_dict()

                    media_streams.append(media_streams_item)

        video_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.video_type, Unset):
            video_type = self.video_type.value if self.video_type else None

        part_count = self.part_count
        media_source_count = self.media_source_count
        image_tags: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.image_tags, Unset):
            image_tags = self.image_tags.to_dict() if self.image_tags else None

        backdrop_image_tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.backdrop_image_tags, Unset):
            if self.backdrop_image_tags is None:
                backdrop_image_tags = None
            else:
                backdrop_image_tags = self.backdrop_image_tags

        screenshot_image_tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.screenshot_image_tags, Unset):
            if self.screenshot_image_tags is None:
                screenshot_image_tags = None
            else:
                screenshot_image_tags = self.screenshot_image_tags

        parent_logo_image_tag = self.parent_logo_image_tag
        parent_art_item_id = self.parent_art_item_id
        parent_art_image_tag = self.parent_art_image_tag
        series_thumb_image_tag = self.series_thumb_image_tag
        image_blur_hashes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.image_blur_hashes, Unset):
            image_blur_hashes = self.image_blur_hashes.to_dict() if self.image_blur_hashes else None

        series_studio = self.series_studio
        parent_thumb_item_id = self.parent_thumb_item_id
        parent_thumb_image_tag = self.parent_thumb_image_tag
        parent_primary_image_item_id = self.parent_primary_image_item_id
        parent_primary_image_tag = self.parent_primary_image_tag
        chapters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.chapters, Unset):
            if self.chapters is None:
                chapters = None
            else:
                chapters = []
                for chapters_item_data in self.chapters:
                    chapters_item = chapters_item_data.to_dict()

                    chapters.append(chapters_item)

        location_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value if self.location_type else None

        iso_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.iso_type, Unset):
            iso_type = self.iso_type.value if self.iso_type else None

        media_type = self.media_type
        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        locked_fields: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.locked_fields, Unset):
            if self.locked_fields is None:
                locked_fields = None
            else:
                locked_fields = []
                for locked_fields_item_data in self.locked_fields:
                    locked_fields_item = locked_fields_item_data.value

                    locked_fields.append(locked_fields_item)

        trailer_count = self.trailer_count
        movie_count = self.movie_count
        series_count = self.series_count
        program_count = self.program_count
        episode_count = self.episode_count
        song_count = self.song_count
        album_count = self.album_count
        artist_count = self.artist_count
        music_video_count = self.music_video_count
        lock_data = self.lock_data
        width = self.width
        height = self.height
        camera_make = self.camera_make
        camera_model = self.camera_model
        software = self.software
        exposure_time = self.exposure_time
        focal_length = self.focal_length
        image_orientation: Union[Unset, None, str] = UNSET
        if not isinstance(self.image_orientation, Unset):
            image_orientation = self.image_orientation.value if self.image_orientation else None

        aperture = self.aperture
        shutter_speed = self.shutter_speed
        latitude = self.latitude
        longitude = self.longitude
        altitude = self.altitude
        iso_speed_rating = self.iso_speed_rating
        series_timer_id = self.series_timer_id
        program_id = self.program_id
        channel_primary_image_tag = self.channel_primary_image_tag
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        completion_percentage = self.completion_percentage
        is_repeat = self.is_repeat
        episode_title = self.episode_title
        channel_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.channel_type, Unset):
            channel_type = self.channel_type.value if self.channel_type else None

        audio: Union[Unset, None, str] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.value if self.audio else None

        is_movie = self.is_movie
        is_sports = self.is_sports
        is_series = self.is_series
        is_live = self.is_live
        is_news = self.is_news
        is_kids = self.is_kids
        is_premiere = self.is_premiere
        timer_id = self.timer_id
        current_program: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.current_program, Unset):
            current_program = self.current_program.to_dict() if self.current_program else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if original_title is not UNSET:
            field_dict["OriginalTitle"] = original_title
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if id is not UNSET:
            field_dict["Id"] = id
        if etag is not UNSET:
            field_dict["Etag"] = etag
        if source_type is not UNSET:
            field_dict["SourceType"] = source_type
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_last_media_added is not UNSET:
            field_dict["DateLastMediaAdded"] = date_last_media_added
        if extra_type is not UNSET:
            field_dict["ExtraType"] = extra_type
        if airs_before_season_number is not UNSET:
            field_dict["AirsBeforeSeasonNumber"] = airs_before_season_number
        if airs_after_season_number is not UNSET:
            field_dict["AirsAfterSeasonNumber"] = airs_after_season_number
        if airs_before_episode_number is not UNSET:
            field_dict["AirsBeforeEpisodeNumber"] = airs_before_episode_number
        if can_delete is not UNSET:
            field_dict["CanDelete"] = can_delete
        if can_download is not UNSET:
            field_dict["CanDownload"] = can_download
        if has_subtitles is not UNSET:
            field_dict["HasSubtitles"] = has_subtitles
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language
        if preferred_metadata_country_code is not UNSET:
            field_dict["PreferredMetadataCountryCode"] = preferred_metadata_country_code
        if supports_sync is not UNSET:
            field_dict["SupportsSync"] = supports_sync
        if container is not UNSET:
            field_dict["Container"] = container
        if sort_name is not UNSET:
            field_dict["SortName"] = sort_name
        if forced_sort_name is not UNSET:
            field_dict["ForcedSortName"] = forced_sort_name
        if video_3d_format is not UNSET:
            field_dict["Video3DFormat"] = video_3d_format
        if premiere_date is not UNSET:
            field_dict["PremiereDate"] = premiere_date
        if external_urls is not UNSET:
            field_dict["ExternalUrls"] = external_urls
        if media_sources is not UNSET:
            field_dict["MediaSources"] = media_sources
        if critic_rating is not UNSET:
            field_dict["CriticRating"] = critic_rating
        if production_locations is not UNSET:
            field_dict["ProductionLocations"] = production_locations
        if path is not UNSET:
            field_dict["Path"] = path
        if enable_media_source_display is not UNSET:
            field_dict["EnableMediaSourceDisplay"] = enable_media_source_display
        if official_rating is not UNSET:
            field_dict["OfficialRating"] = official_rating
        if custom_rating is not UNSET:
            field_dict["CustomRating"] = custom_rating
        if channel_id is not UNSET:
            field_dict["ChannelId"] = channel_id
        if channel_name is not UNSET:
            field_dict["ChannelName"] = channel_name
        if overview is not UNSET:
            field_dict["Overview"] = overview
        if taglines is not UNSET:
            field_dict["Taglines"] = taglines
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if cumulative_run_time_ticks is not UNSET:
            field_dict["CumulativeRunTimeTicks"] = cumulative_run_time_ticks
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if play_access is not UNSET:
            field_dict["PlayAccess"] = play_access
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if production_year is not UNSET:
            field_dict["ProductionYear"] = production_year
        if is_place_holder is not UNSET:
            field_dict["IsPlaceHolder"] = is_place_holder
        if number is not UNSET:
            field_dict["Number"] = number
        if channel_number is not UNSET:
            field_dict["ChannelNumber"] = channel_number
        if index_number is not UNSET:
            field_dict["IndexNumber"] = index_number
        if index_number_end is not UNSET:
            field_dict["IndexNumberEnd"] = index_number_end
        if parent_index_number is not UNSET:
            field_dict["ParentIndexNumber"] = parent_index_number
        if remote_trailers is not UNSET:
            field_dict["RemoteTrailers"] = remote_trailers
        if provider_ids is not UNSET:
            field_dict["ProviderIds"] = provider_ids
        if is_hd is not UNSET:
            field_dict["IsHD"] = is_hd
        if is_folder is not UNSET:
            field_dict["IsFolder"] = is_folder
        if parent_id is not UNSET:
            field_dict["ParentId"] = parent_id
        if type is not UNSET:
            field_dict["Type"] = type
        if people is not UNSET:
            field_dict["People"] = people
        if studios is not UNSET:
            field_dict["Studios"] = studios
        if genre_items is not UNSET:
            field_dict["GenreItems"] = genre_items
        if parent_logo_item_id is not UNSET:
            field_dict["ParentLogoItemId"] = parent_logo_item_id
        if parent_backdrop_item_id is not UNSET:
            field_dict["ParentBackdropItemId"] = parent_backdrop_item_id
        if parent_backdrop_image_tags is not UNSET:
            field_dict["ParentBackdropImageTags"] = parent_backdrop_image_tags
        if local_trailer_count is not UNSET:
            field_dict["LocalTrailerCount"] = local_trailer_count
        if user_data is not UNSET:
            field_dict["UserData"] = user_data
        if recursive_item_count is not UNSET:
            field_dict["RecursiveItemCount"] = recursive_item_count
        if child_count is not UNSET:
            field_dict["ChildCount"] = child_count
        if series_name is not UNSET:
            field_dict["SeriesName"] = series_name
        if series_id is not UNSET:
            field_dict["SeriesId"] = series_id
        if season_id is not UNSET:
            field_dict["SeasonId"] = season_id
        if special_feature_count is not UNSET:
            field_dict["SpecialFeatureCount"] = special_feature_count
        if display_preferences_id is not UNSET:
            field_dict["DisplayPreferencesId"] = display_preferences_id
        if status is not UNSET:
            field_dict["Status"] = status
        if air_time is not UNSET:
            field_dict["AirTime"] = air_time
        if air_days is not UNSET:
            field_dict["AirDays"] = air_days
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if primary_image_aspect_ratio is not UNSET:
            field_dict["PrimaryImageAspectRatio"] = primary_image_aspect_ratio
        if artists is not UNSET:
            field_dict["Artists"] = artists
        if artist_items is not UNSET:
            field_dict["ArtistItems"] = artist_items
        if album is not UNSET:
            field_dict["Album"] = album
        if collection_type is not UNSET:
            field_dict["CollectionType"] = collection_type
        if display_order is not UNSET:
            field_dict["DisplayOrder"] = display_order
        if album_id is not UNSET:
            field_dict["AlbumId"] = album_id
        if album_primary_image_tag is not UNSET:
            field_dict["AlbumPrimaryImageTag"] = album_primary_image_tag
        if series_primary_image_tag is not UNSET:
            field_dict["SeriesPrimaryImageTag"] = series_primary_image_tag
        if album_artist is not UNSET:
            field_dict["AlbumArtist"] = album_artist
        if album_artists is not UNSET:
            field_dict["AlbumArtists"] = album_artists
        if season_name is not UNSET:
            field_dict["SeasonName"] = season_name
        if media_streams is not UNSET:
            field_dict["MediaStreams"] = media_streams
        if video_type is not UNSET:
            field_dict["VideoType"] = video_type
        if part_count is not UNSET:
            field_dict["PartCount"] = part_count
        if media_source_count is not UNSET:
            field_dict["MediaSourceCount"] = media_source_count
        if image_tags is not UNSET:
            field_dict["ImageTags"] = image_tags
        if backdrop_image_tags is not UNSET:
            field_dict["BackdropImageTags"] = backdrop_image_tags
        if screenshot_image_tags is not UNSET:
            field_dict["ScreenshotImageTags"] = screenshot_image_tags
        if parent_logo_image_tag is not UNSET:
            field_dict["ParentLogoImageTag"] = parent_logo_image_tag
        if parent_art_item_id is not UNSET:
            field_dict["ParentArtItemId"] = parent_art_item_id
        if parent_art_image_tag is not UNSET:
            field_dict["ParentArtImageTag"] = parent_art_image_tag
        if series_thumb_image_tag is not UNSET:
            field_dict["SeriesThumbImageTag"] = series_thumb_image_tag
        if image_blur_hashes is not UNSET:
            field_dict["ImageBlurHashes"] = image_blur_hashes
        if series_studio is not UNSET:
            field_dict["SeriesStudio"] = series_studio
        if parent_thumb_item_id is not UNSET:
            field_dict["ParentThumbItemId"] = parent_thumb_item_id
        if parent_thumb_image_tag is not UNSET:
            field_dict["ParentThumbImageTag"] = parent_thumb_image_tag
        if parent_primary_image_item_id is not UNSET:
            field_dict["ParentPrimaryImageItemId"] = parent_primary_image_item_id
        if parent_primary_image_tag is not UNSET:
            field_dict["ParentPrimaryImageTag"] = parent_primary_image_tag
        if chapters is not UNSET:
            field_dict["Chapters"] = chapters
        if location_type is not UNSET:
            field_dict["LocationType"] = location_type
        if iso_type is not UNSET:
            field_dict["IsoType"] = iso_type
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type
        if end_date is not UNSET:
            field_dict["EndDate"] = end_date
        if locked_fields is not UNSET:
            field_dict["LockedFields"] = locked_fields
        if trailer_count is not UNSET:
            field_dict["TrailerCount"] = trailer_count
        if movie_count is not UNSET:
            field_dict["MovieCount"] = movie_count
        if series_count is not UNSET:
            field_dict["SeriesCount"] = series_count
        if program_count is not UNSET:
            field_dict["ProgramCount"] = program_count
        if episode_count is not UNSET:
            field_dict["EpisodeCount"] = episode_count
        if song_count is not UNSET:
            field_dict["SongCount"] = song_count
        if album_count is not UNSET:
            field_dict["AlbumCount"] = album_count
        if artist_count is not UNSET:
            field_dict["ArtistCount"] = artist_count
        if music_video_count is not UNSET:
            field_dict["MusicVideoCount"] = music_video_count
        if lock_data is not UNSET:
            field_dict["LockData"] = lock_data
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if camera_make is not UNSET:
            field_dict["CameraMake"] = camera_make
        if camera_model is not UNSET:
            field_dict["CameraModel"] = camera_model
        if software is not UNSET:
            field_dict["Software"] = software
        if exposure_time is not UNSET:
            field_dict["ExposureTime"] = exposure_time
        if focal_length is not UNSET:
            field_dict["FocalLength"] = focal_length
        if image_orientation is not UNSET:
            field_dict["ImageOrientation"] = image_orientation
        if aperture is not UNSET:
            field_dict["Aperture"] = aperture
        if shutter_speed is not UNSET:
            field_dict["ShutterSpeed"] = shutter_speed
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if altitude is not UNSET:
            field_dict["Altitude"] = altitude
        if iso_speed_rating is not UNSET:
            field_dict["IsoSpeedRating"] = iso_speed_rating
        if series_timer_id is not UNSET:
            field_dict["SeriesTimerId"] = series_timer_id
        if program_id is not UNSET:
            field_dict["ProgramId"] = program_id
        if channel_primary_image_tag is not UNSET:
            field_dict["ChannelPrimaryImageTag"] = channel_primary_image_tag
        if start_date is not UNSET:
            field_dict["StartDate"] = start_date
        if completion_percentage is not UNSET:
            field_dict["CompletionPercentage"] = completion_percentage
        if is_repeat is not UNSET:
            field_dict["IsRepeat"] = is_repeat
        if episode_title is not UNSET:
            field_dict["EpisodeTitle"] = episode_title
        if channel_type is not UNSET:
            field_dict["ChannelType"] = channel_type
        if audio is not UNSET:
            field_dict["Audio"] = audio
        if is_movie is not UNSET:
            field_dict["IsMovie"] = is_movie
        if is_sports is not UNSET:
            field_dict["IsSports"] = is_sports
        if is_series is not UNSET:
            field_dict["IsSeries"] = is_series
        if is_live is not UNSET:
            field_dict["IsLive"] = is_live
        if is_news is not UNSET:
            field_dict["IsNews"] = is_news
        if is_kids is not UNSET:
            field_dict["IsKids"] = is_kids
        if is_premiere is not UNSET:
            field_dict["IsPremiere"] = is_premiere
        if timer_id is not UNSET:
            field_dict["TimerId"] = timer_id
        if current_program is not UNSET:
            field_dict["CurrentProgram"] = current_program

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto_image_blur_hashes import BaseItemDtoImageBlurHashes
        from ..models.base_item_dto_image_tags import BaseItemDtoImageTags
        from ..models.base_item_dto_provider_ids import BaseItemDtoProviderIds
        from ..models.base_item_person import BaseItemPerson
        from ..models.chapter_info import ChapterInfo
        from ..models.external_url import ExternalUrl
        from ..models.media_source_info import MediaSourceInfo
        from ..models.media_stream import MediaStream
        from ..models.media_url import MediaUrl
        from ..models.name_guid_pair import NameGuidPair
        from ..models.user_item_data_dto import UserItemDataDto

        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        original_title = d.pop("OriginalTitle", UNSET)

        server_id = d.pop("ServerId", UNSET)

        id = d.pop("Id", UNSET)

        etag = d.pop("Etag", UNSET)

        source_type = d.pop("SourceType", UNSET)

        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, None, datetime.datetime]
        if _date_created is None:
            date_created = None
        elif isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_last_media_added = d.pop("DateLastMediaAdded", UNSET)
        date_last_media_added: Union[Unset, None, datetime.datetime]
        if _date_last_media_added is None:
            date_last_media_added = None
        elif isinstance(_date_last_media_added, Unset):
            date_last_media_added = UNSET
        else:
            date_last_media_added = isoparse(_date_last_media_added)

        extra_type = d.pop("ExtraType", UNSET)

        airs_before_season_number = d.pop("AirsBeforeSeasonNumber", UNSET)

        airs_after_season_number = d.pop("AirsAfterSeasonNumber", UNSET)

        airs_before_episode_number = d.pop("AirsBeforeEpisodeNumber", UNSET)

        can_delete = d.pop("CanDelete", UNSET)

        can_download = d.pop("CanDownload", UNSET)

        has_subtitles = d.pop("HasSubtitles", UNSET)

        preferred_metadata_language = d.pop("PreferredMetadataLanguage", UNSET)

        preferred_metadata_country_code = d.pop("PreferredMetadataCountryCode", UNSET)

        supports_sync = d.pop("SupportsSync", UNSET)

        container = d.pop("Container", UNSET)

        sort_name = d.pop("SortName", UNSET)

        forced_sort_name = d.pop("ForcedSortName", UNSET)

        _video_3d_format = d.pop("Video3DFormat", UNSET)
        video_3d_format: Union[Unset, None, Video3DFormat]
        if _video_3d_format is None:
            video_3d_format = None
        elif isinstance(_video_3d_format, Unset):
            video_3d_format = UNSET
        else:
            video_3d_format = Video3DFormat(_video_3d_format)

        _premiere_date = d.pop("PremiereDate", UNSET)
        premiere_date: Union[Unset, None, datetime.datetime]
        if _premiere_date is None:
            premiere_date = None
        elif isinstance(_premiere_date, Unset):
            premiere_date = UNSET
        else:
            premiere_date = isoparse(_premiere_date)

        external_urls = []
        _external_urls = d.pop("ExternalUrls", UNSET)
        for external_urls_item_data in _external_urls or []:
            external_urls_item = ExternalUrl.from_dict(external_urls_item_data)

            external_urls.append(external_urls_item)

        media_sources = []
        _media_sources = d.pop("MediaSources", UNSET)
        for media_sources_item_data in _media_sources or []:
            media_sources_item = MediaSourceInfo.from_dict(media_sources_item_data)

            media_sources.append(media_sources_item)

        critic_rating = d.pop("CriticRating", UNSET)

        production_locations = cast(List[str], d.pop("ProductionLocations", UNSET))

        path = d.pop("Path", UNSET)

        enable_media_source_display = d.pop("EnableMediaSourceDisplay", UNSET)

        official_rating = d.pop("OfficialRating", UNSET)

        custom_rating = d.pop("CustomRating", UNSET)

        channel_id = d.pop("ChannelId", UNSET)

        channel_name = d.pop("ChannelName", UNSET)

        overview = d.pop("Overview", UNSET)

        taglines = cast(List[str], d.pop("Taglines", UNSET))

        genres = cast(List[str], d.pop("Genres", UNSET))

        community_rating = d.pop("CommunityRating", UNSET)

        cumulative_run_time_ticks = d.pop("CumulativeRunTimeTicks", UNSET)

        run_time_ticks = d.pop("RunTimeTicks", UNSET)

        _play_access = d.pop("PlayAccess", UNSET)
        play_access: Union[Unset, None, PlayAccess]
        if _play_access is None:
            play_access = None
        elif isinstance(_play_access, Unset):
            play_access = UNSET
        else:
            play_access = PlayAccess(_play_access)

        aspect_ratio = d.pop("AspectRatio", UNSET)

        production_year = d.pop("ProductionYear", UNSET)

        is_place_holder = d.pop("IsPlaceHolder", UNSET)

        number = d.pop("Number", UNSET)

        channel_number = d.pop("ChannelNumber", UNSET)

        index_number = d.pop("IndexNumber", UNSET)

        index_number_end = d.pop("IndexNumberEnd", UNSET)

        parent_index_number = d.pop("ParentIndexNumber", UNSET)

        remote_trailers = []
        _remote_trailers = d.pop("RemoteTrailers", UNSET)
        for remote_trailers_item_data in _remote_trailers or []:
            remote_trailers_item = MediaUrl.from_dict(remote_trailers_item_data)

            remote_trailers.append(remote_trailers_item)

        _provider_ids = d.pop("ProviderIds", UNSET)
        provider_ids: Union[Unset, None, BaseItemDtoProviderIds]
        if _provider_ids is None:
            provider_ids = None
        elif isinstance(_provider_ids, Unset):
            provider_ids = UNSET
        else:
            provider_ids = BaseItemDtoProviderIds.from_dict(_provider_ids)

        is_hd = d.pop("IsHD", UNSET)

        is_folder = d.pop("IsFolder", UNSET)

        parent_id = d.pop("ParentId", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, BaseItemKind]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BaseItemKind(_type)

        people = []
        _people = d.pop("People", UNSET)
        for people_item_data in _people or []:
            people_item = BaseItemPerson.from_dict(people_item_data)

            people.append(people_item)

        studios = []
        _studios = d.pop("Studios", UNSET)
        for studios_item_data in _studios or []:
            studios_item = NameGuidPair.from_dict(studios_item_data)

            studios.append(studios_item)

        genre_items = []
        _genre_items = d.pop("GenreItems", UNSET)
        for genre_items_item_data in _genre_items or []:
            genre_items_item = NameGuidPair.from_dict(genre_items_item_data)

            genre_items.append(genre_items_item)

        parent_logo_item_id = d.pop("ParentLogoItemId", UNSET)

        parent_backdrop_item_id = d.pop("ParentBackdropItemId", UNSET)

        parent_backdrop_image_tags = cast(List[str], d.pop("ParentBackdropImageTags", UNSET))

        local_trailer_count = d.pop("LocalTrailerCount", UNSET)

        _user_data = d.pop("UserData", UNSET)
        user_data: Union[Unset, None, UserItemDataDto]
        if _user_data is None:
            user_data = None
        elif isinstance(_user_data, Unset):
            user_data = UNSET
        else:
            user_data = UserItemDataDto.from_dict(_user_data)

        recursive_item_count = d.pop("RecursiveItemCount", UNSET)

        child_count = d.pop("ChildCount", UNSET)

        series_name = d.pop("SeriesName", UNSET)

        series_id = d.pop("SeriesId", UNSET)

        season_id = d.pop("SeasonId", UNSET)

        special_feature_count = d.pop("SpecialFeatureCount", UNSET)

        display_preferences_id = d.pop("DisplayPreferencesId", UNSET)

        status = d.pop("Status", UNSET)

        air_time = d.pop("AirTime", UNSET)

        air_days = []
        _air_days = d.pop("AirDays", UNSET)
        for air_days_item_data in _air_days or []:
            air_days_item = DayOfWeek(air_days_item_data)

            air_days.append(air_days_item)

        tags = cast(List[str], d.pop("Tags", UNSET))

        primary_image_aspect_ratio = d.pop("PrimaryImageAspectRatio", UNSET)

        artists = cast(List[str], d.pop("Artists", UNSET))

        artist_items = []
        _artist_items = d.pop("ArtistItems", UNSET)
        for artist_items_item_data in _artist_items or []:
            artist_items_item = NameGuidPair.from_dict(artist_items_item_data)

            artist_items.append(artist_items_item)

        album = d.pop("Album", UNSET)

        collection_type = d.pop("CollectionType", UNSET)

        display_order = d.pop("DisplayOrder", UNSET)

        album_id = d.pop("AlbumId", UNSET)

        album_primary_image_tag = d.pop("AlbumPrimaryImageTag", UNSET)

        series_primary_image_tag = d.pop("SeriesPrimaryImageTag", UNSET)

        album_artist = d.pop("AlbumArtist", UNSET)

        album_artists = []
        _album_artists = d.pop("AlbumArtists", UNSET)
        for album_artists_item_data in _album_artists or []:
            album_artists_item = NameGuidPair.from_dict(album_artists_item_data)

            album_artists.append(album_artists_item)

        season_name = d.pop("SeasonName", UNSET)

        media_streams = []
        _media_streams = d.pop("MediaStreams", UNSET)
        for media_streams_item_data in _media_streams or []:
            media_streams_item = MediaStream.from_dict(media_streams_item_data)

            media_streams.append(media_streams_item)

        _video_type = d.pop("VideoType", UNSET)
        video_type: Union[Unset, None, VideoType]
        if _video_type is None:
            video_type = None
        elif isinstance(_video_type, Unset):
            video_type = UNSET
        else:
            video_type = VideoType(_video_type)

        part_count = d.pop("PartCount", UNSET)

        media_source_count = d.pop("MediaSourceCount", UNSET)

        _image_tags = d.pop("ImageTags", UNSET)
        image_tags: Union[Unset, None, BaseItemDtoImageTags]
        if _image_tags is None:
            image_tags = None
        elif isinstance(_image_tags, Unset):
            image_tags = UNSET
        else:
            image_tags = BaseItemDtoImageTags.from_dict(_image_tags)

        backdrop_image_tags = cast(List[str], d.pop("BackdropImageTags", UNSET))

        screenshot_image_tags = cast(List[str], d.pop("ScreenshotImageTags", UNSET))

        parent_logo_image_tag = d.pop("ParentLogoImageTag", UNSET)

        parent_art_item_id = d.pop("ParentArtItemId", UNSET)

        parent_art_image_tag = d.pop("ParentArtImageTag", UNSET)

        series_thumb_image_tag = d.pop("SeriesThumbImageTag", UNSET)

        _image_blur_hashes = d.pop("ImageBlurHashes", UNSET)
        image_blur_hashes: Union[Unset, None, BaseItemDtoImageBlurHashes]
        if _image_blur_hashes is None:
            image_blur_hashes = None
        elif isinstance(_image_blur_hashes, Unset):
            image_blur_hashes = UNSET
        else:
            image_blur_hashes = BaseItemDtoImageBlurHashes.from_dict(_image_blur_hashes)

        series_studio = d.pop("SeriesStudio", UNSET)

        parent_thumb_item_id = d.pop("ParentThumbItemId", UNSET)

        parent_thumb_image_tag = d.pop("ParentThumbImageTag", UNSET)

        parent_primary_image_item_id = d.pop("ParentPrimaryImageItemId", UNSET)

        parent_primary_image_tag = d.pop("ParentPrimaryImageTag", UNSET)

        chapters = []
        _chapters = d.pop("Chapters", UNSET)
        for chapters_item_data in _chapters or []:
            chapters_item = ChapterInfo.from_dict(chapters_item_data)

            chapters.append(chapters_item)

        _location_type = d.pop("LocationType", UNSET)
        location_type: Union[Unset, None, LocationType]
        if _location_type is None:
            location_type = None
        elif isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = LocationType(_location_type)

        _iso_type = d.pop("IsoType", UNSET)
        iso_type: Union[Unset, None, IsoType]
        if _iso_type is None:
            iso_type = None
        elif isinstance(_iso_type, Unset):
            iso_type = UNSET
        else:
            iso_type = IsoType(_iso_type)

        media_type = d.pop("MediaType", UNSET)

        _end_date = d.pop("EndDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        locked_fields = []
        _locked_fields = d.pop("LockedFields", UNSET)
        for locked_fields_item_data in _locked_fields or []:
            locked_fields_item = MetadataField(locked_fields_item_data)

            locked_fields.append(locked_fields_item)

        trailer_count = d.pop("TrailerCount", UNSET)

        movie_count = d.pop("MovieCount", UNSET)

        series_count = d.pop("SeriesCount", UNSET)

        program_count = d.pop("ProgramCount", UNSET)

        episode_count = d.pop("EpisodeCount", UNSET)

        song_count = d.pop("SongCount", UNSET)

        album_count = d.pop("AlbumCount", UNSET)

        artist_count = d.pop("ArtistCount", UNSET)

        music_video_count = d.pop("MusicVideoCount", UNSET)

        lock_data = d.pop("LockData", UNSET)

        width = d.pop("Width", UNSET)

        height = d.pop("Height", UNSET)

        camera_make = d.pop("CameraMake", UNSET)

        camera_model = d.pop("CameraModel", UNSET)

        software = d.pop("Software", UNSET)

        exposure_time = d.pop("ExposureTime", UNSET)

        focal_length = d.pop("FocalLength", UNSET)

        _image_orientation = d.pop("ImageOrientation", UNSET)
        image_orientation: Union[Unset, None, ImageOrientation]
        if _image_orientation is None:
            image_orientation = None
        elif isinstance(_image_orientation, Unset):
            image_orientation = UNSET
        else:
            image_orientation = ImageOrientation(_image_orientation)

        aperture = d.pop("Aperture", UNSET)

        shutter_speed = d.pop("ShutterSpeed", UNSET)

        latitude = d.pop("Latitude", UNSET)

        longitude = d.pop("Longitude", UNSET)

        altitude = d.pop("Altitude", UNSET)

        iso_speed_rating = d.pop("IsoSpeedRating", UNSET)

        series_timer_id = d.pop("SeriesTimerId", UNSET)

        program_id = d.pop("ProgramId", UNSET)

        channel_primary_image_tag = d.pop("ChannelPrimaryImageTag", UNSET)

        _start_date = d.pop("StartDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        completion_percentage = d.pop("CompletionPercentage", UNSET)

        is_repeat = d.pop("IsRepeat", UNSET)

        episode_title = d.pop("EpisodeTitle", UNSET)

        _channel_type = d.pop("ChannelType", UNSET)
        channel_type: Union[Unset, None, ChannelType]
        if _channel_type is None:
            channel_type = None
        elif isinstance(_channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = ChannelType(_channel_type)

        _audio = d.pop("Audio", UNSET)
        audio: Union[Unset, None, ProgramAudio]
        if _audio is None:
            audio = None
        elif isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = ProgramAudio(_audio)

        is_movie = d.pop("IsMovie", UNSET)

        is_sports = d.pop("IsSports", UNSET)

        is_series = d.pop("IsSeries", UNSET)

        is_live = d.pop("IsLive", UNSET)

        is_news = d.pop("IsNews", UNSET)

        is_kids = d.pop("IsKids", UNSET)

        is_premiere = d.pop("IsPremiere", UNSET)

        timer_id = d.pop("TimerId", UNSET)

        _current_program = d.pop("CurrentProgram", UNSET)
        current_program: Union[Unset, None, BaseItemDto]
        if _current_program is None:
            current_program = None
        elif isinstance(_current_program, Unset):
            current_program = UNSET
        else:
            current_program = BaseItemDto.from_dict(_current_program)

        base_item_dto = cls(
            name=name,
            original_title=original_title,
            server_id=server_id,
            id=id,
            etag=etag,
            source_type=source_type,
            playlist_item_id=playlist_item_id,
            date_created=date_created,
            date_last_media_added=date_last_media_added,
            extra_type=extra_type,
            airs_before_season_number=airs_before_season_number,
            airs_after_season_number=airs_after_season_number,
            airs_before_episode_number=airs_before_episode_number,
            can_delete=can_delete,
            can_download=can_download,
            has_subtitles=has_subtitles,
            preferred_metadata_language=preferred_metadata_language,
            preferred_metadata_country_code=preferred_metadata_country_code,
            supports_sync=supports_sync,
            container=container,
            sort_name=sort_name,
            forced_sort_name=forced_sort_name,
            video_3d_format=video_3d_format,
            premiere_date=premiere_date,
            external_urls=external_urls,
            media_sources=media_sources,
            critic_rating=critic_rating,
            production_locations=production_locations,
            path=path,
            enable_media_source_display=enable_media_source_display,
            official_rating=official_rating,
            custom_rating=custom_rating,
            channel_id=channel_id,
            channel_name=channel_name,
            overview=overview,
            taglines=taglines,
            genres=genres,
            community_rating=community_rating,
            cumulative_run_time_ticks=cumulative_run_time_ticks,
            run_time_ticks=run_time_ticks,
            play_access=play_access,
            aspect_ratio=aspect_ratio,
            production_year=production_year,
            is_place_holder=is_place_holder,
            number=number,
            channel_number=channel_number,
            index_number=index_number,
            index_number_end=index_number_end,
            parent_index_number=parent_index_number,
            remote_trailers=remote_trailers,
            provider_ids=provider_ids,
            is_hd=is_hd,
            is_folder=is_folder,
            parent_id=parent_id,
            type=type,
            people=people,
            studios=studios,
            genre_items=genre_items,
            parent_logo_item_id=parent_logo_item_id,
            parent_backdrop_item_id=parent_backdrop_item_id,
            parent_backdrop_image_tags=parent_backdrop_image_tags,
            local_trailer_count=local_trailer_count,
            user_data=user_data,
            recursive_item_count=recursive_item_count,
            child_count=child_count,
            series_name=series_name,
            series_id=series_id,
            season_id=season_id,
            special_feature_count=special_feature_count,
            display_preferences_id=display_preferences_id,
            status=status,
            air_time=air_time,
            air_days=air_days,
            tags=tags,
            primary_image_aspect_ratio=primary_image_aspect_ratio,
            artists=artists,
            artist_items=artist_items,
            album=album,
            collection_type=collection_type,
            display_order=display_order,
            album_id=album_id,
            album_primary_image_tag=album_primary_image_tag,
            series_primary_image_tag=series_primary_image_tag,
            album_artist=album_artist,
            album_artists=album_artists,
            season_name=season_name,
            media_streams=media_streams,
            video_type=video_type,
            part_count=part_count,
            media_source_count=media_source_count,
            image_tags=image_tags,
            backdrop_image_tags=backdrop_image_tags,
            screenshot_image_tags=screenshot_image_tags,
            parent_logo_image_tag=parent_logo_image_tag,
            parent_art_item_id=parent_art_item_id,
            parent_art_image_tag=parent_art_image_tag,
            series_thumb_image_tag=series_thumb_image_tag,
            image_blur_hashes=image_blur_hashes,
            series_studio=series_studio,
            parent_thumb_item_id=parent_thumb_item_id,
            parent_thumb_image_tag=parent_thumb_image_tag,
            parent_primary_image_item_id=parent_primary_image_item_id,
            parent_primary_image_tag=parent_primary_image_tag,
            chapters=chapters,
            location_type=location_type,
            iso_type=iso_type,
            media_type=media_type,
            end_date=end_date,
            locked_fields=locked_fields,
            trailer_count=trailer_count,
            movie_count=movie_count,
            series_count=series_count,
            program_count=program_count,
            episode_count=episode_count,
            song_count=song_count,
            album_count=album_count,
            artist_count=artist_count,
            music_video_count=music_video_count,
            lock_data=lock_data,
            width=width,
            height=height,
            camera_make=camera_make,
            camera_model=camera_model,
            software=software,
            exposure_time=exposure_time,
            focal_length=focal_length,
            image_orientation=image_orientation,
            aperture=aperture,
            shutter_speed=shutter_speed,
            latitude=latitude,
            longitude=longitude,
            altitude=altitude,
            iso_speed_rating=iso_speed_rating,
            series_timer_id=series_timer_id,
            program_id=program_id,
            channel_primary_image_tag=channel_primary_image_tag,
            start_date=start_date,
            completion_percentage=completion_percentage,
            is_repeat=is_repeat,
            episode_title=episode_title,
            channel_type=channel_type,
            audio=audio,
            is_movie=is_movie,
            is_sports=is_sports,
            is_series=is_series,
            is_live=is_live,
            is_news=is_news,
            is_kids=is_kids,
            is_premiere=is_premiere,
            timer_id=timer_id,
            current_program=current_program,
        )

        return base_item_dto
