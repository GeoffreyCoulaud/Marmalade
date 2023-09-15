from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveFromPlaylistRequestDto")


@_attrs_define
class RemoveFromPlaylistRequestDto:
    """Class RemoveFromPlaylistRequestDto.

    Attributes:
        playlist_item_ids (Union[Unset, List[str]]): Gets or sets the playlist identifiers ot the items. Ignored when
            clearing the playlist.
        clear_playlist (Union[Unset, bool]): Gets or sets a value indicating whether the entire playlist should be
            cleared.
        clear_playing_item (Union[Unset, bool]): Gets or sets a value indicating whether the playing item should be
            removed as well. Used only when clearing the playlist.
    """

    playlist_item_ids: Union[Unset, List[str]] = UNSET
    clear_playlist: Union[Unset, bool] = UNSET
    clear_playing_item: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        playlist_item_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.playlist_item_ids, Unset):
            playlist_item_ids = self.playlist_item_ids

        clear_playlist = self.clear_playlist
        clear_playing_item = self.clear_playing_item

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if playlist_item_ids is not UNSET:
            field_dict["PlaylistItemIds"] = playlist_item_ids
        if clear_playlist is not UNSET:
            field_dict["ClearPlaylist"] = clear_playlist
        if clear_playing_item is not UNSET:
            field_dict["ClearPlayingItem"] = clear_playing_item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        playlist_item_ids = cast(List[str], d.pop("PlaylistItemIds", UNSET))

        clear_playlist = d.pop("ClearPlaylist", UNSET)

        clear_playing_item = d.pop("ClearPlayingItem", UNSET)

        remove_from_playlist_request_dto = cls(
            playlist_item_ids=playlist_item_ids,
            clear_playlist=clear_playlist,
            clear_playing_item=clear_playing_item,
        )

        return remove_from_playlist_request_dto
