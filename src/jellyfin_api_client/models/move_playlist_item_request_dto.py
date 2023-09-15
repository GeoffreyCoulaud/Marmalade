from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MovePlaylistItemRequestDto")


@_attrs_define
class MovePlaylistItemRequestDto:
    """Class MovePlaylistItemRequestDto.

    Attributes:
        playlist_item_id (Union[Unset, str]): Gets or sets the playlist identifier of the item.
        new_index (Union[Unset, int]): Gets or sets the new position.
    """

    playlist_item_id: Union[Unset, str] = UNSET
    new_index: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        playlist_item_id = self.playlist_item_id
        new_index = self.new_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if new_index is not UNSET:
            field_dict["NewIndex"] = new_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        new_index = d.pop("NewIndex", UNSET)

        move_playlist_item_request_dto = cls(
            playlist_item_id=playlist_item_id,
            new_index=new_index,
        )

        return move_playlist_item_request_dto
