from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="PlaybackInfoDto")


@_attrs_define
class PlaybackInfoDto:
    """Plabyback info dto.

    Attributes:
        user_id (Union[Unset, None, str]): Gets or sets the playback userId.
        max_streaming_bitrate (Union[Unset, None, int]): Gets or sets the max streaming bitrate.
        start_time_ticks (Union[Unset, None, int]): Gets or sets the start time in ticks.
        audio_stream_index (Union[Unset, None, int]): Gets or sets the audio stream index.
        subtitle_stream_index (Union[Unset, None, int]): Gets or sets the subtitle stream index.
        max_audio_channels (Union[Unset, None, int]): Gets or sets the max audio channels.
        media_source_id (Union[Unset, None, str]): Gets or sets the media source id.
        live_stream_id (Union[Unset, None, str]): Gets or sets the live stream id.
        device_profile (Union[Unset, None, DeviceProfile]): A MediaBrowser.Model.Dlna.DeviceProfile represents a set of
            metadata which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including
            codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.
        enable_direct_play (Union[Unset, None, bool]): Gets or sets a value indicating whether to enable direct play.
        enable_direct_stream (Union[Unset, None, bool]): Gets or sets a value indicating whether to enable direct
            stream.
        enable_transcoding (Union[Unset, None, bool]): Gets or sets a value indicating whether to enable transcoding.
        allow_video_stream_copy (Union[Unset, None, bool]): Gets or sets a value indicating whether to enable video
            stream copy.
        allow_audio_stream_copy (Union[Unset, None, bool]): Gets or sets a value indicating whether to allow audio
            stream copy.
        auto_open_live_stream (Union[Unset, None, bool]): Gets or sets a value indicating whether to auto open the live
            stream.
    """

    user_id: Union[Unset, None, str] = UNSET
    max_streaming_bitrate: Union[Unset, None, int] = UNSET
    start_time_ticks: Union[Unset, None, int] = UNSET
    audio_stream_index: Union[Unset, None, int] = UNSET
    subtitle_stream_index: Union[Unset, None, int] = UNSET
    max_audio_channels: Union[Unset, None, int] = UNSET
    media_source_id: Union[Unset, None, str] = UNSET
    live_stream_id: Union[Unset, None, str] = UNSET
    device_profile: Union[Unset, None, "DeviceProfile"] = UNSET
    enable_direct_play: Union[Unset, None, bool] = UNSET
    enable_direct_stream: Union[Unset, None, bool] = UNSET
    enable_transcoding: Union[Unset, None, bool] = UNSET
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET
    auto_open_live_stream: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        max_streaming_bitrate = self.max_streaming_bitrate
        start_time_ticks = self.start_time_ticks
        audio_stream_index = self.audio_stream_index
        subtitle_stream_index = self.subtitle_stream_index
        max_audio_channels = self.max_audio_channels
        media_source_id = self.media_source_id
        live_stream_id = self.live_stream_id
        device_profile: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.device_profile, Unset):
            device_profile = self.device_profile.to_dict() if self.device_profile else None

        enable_direct_play = self.enable_direct_play
        enable_direct_stream = self.enable_direct_stream
        enable_transcoding = self.enable_transcoding
        allow_video_stream_copy = self.allow_video_stream_copy
        allow_audio_stream_copy = self.allow_audio_stream_copy
        auto_open_live_stream = self.auto_open_live_stream

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if max_streaming_bitrate is not UNSET:
            field_dict["MaxStreamingBitrate"] = max_streaming_bitrate
        if start_time_ticks is not UNSET:
            field_dict["StartTimeTicks"] = start_time_ticks
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if max_audio_channels is not UNSET:
            field_dict["MaxAudioChannels"] = max_audio_channels
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if enable_direct_play is not UNSET:
            field_dict["EnableDirectPlay"] = enable_direct_play
        if enable_direct_stream is not UNSET:
            field_dict["EnableDirectStream"] = enable_direct_stream
        if enable_transcoding is not UNSET:
            field_dict["EnableTranscoding"] = enable_transcoding
        if allow_video_stream_copy is not UNSET:
            field_dict["AllowVideoStreamCopy"] = allow_video_stream_copy
        if allow_audio_stream_copy is not UNSET:
            field_dict["AllowAudioStreamCopy"] = allow_audio_stream_copy
        if auto_open_live_stream is not UNSET:
            field_dict["AutoOpenLiveStream"] = auto_open_live_stream

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = src_dict.copy()
        user_id = d.pop("UserId", UNSET)

        max_streaming_bitrate = d.pop("MaxStreamingBitrate", UNSET)

        start_time_ticks = d.pop("StartTimeTicks", UNSET)

        audio_stream_index = d.pop("AudioStreamIndex", UNSET)

        subtitle_stream_index = d.pop("SubtitleStreamIndex", UNSET)

        max_audio_channels = d.pop("MaxAudioChannels", UNSET)

        media_source_id = d.pop("MediaSourceId", UNSET)

        live_stream_id = d.pop("LiveStreamId", UNSET)

        _device_profile = d.pop("DeviceProfile", UNSET)
        device_profile: Union[Unset, None, DeviceProfile]
        if _device_profile is None:
            device_profile = None
        elif isinstance(_device_profile, Unset):
            device_profile = UNSET
        else:
            device_profile = DeviceProfile.from_dict(_device_profile)

        enable_direct_play = d.pop("EnableDirectPlay", UNSET)

        enable_direct_stream = d.pop("EnableDirectStream", UNSET)

        enable_transcoding = d.pop("EnableTranscoding", UNSET)

        allow_video_stream_copy = d.pop("AllowVideoStreamCopy", UNSET)

        allow_audio_stream_copy = d.pop("AllowAudioStreamCopy", UNSET)

        auto_open_live_stream = d.pop("AutoOpenLiveStream", UNSET)

        playback_info_dto = cls(
            user_id=user_id,
            max_streaming_bitrate=max_streaming_bitrate,
            start_time_ticks=start_time_ticks,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            max_audio_channels=max_audio_channels,
            media_source_id=media_source_id,
            live_stream_id=live_stream_id,
            device_profile=device_profile,
            enable_direct_play=enable_direct_play,
            enable_direct_stream=enable_direct_stream,
            enable_transcoding=enable_transcoding,
            allow_video_stream_copy=allow_video_stream_copy,
            allow_audio_stream_copy=allow_audio_stream_copy,
            auto_open_live_stream=auto_open_live_stream,
        )

        return playback_info_dto
