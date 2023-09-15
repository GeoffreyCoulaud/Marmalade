from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.media_protocol import MediaProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="OpenLiveStreamDto")


@_attrs_define
class OpenLiveStreamDto:
    """Open live stream dto.

    Attributes:
        open_token (Union[Unset, None, str]): Gets or sets the open token.
        user_id (Union[Unset, None, str]): Gets or sets the user id.
        play_session_id (Union[Unset, None, str]): Gets or sets the play session id.
        max_streaming_bitrate (Union[Unset, None, int]): Gets or sets the max streaming bitrate.
        start_time_ticks (Union[Unset, None, int]): Gets or sets the start time in ticks.
        audio_stream_index (Union[Unset, None, int]): Gets or sets the audio stream index.
        subtitle_stream_index (Union[Unset, None, int]): Gets or sets the subtitle stream index.
        max_audio_channels (Union[Unset, None, int]): Gets or sets the max audio channels.
        item_id (Union[Unset, None, str]): Gets or sets the item id.
        enable_direct_play (Union[Unset, None, bool]): Gets or sets a value indicating whether to enable direct play.
        enable_direct_stream (Union[Unset, None, bool]): Gets or sets a value indicating whether to enale direct stream.
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
        direct_play_protocols (Union[Unset, List[MediaProtocol]]): Gets or sets the device play protocols.
    """

    open_token: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    play_session_id: Union[Unset, None, str] = UNSET
    max_streaming_bitrate: Union[Unset, None, int] = UNSET
    start_time_ticks: Union[Unset, None, int] = UNSET
    audio_stream_index: Union[Unset, None, int] = UNSET
    subtitle_stream_index: Union[Unset, None, int] = UNSET
    max_audio_channels: Union[Unset, None, int] = UNSET
    item_id: Union[Unset, None, str] = UNSET
    enable_direct_play: Union[Unset, None, bool] = UNSET
    enable_direct_stream: Union[Unset, None, bool] = UNSET
    device_profile: Union[Unset, None, "DeviceProfile"] = UNSET
    direct_play_protocols: Union[Unset, List[MediaProtocol]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        open_token = self.open_token
        user_id = self.user_id
        play_session_id = self.play_session_id
        max_streaming_bitrate = self.max_streaming_bitrate
        start_time_ticks = self.start_time_ticks
        audio_stream_index = self.audio_stream_index
        subtitle_stream_index = self.subtitle_stream_index
        max_audio_channels = self.max_audio_channels
        item_id = self.item_id
        enable_direct_play = self.enable_direct_play
        enable_direct_stream = self.enable_direct_stream
        device_profile: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.device_profile, Unset):
            device_profile = self.device_profile.to_dict() if self.device_profile else None

        direct_play_protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.direct_play_protocols, Unset):
            direct_play_protocols = []
            for direct_play_protocols_item_data in self.direct_play_protocols:
                direct_play_protocols_item = direct_play_protocols_item_data.value

                direct_play_protocols.append(direct_play_protocols_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if open_token is not UNSET:
            field_dict["OpenToken"] = open_token
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
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
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if enable_direct_play is not UNSET:
            field_dict["EnableDirectPlay"] = enable_direct_play
        if enable_direct_stream is not UNSET:
            field_dict["EnableDirectStream"] = enable_direct_stream
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if direct_play_protocols is not UNSET:
            field_dict["DirectPlayProtocols"] = direct_play_protocols

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = src_dict.copy()
        open_token = d.pop("OpenToken", UNSET)

        user_id = d.pop("UserId", UNSET)

        play_session_id = d.pop("PlaySessionId", UNSET)

        max_streaming_bitrate = d.pop("MaxStreamingBitrate", UNSET)

        start_time_ticks = d.pop("StartTimeTicks", UNSET)

        audio_stream_index = d.pop("AudioStreamIndex", UNSET)

        subtitle_stream_index = d.pop("SubtitleStreamIndex", UNSET)

        max_audio_channels = d.pop("MaxAudioChannels", UNSET)

        item_id = d.pop("ItemId", UNSET)

        enable_direct_play = d.pop("EnableDirectPlay", UNSET)

        enable_direct_stream = d.pop("EnableDirectStream", UNSET)

        _device_profile = d.pop("DeviceProfile", UNSET)
        device_profile: Union[Unset, None, DeviceProfile]
        if _device_profile is None:
            device_profile = None
        elif isinstance(_device_profile, Unset):
            device_profile = UNSET
        else:
            device_profile = DeviceProfile.from_dict(_device_profile)

        direct_play_protocols = []
        _direct_play_protocols = d.pop("DirectPlayProtocols", UNSET)
        for direct_play_protocols_item_data in _direct_play_protocols or []:
            direct_play_protocols_item = MediaProtocol(direct_play_protocols_item_data)

            direct_play_protocols.append(direct_play_protocols_item)

        open_live_stream_dto = cls(
            open_token=open_token,
            user_id=user_id,
            play_session_id=play_session_id,
            max_streaming_bitrate=max_streaming_bitrate,
            start_time_ticks=start_time_ticks,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            max_audio_channels=max_audio_channels,
            item_id=item_id,
            enable_direct_play=enable_direct_play,
            enable_direct_stream=enable_direct_stream,
            device_profile=device_profile,
            direct_play_protocols=direct_play_protocols,
        )

        return open_live_stream_dto
