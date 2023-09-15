from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..models.encoding_context import EncodingContext
from ..models.transcode_seek_info import TranscodeSeekInfo
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="TranscodingProfile")


@_attrs_define
class TranscodingProfile:
    """
    Attributes:
        container (Union[Unset, str]):
        type (Union[Unset, DlnaProfileType]):
        video_codec (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        protocol (Union[Unset, str]):
        estimate_content_length (Union[Unset, bool]):
        enable_mpegts_m2_ts_mode (Union[Unset, bool]):
        transcode_seek_info (Union[Unset, TranscodeSeekInfo]):  Default: TranscodeSeekInfo.AUTO.
        copy_timestamps (Union[Unset, bool]):
        context (Union[Unset, EncodingContext]):  Default: EncodingContext.STREAMING.
        enable_subtitles_in_manifest (Union[Unset, bool]):
        max_audio_channels (Union[Unset, None, str]):
        min_segments (Union[Unset, int]):
        segment_length (Union[Unset, int]):
        break_on_non_key_frames (Union[Unset, bool]):
        conditions (Union[Unset, List['ProfileCondition']]):
    """

    container: Union[Unset, str] = UNSET
    type: Union[Unset, DlnaProfileType] = UNSET
    video_codec: Union[Unset, str] = UNSET
    audio_codec: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    estimate_content_length: Union[Unset, bool] = False
    enable_mpegts_m2_ts_mode: Union[Unset, bool] = False
    transcode_seek_info: Union[Unset, TranscodeSeekInfo] = TranscodeSeekInfo.AUTO
    copy_timestamps: Union[Unset, bool] = False
    context: Union[Unset, EncodingContext] = EncodingContext.STREAMING
    enable_subtitles_in_manifest: Union[Unset, bool] = False
    max_audio_channels: Union[Unset, None, str] = UNSET
    min_segments: Union[Unset, int] = 0
    segment_length: Union[Unset, int] = 0
    break_on_non_key_frames: Union[Unset, bool] = False
    conditions: Union[Unset, List["ProfileCondition"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        container = self.container
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        video_codec = self.video_codec
        audio_codec = self.audio_codec
        protocol = self.protocol
        estimate_content_length = self.estimate_content_length
        enable_mpegts_m2_ts_mode = self.enable_mpegts_m2_ts_mode
        transcode_seek_info: Union[Unset, str] = UNSET
        if not isinstance(self.transcode_seek_info, Unset):
            transcode_seek_info = self.transcode_seek_info.value

        copy_timestamps = self.copy_timestamps
        context: Union[Unset, str] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.value

        enable_subtitles_in_manifest = self.enable_subtitles_in_manifest
        max_audio_channels = self.max_audio_channels
        min_segments = self.min_segments
        segment_length = self.segment_length
        break_on_non_key_frames = self.break_on_non_key_frames
        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()

                conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if container is not UNSET:
            field_dict["Container"] = container
        if type is not UNSET:
            field_dict["Type"] = type
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if protocol is not UNSET:
            field_dict["Protocol"] = protocol
        if estimate_content_length is not UNSET:
            field_dict["EstimateContentLength"] = estimate_content_length
        if enable_mpegts_m2_ts_mode is not UNSET:
            field_dict["EnableMpegtsM2TsMode"] = enable_mpegts_m2_ts_mode
        if transcode_seek_info is not UNSET:
            field_dict["TranscodeSeekInfo"] = transcode_seek_info
        if copy_timestamps is not UNSET:
            field_dict["CopyTimestamps"] = copy_timestamps
        if context is not UNSET:
            field_dict["Context"] = context
        if enable_subtitles_in_manifest is not UNSET:
            field_dict["EnableSubtitlesInManifest"] = enable_subtitles_in_manifest
        if max_audio_channels is not UNSET:
            field_dict["MaxAudioChannels"] = max_audio_channels
        if min_segments is not UNSET:
            field_dict["MinSegments"] = min_segments
        if segment_length is not UNSET:
            field_dict["SegmentLength"] = segment_length
        if break_on_non_key_frames is not UNSET:
            field_dict["BreakOnNonKeyFrames"] = break_on_non_key_frames
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = src_dict.copy()
        container = d.pop("Container", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, DlnaProfileType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DlnaProfileType(_type)

        video_codec = d.pop("VideoCodec", UNSET)

        audio_codec = d.pop("AudioCodec", UNSET)

        protocol = d.pop("Protocol", UNSET)

        estimate_content_length = d.pop("EstimateContentLength", UNSET)

        enable_mpegts_m2_ts_mode = d.pop("EnableMpegtsM2TsMode", UNSET)

        _transcode_seek_info = d.pop("TranscodeSeekInfo", UNSET)
        transcode_seek_info: Union[Unset, TranscodeSeekInfo]
        if isinstance(_transcode_seek_info, Unset):
            transcode_seek_info = UNSET
        else:
            transcode_seek_info = TranscodeSeekInfo(_transcode_seek_info)

        copy_timestamps = d.pop("CopyTimestamps", UNSET)

        _context = d.pop("Context", UNSET)
        context: Union[Unset, EncodingContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = EncodingContext(_context)

        enable_subtitles_in_manifest = d.pop("EnableSubtitlesInManifest", UNSET)

        max_audio_channels = d.pop("MaxAudioChannels", UNSET)

        min_segments = d.pop("MinSegments", UNSET)

        segment_length = d.pop("SegmentLength", UNSET)

        break_on_non_key_frames = d.pop("BreakOnNonKeyFrames", UNSET)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ProfileCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        transcoding_profile = cls(
            container=container,
            type=type,
            video_codec=video_codec,
            audio_codec=audio_codec,
            protocol=protocol,
            estimate_content_length=estimate_content_length,
            enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
            transcode_seek_info=transcode_seek_info,
            copy_timestamps=copy_timestamps,
            context=context,
            enable_subtitles_in_manifest=enable_subtitles_in_manifest,
            max_audio_channels=max_audio_channels,
            min_segments=min_segments,
            segment_length=segment_length,
            break_on_non_key_frames=break_on_non_key_frames,
            conditions=conditions,
        )

        return transcoding_profile
