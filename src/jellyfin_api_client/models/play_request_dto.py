from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayRequestDto")


@_attrs_define
class PlayRequestDto:
    """Class PlayRequestDto.

    Attributes:
        playing_queue (Union[Unset, List[str]]): Gets or sets the playing queue.
        playing_item_position (Union[Unset, int]): Gets or sets the position of the playing item in the queue.
        start_position_ticks (Union[Unset, int]): Gets or sets the start position ticks.
    """

    playing_queue: Union[Unset, List[str]] = UNSET
    playing_item_position: Union[Unset, int] = UNSET
    start_position_ticks: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        playing_queue: Union[Unset, List[str]] = UNSET
        if not isinstance(self.playing_queue, Unset):
            playing_queue = self.playing_queue

        playing_item_position = self.playing_item_position
        start_position_ticks = self.start_position_ticks

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if playing_queue is not UNSET:
            field_dict["PlayingQueue"] = playing_queue
        if playing_item_position is not UNSET:
            field_dict["PlayingItemPosition"] = playing_item_position
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        playing_queue = cast(List[str], d.pop("PlayingQueue", UNSET))

        playing_item_position = d.pop("PlayingItemPosition", UNSET)

        start_position_ticks = d.pop("StartPositionTicks", UNSET)

        play_request_dto = cls(
            playing_queue=playing_queue,
            playing_item_position=playing_item_position,
            start_position_ticks=start_position_ticks,
        )

        return play_request_dto
