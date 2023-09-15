from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePlaylistDto")


@_attrs_define
class CreatePlaylistDto:
    """Create new playlist dto.

    Attributes:
        name (Union[Unset, None, str]): Gets or sets the name of the new playlist.
        ids (Union[Unset, List[str]]): Gets or sets item ids to add to the playlist.
        user_id (Union[Unset, None, str]): Gets or sets the user id.
        media_type (Union[Unset, None, str]): Gets or sets the media type.
    """

    name: Union[Unset, None, str] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    media_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        user_id = self.user_id
        media_type = self.media_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        ids = cast(List[str], d.pop("Ids", UNSET))

        user_id = d.pop("UserId", UNSET)

        media_type = d.pop("MediaType", UNSET)

        create_playlist_dto = cls(
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
        )

        return create_playlist_dto
