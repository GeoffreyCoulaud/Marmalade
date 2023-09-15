from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.group_queue_mode import GroupQueueMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueRequestDto")


@_attrs_define
class QueueRequestDto:
    """Class QueueRequestDto.

    Attributes:
        item_ids (Union[Unset, List[str]]): Gets or sets the items to enqueue.
        mode (Union[Unset, GroupQueueMode]): Enum GroupQueueMode.
    """

    item_ids: Union[Unset, List[str]] = UNSET
    mode: Union[Unset, GroupQueueMode] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = self.item_ids

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_ids = cast(List[str], d.pop("ItemIds", UNSET))

        _mode = d.pop("Mode", UNSET)
        mode: Union[Unset, GroupQueueMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GroupQueueMode(_mode)

        queue_request_dto = cls(
            item_ids=item_ids,
            mode=mode,
        )

        return queue_request_dto
