from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.subtitle_playback_mode import SubtitlePlaybackMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserConfiguration")


@_attrs_define
class UserConfiguration:
    """Class UserConfiguration.

    Attributes:
        audio_language_preference (Union[Unset, None, str]): Gets or sets the audio language preference.
        play_default_audio_track (Union[Unset, bool]): Gets or sets a value indicating whether [play default audio
            track].
        subtitle_language_preference (Union[Unset, None, str]): Gets or sets the subtitle language preference.
        display_missing_episodes (Union[Unset, bool]):
        grouped_folders (Union[Unset, List[str]]):
        subtitle_mode (Union[Unset, SubtitlePlaybackMode]): An enum representing a subtitle playback mode.
        display_collections_view (Union[Unset, bool]):
        enable_local_password (Union[Unset, bool]):
        ordered_views (Union[Unset, List[str]]):
        latest_items_excludes (Union[Unset, List[str]]):
        my_media_excludes (Union[Unset, List[str]]):
        hide_played_in_latest (Union[Unset, bool]):
        remember_audio_selections (Union[Unset, bool]):
        remember_subtitle_selections (Union[Unset, bool]):
        enable_next_episode_auto_play (Union[Unset, bool]):
    """

    audio_language_preference: Union[Unset, None, str] = UNSET
    play_default_audio_track: Union[Unset, bool] = UNSET
    subtitle_language_preference: Union[Unset, None, str] = UNSET
    display_missing_episodes: Union[Unset, bool] = UNSET
    grouped_folders: Union[Unset, List[str]] = UNSET
    subtitle_mode: Union[Unset, SubtitlePlaybackMode] = UNSET
    display_collections_view: Union[Unset, bool] = UNSET
    enable_local_password: Union[Unset, bool] = UNSET
    ordered_views: Union[Unset, List[str]] = UNSET
    latest_items_excludes: Union[Unset, List[str]] = UNSET
    my_media_excludes: Union[Unset, List[str]] = UNSET
    hide_played_in_latest: Union[Unset, bool] = UNSET
    remember_audio_selections: Union[Unset, bool] = UNSET
    remember_subtitle_selections: Union[Unset, bool] = UNSET
    enable_next_episode_auto_play: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        audio_language_preference = self.audio_language_preference
        play_default_audio_track = self.play_default_audio_track
        subtitle_language_preference = self.subtitle_language_preference
        display_missing_episodes = self.display_missing_episodes
        grouped_folders: Union[Unset, List[str]] = UNSET
        if not isinstance(self.grouped_folders, Unset):
            grouped_folders = self.grouped_folders

        subtitle_mode: Union[Unset, str] = UNSET
        if not isinstance(self.subtitle_mode, Unset):
            subtitle_mode = self.subtitle_mode.value

        display_collections_view = self.display_collections_view
        enable_local_password = self.enable_local_password
        ordered_views: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ordered_views, Unset):
            ordered_views = self.ordered_views

        latest_items_excludes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.latest_items_excludes, Unset):
            latest_items_excludes = self.latest_items_excludes

        my_media_excludes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.my_media_excludes, Unset):
            my_media_excludes = self.my_media_excludes

        hide_played_in_latest = self.hide_played_in_latest
        remember_audio_selections = self.remember_audio_selections
        remember_subtitle_selections = self.remember_subtitle_selections
        enable_next_episode_auto_play = self.enable_next_episode_auto_play

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if audio_language_preference is not UNSET:
            field_dict["AudioLanguagePreference"] = audio_language_preference
        if play_default_audio_track is not UNSET:
            field_dict["PlayDefaultAudioTrack"] = play_default_audio_track
        if subtitle_language_preference is not UNSET:
            field_dict["SubtitleLanguagePreference"] = subtitle_language_preference
        if display_missing_episodes is not UNSET:
            field_dict["DisplayMissingEpisodes"] = display_missing_episodes
        if grouped_folders is not UNSET:
            field_dict["GroupedFolders"] = grouped_folders
        if subtitle_mode is not UNSET:
            field_dict["SubtitleMode"] = subtitle_mode
        if display_collections_view is not UNSET:
            field_dict["DisplayCollectionsView"] = display_collections_view
        if enable_local_password is not UNSET:
            field_dict["EnableLocalPassword"] = enable_local_password
        if ordered_views is not UNSET:
            field_dict["OrderedViews"] = ordered_views
        if latest_items_excludes is not UNSET:
            field_dict["LatestItemsExcludes"] = latest_items_excludes
        if my_media_excludes is not UNSET:
            field_dict["MyMediaExcludes"] = my_media_excludes
        if hide_played_in_latest is not UNSET:
            field_dict["HidePlayedInLatest"] = hide_played_in_latest
        if remember_audio_selections is not UNSET:
            field_dict["RememberAudioSelections"] = remember_audio_selections
        if remember_subtitle_selections is not UNSET:
            field_dict["RememberSubtitleSelections"] = remember_subtitle_selections
        if enable_next_episode_auto_play is not UNSET:
            field_dict["EnableNextEpisodeAutoPlay"] = enable_next_episode_auto_play

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        audio_language_preference = d.pop("AudioLanguagePreference", UNSET)

        play_default_audio_track = d.pop("PlayDefaultAudioTrack", UNSET)

        subtitle_language_preference = d.pop("SubtitleLanguagePreference", UNSET)

        display_missing_episodes = d.pop("DisplayMissingEpisodes", UNSET)

        grouped_folders = cast(List[str], d.pop("GroupedFolders", UNSET))

        _subtitle_mode = d.pop("SubtitleMode", UNSET)
        subtitle_mode: Union[Unset, SubtitlePlaybackMode]
        if isinstance(_subtitle_mode, Unset):
            subtitle_mode = UNSET
        else:
            subtitle_mode = SubtitlePlaybackMode(_subtitle_mode)

        display_collections_view = d.pop("DisplayCollectionsView", UNSET)

        enable_local_password = d.pop("EnableLocalPassword", UNSET)

        ordered_views = cast(List[str], d.pop("OrderedViews", UNSET))

        latest_items_excludes = cast(List[str], d.pop("LatestItemsExcludes", UNSET))

        my_media_excludes = cast(List[str], d.pop("MyMediaExcludes", UNSET))

        hide_played_in_latest = d.pop("HidePlayedInLatest", UNSET)

        remember_audio_selections = d.pop("RememberAudioSelections", UNSET)

        remember_subtitle_selections = d.pop("RememberSubtitleSelections", UNSET)

        enable_next_episode_auto_play = d.pop("EnableNextEpisodeAutoPlay", UNSET)

        user_configuration = cls(
            audio_language_preference=audio_language_preference,
            play_default_audio_track=play_default_audio_track,
            subtitle_language_preference=subtitle_language_preference,
            display_missing_episodes=display_missing_episodes,
            grouped_folders=grouped_folders,
            subtitle_mode=subtitle_mode,
            display_collections_view=display_collections_view,
            enable_local_password=enable_local_password,
            ordered_views=ordered_views,
            latest_items_excludes=latest_items_excludes,
            my_media_excludes=my_media_excludes,
            hide_played_in_latest=hide_played_in_latest,
            remember_audio_selections=remember_audio_selections,
            remember_subtitle_selections=remember_subtitle_selections,
            enable_next_episode_auto_play=enable_next_episode_auto_play,
        )

        return user_configuration
