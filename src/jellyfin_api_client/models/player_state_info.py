from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.play_method import PlayMethod
from ..models.repeat_mode import RepeatMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerStateInfo")


@_attrs_define
class PlayerStateInfo:
    """
    Attributes:
        position_ticks (Union[Unset, None, int]): Gets or sets the now playing position ticks.
        can_seek (Union[Unset, bool]): Gets or sets a value indicating whether this instance can seek.
        is_paused (Union[Unset, bool]): Gets or sets a value indicating whether this instance is paused.
        is_muted (Union[Unset, bool]): Gets or sets a value indicating whether this instance is muted.
        volume_level (Union[Unset, None, int]): Gets or sets the volume level.
        audio_stream_index (Union[Unset, None, int]): Gets or sets the index of the now playing audio stream.
        subtitle_stream_index (Union[Unset, None, int]): Gets or sets the index of the now playing subtitle stream.
        media_source_id (Union[Unset, None, str]): Gets or sets the now playing media version identifier.
        play_method (Union[Unset, None, PlayMethod]):
        repeat_mode (Union[Unset, RepeatMode]):
        live_stream_id (Union[Unset, None, str]): Gets or sets the now playing live stream identifier.
    """

    position_ticks: Union[Unset, None, int] = UNSET
    can_seek: Union[Unset, bool] = UNSET
    is_paused: Union[Unset, bool] = UNSET
    is_muted: Union[Unset, bool] = UNSET
    volume_level: Union[Unset, None, int] = UNSET
    audio_stream_index: Union[Unset, None, int] = UNSET
    subtitle_stream_index: Union[Unset, None, int] = UNSET
    media_source_id: Union[Unset, None, str] = UNSET
    play_method: Union[Unset, None, PlayMethod] = UNSET
    repeat_mode: Union[Unset, RepeatMode] = UNSET
    live_stream_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        position_ticks = self.position_ticks
        can_seek = self.can_seek
        is_paused = self.is_paused
        is_muted = self.is_muted
        volume_level = self.volume_level
        audio_stream_index = self.audio_stream_index
        subtitle_stream_index = self.subtitle_stream_index
        media_source_id = self.media_source_id
        play_method: Union[Unset, None, str] = UNSET
        if not isinstance(self.play_method, Unset):
            play_method = self.play_method.value if self.play_method else None

        repeat_mode: Union[Unset, str] = UNSET
        if not isinstance(self.repeat_mode, Unset):
            repeat_mode = self.repeat_mode.value

        live_stream_id = self.live_stream_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if can_seek is not UNSET:
            field_dict["CanSeek"] = can_seek
        if is_paused is not UNSET:
            field_dict["IsPaused"] = is_paused
        if is_muted is not UNSET:
            field_dict["IsMuted"] = is_muted
        if volume_level is not UNSET:
            field_dict["VolumeLevel"] = volume_level
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if play_method is not UNSET:
            field_dict["PlayMethod"] = play_method
        if repeat_mode is not UNSET:
            field_dict["RepeatMode"] = repeat_mode
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position_ticks = d.pop("PositionTicks", UNSET)

        can_seek = d.pop("CanSeek", UNSET)

        is_paused = d.pop("IsPaused", UNSET)

        is_muted = d.pop("IsMuted", UNSET)

        volume_level = d.pop("VolumeLevel", UNSET)

        audio_stream_index = d.pop("AudioStreamIndex", UNSET)

        subtitle_stream_index = d.pop("SubtitleStreamIndex", UNSET)

        media_source_id = d.pop("MediaSourceId", UNSET)

        _play_method = d.pop("PlayMethod", UNSET)
        play_method: Union[Unset, None, PlayMethod]
        if _play_method is None:
            play_method = None
        elif isinstance(_play_method, Unset):
            play_method = UNSET
        else:
            play_method = PlayMethod(_play_method)

        _repeat_mode = d.pop("RepeatMode", UNSET)
        repeat_mode: Union[Unset, RepeatMode]
        if isinstance(_repeat_mode, Unset):
            repeat_mode = UNSET
        else:
            repeat_mode = RepeatMode(_repeat_mode)

        live_stream_id = d.pop("LiveStreamId", UNSET)

        player_state_info = cls(
            position_ticks=position_ticks,
            can_seek=can_seek,
            is_paused=is_paused,
            is_muted=is_muted,
            volume_level=volume_level,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            media_source_id=media_source_id,
            play_method=play_method,
            repeat_mode=repeat_mode,
            live_stream_id=live_stream_id,
        )

        return player_state_info
