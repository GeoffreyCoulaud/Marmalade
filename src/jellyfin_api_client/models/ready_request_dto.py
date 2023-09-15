import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadyRequestDto")


@_attrs_define
class ReadyRequestDto:
    """Class ReadyRequest.

    Attributes:
        when (Union[Unset, datetime.datetime]): Gets or sets when the request has been made by the client.
        position_ticks (Union[Unset, int]): Gets or sets the position ticks.
        is_playing (Union[Unset, bool]): Gets or sets a value indicating whether the client playback is unpaused.
        playlist_item_id (Union[Unset, str]): Gets or sets the playlist item identifier of the playing item.
    """

    when: Union[Unset, datetime.datetime] = UNSET
    position_ticks: Union[Unset, int] = UNSET
    is_playing: Union[Unset, bool] = UNSET
    playlist_item_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        when: Union[Unset, str] = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.isoformat()

        position_ticks = self.position_ticks
        is_playing = self.is_playing
        playlist_item_id = self.playlist_item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if when is not UNSET:
            field_dict["When"] = when
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if is_playing is not UNSET:
            field_dict["IsPlaying"] = is_playing
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _when = d.pop("When", UNSET)
        when: Union[Unset, datetime.datetime]
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = isoparse(_when)

        position_ticks = d.pop("PositionTicks", UNSET)

        is_playing = d.pop("IsPlaying", UNSET)

        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        ready_request_dto = cls(
            when=when,
            position_ticks=position_ticks,
            is_playing=is_playing,
            playlist_item_id=playlist_item_id,
        )

        return ready_request_dto
