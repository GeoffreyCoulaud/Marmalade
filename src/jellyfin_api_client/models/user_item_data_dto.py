import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserItemDataDto")


@_attrs_define
class UserItemDataDto:
    """Class UserItemDataDto.

    Attributes:
        rating (Union[Unset, None, float]): Gets or sets the rating.
        played_percentage (Union[Unset, None, float]): Gets or sets the played percentage.
        unplayed_item_count (Union[Unset, None, int]): Gets or sets the unplayed item count.
        playback_position_ticks (Union[Unset, int]): Gets or sets the playback position ticks.
        play_count (Union[Unset, int]): Gets or sets the play count.
        is_favorite (Union[Unset, bool]): Gets or sets a value indicating whether this instance is favorite.
        likes (Union[Unset, None, bool]): Gets or sets a value indicating whether this
            MediaBrowser.Model.Dto.UserItemDataDto is likes.
        last_played_date (Union[Unset, None, datetime.datetime]): Gets or sets the last played date.
        played (Union[Unset, bool]): Gets or sets a value indicating whether this MediaBrowser.Model.Dto.UserItemDataDto
            is played.
        key (Union[Unset, None, str]): Gets or sets the key.
        item_id (Union[Unset, None, str]): Gets or sets the item identifier.
    """

    rating: Union[Unset, None, float] = UNSET
    played_percentage: Union[Unset, None, float] = UNSET
    unplayed_item_count: Union[Unset, None, int] = UNSET
    playback_position_ticks: Union[Unset, int] = UNSET
    play_count: Union[Unset, int] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    likes: Union[Unset, None, bool] = UNSET
    last_played_date: Union[Unset, None, datetime.datetime] = UNSET
    played: Union[Unset, bool] = UNSET
    key: Union[Unset, None, str] = UNSET
    item_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rating = self.rating
        played_percentage = self.played_percentage
        unplayed_item_count = self.unplayed_item_count
        playback_position_ticks = self.playback_position_ticks
        play_count = self.play_count
        is_favorite = self.is_favorite
        likes = self.likes
        last_played_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_played_date, Unset):
            last_played_date = self.last_played_date.isoformat() if self.last_played_date else None

        played = self.played
        key = self.key
        item_id = self.item_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if rating is not UNSET:
            field_dict["Rating"] = rating
        if played_percentage is not UNSET:
            field_dict["PlayedPercentage"] = played_percentage
        if unplayed_item_count is not UNSET:
            field_dict["UnplayedItemCount"] = unplayed_item_count
        if playback_position_ticks is not UNSET:
            field_dict["PlaybackPositionTicks"] = playback_position_ticks
        if play_count is not UNSET:
            field_dict["PlayCount"] = play_count
        if is_favorite is not UNSET:
            field_dict["IsFavorite"] = is_favorite
        if likes is not UNSET:
            field_dict["Likes"] = likes
        if last_played_date is not UNSET:
            field_dict["LastPlayedDate"] = last_played_date
        if played is not UNSET:
            field_dict["Played"] = played
        if key is not UNSET:
            field_dict["Key"] = key
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rating = d.pop("Rating", UNSET)

        played_percentage = d.pop("PlayedPercentage", UNSET)

        unplayed_item_count = d.pop("UnplayedItemCount", UNSET)

        playback_position_ticks = d.pop("PlaybackPositionTicks", UNSET)

        play_count = d.pop("PlayCount", UNSET)

        is_favorite = d.pop("IsFavorite", UNSET)

        likes = d.pop("Likes", UNSET)

        _last_played_date = d.pop("LastPlayedDate", UNSET)
        last_played_date: Union[Unset, None, datetime.datetime]
        if _last_played_date is None:
            last_played_date = None
        elif isinstance(_last_played_date, Unset):
            last_played_date = UNSET
        else:
            last_played_date = isoparse(_last_played_date)

        played = d.pop("Played", UNSET)

        key = d.pop("Key", UNSET)

        item_id = d.pop("ItemId", UNSET)

        user_item_data_dto = cls(
            rating=rating,
            played_percentage=played_percentage,
            unplayed_item_count=unplayed_item_count,
            playback_position_ticks=playback_position_ticks,
            play_count=play_count,
            is_favorite=is_favorite,
            likes=likes,
            last_played_date=last_played_date,
            played=played,
            key=key,
            item_id=item_id,
        )

        return user_item_data_dto
