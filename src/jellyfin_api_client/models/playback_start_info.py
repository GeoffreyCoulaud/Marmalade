from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.play_method import PlayMethod
from ..models.repeat_mode import RepeatMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto
    from ..models.queue_item import QueueItem


T = TypeVar("T", bound="PlaybackStartInfo")


@_attrs_define
class PlaybackStartInfo:
    """Class PlaybackStartInfo.

    Attributes:
        can_seek (Union[Unset, bool]): Gets or sets a value indicating whether this instance can seek.
        item (Union[Unset, None, BaseItemDto]): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        item_id (Union[Unset, str]): Gets or sets the item identifier.
        session_id (Union[Unset, None, str]): Gets or sets the session id.
        media_source_id (Union[Unset, None, str]): Gets or sets the media version identifier.
        audio_stream_index (Union[Unset, None, int]): Gets or sets the index of the audio stream.
        subtitle_stream_index (Union[Unset, None, int]): Gets or sets the index of the subtitle stream.
        is_paused (Union[Unset, bool]): Gets or sets a value indicating whether this instance is paused.
        is_muted (Union[Unset, bool]): Gets or sets a value indicating whether this instance is muted.
        position_ticks (Union[Unset, None, int]): Gets or sets the position ticks.
        playback_start_time_ticks (Union[Unset, None, int]):
        volume_level (Union[Unset, None, int]): Gets or sets the volume level.
        brightness (Union[Unset, None, int]):
        aspect_ratio (Union[Unset, None, str]):
        play_method (Union[Unset, PlayMethod]):
        live_stream_id (Union[Unset, None, str]): Gets or sets the live stream identifier.
        play_session_id (Union[Unset, None, str]): Gets or sets the play session identifier.
        repeat_mode (Union[Unset, RepeatMode]):
        now_playing_queue (Union[Unset, None, List['QueueItem']]):
        playlist_item_id (Union[Unset, None, str]):
    """

    can_seek: Union[Unset, bool] = UNSET
    item: Union[Unset, None, "BaseItemDto"] = UNSET
    item_id: Union[Unset, str] = UNSET
    session_id: Union[Unset, None, str] = UNSET
    media_source_id: Union[Unset, None, str] = UNSET
    audio_stream_index: Union[Unset, None, int] = UNSET
    subtitle_stream_index: Union[Unset, None, int] = UNSET
    is_paused: Union[Unset, bool] = UNSET
    is_muted: Union[Unset, bool] = UNSET
    position_ticks: Union[Unset, None, int] = UNSET
    playback_start_time_ticks: Union[Unset, None, int] = UNSET
    volume_level: Union[Unset, None, int] = UNSET
    brightness: Union[Unset, None, int] = UNSET
    aspect_ratio: Union[Unset, None, str] = UNSET
    play_method: Union[Unset, PlayMethod] = UNSET
    live_stream_id: Union[Unset, None, str] = UNSET
    play_session_id: Union[Unset, None, str] = UNSET
    repeat_mode: Union[Unset, RepeatMode] = UNSET
    now_playing_queue: Union[Unset, None, List["QueueItem"]] = UNSET
    playlist_item_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        can_seek = self.can_seek
        item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict() if self.item else None

        item_id = self.item_id
        session_id = self.session_id
        media_source_id = self.media_source_id
        audio_stream_index = self.audio_stream_index
        subtitle_stream_index = self.subtitle_stream_index
        is_paused = self.is_paused
        is_muted = self.is_muted
        position_ticks = self.position_ticks
        playback_start_time_ticks = self.playback_start_time_ticks
        volume_level = self.volume_level
        brightness = self.brightness
        aspect_ratio = self.aspect_ratio
        play_method: Union[Unset, str] = UNSET
        if not isinstance(self.play_method, Unset):
            play_method = self.play_method.value

        live_stream_id = self.live_stream_id
        play_session_id = self.play_session_id
        repeat_mode: Union[Unset, str] = UNSET
        if not isinstance(self.repeat_mode, Unset):
            repeat_mode = self.repeat_mode.value

        now_playing_queue: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.now_playing_queue, Unset):
            if self.now_playing_queue is None:
                now_playing_queue = None
            else:
                now_playing_queue = []
                for now_playing_queue_item_data in self.now_playing_queue:
                    now_playing_queue_item = now_playing_queue_item_data.to_dict()

                    now_playing_queue.append(now_playing_queue_item)

        playlist_item_id = self.playlist_item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if can_seek is not UNSET:
            field_dict["CanSeek"] = can_seek
        if item is not UNSET:
            field_dict["Item"] = item
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if session_id is not UNSET:
            field_dict["SessionId"] = session_id
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if is_paused is not UNSET:
            field_dict["IsPaused"] = is_paused
        if is_muted is not UNSET:
            field_dict["IsMuted"] = is_muted
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if playback_start_time_ticks is not UNSET:
            field_dict["PlaybackStartTimeTicks"] = playback_start_time_ticks
        if volume_level is not UNSET:
            field_dict["VolumeLevel"] = volume_level
        if brightness is not UNSET:
            field_dict["Brightness"] = brightness
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if play_method is not UNSET:
            field_dict["PlayMethod"] = play_method
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if repeat_mode is not UNSET:
            field_dict["RepeatMode"] = repeat_mode
        if now_playing_queue is not UNSET:
            field_dict["NowPlayingQueue"] = now_playing_queue
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto
        from ..models.queue_item import QueueItem

        d = src_dict.copy()
        can_seek = d.pop("CanSeek", UNSET)

        _item = d.pop("Item", UNSET)
        item: Union[Unset, None, BaseItemDto]
        if _item is None:
            item = None
        elif isinstance(_item, Unset):
            item = UNSET
        else:
            item = BaseItemDto.from_dict(_item)

        item_id = d.pop("ItemId", UNSET)

        session_id = d.pop("SessionId", UNSET)

        media_source_id = d.pop("MediaSourceId", UNSET)

        audio_stream_index = d.pop("AudioStreamIndex", UNSET)

        subtitle_stream_index = d.pop("SubtitleStreamIndex", UNSET)

        is_paused = d.pop("IsPaused", UNSET)

        is_muted = d.pop("IsMuted", UNSET)

        position_ticks = d.pop("PositionTicks", UNSET)

        playback_start_time_ticks = d.pop("PlaybackStartTimeTicks", UNSET)

        volume_level = d.pop("VolumeLevel", UNSET)

        brightness = d.pop("Brightness", UNSET)

        aspect_ratio = d.pop("AspectRatio", UNSET)

        _play_method = d.pop("PlayMethod", UNSET)
        play_method: Union[Unset, PlayMethod]
        if isinstance(_play_method, Unset):
            play_method = UNSET
        else:
            play_method = PlayMethod(_play_method)

        live_stream_id = d.pop("LiveStreamId", UNSET)

        play_session_id = d.pop("PlaySessionId", UNSET)

        _repeat_mode = d.pop("RepeatMode", UNSET)
        repeat_mode: Union[Unset, RepeatMode]
        if isinstance(_repeat_mode, Unset):
            repeat_mode = UNSET
        else:
            repeat_mode = RepeatMode(_repeat_mode)

        now_playing_queue = []
        _now_playing_queue = d.pop("NowPlayingQueue", UNSET)
        for now_playing_queue_item_data in _now_playing_queue or []:
            now_playing_queue_item = QueueItem.from_dict(now_playing_queue_item_data)

            now_playing_queue.append(now_playing_queue_item)

        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        playback_start_info = cls(
            can_seek=can_seek,
            item=item,
            item_id=item_id,
            session_id=session_id,
            media_source_id=media_source_id,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            is_paused=is_paused,
            is_muted=is_muted,
            position_ticks=position_ticks,
            playback_start_time_ticks=playback_start_time_ticks,
            volume_level=volume_level,
            brightness=brightness,
            aspect_ratio=aspect_ratio,
            play_method=play_method,
            live_stream_id=live_stream_id,
            play_session_id=play_session_id,
            repeat_mode=repeat_mode,
            now_playing_queue=now_playing_queue,
            playlist_item_id=playlist_item_id,
        )

        return playback_start_info
