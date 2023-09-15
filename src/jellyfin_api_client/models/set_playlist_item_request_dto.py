from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetPlaylistItemRequestDto")


@_attrs_define
class SetPlaylistItemRequestDto:
    """Class SetPlaylistItemRequestDto.

    Attributes:
        playlist_item_id (Union[Unset, str]): Gets or sets the playlist identifier of the playing item.
    """

    playlist_item_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        playlist_item_id = self.playlist_item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        set_playlist_item_request_dto = cls(
            playlist_item_id=playlist_item_id,
        )

        return set_playlist_item_request_dto
