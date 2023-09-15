from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.playback_error_code import PlaybackErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_source_info import MediaSourceInfo


T = TypeVar("T", bound="PlaybackInfoResponse")


@_attrs_define
class PlaybackInfoResponse:
    """Class PlaybackInfoResponse.

    Attributes:
        media_sources (Union[Unset, List['MediaSourceInfo']]): Gets or sets the media sources.
        play_session_id (Union[Unset, None, str]): Gets or sets the play session identifier.
        error_code (Union[Unset, None, PlaybackErrorCode]):
    """

    media_sources: Union[Unset, List["MediaSourceInfo"]] = UNSET
    play_session_id: Union[Unset, None, str] = UNSET
    error_code: Union[Unset, None, PlaybackErrorCode] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        media_sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media_sources, Unset):
            media_sources = []
            for media_sources_item_data in self.media_sources:
                media_sources_item = media_sources_item_data.to_dict()

                media_sources.append(media_sources_item)

        play_session_id = self.play_session_id
        error_code: Union[Unset, None, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value if self.error_code else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if media_sources is not UNSET:
            field_dict["MediaSources"] = media_sources
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_source_info import MediaSourceInfo

        d = src_dict.copy()
        media_sources = []
        _media_sources = d.pop("MediaSources", UNSET)
        for media_sources_item_data in _media_sources or []:
            media_sources_item = MediaSourceInfo.from_dict(media_sources_item_data)

            media_sources.append(media_sources_item)

        play_session_id = d.pop("PlaySessionId", UNSET)

        _error_code = d.pop("ErrorCode", UNSET)
        error_code: Union[Unset, None, PlaybackErrorCode]
        if _error_code is None:
            error_code = None
        elif isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = PlaybackErrorCode(_error_code)

        playback_info_response = cls(
            media_sources=media_sources,
            play_session_id=play_session_id,
            error_code=error_code,
        )

        return playback_info_response
