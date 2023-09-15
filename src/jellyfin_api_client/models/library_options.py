from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.embedded_subtitle_options import EmbeddedSubtitleOptions
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_path_info import MediaPathInfo
    from ..models.type_options import TypeOptions


T = TypeVar("T", bound="LibraryOptions")


@_attrs_define
class LibraryOptions:
    """
    Attributes:
        enable_photos (Union[Unset, bool]):
        enable_realtime_monitor (Union[Unset, bool]):
        enable_chapter_image_extraction (Union[Unset, bool]):
        extract_chapter_images_during_library_scan (Union[Unset, bool]):
        path_infos (Union[Unset, List['MediaPathInfo']]):
        save_local_metadata (Union[Unset, bool]):
        enable_internet_providers (Union[Unset, bool]):
        enable_automatic_series_grouping (Union[Unset, bool]):
        enable_embedded_titles (Union[Unset, bool]):
        enable_embedded_episode_infos (Union[Unset, bool]):
        automatic_refresh_interval_days (Union[Unset, int]):
        preferred_metadata_language (Union[Unset, None, str]): Gets or sets the preferred metadata language.
        metadata_country_code (Union[Unset, None, str]): Gets or sets the metadata country code.
        season_zero_display_name (Union[Unset, str]):
        metadata_savers (Union[Unset, None, List[str]]):
        disabled_local_metadata_readers (Union[Unset, List[str]]):
        local_metadata_reader_order (Union[Unset, None, List[str]]):
        disabled_subtitle_fetchers (Union[Unset, List[str]]):
        subtitle_fetcher_order (Union[Unset, List[str]]):
        skip_subtitles_if_embedded_subtitles_present (Union[Unset, bool]):
        skip_subtitles_if_audio_track_matches (Union[Unset, bool]):
        subtitle_download_languages (Union[Unset, None, List[str]]):
        require_perfect_subtitle_match (Union[Unset, bool]):
        save_subtitles_with_media (Union[Unset, bool]):
        automatically_add_to_collection (Union[Unset, bool]):
        allow_embedded_subtitles (Union[Unset, EmbeddedSubtitleOptions]): An enum representing the options to disable
            embedded subs.
        type_options (Union[Unset, List['TypeOptions']]):
    """

    enable_photos: Union[Unset, bool] = UNSET
    enable_realtime_monitor: Union[Unset, bool] = UNSET
    enable_chapter_image_extraction: Union[Unset, bool] = UNSET
    extract_chapter_images_during_library_scan: Union[Unset, bool] = UNSET
    path_infos: Union[Unset, List["MediaPathInfo"]] = UNSET
    save_local_metadata: Union[Unset, bool] = UNSET
    enable_internet_providers: Union[Unset, bool] = UNSET
    enable_automatic_series_grouping: Union[Unset, bool] = UNSET
    enable_embedded_titles: Union[Unset, bool] = UNSET
    enable_embedded_episode_infos: Union[Unset, bool] = UNSET
    automatic_refresh_interval_days: Union[Unset, int] = UNSET
    preferred_metadata_language: Union[Unset, None, str] = UNSET
    metadata_country_code: Union[Unset, None, str] = UNSET
    season_zero_display_name: Union[Unset, str] = UNSET
    metadata_savers: Union[Unset, None, List[str]] = UNSET
    disabled_local_metadata_readers: Union[Unset, List[str]] = UNSET
    local_metadata_reader_order: Union[Unset, None, List[str]] = UNSET
    disabled_subtitle_fetchers: Union[Unset, List[str]] = UNSET
    subtitle_fetcher_order: Union[Unset, List[str]] = UNSET
    skip_subtitles_if_embedded_subtitles_present: Union[Unset, bool] = UNSET
    skip_subtitles_if_audio_track_matches: Union[Unset, bool] = UNSET
    subtitle_download_languages: Union[Unset, None, List[str]] = UNSET
    require_perfect_subtitle_match: Union[Unset, bool] = UNSET
    save_subtitles_with_media: Union[Unset, bool] = UNSET
    automatically_add_to_collection: Union[Unset, bool] = UNSET
    allow_embedded_subtitles: Union[Unset, EmbeddedSubtitleOptions] = UNSET
    type_options: Union[Unset, List["TypeOptions"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enable_photos = self.enable_photos
        enable_realtime_monitor = self.enable_realtime_monitor
        enable_chapter_image_extraction = self.enable_chapter_image_extraction
        extract_chapter_images_during_library_scan = self.extract_chapter_images_during_library_scan
        path_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.path_infos, Unset):
            path_infos = []
            for path_infos_item_data in self.path_infos:
                path_infos_item = path_infos_item_data.to_dict()

                path_infos.append(path_infos_item)

        save_local_metadata = self.save_local_metadata
        enable_internet_providers = self.enable_internet_providers
        enable_automatic_series_grouping = self.enable_automatic_series_grouping
        enable_embedded_titles = self.enable_embedded_titles
        enable_embedded_episode_infos = self.enable_embedded_episode_infos
        automatic_refresh_interval_days = self.automatic_refresh_interval_days
        preferred_metadata_language = self.preferred_metadata_language
        metadata_country_code = self.metadata_country_code
        season_zero_display_name = self.season_zero_display_name
        metadata_savers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.metadata_savers, Unset):
            if self.metadata_savers is None:
                metadata_savers = None
            else:
                metadata_savers = self.metadata_savers

        disabled_local_metadata_readers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disabled_local_metadata_readers, Unset):
            disabled_local_metadata_readers = self.disabled_local_metadata_readers

        local_metadata_reader_order: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.local_metadata_reader_order, Unset):
            if self.local_metadata_reader_order is None:
                local_metadata_reader_order = None
            else:
                local_metadata_reader_order = self.local_metadata_reader_order

        disabled_subtitle_fetchers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disabled_subtitle_fetchers, Unset):
            disabled_subtitle_fetchers = self.disabled_subtitle_fetchers

        subtitle_fetcher_order: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subtitle_fetcher_order, Unset):
            subtitle_fetcher_order = self.subtitle_fetcher_order

        skip_subtitles_if_embedded_subtitles_present = self.skip_subtitles_if_embedded_subtitles_present
        skip_subtitles_if_audio_track_matches = self.skip_subtitles_if_audio_track_matches
        subtitle_download_languages: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.subtitle_download_languages, Unset):
            if self.subtitle_download_languages is None:
                subtitle_download_languages = None
            else:
                subtitle_download_languages = self.subtitle_download_languages

        require_perfect_subtitle_match = self.require_perfect_subtitle_match
        save_subtitles_with_media = self.save_subtitles_with_media
        automatically_add_to_collection = self.automatically_add_to_collection
        allow_embedded_subtitles: Union[Unset, str] = UNSET
        if not isinstance(self.allow_embedded_subtitles, Unset):
            allow_embedded_subtitles = self.allow_embedded_subtitles.value

        type_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.type_options, Unset):
            type_options = []
            for type_options_item_data in self.type_options:
                type_options_item = type_options_item_data.to_dict()

                type_options.append(type_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enable_photos is not UNSET:
            field_dict["EnablePhotos"] = enable_photos
        if enable_realtime_monitor is not UNSET:
            field_dict["EnableRealtimeMonitor"] = enable_realtime_monitor
        if enable_chapter_image_extraction is not UNSET:
            field_dict["EnableChapterImageExtraction"] = enable_chapter_image_extraction
        if extract_chapter_images_during_library_scan is not UNSET:
            field_dict["ExtractChapterImagesDuringLibraryScan"] = extract_chapter_images_during_library_scan
        if path_infos is not UNSET:
            field_dict["PathInfos"] = path_infos
        if save_local_metadata is not UNSET:
            field_dict["SaveLocalMetadata"] = save_local_metadata
        if enable_internet_providers is not UNSET:
            field_dict["EnableInternetProviders"] = enable_internet_providers
        if enable_automatic_series_grouping is not UNSET:
            field_dict["EnableAutomaticSeriesGrouping"] = enable_automatic_series_grouping
        if enable_embedded_titles is not UNSET:
            field_dict["EnableEmbeddedTitles"] = enable_embedded_titles
        if enable_embedded_episode_infos is not UNSET:
            field_dict["EnableEmbeddedEpisodeInfos"] = enable_embedded_episode_infos
        if automatic_refresh_interval_days is not UNSET:
            field_dict["AutomaticRefreshIntervalDays"] = automatic_refresh_interval_days
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if season_zero_display_name is not UNSET:
            field_dict["SeasonZeroDisplayName"] = season_zero_display_name
        if metadata_savers is not UNSET:
            field_dict["MetadataSavers"] = metadata_savers
        if disabled_local_metadata_readers is not UNSET:
            field_dict["DisabledLocalMetadataReaders"] = disabled_local_metadata_readers
        if local_metadata_reader_order is not UNSET:
            field_dict["LocalMetadataReaderOrder"] = local_metadata_reader_order
        if disabled_subtitle_fetchers is not UNSET:
            field_dict["DisabledSubtitleFetchers"] = disabled_subtitle_fetchers
        if subtitle_fetcher_order is not UNSET:
            field_dict["SubtitleFetcherOrder"] = subtitle_fetcher_order
        if skip_subtitles_if_embedded_subtitles_present is not UNSET:
            field_dict["SkipSubtitlesIfEmbeddedSubtitlesPresent"] = skip_subtitles_if_embedded_subtitles_present
        if skip_subtitles_if_audio_track_matches is not UNSET:
            field_dict["SkipSubtitlesIfAudioTrackMatches"] = skip_subtitles_if_audio_track_matches
        if subtitle_download_languages is not UNSET:
            field_dict["SubtitleDownloadLanguages"] = subtitle_download_languages
        if require_perfect_subtitle_match is not UNSET:
            field_dict["RequirePerfectSubtitleMatch"] = require_perfect_subtitle_match
        if save_subtitles_with_media is not UNSET:
            field_dict["SaveSubtitlesWithMedia"] = save_subtitles_with_media
        if automatically_add_to_collection is not UNSET:
            field_dict["AutomaticallyAddToCollection"] = automatically_add_to_collection
        if allow_embedded_subtitles is not UNSET:
            field_dict["AllowEmbeddedSubtitles"] = allow_embedded_subtitles
        if type_options is not UNSET:
            field_dict["TypeOptions"] = type_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_path_info import MediaPathInfo
        from ..models.type_options import TypeOptions

        d = src_dict.copy()
        enable_photos = d.pop("EnablePhotos", UNSET)

        enable_realtime_monitor = d.pop("EnableRealtimeMonitor", UNSET)

        enable_chapter_image_extraction = d.pop("EnableChapterImageExtraction", UNSET)

        extract_chapter_images_during_library_scan = d.pop("ExtractChapterImagesDuringLibraryScan", UNSET)

        path_infos = []
        _path_infos = d.pop("PathInfos", UNSET)
        for path_infos_item_data in _path_infos or []:
            path_infos_item = MediaPathInfo.from_dict(path_infos_item_data)

            path_infos.append(path_infos_item)

        save_local_metadata = d.pop("SaveLocalMetadata", UNSET)

        enable_internet_providers = d.pop("EnableInternetProviders", UNSET)

        enable_automatic_series_grouping = d.pop("EnableAutomaticSeriesGrouping", UNSET)

        enable_embedded_titles = d.pop("EnableEmbeddedTitles", UNSET)

        enable_embedded_episode_infos = d.pop("EnableEmbeddedEpisodeInfos", UNSET)

        automatic_refresh_interval_days = d.pop("AutomaticRefreshIntervalDays", UNSET)

        preferred_metadata_language = d.pop("PreferredMetadataLanguage", UNSET)

        metadata_country_code = d.pop("MetadataCountryCode", UNSET)

        season_zero_display_name = d.pop("SeasonZeroDisplayName", UNSET)

        metadata_savers = cast(List[str], d.pop("MetadataSavers", UNSET))

        disabled_local_metadata_readers = cast(List[str], d.pop("DisabledLocalMetadataReaders", UNSET))

        local_metadata_reader_order = cast(List[str], d.pop("LocalMetadataReaderOrder", UNSET))

        disabled_subtitle_fetchers = cast(List[str], d.pop("DisabledSubtitleFetchers", UNSET))

        subtitle_fetcher_order = cast(List[str], d.pop("SubtitleFetcherOrder", UNSET))

        skip_subtitles_if_embedded_subtitles_present = d.pop("SkipSubtitlesIfEmbeddedSubtitlesPresent", UNSET)

        skip_subtitles_if_audio_track_matches = d.pop("SkipSubtitlesIfAudioTrackMatches", UNSET)

        subtitle_download_languages = cast(List[str], d.pop("SubtitleDownloadLanguages", UNSET))

        require_perfect_subtitle_match = d.pop("RequirePerfectSubtitleMatch", UNSET)

        save_subtitles_with_media = d.pop("SaveSubtitlesWithMedia", UNSET)

        automatically_add_to_collection = d.pop("AutomaticallyAddToCollection", UNSET)

        _allow_embedded_subtitles = d.pop("AllowEmbeddedSubtitles", UNSET)
        allow_embedded_subtitles: Union[Unset, EmbeddedSubtitleOptions]
        if isinstance(_allow_embedded_subtitles, Unset):
            allow_embedded_subtitles = UNSET
        else:
            allow_embedded_subtitles = EmbeddedSubtitleOptions(_allow_embedded_subtitles)

        type_options = []
        _type_options = d.pop("TypeOptions", UNSET)
        for type_options_item_data in _type_options or []:
            type_options_item = TypeOptions.from_dict(type_options_item_data)

            type_options.append(type_options_item)

        library_options = cls(
            enable_photos=enable_photos,
            enable_realtime_monitor=enable_realtime_monitor,
            enable_chapter_image_extraction=enable_chapter_image_extraction,
            extract_chapter_images_during_library_scan=extract_chapter_images_during_library_scan,
            path_infos=path_infos,
            save_local_metadata=save_local_metadata,
            enable_internet_providers=enable_internet_providers,
            enable_automatic_series_grouping=enable_automatic_series_grouping,
            enable_embedded_titles=enable_embedded_titles,
            enable_embedded_episode_infos=enable_embedded_episode_infos,
            automatic_refresh_interval_days=automatic_refresh_interval_days,
            preferred_metadata_language=preferred_metadata_language,
            metadata_country_code=metadata_country_code,
            season_zero_display_name=season_zero_display_name,
            metadata_savers=metadata_savers,
            disabled_local_metadata_readers=disabled_local_metadata_readers,
            local_metadata_reader_order=local_metadata_reader_order,
            disabled_subtitle_fetchers=disabled_subtitle_fetchers,
            subtitle_fetcher_order=subtitle_fetcher_order,
            skip_subtitles_if_embedded_subtitles_present=skip_subtitles_if_embedded_subtitles_present,
            skip_subtitles_if_audio_track_matches=skip_subtitles_if_audio_track_matches,
            subtitle_download_languages=subtitle_download_languages,
            require_perfect_subtitle_match=require_perfect_subtitle_match,
            save_subtitles_with_media=save_subtitles_with_media,
            automatically_add_to_collection=automatically_add_to_collection,
            allow_embedded_subtitles=allow_embedded_subtitles,
            type_options=type_options,
        )

        return library_options
