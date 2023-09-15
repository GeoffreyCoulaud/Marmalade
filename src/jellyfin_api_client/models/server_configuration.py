from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.image_saving_convention import ImageSavingConvention
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_options import MetadataOptions
    from ..models.name_value_pair import NameValuePair
    from ..models.path_substitution import PathSubstitution
    from ..models.repository_info import RepositoryInfo


T = TypeVar("T", bound="ServerConfiguration")


@_attrs_define
class ServerConfiguration:
    """Represents the server configuration.

    Attributes:
        log_file_retention_days (Union[Unset, int]): Gets or sets the number of days we should retain log files.
        is_startup_wizard_completed (Union[Unset, bool]): Gets or sets a value indicating whether this instance is first
            run.
        cache_path (Union[Unset, None, str]): Gets or sets the cache path.
        previous_version (Union[Unset, None, str]): Gets or sets the last known version that was ran using the
            configuration.
        previous_version_str (Union[Unset, None, str]): Gets or sets the stringified PreviousVersion to be
            stored/loaded,
            because System.Version itself isn't xml-serializable.
        enable_metrics (Union[Unset, bool]): Gets or sets a value indicating whether to enable prometheus metrics
            exporting.
        enable_normalized_item_by_name_ids (Union[Unset, bool]):
        is_port_authorized (Union[Unset, bool]): Gets or sets a value indicating whether this instance is port
            authorized.
        quick_connect_available (Union[Unset, bool]): Gets or sets a value indicating whether quick connect is available
            for use on this server.
        enable_case_sensitive_item_ids (Union[Unset, bool]): Gets or sets a value indicating whether [enable case
            sensitive item ids].
        disable_live_tv_channel_user_data_name (Union[Unset, bool]):
        metadata_path (Union[Unset, str]): Gets or sets the metadata path.
        metadata_network_path (Union[Unset, str]):
        preferred_metadata_language (Union[Unset, str]): Gets or sets the preferred metadata language.
        metadata_country_code (Union[Unset, str]): Gets or sets the metadata country code.
        sort_replace_characters (Union[Unset, List[str]]): Gets or sets characters to be replaced with a ' ' in strings
            to create a sort name.
        sort_remove_characters (Union[Unset, List[str]]): Gets or sets characters to be removed from strings to create a
            sort name.
        sort_remove_words (Union[Unset, List[str]]): Gets or sets words to be removed from strings to create a sort
            name.
        min_resume_pct (Union[Unset, int]): Gets or sets the minimum percentage of an item that must be played in order
            for playstate to be updated.
        max_resume_pct (Union[Unset, int]): Gets or sets the maximum percentage of an item that can be played while
            still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will
            be marked watched.
        min_resume_duration_seconds (Union[Unset, int]): Gets or sets the minimum duration that an item must have in
            order to be eligible for playstate updates..
        min_audiobook_resume (Union[Unset, int]): Gets or sets the minimum minutes of a book that must be played in
            order for playstate to be updated.
        max_audiobook_resume (Union[Unset, int]): Gets or sets the remaining minutes of a book that can be played while
            still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will
            be marked watched.
        library_monitor_delay (Union[Unset, int]): Gets or sets the delay in seconds that we will wait after a file
            system change to try and discover what has been added/removed
            Some delay is necessary with some items because their creation is not atomic.  It involves the creation of
            several
            different directories and files.
        image_saving_convention (Union[Unset, ImageSavingConvention]):
        metadata_options (Union[Unset, List['MetadataOptions']]):
        skip_deserialization_for_basic_types (Union[Unset, bool]):
        server_name (Union[Unset, str]):
        ui_culture (Union[Unset, str]):
        save_metadata_hidden (Union[Unset, bool]):
        content_types (Union[Unset, List['NameValuePair']]):
        remote_client_bitrate_limit (Union[Unset, int]):
        enable_folder_view (Union[Unset, bool]):
        enable_grouping_into_collections (Union[Unset, bool]):
        display_specials_within_seasons (Union[Unset, bool]):
        codecs_used (Union[Unset, List[str]]):
        plugin_repositories (Union[Unset, List['RepositoryInfo']]):
        enable_external_content_in_suggestions (Union[Unset, bool]):
        image_extraction_timeout_ms (Union[Unset, int]):
        path_substitutions (Union[Unset, List['PathSubstitution']]):
        enable_slow_response_warning (Union[Unset, bool]): Gets or sets a value indicating whether slow server responses
            should be logged as a warning.
        slow_response_threshold_ms (Union[Unset, int]): Gets or sets the threshold for the slow response time warning in
            ms.
        cors_hosts (Union[Unset, List[str]]): Gets or sets the cors hosts.
        activity_log_retention_days (Union[Unset, None, int]): Gets or sets the number of days we should retain activity
            logs.
        library_scan_fanout_concurrency (Union[Unset, int]): Gets or sets the how the library scan fans out.
        library_metadata_refresh_concurrency (Union[Unset, int]): Gets or sets the how many metadata refreshes can run
            concurrently.
        remove_old_plugins (Union[Unset, bool]): Gets or sets a value indicating whether older plugins should
            automatically be deleted from the plugin folder.
        allow_client_log_upload (Union[Unset, bool]): Gets or sets a value indicating whether clients should be allowed
            to upload logs.
    """

    log_file_retention_days: Union[Unset, int] = UNSET
    is_startup_wizard_completed: Union[Unset, bool] = UNSET
    cache_path: Union[Unset, None, str] = UNSET
    previous_version: Union[Unset, None, str] = UNSET
    previous_version_str: Union[Unset, None, str] = UNSET
    enable_metrics: Union[Unset, bool] = UNSET
    enable_normalized_item_by_name_ids: Union[Unset, bool] = UNSET
    is_port_authorized: Union[Unset, bool] = UNSET
    quick_connect_available: Union[Unset, bool] = UNSET
    enable_case_sensitive_item_ids: Union[Unset, bool] = UNSET
    disable_live_tv_channel_user_data_name: Union[Unset, bool] = UNSET
    metadata_path: Union[Unset, str] = UNSET
    metadata_network_path: Union[Unset, str] = UNSET
    preferred_metadata_language: Union[Unset, str] = UNSET
    metadata_country_code: Union[Unset, str] = UNSET
    sort_replace_characters: Union[Unset, List[str]] = UNSET
    sort_remove_characters: Union[Unset, List[str]] = UNSET
    sort_remove_words: Union[Unset, List[str]] = UNSET
    min_resume_pct: Union[Unset, int] = UNSET
    max_resume_pct: Union[Unset, int] = UNSET
    min_resume_duration_seconds: Union[Unset, int] = UNSET
    min_audiobook_resume: Union[Unset, int] = UNSET
    max_audiobook_resume: Union[Unset, int] = UNSET
    library_monitor_delay: Union[Unset, int] = UNSET
    image_saving_convention: Union[Unset, ImageSavingConvention] = UNSET
    metadata_options: Union[Unset, List["MetadataOptions"]] = UNSET
    skip_deserialization_for_basic_types: Union[Unset, bool] = UNSET
    server_name: Union[Unset, str] = UNSET
    ui_culture: Union[Unset, str] = UNSET
    save_metadata_hidden: Union[Unset, bool] = UNSET
    content_types: Union[Unset, List["NameValuePair"]] = UNSET
    remote_client_bitrate_limit: Union[Unset, int] = UNSET
    enable_folder_view: Union[Unset, bool] = UNSET
    enable_grouping_into_collections: Union[Unset, bool] = UNSET
    display_specials_within_seasons: Union[Unset, bool] = UNSET
    codecs_used: Union[Unset, List[str]] = UNSET
    plugin_repositories: Union[Unset, List["RepositoryInfo"]] = UNSET
    enable_external_content_in_suggestions: Union[Unset, bool] = UNSET
    image_extraction_timeout_ms: Union[Unset, int] = UNSET
    path_substitutions: Union[Unset, List["PathSubstitution"]] = UNSET
    enable_slow_response_warning: Union[Unset, bool] = UNSET
    slow_response_threshold_ms: Union[Unset, int] = UNSET
    cors_hosts: Union[Unset, List[str]] = UNSET
    activity_log_retention_days: Union[Unset, None, int] = UNSET
    library_scan_fanout_concurrency: Union[Unset, int] = UNSET
    library_metadata_refresh_concurrency: Union[Unset, int] = UNSET
    remove_old_plugins: Union[Unset, bool] = UNSET
    allow_client_log_upload: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        log_file_retention_days = self.log_file_retention_days
        is_startup_wizard_completed = self.is_startup_wizard_completed
        cache_path = self.cache_path
        previous_version = self.previous_version
        previous_version_str = self.previous_version_str
        enable_metrics = self.enable_metrics
        enable_normalized_item_by_name_ids = self.enable_normalized_item_by_name_ids
        is_port_authorized = self.is_port_authorized
        quick_connect_available = self.quick_connect_available
        enable_case_sensitive_item_ids = self.enable_case_sensitive_item_ids
        disable_live_tv_channel_user_data_name = self.disable_live_tv_channel_user_data_name
        metadata_path = self.metadata_path
        metadata_network_path = self.metadata_network_path
        preferred_metadata_language = self.preferred_metadata_language
        metadata_country_code = self.metadata_country_code
        sort_replace_characters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_replace_characters, Unset):
            sort_replace_characters = self.sort_replace_characters

        sort_remove_characters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_remove_characters, Unset):
            sort_remove_characters = self.sort_remove_characters

        sort_remove_words: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_remove_words, Unset):
            sort_remove_words = self.sort_remove_words

        min_resume_pct = self.min_resume_pct
        max_resume_pct = self.max_resume_pct
        min_resume_duration_seconds = self.min_resume_duration_seconds
        min_audiobook_resume = self.min_audiobook_resume
        max_audiobook_resume = self.max_audiobook_resume
        library_monitor_delay = self.library_monitor_delay
        image_saving_convention: Union[Unset, str] = UNSET
        if not isinstance(self.image_saving_convention, Unset):
            image_saving_convention = self.image_saving_convention.value

        metadata_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_options, Unset):
            metadata_options = []
            for metadata_options_item_data in self.metadata_options:
                metadata_options_item = metadata_options_item_data.to_dict()

                metadata_options.append(metadata_options_item)

        skip_deserialization_for_basic_types = self.skip_deserialization_for_basic_types
        server_name = self.server_name
        ui_culture = self.ui_culture
        save_metadata_hidden = self.save_metadata_hidden
        content_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.content_types, Unset):
            content_types = []
            for content_types_item_data in self.content_types:
                content_types_item = content_types_item_data.to_dict()

                content_types.append(content_types_item)

        remote_client_bitrate_limit = self.remote_client_bitrate_limit
        enable_folder_view = self.enable_folder_view
        enable_grouping_into_collections = self.enable_grouping_into_collections
        display_specials_within_seasons = self.display_specials_within_seasons
        codecs_used: Union[Unset, List[str]] = UNSET
        if not isinstance(self.codecs_used, Unset):
            codecs_used = self.codecs_used

        plugin_repositories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.plugin_repositories, Unset):
            plugin_repositories = []
            for plugin_repositories_item_data in self.plugin_repositories:
                plugin_repositories_item = plugin_repositories_item_data.to_dict()

                plugin_repositories.append(plugin_repositories_item)

        enable_external_content_in_suggestions = self.enable_external_content_in_suggestions
        image_extraction_timeout_ms = self.image_extraction_timeout_ms
        path_substitutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.path_substitutions, Unset):
            path_substitutions = []
            for path_substitutions_item_data in self.path_substitutions:
                path_substitutions_item = path_substitutions_item_data.to_dict()

                path_substitutions.append(path_substitutions_item)

        enable_slow_response_warning = self.enable_slow_response_warning
        slow_response_threshold_ms = self.slow_response_threshold_ms
        cors_hosts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cors_hosts, Unset):
            cors_hosts = self.cors_hosts

        activity_log_retention_days = self.activity_log_retention_days
        library_scan_fanout_concurrency = self.library_scan_fanout_concurrency
        library_metadata_refresh_concurrency = self.library_metadata_refresh_concurrency
        remove_old_plugins = self.remove_old_plugins
        allow_client_log_upload = self.allow_client_log_upload

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if log_file_retention_days is not UNSET:
            field_dict["LogFileRetentionDays"] = log_file_retention_days
        if is_startup_wizard_completed is not UNSET:
            field_dict["IsStartupWizardCompleted"] = is_startup_wizard_completed
        if cache_path is not UNSET:
            field_dict["CachePath"] = cache_path
        if previous_version is not UNSET:
            field_dict["PreviousVersion"] = previous_version
        if previous_version_str is not UNSET:
            field_dict["PreviousVersionStr"] = previous_version_str
        if enable_metrics is not UNSET:
            field_dict["EnableMetrics"] = enable_metrics
        if enable_normalized_item_by_name_ids is not UNSET:
            field_dict["EnableNormalizedItemByNameIds"] = enable_normalized_item_by_name_ids
        if is_port_authorized is not UNSET:
            field_dict["IsPortAuthorized"] = is_port_authorized
        if quick_connect_available is not UNSET:
            field_dict["QuickConnectAvailable"] = quick_connect_available
        if enable_case_sensitive_item_ids is not UNSET:
            field_dict["EnableCaseSensitiveItemIds"] = enable_case_sensitive_item_ids
        if disable_live_tv_channel_user_data_name is not UNSET:
            field_dict["DisableLiveTvChannelUserDataName"] = disable_live_tv_channel_user_data_name
        if metadata_path is not UNSET:
            field_dict["MetadataPath"] = metadata_path
        if metadata_network_path is not UNSET:
            field_dict["MetadataNetworkPath"] = metadata_network_path
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if sort_replace_characters is not UNSET:
            field_dict["SortReplaceCharacters"] = sort_replace_characters
        if sort_remove_characters is not UNSET:
            field_dict["SortRemoveCharacters"] = sort_remove_characters
        if sort_remove_words is not UNSET:
            field_dict["SortRemoveWords"] = sort_remove_words
        if min_resume_pct is not UNSET:
            field_dict["MinResumePct"] = min_resume_pct
        if max_resume_pct is not UNSET:
            field_dict["MaxResumePct"] = max_resume_pct
        if min_resume_duration_seconds is not UNSET:
            field_dict["MinResumeDurationSeconds"] = min_resume_duration_seconds
        if min_audiobook_resume is not UNSET:
            field_dict["MinAudiobookResume"] = min_audiobook_resume
        if max_audiobook_resume is not UNSET:
            field_dict["MaxAudiobookResume"] = max_audiobook_resume
        if library_monitor_delay is not UNSET:
            field_dict["LibraryMonitorDelay"] = library_monitor_delay
        if image_saving_convention is not UNSET:
            field_dict["ImageSavingConvention"] = image_saving_convention
        if metadata_options is not UNSET:
            field_dict["MetadataOptions"] = metadata_options
        if skip_deserialization_for_basic_types is not UNSET:
            field_dict["SkipDeserializationForBasicTypes"] = skip_deserialization_for_basic_types
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if ui_culture is not UNSET:
            field_dict["UICulture"] = ui_culture
        if save_metadata_hidden is not UNSET:
            field_dict["SaveMetadataHidden"] = save_metadata_hidden
        if content_types is not UNSET:
            field_dict["ContentTypes"] = content_types
        if remote_client_bitrate_limit is not UNSET:
            field_dict["RemoteClientBitrateLimit"] = remote_client_bitrate_limit
        if enable_folder_view is not UNSET:
            field_dict["EnableFolderView"] = enable_folder_view
        if enable_grouping_into_collections is not UNSET:
            field_dict["EnableGroupingIntoCollections"] = enable_grouping_into_collections
        if display_specials_within_seasons is not UNSET:
            field_dict["DisplaySpecialsWithinSeasons"] = display_specials_within_seasons
        if codecs_used is not UNSET:
            field_dict["CodecsUsed"] = codecs_used
        if plugin_repositories is not UNSET:
            field_dict["PluginRepositories"] = plugin_repositories
        if enable_external_content_in_suggestions is not UNSET:
            field_dict["EnableExternalContentInSuggestions"] = enable_external_content_in_suggestions
        if image_extraction_timeout_ms is not UNSET:
            field_dict["ImageExtractionTimeoutMs"] = image_extraction_timeout_ms
        if path_substitutions is not UNSET:
            field_dict["PathSubstitutions"] = path_substitutions
        if enable_slow_response_warning is not UNSET:
            field_dict["EnableSlowResponseWarning"] = enable_slow_response_warning
        if slow_response_threshold_ms is not UNSET:
            field_dict["SlowResponseThresholdMs"] = slow_response_threshold_ms
        if cors_hosts is not UNSET:
            field_dict["CorsHosts"] = cors_hosts
        if activity_log_retention_days is not UNSET:
            field_dict["ActivityLogRetentionDays"] = activity_log_retention_days
        if library_scan_fanout_concurrency is not UNSET:
            field_dict["LibraryScanFanoutConcurrency"] = library_scan_fanout_concurrency
        if library_metadata_refresh_concurrency is not UNSET:
            field_dict["LibraryMetadataRefreshConcurrency"] = library_metadata_refresh_concurrency
        if remove_old_plugins is not UNSET:
            field_dict["RemoveOldPlugins"] = remove_old_plugins
        if allow_client_log_upload is not UNSET:
            field_dict["AllowClientLogUpload"] = allow_client_log_upload

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metadata_options import MetadataOptions
        from ..models.name_value_pair import NameValuePair
        from ..models.path_substitution import PathSubstitution
        from ..models.repository_info import RepositoryInfo

        d = src_dict.copy()
        log_file_retention_days = d.pop("LogFileRetentionDays", UNSET)

        is_startup_wizard_completed = d.pop("IsStartupWizardCompleted", UNSET)

        cache_path = d.pop("CachePath", UNSET)

        previous_version = d.pop("PreviousVersion", UNSET)

        previous_version_str = d.pop("PreviousVersionStr", UNSET)

        enable_metrics = d.pop("EnableMetrics", UNSET)

        enable_normalized_item_by_name_ids = d.pop("EnableNormalizedItemByNameIds", UNSET)

        is_port_authorized = d.pop("IsPortAuthorized", UNSET)

        quick_connect_available = d.pop("QuickConnectAvailable", UNSET)

        enable_case_sensitive_item_ids = d.pop("EnableCaseSensitiveItemIds", UNSET)

        disable_live_tv_channel_user_data_name = d.pop("DisableLiveTvChannelUserDataName", UNSET)

        metadata_path = d.pop("MetadataPath", UNSET)

        metadata_network_path = d.pop("MetadataNetworkPath", UNSET)

        preferred_metadata_language = d.pop("PreferredMetadataLanguage", UNSET)

        metadata_country_code = d.pop("MetadataCountryCode", UNSET)

        sort_replace_characters = cast(List[str], d.pop("SortReplaceCharacters", UNSET))

        sort_remove_characters = cast(List[str], d.pop("SortRemoveCharacters", UNSET))

        sort_remove_words = cast(List[str], d.pop("SortRemoveWords", UNSET))

        min_resume_pct = d.pop("MinResumePct", UNSET)

        max_resume_pct = d.pop("MaxResumePct", UNSET)

        min_resume_duration_seconds = d.pop("MinResumeDurationSeconds", UNSET)

        min_audiobook_resume = d.pop("MinAudiobookResume", UNSET)

        max_audiobook_resume = d.pop("MaxAudiobookResume", UNSET)

        library_monitor_delay = d.pop("LibraryMonitorDelay", UNSET)

        _image_saving_convention = d.pop("ImageSavingConvention", UNSET)
        image_saving_convention: Union[Unset, ImageSavingConvention]
        if isinstance(_image_saving_convention, Unset):
            image_saving_convention = UNSET
        else:
            image_saving_convention = ImageSavingConvention(_image_saving_convention)

        metadata_options = []
        _metadata_options = d.pop("MetadataOptions", UNSET)
        for metadata_options_item_data in _metadata_options or []:
            metadata_options_item = MetadataOptions.from_dict(metadata_options_item_data)

            metadata_options.append(metadata_options_item)

        skip_deserialization_for_basic_types = d.pop("SkipDeserializationForBasicTypes", UNSET)

        server_name = d.pop("ServerName", UNSET)

        ui_culture = d.pop("UICulture", UNSET)

        save_metadata_hidden = d.pop("SaveMetadataHidden", UNSET)

        content_types = []
        _content_types = d.pop("ContentTypes", UNSET)
        for content_types_item_data in _content_types or []:
            content_types_item = NameValuePair.from_dict(content_types_item_data)

            content_types.append(content_types_item)

        remote_client_bitrate_limit = d.pop("RemoteClientBitrateLimit", UNSET)

        enable_folder_view = d.pop("EnableFolderView", UNSET)

        enable_grouping_into_collections = d.pop("EnableGroupingIntoCollections", UNSET)

        display_specials_within_seasons = d.pop("DisplaySpecialsWithinSeasons", UNSET)

        codecs_used = cast(List[str], d.pop("CodecsUsed", UNSET))

        plugin_repositories = []
        _plugin_repositories = d.pop("PluginRepositories", UNSET)
        for plugin_repositories_item_data in _plugin_repositories or []:
            plugin_repositories_item = RepositoryInfo.from_dict(plugin_repositories_item_data)

            plugin_repositories.append(plugin_repositories_item)

        enable_external_content_in_suggestions = d.pop("EnableExternalContentInSuggestions", UNSET)

        image_extraction_timeout_ms = d.pop("ImageExtractionTimeoutMs", UNSET)

        path_substitutions = []
        _path_substitutions = d.pop("PathSubstitutions", UNSET)
        for path_substitutions_item_data in _path_substitutions or []:
            path_substitutions_item = PathSubstitution.from_dict(path_substitutions_item_data)

            path_substitutions.append(path_substitutions_item)

        enable_slow_response_warning = d.pop("EnableSlowResponseWarning", UNSET)

        slow_response_threshold_ms = d.pop("SlowResponseThresholdMs", UNSET)

        cors_hosts = cast(List[str], d.pop("CorsHosts", UNSET))

        activity_log_retention_days = d.pop("ActivityLogRetentionDays", UNSET)

        library_scan_fanout_concurrency = d.pop("LibraryScanFanoutConcurrency", UNSET)

        library_metadata_refresh_concurrency = d.pop("LibraryMetadataRefreshConcurrency", UNSET)

        remove_old_plugins = d.pop("RemoveOldPlugins", UNSET)

        allow_client_log_upload = d.pop("AllowClientLogUpload", UNSET)

        server_configuration = cls(
            log_file_retention_days=log_file_retention_days,
            is_startup_wizard_completed=is_startup_wizard_completed,
            cache_path=cache_path,
            previous_version=previous_version,
            previous_version_str=previous_version_str,
            enable_metrics=enable_metrics,
            enable_normalized_item_by_name_ids=enable_normalized_item_by_name_ids,
            is_port_authorized=is_port_authorized,
            quick_connect_available=quick_connect_available,
            enable_case_sensitive_item_ids=enable_case_sensitive_item_ids,
            disable_live_tv_channel_user_data_name=disable_live_tv_channel_user_data_name,
            metadata_path=metadata_path,
            metadata_network_path=metadata_network_path,
            preferred_metadata_language=preferred_metadata_language,
            metadata_country_code=metadata_country_code,
            sort_replace_characters=sort_replace_characters,
            sort_remove_characters=sort_remove_characters,
            sort_remove_words=sort_remove_words,
            min_resume_pct=min_resume_pct,
            max_resume_pct=max_resume_pct,
            min_resume_duration_seconds=min_resume_duration_seconds,
            min_audiobook_resume=min_audiobook_resume,
            max_audiobook_resume=max_audiobook_resume,
            library_monitor_delay=library_monitor_delay,
            image_saving_convention=image_saving_convention,
            metadata_options=metadata_options,
            skip_deserialization_for_basic_types=skip_deserialization_for_basic_types,
            server_name=server_name,
            ui_culture=ui_culture,
            save_metadata_hidden=save_metadata_hidden,
            content_types=content_types,
            remote_client_bitrate_limit=remote_client_bitrate_limit,
            enable_folder_view=enable_folder_view,
            enable_grouping_into_collections=enable_grouping_into_collections,
            display_specials_within_seasons=display_specials_within_seasons,
            codecs_used=codecs_used,
            plugin_repositories=plugin_repositories,
            enable_external_content_in_suggestions=enable_external_content_in_suggestions,
            image_extraction_timeout_ms=image_extraction_timeout_ms,
            path_substitutions=path_substitutions,
            enable_slow_response_warning=enable_slow_response_warning,
            slow_response_threshold_ms=slow_response_threshold_ms,
            cors_hosts=cors_hosts,
            activity_log_retention_days=activity_log_retention_days,
            library_scan_fanout_concurrency=library_scan_fanout_concurrency,
            library_metadata_refresh_concurrency=library_metadata_refresh_concurrency,
            remove_old_plugins=remove_old_plugins,
            allow_client_log_upload=allow_client_log_upload,
        )

        return server_configuration
