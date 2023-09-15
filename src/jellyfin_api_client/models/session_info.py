import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.general_command_type import GeneralCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item import BaseItem
    from ..models.base_item_dto import BaseItemDto
    from ..models.client_capabilities import ClientCapabilities
    from ..models.player_state_info import PlayerStateInfo
    from ..models.queue_item import QueueItem
    from ..models.session_user_info import SessionUserInfo
    from ..models.transcoding_info import TranscodingInfo


T = TypeVar("T", bound="SessionInfo")


@_attrs_define
class SessionInfo:
    """Class SessionInfo.

    Attributes:
        play_state (Union[Unset, None, PlayerStateInfo]):
        additional_users (Union[Unset, None, List['SessionUserInfo']]):
        capabilities (Union[Unset, None, ClientCapabilities]):
        remote_end_point (Union[Unset, None, str]): Gets or sets the remote end point.
        playable_media_types (Union[Unset, None, List[str]]): Gets the playable media types.
        id (Union[Unset, None, str]): Gets or sets the id.
        user_id (Union[Unset, str]): Gets or sets the user id.
        user_name (Union[Unset, None, str]): Gets or sets the username.
        client (Union[Unset, None, str]): Gets or sets the type of the client.
        last_activity_date (Union[Unset, datetime.datetime]): Gets or sets the last activity date.
        last_playback_check_in (Union[Unset, datetime.datetime]): Gets or sets the last playback check in.
        device_name (Union[Unset, None, str]): Gets or sets the name of the device.
        device_type (Union[Unset, None, str]): Gets or sets the type of the device.
        now_playing_item (Union[Unset, None, BaseItemDto]): This is strictly used as a data transfer object from the api
            layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        full_now_playing_item (Union[Unset, None, BaseItem]): Class BaseItem.
        now_viewing_item (Union[Unset, None, BaseItemDto]): This is strictly used as a data transfer object from the api
            layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        device_id (Union[Unset, None, str]): Gets or sets the device id.
        application_version (Union[Unset, None, str]): Gets or sets the application version.
        transcoding_info (Union[Unset, None, TranscodingInfo]):
        is_active (Union[Unset, bool]): Gets a value indicating whether this instance is active.
        supports_media_control (Union[Unset, bool]):
        supports_remote_control (Union[Unset, bool]):
        now_playing_queue (Union[Unset, None, List['QueueItem']]):
        now_playing_queue_full_items (Union[Unset, None, List['BaseItemDto']]):
        has_custom_device_name (Union[Unset, bool]):
        playlist_item_id (Union[Unset, None, str]):
        server_id (Union[Unset, None, str]):
        user_primary_image_tag (Union[Unset, None, str]):
        supported_commands (Union[Unset, None, List[GeneralCommandType]]): Gets the supported commands.
    """

    play_state: Union[Unset, None, "PlayerStateInfo"] = UNSET
    additional_users: Union[Unset, None, List["SessionUserInfo"]] = UNSET
    capabilities: Union[Unset, None, "ClientCapabilities"] = UNSET
    remote_end_point: Union[Unset, None, str] = UNSET
    playable_media_types: Union[Unset, None, List[str]] = UNSET
    id: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    client: Union[Unset, None, str] = UNSET
    last_activity_date: Union[Unset, datetime.datetime] = UNSET
    last_playback_check_in: Union[Unset, datetime.datetime] = UNSET
    device_name: Union[Unset, None, str] = UNSET
    device_type: Union[Unset, None, str] = UNSET
    now_playing_item: Union[Unset, None, "BaseItemDto"] = UNSET
    full_now_playing_item: Union[Unset, None, "BaseItem"] = UNSET
    now_viewing_item: Union[Unset, None, "BaseItemDto"] = UNSET
    device_id: Union[Unset, None, str] = UNSET
    application_version: Union[Unset, None, str] = UNSET
    transcoding_info: Union[Unset, None, "TranscodingInfo"] = UNSET
    is_active: Union[Unset, bool] = UNSET
    supports_media_control: Union[Unset, bool] = UNSET
    supports_remote_control: Union[Unset, bool] = UNSET
    now_playing_queue: Union[Unset, None, List["QueueItem"]] = UNSET
    now_playing_queue_full_items: Union[Unset, None, List["BaseItemDto"]] = UNSET
    has_custom_device_name: Union[Unset, bool] = UNSET
    playlist_item_id: Union[Unset, None, str] = UNSET
    server_id: Union[Unset, None, str] = UNSET
    user_primary_image_tag: Union[Unset, None, str] = UNSET
    supported_commands: Union[Unset, None, List[GeneralCommandType]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        play_state: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.play_state, Unset):
            play_state = self.play_state.to_dict() if self.play_state else None

        additional_users: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_users, Unset):
            if self.additional_users is None:
                additional_users = None
            else:
                additional_users = []
                for additional_users_item_data in self.additional_users:
                    additional_users_item = additional_users_item_data.to_dict()

                    additional_users.append(additional_users_item)

        capabilities: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict() if self.capabilities else None

        remote_end_point = self.remote_end_point
        playable_media_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.playable_media_types, Unset):
            if self.playable_media_types is None:
                playable_media_types = None
            else:
                playable_media_types = self.playable_media_types

        id = self.id
        user_id = self.user_id
        user_name = self.user_name
        client = self.client
        last_activity_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_activity_date, Unset):
            last_activity_date = self.last_activity_date.isoformat()

        last_playback_check_in: Union[Unset, str] = UNSET
        if not isinstance(self.last_playback_check_in, Unset):
            last_playback_check_in = self.last_playback_check_in.isoformat()

        device_name = self.device_name
        device_type = self.device_type
        now_playing_item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.now_playing_item, Unset):
            now_playing_item = self.now_playing_item.to_dict() if self.now_playing_item else None

        full_now_playing_item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.full_now_playing_item, Unset):
            full_now_playing_item = self.full_now_playing_item.to_dict() if self.full_now_playing_item else None

        now_viewing_item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.now_viewing_item, Unset):
            now_viewing_item = self.now_viewing_item.to_dict() if self.now_viewing_item else None

        device_id = self.device_id
        application_version = self.application_version
        transcoding_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.transcoding_info, Unset):
            transcoding_info = self.transcoding_info.to_dict() if self.transcoding_info else None

        is_active = self.is_active
        supports_media_control = self.supports_media_control
        supports_remote_control = self.supports_remote_control
        now_playing_queue: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.now_playing_queue, Unset):
            if self.now_playing_queue is None:
                now_playing_queue = None
            else:
                now_playing_queue = []
                for now_playing_queue_item_data in self.now_playing_queue:
                    now_playing_queue_item = now_playing_queue_item_data.to_dict()

                    now_playing_queue.append(now_playing_queue_item)

        now_playing_queue_full_items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.now_playing_queue_full_items, Unset):
            if self.now_playing_queue_full_items is None:
                now_playing_queue_full_items = None
            else:
                now_playing_queue_full_items = []
                for now_playing_queue_full_items_item_data in self.now_playing_queue_full_items:
                    now_playing_queue_full_items_item = now_playing_queue_full_items_item_data.to_dict()

                    now_playing_queue_full_items.append(now_playing_queue_full_items_item)

        has_custom_device_name = self.has_custom_device_name
        playlist_item_id = self.playlist_item_id
        server_id = self.server_id
        user_primary_image_tag = self.user_primary_image_tag
        supported_commands: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.supported_commands, Unset):
            if self.supported_commands is None:
                supported_commands = None
            else:
                supported_commands = []
                for supported_commands_item_data in self.supported_commands:
                    supported_commands_item = supported_commands_item_data.value

                    supported_commands.append(supported_commands_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if play_state is not UNSET:
            field_dict["PlayState"] = play_state
        if additional_users is not UNSET:
            field_dict["AdditionalUsers"] = additional_users
        if capabilities is not UNSET:
            field_dict["Capabilities"] = capabilities
        if remote_end_point is not UNSET:
            field_dict["RemoteEndPoint"] = remote_end_point
        if playable_media_types is not UNSET:
            field_dict["PlayableMediaTypes"] = playable_media_types
        if id is not UNSET:
            field_dict["Id"] = id
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name
        if client is not UNSET:
            field_dict["Client"] = client
        if last_activity_date is not UNSET:
            field_dict["LastActivityDate"] = last_activity_date
        if last_playback_check_in is not UNSET:
            field_dict["LastPlaybackCheckIn"] = last_playback_check_in
        if device_name is not UNSET:
            field_dict["DeviceName"] = device_name
        if device_type is not UNSET:
            field_dict["DeviceType"] = device_type
        if now_playing_item is not UNSET:
            field_dict["NowPlayingItem"] = now_playing_item
        if full_now_playing_item is not UNSET:
            field_dict["FullNowPlayingItem"] = full_now_playing_item
        if now_viewing_item is not UNSET:
            field_dict["NowViewingItem"] = now_viewing_item
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if application_version is not UNSET:
            field_dict["ApplicationVersion"] = application_version
        if transcoding_info is not UNSET:
            field_dict["TranscodingInfo"] = transcoding_info
        if is_active is not UNSET:
            field_dict["IsActive"] = is_active
        if supports_media_control is not UNSET:
            field_dict["SupportsMediaControl"] = supports_media_control
        if supports_remote_control is not UNSET:
            field_dict["SupportsRemoteControl"] = supports_remote_control
        if now_playing_queue is not UNSET:
            field_dict["NowPlayingQueue"] = now_playing_queue
        if now_playing_queue_full_items is not UNSET:
            field_dict["NowPlayingQueueFullItems"] = now_playing_queue_full_items
        if has_custom_device_name is not UNSET:
            field_dict["HasCustomDeviceName"] = has_custom_device_name
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id
        if user_primary_image_tag is not UNSET:
            field_dict["UserPrimaryImageTag"] = user_primary_image_tag
        if supported_commands is not UNSET:
            field_dict["SupportedCommands"] = supported_commands

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item import BaseItem
        from ..models.base_item_dto import BaseItemDto
        from ..models.client_capabilities import ClientCapabilities
        from ..models.player_state_info import PlayerStateInfo
        from ..models.queue_item import QueueItem
        from ..models.session_user_info import SessionUserInfo
        from ..models.transcoding_info import TranscodingInfo

        d = src_dict.copy()
        _play_state = d.pop("PlayState", UNSET)
        play_state: Union[Unset, None, PlayerStateInfo]
        if _play_state is None:
            play_state = None
        elif isinstance(_play_state, Unset):
            play_state = UNSET
        else:
            play_state = PlayerStateInfo.from_dict(_play_state)

        additional_users = []
        _additional_users = d.pop("AdditionalUsers", UNSET)
        for additional_users_item_data in _additional_users or []:
            additional_users_item = SessionUserInfo.from_dict(additional_users_item_data)

            additional_users.append(additional_users_item)

        _capabilities = d.pop("Capabilities", UNSET)
        capabilities: Union[Unset, None, ClientCapabilities]
        if _capabilities is None:
            capabilities = None
        elif isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = ClientCapabilities.from_dict(_capabilities)

        remote_end_point = d.pop("RemoteEndPoint", UNSET)

        playable_media_types = cast(List[str], d.pop("PlayableMediaTypes", UNSET))

        id = d.pop("Id", UNSET)

        user_id = d.pop("UserId", UNSET)

        user_name = d.pop("UserName", UNSET)

        client = d.pop("Client", UNSET)

        _last_activity_date = d.pop("LastActivityDate", UNSET)
        last_activity_date: Union[Unset, datetime.datetime]
        if isinstance(_last_activity_date, Unset):
            last_activity_date = UNSET
        else:
            last_activity_date = isoparse(_last_activity_date)

        _last_playback_check_in = d.pop("LastPlaybackCheckIn", UNSET)
        last_playback_check_in: Union[Unset, datetime.datetime]
        if isinstance(_last_playback_check_in, Unset):
            last_playback_check_in = UNSET
        else:
            last_playback_check_in = isoparse(_last_playback_check_in)

        device_name = d.pop("DeviceName", UNSET)

        device_type = d.pop("DeviceType", UNSET)

        _now_playing_item = d.pop("NowPlayingItem", UNSET)
        now_playing_item: Union[Unset, None, BaseItemDto]
        if _now_playing_item is None:
            now_playing_item = None
        elif isinstance(_now_playing_item, Unset):
            now_playing_item = UNSET
        else:
            now_playing_item = BaseItemDto.from_dict(_now_playing_item)

        _full_now_playing_item = d.pop("FullNowPlayingItem", UNSET)
        full_now_playing_item: Union[Unset, None, BaseItem]
        if _full_now_playing_item is None:
            full_now_playing_item = None
        elif isinstance(_full_now_playing_item, Unset):
            full_now_playing_item = UNSET
        else:
            full_now_playing_item = BaseItem.from_dict(_full_now_playing_item)

        _now_viewing_item = d.pop("NowViewingItem", UNSET)
        now_viewing_item: Union[Unset, None, BaseItemDto]
        if _now_viewing_item is None:
            now_viewing_item = None
        elif isinstance(_now_viewing_item, Unset):
            now_viewing_item = UNSET
        else:
            now_viewing_item = BaseItemDto.from_dict(_now_viewing_item)

        device_id = d.pop("DeviceId", UNSET)

        application_version = d.pop("ApplicationVersion", UNSET)

        _transcoding_info = d.pop("TranscodingInfo", UNSET)
        transcoding_info: Union[Unset, None, TranscodingInfo]
        if _transcoding_info is None:
            transcoding_info = None
        elif isinstance(_transcoding_info, Unset):
            transcoding_info = UNSET
        else:
            transcoding_info = TranscodingInfo.from_dict(_transcoding_info)

        is_active = d.pop("IsActive", UNSET)

        supports_media_control = d.pop("SupportsMediaControl", UNSET)

        supports_remote_control = d.pop("SupportsRemoteControl", UNSET)

        now_playing_queue = []
        _now_playing_queue = d.pop("NowPlayingQueue", UNSET)
        for now_playing_queue_item_data in _now_playing_queue or []:
            now_playing_queue_item = QueueItem.from_dict(now_playing_queue_item_data)

            now_playing_queue.append(now_playing_queue_item)

        now_playing_queue_full_items = []
        _now_playing_queue_full_items = d.pop("NowPlayingQueueFullItems", UNSET)
        for now_playing_queue_full_items_item_data in _now_playing_queue_full_items or []:
            now_playing_queue_full_items_item = BaseItemDto.from_dict(now_playing_queue_full_items_item_data)

            now_playing_queue_full_items.append(now_playing_queue_full_items_item)

        has_custom_device_name = d.pop("HasCustomDeviceName", UNSET)

        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        server_id = d.pop("ServerId", UNSET)

        user_primary_image_tag = d.pop("UserPrimaryImageTag", UNSET)

        supported_commands = []
        _supported_commands = d.pop("SupportedCommands", UNSET)
        for supported_commands_item_data in _supported_commands or []:
            supported_commands_item = GeneralCommandType(supported_commands_item_data)

            supported_commands.append(supported_commands_item)

        session_info = cls(
            play_state=play_state,
            additional_users=additional_users,
            capabilities=capabilities,
            remote_end_point=remote_end_point,
            playable_media_types=playable_media_types,
            id=id,
            user_id=user_id,
            user_name=user_name,
            client=client,
            last_activity_date=last_activity_date,
            last_playback_check_in=last_playback_check_in,
            device_name=device_name,
            device_type=device_type,
            now_playing_item=now_playing_item,
            full_now_playing_item=full_now_playing_item,
            now_viewing_item=now_viewing_item,
            device_id=device_id,
            application_version=application_version,
            transcoding_info=transcoding_info,
            is_active=is_active,
            supports_media_control=supports_media_control,
            supports_remote_control=supports_remote_control,
            now_playing_queue=now_playing_queue,
            now_playing_queue_full_items=now_playing_queue_full_items,
            has_custom_device_name=has_custom_device_name,
            playlist_item_id=playlist_item_id,
            server_id=server_id,
            user_primary_image_tag=user_primary_image_tag,
            supported_commands=supported_commands,
        )

        return session_info
