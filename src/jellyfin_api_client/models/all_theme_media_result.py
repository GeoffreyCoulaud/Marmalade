from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.theme_media_result import ThemeMediaResult


T = TypeVar("T", bound="AllThemeMediaResult")


@_attrs_define
class AllThemeMediaResult:
    """
    Attributes:
        theme_videos_result (Union[Unset, None, ThemeMediaResult]): Class ThemeMediaResult.
        theme_songs_result (Union[Unset, None, ThemeMediaResult]): Class ThemeMediaResult.
        soundtrack_songs_result (Union[Unset, None, ThemeMediaResult]): Class ThemeMediaResult.
    """

    theme_videos_result: Union[Unset, None, "ThemeMediaResult"] = UNSET
    theme_songs_result: Union[Unset, None, "ThemeMediaResult"] = UNSET
    soundtrack_songs_result: Union[Unset, None, "ThemeMediaResult"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        theme_videos_result: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.theme_videos_result, Unset):
            theme_videos_result = self.theme_videos_result.to_dict() if self.theme_videos_result else None

        theme_songs_result: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.theme_songs_result, Unset):
            theme_songs_result = self.theme_songs_result.to_dict() if self.theme_songs_result else None

        soundtrack_songs_result: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.soundtrack_songs_result, Unset):
            soundtrack_songs_result = self.soundtrack_songs_result.to_dict() if self.soundtrack_songs_result else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if theme_videos_result is not UNSET:
            field_dict["ThemeVideosResult"] = theme_videos_result
        if theme_songs_result is not UNSET:
            field_dict["ThemeSongsResult"] = theme_songs_result
        if soundtrack_songs_result is not UNSET:
            field_dict["SoundtrackSongsResult"] = soundtrack_songs_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.theme_media_result import ThemeMediaResult

        d = src_dict.copy()
        _theme_videos_result = d.pop("ThemeVideosResult", UNSET)
        theme_videos_result: Union[Unset, None, ThemeMediaResult]
        if _theme_videos_result is None:
            theme_videos_result = None
        elif isinstance(_theme_videos_result, Unset):
            theme_videos_result = UNSET
        else:
            theme_videos_result = ThemeMediaResult.from_dict(_theme_videos_result)

        _theme_songs_result = d.pop("ThemeSongsResult", UNSET)
        theme_songs_result: Union[Unset, None, ThemeMediaResult]
        if _theme_songs_result is None:
            theme_songs_result = None
        elif isinstance(_theme_songs_result, Unset):
            theme_songs_result = UNSET
        else:
            theme_songs_result = ThemeMediaResult.from_dict(_theme_songs_result)

        _soundtrack_songs_result = d.pop("SoundtrackSongsResult", UNSET)
        soundtrack_songs_result: Union[Unset, None, ThemeMediaResult]
        if _soundtrack_songs_result is None:
            soundtrack_songs_result = None
        elif isinstance(_soundtrack_songs_result, Unset):
            soundtrack_songs_result = UNSET
        else:
            soundtrack_songs_result = ThemeMediaResult.from_dict(_soundtrack_songs_result)

        all_theme_media_result = cls(
            theme_videos_result=theme_videos_result,
            theme_songs_result=theme_songs_result,
            soundtrack_songs_result=soundtrack_songs_result,
        )

        return all_theme_media_result
