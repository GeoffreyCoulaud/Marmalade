""" Contains all the data models used in inputs/outputs """

from .access_schedule import AccessSchedule
from .activity_log_entry import ActivityLogEntry
from .activity_log_entry_query_result import ActivityLogEntryQueryResult
from .add_virtual_folder_dto import AddVirtualFolderDto
from .admin_notification_dto import AdminNotificationDto
from .album_info import AlbumInfo
from .album_info_artist_provider_ids import AlbumInfoArtistProviderIds
from .album_info_provider_ids import AlbumInfoProviderIds
from .album_info_remote_search_query import AlbumInfoRemoteSearchQuery
from .all_theme_media_result import AllThemeMediaResult
from .architecture import Architecture
from .artist_info import ArtistInfo
from .artist_info_provider_ids import ArtistInfoProviderIds
from .artist_info_remote_search_query import ArtistInfoRemoteSearchQuery
from .authenticate_user_by_name import AuthenticateUserByName
from .authentication_info import AuthenticationInfo
from .authentication_info_query_result import AuthenticationInfoQueryResult
from .authentication_result import AuthenticationResult
from .base_item import BaseItem
from .base_item_dto import BaseItemDto
from .base_item_dto_image_blur_hashes import BaseItemDtoImageBlurHashes
from .base_item_dto_image_blur_hashes_art import BaseItemDtoImageBlurHashesArt
from .base_item_dto_image_blur_hashes_backdrop import BaseItemDtoImageBlurHashesBackdrop
from .base_item_dto_image_blur_hashes_banner import BaseItemDtoImageBlurHashesBanner
from .base_item_dto_image_blur_hashes_box import BaseItemDtoImageBlurHashesBox
from .base_item_dto_image_blur_hashes_box_rear import BaseItemDtoImageBlurHashesBoxRear
from .base_item_dto_image_blur_hashes_chapter import BaseItemDtoImageBlurHashesChapter
from .base_item_dto_image_blur_hashes_disc import BaseItemDtoImageBlurHashesDisc
from .base_item_dto_image_blur_hashes_logo import BaseItemDtoImageBlurHashesLogo
from .base_item_dto_image_blur_hashes_menu import BaseItemDtoImageBlurHashesMenu
from .base_item_dto_image_blur_hashes_primary import BaseItemDtoImageBlurHashesPrimary
from .base_item_dto_image_blur_hashes_profile import BaseItemDtoImageBlurHashesProfile
from .base_item_dto_image_blur_hashes_screenshot import BaseItemDtoImageBlurHashesScreenshot
from .base_item_dto_image_blur_hashes_thumb import BaseItemDtoImageBlurHashesThumb
from .base_item_dto_image_tags import BaseItemDtoImageTags
from .base_item_dto_provider_ids import BaseItemDtoProviderIds
from .base_item_dto_query_result import BaseItemDtoQueryResult
from .base_item_kind import BaseItemKind
from .base_item_person import BaseItemPerson
from .base_item_person_image_blur_hashes import BaseItemPersonImageBlurHashes
from .base_item_person_image_blur_hashes_art import BaseItemPersonImageBlurHashesArt
from .base_item_person_image_blur_hashes_backdrop import BaseItemPersonImageBlurHashesBackdrop
from .base_item_person_image_blur_hashes_banner import BaseItemPersonImageBlurHashesBanner
from .base_item_person_image_blur_hashes_box import BaseItemPersonImageBlurHashesBox
from .base_item_person_image_blur_hashes_box_rear import BaseItemPersonImageBlurHashesBoxRear
from .base_item_person_image_blur_hashes_chapter import BaseItemPersonImageBlurHashesChapter
from .base_item_person_image_blur_hashes_disc import BaseItemPersonImageBlurHashesDisc
from .base_item_person_image_blur_hashes_logo import BaseItemPersonImageBlurHashesLogo
from .base_item_person_image_blur_hashes_menu import BaseItemPersonImageBlurHashesMenu
from .base_item_person_image_blur_hashes_primary import BaseItemPersonImageBlurHashesPrimary
from .base_item_person_image_blur_hashes_profile import BaseItemPersonImageBlurHashesProfile
from .base_item_person_image_blur_hashes_screenshot import BaseItemPersonImageBlurHashesScreenshot
from .base_item_person_image_blur_hashes_thumb import BaseItemPersonImageBlurHashesThumb
from .base_plugin_configuration import BasePluginConfiguration
from .book_info import BookInfo
from .book_info_provider_ids import BookInfoProviderIds
from .book_info_remote_search_query import BookInfoRemoteSearchQuery
from .box_set_info import BoxSetInfo
from .box_set_info_provider_ids import BoxSetInfoProviderIds
from .box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery
from .branding_options import BrandingOptions
from .buffer_request_dto import BufferRequestDto
from .channel_features import ChannelFeatures
from .channel_item_sort_field import ChannelItemSortField
from .channel_mapping_options_dto import ChannelMappingOptionsDto
from .channel_media_content_type import ChannelMediaContentType
from .channel_media_type import ChannelMediaType
from .channel_type import ChannelType
from .chapter_info import ChapterInfo
from .client_capabilities import ClientCapabilities
from .client_capabilities_dto import ClientCapabilitiesDto
from .client_log_document_response_dto import ClientLogDocumentResponseDto
from .codec_profile import CodecProfile
from .codec_type import CodecType
from .collection_creation_result import CollectionCreationResult
from .collection_type_options import CollectionTypeOptions
from .config_image_types import ConfigImageTypes
from .configuration_page_info import ConfigurationPageInfo
from .container_profile import ContainerProfile
from .control_response import ControlResponse
from .control_response_headers import ControlResponseHeaders
from .country_info import CountryInfo
from .create_playlist_dto import CreatePlaylistDto
from .create_user_by_name import CreateUserByName
from .culture_dto import CultureDto
from .day_of_week import DayOfWeek
from .day_pattern import DayPattern
from .default_directory_browser_info_dto import DefaultDirectoryBrowserInfoDto
from .device_identification import DeviceIdentification
from .device_info import DeviceInfo
from .device_info_query_result import DeviceInfoQueryResult
from .device_options import DeviceOptions
from .device_options_dto import DeviceOptionsDto
from .device_profile import DeviceProfile
from .device_profile_info import DeviceProfileInfo
from .device_profile_type import DeviceProfileType
from .direct_play_profile import DirectPlayProfile
from .display_preferences_dto import DisplayPreferencesDto
from .display_preferences_dto_custom_prefs import DisplayPreferencesDtoCustomPrefs
from .dlna_options import DlnaOptions
from .dlna_profile_type import DlnaProfileType
from .dynamic_day_of_week import DynamicDayOfWeek
from .embedded_subtitle_options import EmbeddedSubtitleOptions
from .encoding_context import EncodingContext
from .encoding_options import EncodingOptions
from .end_point_info import EndPointInfo
from .external_id_info import ExternalIdInfo
from .external_id_media_type import ExternalIdMediaType
from .external_url import ExternalUrl
from .f_fmpeg_location import FFmpegLocation
from .file_system_entry_info import FileSystemEntryInfo
from .file_system_entry_type import FileSystemEntryType
from .font_file import FontFile
from .forgot_password_action import ForgotPasswordAction
from .forgot_password_dto import ForgotPasswordDto
from .forgot_password_pin_dto import ForgotPasswordPinDto
from .forgot_password_result import ForgotPasswordResult
from .general_command import GeneralCommand
from .general_command_arguments import GeneralCommandArguments
from .general_command_type import GeneralCommandType
from .get_audio_stream_by_container_stream_options import GetAudioStreamByContainerStreamOptions
from .get_audio_stream_stream_options import GetAudioStreamStreamOptions
from .get_hls_audio_segment_stream_options import GetHlsAudioSegmentStreamOptions
from .get_hls_video_segment_stream_options import GetHlsVideoSegmentStreamOptions
from .get_live_hls_stream_stream_options import GetLiveHlsStreamStreamOptions
from .get_master_hls_audio_playlist_stream_options import GetMasterHlsAudioPlaylistStreamOptions
from .get_master_hls_video_playlist_stream_options import GetMasterHlsVideoPlaylistStreamOptions
from .get_programs_dto import GetProgramsDto
from .get_variant_hls_audio_playlist_stream_options import GetVariantHlsAudioPlaylistStreamOptions
from .get_variant_hls_video_playlist_stream_options import GetVariantHlsVideoPlaylistStreamOptions
from .get_video_stream_by_container_stream_options import GetVideoStreamByContainerStreamOptions
from .get_video_stream_stream_options import GetVideoStreamStreamOptions
from .group_info_dto import GroupInfoDto
from .group_queue_mode import GroupQueueMode
from .group_repeat_mode import GroupRepeatMode
from .group_shuffle_mode import GroupShuffleMode
from .group_state_type import GroupStateType
from .group_update_type import GroupUpdateType
from .guide_info import GuideInfo
from .hardware_encoding_type import HardwareEncodingType
from .head_audio_stream_by_container_stream_options import HeadAudioStreamByContainerStreamOptions
from .head_audio_stream_stream_options import HeadAudioStreamStreamOptions
from .head_master_hls_audio_playlist_stream_options import HeadMasterHlsAudioPlaylistStreamOptions
from .head_master_hls_video_playlist_stream_options import HeadMasterHlsVideoPlaylistStreamOptions
from .head_video_stream_by_container_stream_options import HeadVideoStreamByContainerStreamOptions
from .head_video_stream_stream_options import HeadVideoStreamStreamOptions
from .header_match_type import HeaderMatchType
from .http_header_info import HttpHeaderInfo
from .i_plugin import IPlugin
from .ignore_wait_request_dto import IgnoreWaitRequestDto
from .image_by_name_info import ImageByNameInfo
from .image_format import ImageFormat
from .image_info import ImageInfo
from .image_option import ImageOption
from .image_orientation import ImageOrientation
from .image_provider_info import ImageProviderInfo
from .image_saving_convention import ImageSavingConvention
from .image_type import ImageType
from .installation_info import InstallationInfo
from .iso_type import IsoType
from .item_counts import ItemCounts
from .item_fields import ItemFields
from .item_filter import ItemFilter
from .join_group_request_dto import JoinGroupRequestDto
from .keep_until import KeepUntil
from .library_option_info_dto import LibraryOptionInfoDto
from .library_options import LibraryOptions
from .library_options_result_dto import LibraryOptionsResultDto
from .library_type_options_dto import LibraryTypeOptionsDto
from .library_update_info import LibraryUpdateInfo
from .listings_provider_info import ListingsProviderInfo
from .live_stream_response import LiveStreamResponse
from .live_tv_info import LiveTvInfo
from .live_tv_options import LiveTvOptions
from .live_tv_service_info import LiveTvServiceInfo
from .live_tv_service_status import LiveTvServiceStatus
from .localization_option import LocalizationOption
from .location_type import LocationType
from .log_file import LogFile
from .log_level import LogLevel
from .media_attachment import MediaAttachment
from .media_encoder_path_dto import MediaEncoderPathDto
from .media_path_dto import MediaPathDto
from .media_path_info import MediaPathInfo
from .media_protocol import MediaProtocol
from .media_source_info import MediaSourceInfo
from .media_source_info_required_http_headers import MediaSourceInfoRequiredHttpHeaders
from .media_source_type import MediaSourceType
from .media_stream import MediaStream
from .media_stream_type import MediaStreamType
from .media_update_info_dto import MediaUpdateInfoDto
from .media_update_info_path_dto import MediaUpdateInfoPathDto
from .media_url import MediaUrl
from .message_command import MessageCommand
from .metadata_configuration import MetadataConfiguration
from .metadata_editor_info import MetadataEditorInfo
from .metadata_field import MetadataField
from .metadata_options import MetadataOptions
from .metadata_refresh_mode import MetadataRefreshMode
from .move_playlist_item_request_dto import MovePlaylistItemRequestDto
from .movie_info import MovieInfo
from .movie_info_provider_ids import MovieInfoProviderIds
from .movie_info_remote_search_query import MovieInfoRemoteSearchQuery
from .music_video_info import MusicVideoInfo
from .music_video_info_provider_ids import MusicVideoInfoProviderIds
from .music_video_info_remote_search_query import MusicVideoInfoRemoteSearchQuery
from .name_guid_pair import NameGuidPair
from .name_id_pair import NameIdPair
from .name_value_pair import NameValuePair
from .network_configuration import NetworkConfiguration
from .new_group_request_dto import NewGroupRequestDto
from .next_item_request_dto import NextItemRequestDto
from .notification_dto import NotificationDto
from .notification_level import NotificationLevel
from .notification_option import NotificationOption
from .notification_options import NotificationOptions
from .notification_result_dto import NotificationResultDto
from .notification_type_info import NotificationTypeInfo
from .notifications_summary_dto import NotificationsSummaryDto
from .object_group_update import ObjectGroupUpdate
from .open_live_stream_dto import OpenLiveStreamDto
from .package_info import PackageInfo
from .parental_rating import ParentalRating
from .path_substitution import PathSubstitution
from .person_lookup_info import PersonLookupInfo
from .person_lookup_info_provider_ids import PersonLookupInfoProviderIds
from .person_lookup_info_remote_search_query import PersonLookupInfoRemoteSearchQuery
from .pin_redeem_result import PinRedeemResult
from .ping_request_dto import PingRequestDto
from .play_access import PlayAccess
from .play_command import PlayCommand
from .play_method import PlayMethod
from .play_request import PlayRequest
from .play_request_dto import PlayRequestDto
from .playback_error_code import PlaybackErrorCode
from .playback_info_dto import PlaybackInfoDto
from .playback_info_response import PlaybackInfoResponse
from .playback_progress_info import PlaybackProgressInfo
from .playback_start_info import PlaybackStartInfo
from .playback_stop_info import PlaybackStopInfo
from .player_state_info import PlayerStateInfo
from .playlist_creation_result import PlaylistCreationResult
from .playstate_command import PlaystateCommand
from .playstate_request import PlaystateRequest
from .plugin_info import PluginInfo
from .plugin_status import PluginStatus
from .previous_item_request_dto import PreviousItemRequestDto
from .problem_details import ProblemDetails
from .profile_condition import ProfileCondition
from .profile_condition_type import ProfileConditionType
from .profile_condition_value import ProfileConditionValue
from .program_audio import ProgramAudio
from .public_system_info import PublicSystemInfo
from .query_filters import QueryFilters
from .query_filters_legacy import QueryFiltersLegacy
from .queue_item import QueueItem
from .queue_request_dto import QueueRequestDto
from .quick_connect_dto import QuickConnectDto
from .quick_connect_result import QuickConnectResult
from .rating_type import RatingType
from .ready_request_dto import ReadyRequestDto
from .recommendation_dto import RecommendationDto
from .recommendation_type import RecommendationType
from .recording_status import RecordingStatus
from .remote_image_info import RemoteImageInfo
from .remote_image_result import RemoteImageResult
from .remote_search_result import RemoteSearchResult
from .remote_search_result_provider_ids import RemoteSearchResultProviderIds
from .remote_subtitle_info import RemoteSubtitleInfo
from .remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto
from .repeat_mode import RepeatMode
from .repository_info import RepositoryInfo
from .response_profile import ResponseProfile
from .scroll_direction import ScrollDirection
from .search_hint import SearchHint
from .search_hint_result import SearchHintResult
from .seek_request_dto import SeekRequestDto
from .send_command import SendCommand
from .send_command_type import SendCommandType
from .send_to_user_type import SendToUserType
from .series_info import SeriesInfo
from .series_info_provider_ids import SeriesInfoProviderIds
from .series_info_remote_search_query import SeriesInfoRemoteSearchQuery
from .series_status import SeriesStatus
from .series_timer_info_dto import SeriesTimerInfoDto
from .series_timer_info_dto_image_tags import SeriesTimerInfoDtoImageTags
from .series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult
from .server_configuration import ServerConfiguration
from .server_discovery_info import ServerDiscoveryInfo
from .session_info import SessionInfo
from .session_message_type import SessionMessageType
from .session_user_info import SessionUserInfo
from .set_channel_mapping_dto import SetChannelMappingDto
from .set_playlist_item_request_dto import SetPlaylistItemRequestDto
from .set_repeat_mode_request_dto import SetRepeatModeRequestDto
from .set_shuffle_mode_request_dto import SetShuffleModeRequestDto
from .song_info import SongInfo
from .song_info_provider_ids import SongInfoProviderIds
from .sort_order import SortOrder
from .special_view_option_dto import SpecialViewOptionDto
from .startup_configuration_dto import StartupConfigurationDto
from .startup_remote_access_dto import StartupRemoteAccessDto
from .startup_user_dto import StartupUserDto
from .subtitle_delivery_method import SubtitleDeliveryMethod
from .subtitle_options import SubtitleOptions
from .subtitle_playback_mode import SubtitlePlaybackMode
from .subtitle_profile import SubtitleProfile
from .sync_play_user_access_type import SyncPlayUserAccessType
from .system_info import SystemInfo
from .task_completion_status import TaskCompletionStatus
from .task_info import TaskInfo
from .task_result import TaskResult
from .task_state import TaskState
from .task_trigger_info import TaskTriggerInfo
from .theme_media_result import ThemeMediaResult
from .timer_event_info import TimerEventInfo
from .timer_info_dto import TimerInfoDto
from .timer_info_dto_query_result import TimerInfoDtoQueryResult
from .trailer_info import TrailerInfo
from .trailer_info_provider_ids import TrailerInfoProviderIds
from .trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery
from .transcode_reason import TranscodeReason
from .transcode_seek_info import TranscodeSeekInfo
from .transcoding_info import TranscodingInfo
from .transcoding_profile import TranscodingProfile
from .transport_stream_timestamp import TransportStreamTimestamp
from .tuner_channel_mapping import TunerChannelMapping
from .tuner_host_info import TunerHostInfo
from .type_options import TypeOptions
from .unrated_item import UnratedItem
from .update_library_options_dto import UpdateLibraryOptionsDto
from .update_media_path_request_dto import UpdateMediaPathRequestDto
from .update_user_easy_password import UpdateUserEasyPassword
from .update_user_password import UpdateUserPassword
from .upload_subtitle_dto import UploadSubtitleDto
from .user_configuration import UserConfiguration
from .user_dto import UserDto
from .user_item_data_dto import UserItemDataDto
from .user_policy import UserPolicy
from .utc_time_response import UtcTimeResponse
from .validate_path_dto import ValidatePathDto
from .version_info import VersionInfo
from .video_3d_format import Video3DFormat
from .video_type import VideoType
from .virtual_folder_info import VirtualFolderInfo
from .wake_on_lan_info import WakeOnLanInfo
from .xbmc_metadata_options import XbmcMetadataOptions
from .xml_attribute import XmlAttribute

__all__ = (
    "AccessSchedule",
    "ActivityLogEntry",
    "ActivityLogEntryQueryResult",
    "AddVirtualFolderDto",
    "AdminNotificationDto",
    "AlbumInfo",
    "AlbumInfoArtistProviderIds",
    "AlbumInfoProviderIds",
    "AlbumInfoRemoteSearchQuery",
    "AllThemeMediaResult",
    "Architecture",
    "ArtistInfo",
    "ArtistInfoProviderIds",
    "ArtistInfoRemoteSearchQuery",
    "AuthenticateUserByName",
    "AuthenticationInfo",
    "AuthenticationInfoQueryResult",
    "AuthenticationResult",
    "BaseItem",
    "BaseItemDto",
    "BaseItemDtoImageBlurHashes",
    "BaseItemDtoImageBlurHashesArt",
    "BaseItemDtoImageBlurHashesBackdrop",
    "BaseItemDtoImageBlurHashesBanner",
    "BaseItemDtoImageBlurHashesBox",
    "BaseItemDtoImageBlurHashesBoxRear",
    "BaseItemDtoImageBlurHashesChapter",
    "BaseItemDtoImageBlurHashesDisc",
    "BaseItemDtoImageBlurHashesLogo",
    "BaseItemDtoImageBlurHashesMenu",
    "BaseItemDtoImageBlurHashesPrimary",
    "BaseItemDtoImageBlurHashesProfile",
    "BaseItemDtoImageBlurHashesScreenshot",
    "BaseItemDtoImageBlurHashesThumb",
    "BaseItemDtoImageTags",
    "BaseItemDtoProviderIds",
    "BaseItemDtoQueryResult",
    "BaseItemKind",
    "BaseItemPerson",
    "BaseItemPersonImageBlurHashes",
    "BaseItemPersonImageBlurHashesArt",
    "BaseItemPersonImageBlurHashesBackdrop",
    "BaseItemPersonImageBlurHashesBanner",
    "BaseItemPersonImageBlurHashesBox",
    "BaseItemPersonImageBlurHashesBoxRear",
    "BaseItemPersonImageBlurHashesChapter",
    "BaseItemPersonImageBlurHashesDisc",
    "BaseItemPersonImageBlurHashesLogo",
    "BaseItemPersonImageBlurHashesMenu",
    "BaseItemPersonImageBlurHashesPrimary",
    "BaseItemPersonImageBlurHashesProfile",
    "BaseItemPersonImageBlurHashesScreenshot",
    "BaseItemPersonImageBlurHashesThumb",
    "BasePluginConfiguration",
    "BookInfo",
    "BookInfoProviderIds",
    "BookInfoRemoteSearchQuery",
    "BoxSetInfo",
    "BoxSetInfoProviderIds",
    "BoxSetInfoRemoteSearchQuery",
    "BrandingOptions",
    "BufferRequestDto",
    "ChannelFeatures",
    "ChannelItemSortField",
    "ChannelMappingOptionsDto",
    "ChannelMediaContentType",
    "ChannelMediaType",
    "ChannelType",
    "ChapterInfo",
    "ClientCapabilities",
    "ClientCapabilitiesDto",
    "ClientLogDocumentResponseDto",
    "CodecProfile",
    "CodecType",
    "CollectionCreationResult",
    "CollectionTypeOptions",
    "ConfigImageTypes",
    "ConfigurationPageInfo",
    "ContainerProfile",
    "ControlResponse",
    "ControlResponseHeaders",
    "CountryInfo",
    "CreatePlaylistDto",
    "CreateUserByName",
    "CultureDto",
    "DayOfWeek",
    "DayPattern",
    "DefaultDirectoryBrowserInfoDto",
    "DeviceIdentification",
    "DeviceInfo",
    "DeviceInfoQueryResult",
    "DeviceOptions",
    "DeviceOptionsDto",
    "DeviceProfile",
    "DeviceProfileInfo",
    "DeviceProfileType",
    "DirectPlayProfile",
    "DisplayPreferencesDto",
    "DisplayPreferencesDtoCustomPrefs",
    "DlnaOptions",
    "DlnaProfileType",
    "DynamicDayOfWeek",
    "EmbeddedSubtitleOptions",
    "EncodingContext",
    "EncodingOptions",
    "EndPointInfo",
    "ExternalIdInfo",
    "ExternalIdMediaType",
    "ExternalUrl",
    "FFmpegLocation",
    "FileSystemEntryInfo",
    "FileSystemEntryType",
    "FontFile",
    "ForgotPasswordAction",
    "ForgotPasswordDto",
    "ForgotPasswordPinDto",
    "ForgotPasswordResult",
    "GeneralCommand",
    "GeneralCommandArguments",
    "GeneralCommandType",
    "GetAudioStreamByContainerStreamOptions",
    "GetAudioStreamStreamOptions",
    "GetHlsAudioSegmentStreamOptions",
    "GetHlsVideoSegmentStreamOptions",
    "GetLiveHlsStreamStreamOptions",
    "GetMasterHlsAudioPlaylistStreamOptions",
    "GetMasterHlsVideoPlaylistStreamOptions",
    "GetProgramsDto",
    "GetVariantHlsAudioPlaylistStreamOptions",
    "GetVariantHlsVideoPlaylistStreamOptions",
    "GetVideoStreamByContainerStreamOptions",
    "GetVideoStreamStreamOptions",
    "GroupInfoDto",
    "GroupQueueMode",
    "GroupRepeatMode",
    "GroupShuffleMode",
    "GroupStateType",
    "GroupUpdateType",
    "GuideInfo",
    "HardwareEncodingType",
    "HeadAudioStreamByContainerStreamOptions",
    "HeadAudioStreamStreamOptions",
    "HeaderMatchType",
    "HeadMasterHlsAudioPlaylistStreamOptions",
    "HeadMasterHlsVideoPlaylistStreamOptions",
    "HeadVideoStreamByContainerStreamOptions",
    "HeadVideoStreamStreamOptions",
    "HttpHeaderInfo",
    "IgnoreWaitRequestDto",
    "ImageByNameInfo",
    "ImageFormat",
    "ImageInfo",
    "ImageOption",
    "ImageOrientation",
    "ImageProviderInfo",
    "ImageSavingConvention",
    "ImageType",
    "InstallationInfo",
    "IPlugin",
    "IsoType",
    "ItemCounts",
    "ItemFields",
    "ItemFilter",
    "JoinGroupRequestDto",
    "KeepUntil",
    "LibraryOptionInfoDto",
    "LibraryOptions",
    "LibraryOptionsResultDto",
    "LibraryTypeOptionsDto",
    "LibraryUpdateInfo",
    "ListingsProviderInfo",
    "LiveStreamResponse",
    "LiveTvInfo",
    "LiveTvOptions",
    "LiveTvServiceInfo",
    "LiveTvServiceStatus",
    "LocalizationOption",
    "LocationType",
    "LogFile",
    "LogLevel",
    "MediaAttachment",
    "MediaEncoderPathDto",
    "MediaPathDto",
    "MediaPathInfo",
    "MediaProtocol",
    "MediaSourceInfo",
    "MediaSourceInfoRequiredHttpHeaders",
    "MediaSourceType",
    "MediaStream",
    "MediaStreamType",
    "MediaUpdateInfoDto",
    "MediaUpdateInfoPathDto",
    "MediaUrl",
    "MessageCommand",
    "MetadataConfiguration",
    "MetadataEditorInfo",
    "MetadataField",
    "MetadataOptions",
    "MetadataRefreshMode",
    "MovePlaylistItemRequestDto",
    "MovieInfo",
    "MovieInfoProviderIds",
    "MovieInfoRemoteSearchQuery",
    "MusicVideoInfo",
    "MusicVideoInfoProviderIds",
    "MusicVideoInfoRemoteSearchQuery",
    "NameGuidPair",
    "NameIdPair",
    "NameValuePair",
    "NetworkConfiguration",
    "NewGroupRequestDto",
    "NextItemRequestDto",
    "NotificationDto",
    "NotificationLevel",
    "NotificationOption",
    "NotificationOptions",
    "NotificationResultDto",
    "NotificationsSummaryDto",
    "NotificationTypeInfo",
    "ObjectGroupUpdate",
    "OpenLiveStreamDto",
    "PackageInfo",
    "ParentalRating",
    "PathSubstitution",
    "PersonLookupInfo",
    "PersonLookupInfoProviderIds",
    "PersonLookupInfoRemoteSearchQuery",
    "PingRequestDto",
    "PinRedeemResult",
    "PlayAccess",
    "PlaybackErrorCode",
    "PlaybackInfoDto",
    "PlaybackInfoResponse",
    "PlaybackProgressInfo",
    "PlaybackStartInfo",
    "PlaybackStopInfo",
    "PlayCommand",
    "PlayerStateInfo",
    "PlaylistCreationResult",
    "PlayMethod",
    "PlayRequest",
    "PlayRequestDto",
    "PlaystateCommand",
    "PlaystateRequest",
    "PluginInfo",
    "PluginStatus",
    "PreviousItemRequestDto",
    "ProblemDetails",
    "ProfileCondition",
    "ProfileConditionType",
    "ProfileConditionValue",
    "ProgramAudio",
    "PublicSystemInfo",
    "QueryFilters",
    "QueryFiltersLegacy",
    "QueueItem",
    "QueueRequestDto",
    "QuickConnectDto",
    "QuickConnectResult",
    "RatingType",
    "ReadyRequestDto",
    "RecommendationDto",
    "RecommendationType",
    "RecordingStatus",
    "RemoteImageInfo",
    "RemoteImageResult",
    "RemoteSearchResult",
    "RemoteSearchResultProviderIds",
    "RemoteSubtitleInfo",
    "RemoveFromPlaylistRequestDto",
    "RepeatMode",
    "RepositoryInfo",
    "ResponseProfile",
    "ScrollDirection",
    "SearchHint",
    "SearchHintResult",
    "SeekRequestDto",
    "SendCommand",
    "SendCommandType",
    "SendToUserType",
    "SeriesInfo",
    "SeriesInfoProviderIds",
    "SeriesInfoRemoteSearchQuery",
    "SeriesStatus",
    "SeriesTimerInfoDto",
    "SeriesTimerInfoDtoImageTags",
    "SeriesTimerInfoDtoQueryResult",
    "ServerConfiguration",
    "ServerDiscoveryInfo",
    "SessionInfo",
    "SessionMessageType",
    "SessionUserInfo",
    "SetChannelMappingDto",
    "SetPlaylistItemRequestDto",
    "SetRepeatModeRequestDto",
    "SetShuffleModeRequestDto",
    "SongInfo",
    "SongInfoProviderIds",
    "SortOrder",
    "SpecialViewOptionDto",
    "StartupConfigurationDto",
    "StartupRemoteAccessDto",
    "StartupUserDto",
    "SubtitleDeliveryMethod",
    "SubtitleOptions",
    "SubtitlePlaybackMode",
    "SubtitleProfile",
    "SyncPlayUserAccessType",
    "SystemInfo",
    "TaskCompletionStatus",
    "TaskInfo",
    "TaskResult",
    "TaskState",
    "TaskTriggerInfo",
    "ThemeMediaResult",
    "TimerEventInfo",
    "TimerInfoDto",
    "TimerInfoDtoQueryResult",
    "TrailerInfo",
    "TrailerInfoProviderIds",
    "TrailerInfoRemoteSearchQuery",
    "TranscodeReason",
    "TranscodeSeekInfo",
    "TranscodingInfo",
    "TranscodingProfile",
    "TransportStreamTimestamp",
    "TunerChannelMapping",
    "TunerHostInfo",
    "TypeOptions",
    "UnratedItem",
    "UpdateLibraryOptionsDto",
    "UpdateMediaPathRequestDto",
    "UpdateUserEasyPassword",
    "UpdateUserPassword",
    "UploadSubtitleDto",
    "UserConfiguration",
    "UserDto",
    "UserItemDataDto",
    "UserPolicy",
    "UtcTimeResponse",
    "ValidatePathDto",
    "VersionInfo",
    "Video3DFormat",
    "VideoType",
    "VirtualFolderInfo",
    "WakeOnLanInfo",
    "XbmcMetadataOptions",
    "XmlAttribute",
)
