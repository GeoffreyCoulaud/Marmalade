from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.sync_play_user_access_type import SyncPlayUserAccessType
from ..models.unrated_item import UnratedItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_schedule import AccessSchedule


T = TypeVar("T", bound="UserPolicy")


@_attrs_define
class UserPolicy:
    """
    Attributes:
        is_administrator (Union[Unset, bool]): Gets or sets a value indicating whether this instance is administrator.
        is_hidden (Union[Unset, bool]): Gets or sets a value indicating whether this instance is hidden.
        is_disabled (Union[Unset, bool]): Gets or sets a value indicating whether this instance is disabled.
        max_parental_rating (Union[Unset, None, int]): Gets or sets the max parental rating.
        blocked_tags (Union[Unset, None, List[str]]):
        enable_user_preference_access (Union[Unset, bool]):
        access_schedules (Union[Unset, None, List['AccessSchedule']]):
        block_unrated_items (Union[Unset, None, List[UnratedItem]]):
        enable_remote_control_of_other_users (Union[Unset, bool]):
        enable_shared_device_control (Union[Unset, bool]):
        enable_remote_access (Union[Unset, bool]):
        enable_live_tv_management (Union[Unset, bool]):
        enable_live_tv_access (Union[Unset, bool]):
        enable_media_playback (Union[Unset, bool]):
        enable_audio_playback_transcoding (Union[Unset, bool]):
        enable_video_playback_transcoding (Union[Unset, bool]):
        enable_playback_remuxing (Union[Unset, bool]):
        force_remote_source_transcoding (Union[Unset, bool]):
        enable_content_deletion (Union[Unset, bool]):
        enable_content_deletion_from_folders (Union[Unset, None, List[str]]):
        enable_content_downloading (Union[Unset, bool]):
        enable_sync_transcoding (Union[Unset, bool]): Gets or sets a value indicating whether [enable synchronize].
        enable_media_conversion (Union[Unset, bool]):
        enabled_devices (Union[Unset, None, List[str]]):
        enable_all_devices (Union[Unset, bool]):
        enabled_channels (Union[Unset, None, List[str]]):
        enable_all_channels (Union[Unset, bool]):
        enabled_folders (Union[Unset, None, List[str]]):
        enable_all_folders (Union[Unset, bool]):
        invalid_login_attempt_count (Union[Unset, int]):
        login_attempts_before_lockout (Union[Unset, int]):
        max_active_sessions (Union[Unset, int]):
        enable_public_sharing (Union[Unset, bool]):
        blocked_media_folders (Union[Unset, None, List[str]]):
        blocked_channels (Union[Unset, None, List[str]]):
        remote_client_bitrate_limit (Union[Unset, int]):
        authentication_provider_id (Union[Unset, None, str]):
        password_reset_provider_id (Union[Unset, None, str]):
        sync_play_access (Union[Unset, SyncPlayUserAccessType]): Enum SyncPlayUserAccessType.
    """

    is_administrator: Union[Unset, bool] = UNSET
    is_hidden: Union[Unset, bool] = UNSET
    is_disabled: Union[Unset, bool] = UNSET
    max_parental_rating: Union[Unset, None, int] = UNSET
    blocked_tags: Union[Unset, None, List[str]] = UNSET
    enable_user_preference_access: Union[Unset, bool] = UNSET
    access_schedules: Union[Unset, None, List["AccessSchedule"]] = UNSET
    block_unrated_items: Union[Unset, None, List[UnratedItem]] = UNSET
    enable_remote_control_of_other_users: Union[Unset, bool] = UNSET
    enable_shared_device_control: Union[Unset, bool] = UNSET
    enable_remote_access: Union[Unset, bool] = UNSET
    enable_live_tv_management: Union[Unset, bool] = UNSET
    enable_live_tv_access: Union[Unset, bool] = UNSET
    enable_media_playback: Union[Unset, bool] = UNSET
    enable_audio_playback_transcoding: Union[Unset, bool] = UNSET
    enable_video_playback_transcoding: Union[Unset, bool] = UNSET
    enable_playback_remuxing: Union[Unset, bool] = UNSET
    force_remote_source_transcoding: Union[Unset, bool] = UNSET
    enable_content_deletion: Union[Unset, bool] = UNSET
    enable_content_deletion_from_folders: Union[Unset, None, List[str]] = UNSET
    enable_content_downloading: Union[Unset, bool] = UNSET
    enable_sync_transcoding: Union[Unset, bool] = UNSET
    enable_media_conversion: Union[Unset, bool] = UNSET
    enabled_devices: Union[Unset, None, List[str]] = UNSET
    enable_all_devices: Union[Unset, bool] = UNSET
    enabled_channels: Union[Unset, None, List[str]] = UNSET
    enable_all_channels: Union[Unset, bool] = UNSET
    enabled_folders: Union[Unset, None, List[str]] = UNSET
    enable_all_folders: Union[Unset, bool] = UNSET
    invalid_login_attempt_count: Union[Unset, int] = UNSET
    login_attempts_before_lockout: Union[Unset, int] = UNSET
    max_active_sessions: Union[Unset, int] = UNSET
    enable_public_sharing: Union[Unset, bool] = UNSET
    blocked_media_folders: Union[Unset, None, List[str]] = UNSET
    blocked_channels: Union[Unset, None, List[str]] = UNSET
    remote_client_bitrate_limit: Union[Unset, int] = UNSET
    authentication_provider_id: Union[Unset, None, str] = UNSET
    password_reset_provider_id: Union[Unset, None, str] = UNSET
    sync_play_access: Union[Unset, SyncPlayUserAccessType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_administrator = self.is_administrator
        is_hidden = self.is_hidden
        is_disabled = self.is_disabled
        max_parental_rating = self.max_parental_rating
        blocked_tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.blocked_tags, Unset):
            if self.blocked_tags is None:
                blocked_tags = None
            else:
                blocked_tags = self.blocked_tags

        enable_user_preference_access = self.enable_user_preference_access
        access_schedules: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access_schedules, Unset):
            if self.access_schedules is None:
                access_schedules = None
            else:
                access_schedules = []
                for access_schedules_item_data in self.access_schedules:
                    access_schedules_item = access_schedules_item_data.to_dict()

                    access_schedules.append(access_schedules_item)

        block_unrated_items: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.block_unrated_items, Unset):
            if self.block_unrated_items is None:
                block_unrated_items = None
            else:
                block_unrated_items = []
                for block_unrated_items_item_data in self.block_unrated_items:
                    block_unrated_items_item = block_unrated_items_item_data.value

                    block_unrated_items.append(block_unrated_items_item)

        enable_remote_control_of_other_users = self.enable_remote_control_of_other_users
        enable_shared_device_control = self.enable_shared_device_control
        enable_remote_access = self.enable_remote_access
        enable_live_tv_management = self.enable_live_tv_management
        enable_live_tv_access = self.enable_live_tv_access
        enable_media_playback = self.enable_media_playback
        enable_audio_playback_transcoding = self.enable_audio_playback_transcoding
        enable_video_playback_transcoding = self.enable_video_playback_transcoding
        enable_playback_remuxing = self.enable_playback_remuxing
        force_remote_source_transcoding = self.force_remote_source_transcoding
        enable_content_deletion = self.enable_content_deletion
        enable_content_deletion_from_folders: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.enable_content_deletion_from_folders, Unset):
            if self.enable_content_deletion_from_folders is None:
                enable_content_deletion_from_folders = None
            else:
                enable_content_deletion_from_folders = self.enable_content_deletion_from_folders

        enable_content_downloading = self.enable_content_downloading
        enable_sync_transcoding = self.enable_sync_transcoding
        enable_media_conversion = self.enable_media_conversion
        enabled_devices: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.enabled_devices, Unset):
            if self.enabled_devices is None:
                enabled_devices = None
            else:
                enabled_devices = self.enabled_devices

        enable_all_devices = self.enable_all_devices
        enabled_channels: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.enabled_channels, Unset):
            if self.enabled_channels is None:
                enabled_channels = None
            else:
                enabled_channels = self.enabled_channels

        enable_all_channels = self.enable_all_channels
        enabled_folders: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.enabled_folders, Unset):
            if self.enabled_folders is None:
                enabled_folders = None
            else:
                enabled_folders = self.enabled_folders

        enable_all_folders = self.enable_all_folders
        invalid_login_attempt_count = self.invalid_login_attempt_count
        login_attempts_before_lockout = self.login_attempts_before_lockout
        max_active_sessions = self.max_active_sessions
        enable_public_sharing = self.enable_public_sharing
        blocked_media_folders: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.blocked_media_folders, Unset):
            if self.blocked_media_folders is None:
                blocked_media_folders = None
            else:
                blocked_media_folders = self.blocked_media_folders

        blocked_channels: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.blocked_channels, Unset):
            if self.blocked_channels is None:
                blocked_channels = None
            else:
                blocked_channels = self.blocked_channels

        remote_client_bitrate_limit = self.remote_client_bitrate_limit
        authentication_provider_id = self.authentication_provider_id
        password_reset_provider_id = self.password_reset_provider_id
        sync_play_access: Union[Unset, str] = UNSET
        if not isinstance(self.sync_play_access, Unset):
            sync_play_access = self.sync_play_access.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_administrator is not UNSET:
            field_dict["IsAdministrator"] = is_administrator
        if is_hidden is not UNSET:
            field_dict["IsHidden"] = is_hidden
        if is_disabled is not UNSET:
            field_dict["IsDisabled"] = is_disabled
        if max_parental_rating is not UNSET:
            field_dict["MaxParentalRating"] = max_parental_rating
        if blocked_tags is not UNSET:
            field_dict["BlockedTags"] = blocked_tags
        if enable_user_preference_access is not UNSET:
            field_dict["EnableUserPreferenceAccess"] = enable_user_preference_access
        if access_schedules is not UNSET:
            field_dict["AccessSchedules"] = access_schedules
        if block_unrated_items is not UNSET:
            field_dict["BlockUnratedItems"] = block_unrated_items
        if enable_remote_control_of_other_users is not UNSET:
            field_dict["EnableRemoteControlOfOtherUsers"] = enable_remote_control_of_other_users
        if enable_shared_device_control is not UNSET:
            field_dict["EnableSharedDeviceControl"] = enable_shared_device_control
        if enable_remote_access is not UNSET:
            field_dict["EnableRemoteAccess"] = enable_remote_access
        if enable_live_tv_management is not UNSET:
            field_dict["EnableLiveTvManagement"] = enable_live_tv_management
        if enable_live_tv_access is not UNSET:
            field_dict["EnableLiveTvAccess"] = enable_live_tv_access
        if enable_media_playback is not UNSET:
            field_dict["EnableMediaPlayback"] = enable_media_playback
        if enable_audio_playback_transcoding is not UNSET:
            field_dict["EnableAudioPlaybackTranscoding"] = enable_audio_playback_transcoding
        if enable_video_playback_transcoding is not UNSET:
            field_dict["EnableVideoPlaybackTranscoding"] = enable_video_playback_transcoding
        if enable_playback_remuxing is not UNSET:
            field_dict["EnablePlaybackRemuxing"] = enable_playback_remuxing
        if force_remote_source_transcoding is not UNSET:
            field_dict["ForceRemoteSourceTranscoding"] = force_remote_source_transcoding
        if enable_content_deletion is not UNSET:
            field_dict["EnableContentDeletion"] = enable_content_deletion
        if enable_content_deletion_from_folders is not UNSET:
            field_dict["EnableContentDeletionFromFolders"] = enable_content_deletion_from_folders
        if enable_content_downloading is not UNSET:
            field_dict["EnableContentDownloading"] = enable_content_downloading
        if enable_sync_transcoding is not UNSET:
            field_dict["EnableSyncTranscoding"] = enable_sync_transcoding
        if enable_media_conversion is not UNSET:
            field_dict["EnableMediaConversion"] = enable_media_conversion
        if enabled_devices is not UNSET:
            field_dict["EnabledDevices"] = enabled_devices
        if enable_all_devices is not UNSET:
            field_dict["EnableAllDevices"] = enable_all_devices
        if enabled_channels is not UNSET:
            field_dict["EnabledChannels"] = enabled_channels
        if enable_all_channels is not UNSET:
            field_dict["EnableAllChannels"] = enable_all_channels
        if enabled_folders is not UNSET:
            field_dict["EnabledFolders"] = enabled_folders
        if enable_all_folders is not UNSET:
            field_dict["EnableAllFolders"] = enable_all_folders
        if invalid_login_attempt_count is not UNSET:
            field_dict["InvalidLoginAttemptCount"] = invalid_login_attempt_count
        if login_attempts_before_lockout is not UNSET:
            field_dict["LoginAttemptsBeforeLockout"] = login_attempts_before_lockout
        if max_active_sessions is not UNSET:
            field_dict["MaxActiveSessions"] = max_active_sessions
        if enable_public_sharing is not UNSET:
            field_dict["EnablePublicSharing"] = enable_public_sharing
        if blocked_media_folders is not UNSET:
            field_dict["BlockedMediaFolders"] = blocked_media_folders
        if blocked_channels is not UNSET:
            field_dict["BlockedChannels"] = blocked_channels
        if remote_client_bitrate_limit is not UNSET:
            field_dict["RemoteClientBitrateLimit"] = remote_client_bitrate_limit
        if authentication_provider_id is not UNSET:
            field_dict["AuthenticationProviderId"] = authentication_provider_id
        if password_reset_provider_id is not UNSET:
            field_dict["PasswordResetProviderId"] = password_reset_provider_id
        if sync_play_access is not UNSET:
            field_dict["SyncPlayAccess"] = sync_play_access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_schedule import AccessSchedule

        d = src_dict.copy()
        is_administrator = d.pop("IsAdministrator", UNSET)

        is_hidden = d.pop("IsHidden", UNSET)

        is_disabled = d.pop("IsDisabled", UNSET)

        max_parental_rating = d.pop("MaxParentalRating", UNSET)

        blocked_tags = cast(List[str], d.pop("BlockedTags", UNSET))

        enable_user_preference_access = d.pop("EnableUserPreferenceAccess", UNSET)

        access_schedules = []
        _access_schedules = d.pop("AccessSchedules", UNSET)
        for access_schedules_item_data in _access_schedules or []:
            access_schedules_item = AccessSchedule.from_dict(access_schedules_item_data)

            access_schedules.append(access_schedules_item)

        block_unrated_items = []
        _block_unrated_items = d.pop("BlockUnratedItems", UNSET)
        for block_unrated_items_item_data in _block_unrated_items or []:
            block_unrated_items_item = UnratedItem(block_unrated_items_item_data)

            block_unrated_items.append(block_unrated_items_item)

        enable_remote_control_of_other_users = d.pop("EnableRemoteControlOfOtherUsers", UNSET)

        enable_shared_device_control = d.pop("EnableSharedDeviceControl", UNSET)

        enable_remote_access = d.pop("EnableRemoteAccess", UNSET)

        enable_live_tv_management = d.pop("EnableLiveTvManagement", UNSET)

        enable_live_tv_access = d.pop("EnableLiveTvAccess", UNSET)

        enable_media_playback = d.pop("EnableMediaPlayback", UNSET)

        enable_audio_playback_transcoding = d.pop("EnableAudioPlaybackTranscoding", UNSET)

        enable_video_playback_transcoding = d.pop("EnableVideoPlaybackTranscoding", UNSET)

        enable_playback_remuxing = d.pop("EnablePlaybackRemuxing", UNSET)

        force_remote_source_transcoding = d.pop("ForceRemoteSourceTranscoding", UNSET)

        enable_content_deletion = d.pop("EnableContentDeletion", UNSET)

        enable_content_deletion_from_folders = cast(List[str], d.pop("EnableContentDeletionFromFolders", UNSET))

        enable_content_downloading = d.pop("EnableContentDownloading", UNSET)

        enable_sync_transcoding = d.pop("EnableSyncTranscoding", UNSET)

        enable_media_conversion = d.pop("EnableMediaConversion", UNSET)

        enabled_devices = cast(List[str], d.pop("EnabledDevices", UNSET))

        enable_all_devices = d.pop("EnableAllDevices", UNSET)

        enabled_channels = cast(List[str], d.pop("EnabledChannels", UNSET))

        enable_all_channels = d.pop("EnableAllChannels", UNSET)

        enabled_folders = cast(List[str], d.pop("EnabledFolders", UNSET))

        enable_all_folders = d.pop("EnableAllFolders", UNSET)

        invalid_login_attempt_count = d.pop("InvalidLoginAttemptCount", UNSET)

        login_attempts_before_lockout = d.pop("LoginAttemptsBeforeLockout", UNSET)

        max_active_sessions = d.pop("MaxActiveSessions", UNSET)

        enable_public_sharing = d.pop("EnablePublicSharing", UNSET)

        blocked_media_folders = cast(List[str], d.pop("BlockedMediaFolders", UNSET))

        blocked_channels = cast(List[str], d.pop("BlockedChannels", UNSET))

        remote_client_bitrate_limit = d.pop("RemoteClientBitrateLimit", UNSET)

        authentication_provider_id = d.pop("AuthenticationProviderId", UNSET)

        password_reset_provider_id = d.pop("PasswordResetProviderId", UNSET)

        _sync_play_access = d.pop("SyncPlayAccess", UNSET)
        sync_play_access: Union[Unset, SyncPlayUserAccessType]
        if isinstance(_sync_play_access, Unset):
            sync_play_access = UNSET
        else:
            sync_play_access = SyncPlayUserAccessType(_sync_play_access)

        user_policy = cls(
            is_administrator=is_administrator,
            is_hidden=is_hidden,
            is_disabled=is_disabled,
            max_parental_rating=max_parental_rating,
            blocked_tags=blocked_tags,
            enable_user_preference_access=enable_user_preference_access,
            access_schedules=access_schedules,
            block_unrated_items=block_unrated_items,
            enable_remote_control_of_other_users=enable_remote_control_of_other_users,
            enable_shared_device_control=enable_shared_device_control,
            enable_remote_access=enable_remote_access,
            enable_live_tv_management=enable_live_tv_management,
            enable_live_tv_access=enable_live_tv_access,
            enable_media_playback=enable_media_playback,
            enable_audio_playback_transcoding=enable_audio_playback_transcoding,
            enable_video_playback_transcoding=enable_video_playback_transcoding,
            enable_playback_remuxing=enable_playback_remuxing,
            force_remote_source_transcoding=force_remote_source_transcoding,
            enable_content_deletion=enable_content_deletion,
            enable_content_deletion_from_folders=enable_content_deletion_from_folders,
            enable_content_downloading=enable_content_downloading,
            enable_sync_transcoding=enable_sync_transcoding,
            enable_media_conversion=enable_media_conversion,
            enabled_devices=enabled_devices,
            enable_all_devices=enable_all_devices,
            enabled_channels=enabled_channels,
            enable_all_channels=enable_all_channels,
            enabled_folders=enabled_folders,
            enable_all_folders=enable_all_folders,
            invalid_login_attempt_count=invalid_login_attempt_count,
            login_attempts_before_lockout=login_attempts_before_lockout,
            max_active_sessions=max_active_sessions,
            enable_public_sharing=enable_public_sharing,
            blocked_media_folders=blocked_media_folders,
            blocked_channels=blocked_channels,
            remote_client_bitrate_limit=remote_client_bitrate_limit,
            authentication_provider_id=authentication_provider_id,
            password_reset_provider_id=password_reset_provider_id,
            sync_play_access=sync_play_access,
        )

        return user_policy
