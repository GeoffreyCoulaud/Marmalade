from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_dto import BaseItemDto
    from ..models.queue_item import QueueItem


T = TypeVar("T", bound="PlaybackStopInfo")


@_attrs_define
class PlaybackStopInfo:
    """Class PlaybackStopInfo.

    Attributes:
        item (Union[Unset, None, BaseItemDto]): This is strictly used as a data transfer object from the api layer.
            This holds information about a BaseItem in a format that is convenient for the client.
        item_id (Union[Unset, str]): Gets or sets the item identifier.
        session_id (Union[Unset, None, str]): Gets or sets the session id.
        media_source_id (Union[Unset, None, str]): Gets or sets the media version identifier.
        position_ticks (Union[Unset, None, int]): Gets or sets the position ticks.
        live_stream_id (Union[Unset, None, str]): Gets or sets the live stream identifier.
        play_session_id (Union[Unset, None, str]): Gets or sets the play session identifier.
        failed (Union[Unset, bool]): Gets or sets a value indicating whether this
            MediaBrowser.Model.Session.PlaybackStopInfo is failed.
        next_media_type (Union[Unset, None, str]):
        playlist_item_id (Union[Unset, None, str]):
        now_playing_queue (Union[Unset, None, List['QueueItem']]):
    """

    item: Union[Unset, None, "BaseItemDto"] = UNSET
    item_id: Union[Unset, str] = UNSET
    session_id: Union[Unset, None, str] = UNSET
    media_source_id: Union[Unset, None, str] = UNSET
    position_ticks: Union[Unset, None, int] = UNSET
    live_stream_id: Union[Unset, None, str] = UNSET
    play_session_id: Union[Unset, None, str] = UNSET
    failed: Union[Unset, bool] = UNSET
    next_media_type: Union[Unset, None, str] = UNSET
    playlist_item_id: Union[Unset, None, str] = UNSET
    now_playing_queue: Union[Unset, None, List["QueueItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict() if self.item else None

        item_id = self.item_id
        session_id = self.session_id
        media_source_id = self.media_source_id
        position_ticks = self.position_ticks
        live_stream_id = self.live_stream_id
        play_session_id = self.play_session_id
        failed = self.failed
        next_media_type = self.next_media_type
        playlist_item_id = self.playlist_item_id
        now_playing_queue: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.now_playing_queue, Unset):
            if self.now_playing_queue is None:
                now_playing_queue = None
            else:
                now_playing_queue = []
                for now_playing_queue_item_data in self.now_playing_queue:
                    now_playing_queue_item = now_playing_queue_item_data.to_dict()

                    now_playing_queue.append(now_playing_queue_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item is not UNSET:
            field_dict["Item"] = item
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if session_id is not UNSET:
            field_dict["SessionId"] = session_id
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if failed is not UNSET:
            field_dict["Failed"] = failed
        if next_media_type is not UNSET:
            field_dict["NextMediaType"] = next_media_type
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if now_playing_queue is not UNSET:
            field_dict["NowPlayingQueue"] = now_playing_queue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_item_dto import BaseItemDto
        from ..models.queue_item import QueueItem

        d = src_dict.copy()
        _item = d.pop("Item", UNSET)
        item: Union[Unset, None, BaseItemDto]
        if _item is None:
            item = None
        elif isinstance(_item, Unset):
            item = UNSET
        else:
            item = BaseItemDto.from_dict(_item)

        item_id = d.pop("ItemId", UNSET)

        session_id = d.pop("SessionId", UNSET)

        media_source_id = d.pop("MediaSourceId", UNSET)

        position_ticks = d.pop("PositionTicks", UNSET)

        live_stream_id = d.pop("LiveStreamId", UNSET)

        play_session_id = d.pop("PlaySessionId", UNSET)

        failed = d.pop("Failed", UNSET)

        next_media_type = d.pop("NextMediaType", UNSET)

        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        now_playing_queue = []
        _now_playing_queue = d.pop("NowPlayingQueue", UNSET)
        for now_playing_queue_item_data in _now_playing_queue or []:
            now_playing_queue_item = QueueItem.from_dict(now_playing_queue_item_data)

            now_playing_queue.append(now_playing_queue_item)

        playback_stop_info = cls(
            item=item,
            item_id=item_id,
            session_id=session_id,
            media_source_id=media_source_id,
            position_ticks=position_ticks,
            live_stream_id=live_stream_id,
            play_session_id=play_session_id,
            failed=failed,
            next_media_type=next_media_type,
            playlist_item_id=playlist_item_id,
            now_playing_queue=now_playing_queue,
        )

        return playback_stop_info
