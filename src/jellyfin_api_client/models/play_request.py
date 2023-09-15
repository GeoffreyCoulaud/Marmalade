from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.play_command import PlayCommand
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayRequest")


@_attrs_define
class PlayRequest:
    """Class PlayRequest.

    Attributes:
        item_ids (Union[Unset, None, List[str]]): Gets or sets the item ids.
        start_position_ticks (Union[Unset, None, int]): Gets or sets the start position ticks that the first item should
            be played at.
        play_command (Union[Unset, PlayCommand]): Enum PlayCommand.
        controlling_user_id (Union[Unset, str]): Gets or sets the controlling user identifier.
        subtitle_stream_index (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
    """

    item_ids: Union[Unset, None, List[str]] = UNSET
    start_position_ticks: Union[Unset, None, int] = UNSET
    play_command: Union[Unset, PlayCommand] = UNSET
    controlling_user_id: Union[Unset, str] = UNSET
    subtitle_stream_index: Union[Unset, None, int] = UNSET
    audio_stream_index: Union[Unset, None, int] = UNSET
    media_source_id: Union[Unset, None, str] = UNSET
    start_index: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.item_ids, Unset):
            if self.item_ids is None:
                item_ids = None
            else:
                item_ids = self.item_ids

        start_position_ticks = self.start_position_ticks
        play_command: Union[Unset, str] = UNSET
        if not isinstance(self.play_command, Unset):
            play_command = self.play_command.value

        controlling_user_id = self.controlling_user_id
        subtitle_stream_index = self.subtitle_stream_index
        audio_stream_index = self.audio_stream_index
        media_source_id = self.media_source_id
        start_index = self.start_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks
        if play_command is not UNSET:
            field_dict["PlayCommand"] = play_command
        if controlling_user_id is not UNSET:
            field_dict["ControllingUserId"] = controlling_user_id
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_ids = cast(List[str], d.pop("ItemIds", UNSET))

        start_position_ticks = d.pop("StartPositionTicks", UNSET)

        _play_command = d.pop("PlayCommand", UNSET)
        play_command: Union[Unset, PlayCommand]
        if isinstance(_play_command, Unset):
            play_command = UNSET
        else:
            play_command = PlayCommand(_play_command)

        controlling_user_id = d.pop("ControllingUserId", UNSET)

        subtitle_stream_index = d.pop("SubtitleStreamIndex", UNSET)

        audio_stream_index = d.pop("AudioStreamIndex", UNSET)

        media_source_id = d.pop("MediaSourceId", UNSET)

        start_index = d.pop("StartIndex", UNSET)

        play_request = cls(
            item_ids=item_ids,
            start_position_ticks=start_position_ticks,
            play_command=play_command,
            controlling_user_id=controlling_user_id,
            subtitle_stream_index=subtitle_stream_index,
            audio_stream_index=audio_stream_index,
            media_source_id=media_source_id,
            start_index=start_index,
        )

        return play_request
