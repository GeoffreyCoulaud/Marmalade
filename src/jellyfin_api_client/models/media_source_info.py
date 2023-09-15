from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.iso_type import IsoType
from ..models.media_protocol import MediaProtocol
from ..models.media_source_type import MediaSourceType
from ..models.transport_stream_timestamp import TransportStreamTimestamp
from ..models.video_3d_format import Video3DFormat
from ..models.video_type import VideoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_attachment import MediaAttachment
    from ..models.media_source_info_required_http_headers import MediaSourceInfoRequiredHttpHeaders
    from ..models.media_stream import MediaStream


T = TypeVar("T", bound="MediaSourceInfo")


@_attrs_define
class MediaSourceInfo:
    """
    Attributes:
        protocol (Union[Unset, MediaProtocol]):
        id (Union[Unset, None, str]):
        path (Union[Unset, None, str]):
        encoder_path (Union[Unset, None, str]):
        encoder_protocol (Union[Unset, None, MediaProtocol]):
        type (Union[Unset, MediaSourceType]):
        container (Union[Unset, None, str]):
        size (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        is_remote (Union[Unset, bool]): Gets or sets a value indicating whether the media is remote.
            Differentiate internet url vs local network.
        e_tag (Union[Unset, None, str]):
        run_time_ticks (Union[Unset, None, int]):
        read_at_native_framerate (Union[Unset, bool]):
        ignore_dts (Union[Unset, bool]):
        ignore_index (Union[Unset, bool]):
        gen_pts_input (Union[Unset, bool]):
        supports_transcoding (Union[Unset, bool]):
        supports_direct_stream (Union[Unset, bool]):
        supports_direct_play (Union[Unset, bool]):
        is_infinite_stream (Union[Unset, bool]):
        requires_opening (Union[Unset, bool]):
        open_token (Union[Unset, None, str]):
        requires_closing (Union[Unset, bool]):
        live_stream_id (Union[Unset, None, str]):
        buffer_ms (Union[Unset, None, int]):
        requires_looping (Union[Unset, bool]):
        supports_probing (Union[Unset, bool]):
        video_type (Union[Unset, None, VideoType]): Enum VideoType.
        iso_type (Union[Unset, None, IsoType]): Enum IsoType.
        video_3d_format (Union[Unset, None, Video3DFormat]):
        media_streams (Union[Unset, None, List['MediaStream']]):
        media_attachments (Union[Unset, None, List['MediaAttachment']]):
        formats (Union[Unset, None, List[str]]):
        bitrate (Union[Unset, None, int]):
        timestamp (Union[Unset, None, TransportStreamTimestamp]):
        required_http_headers (Union[Unset, None, MediaSourceInfoRequiredHttpHeaders]):
        transcoding_url (Union[Unset, None, str]):
        transcoding_sub_protocol (Union[Unset, None, str]):
        transcoding_container (Union[Unset, None, str]):
        analyze_duration_ms (Union[Unset, None, int]):
        default_audio_stream_index (Union[Unset, None, int]):
        default_subtitle_stream_index (Union[Unset, None, int]):
    """

    protocol: Union[Unset, MediaProtocol] = UNSET
    id: Union[Unset, None, str] = UNSET
    path: Union[Unset, None, str] = UNSET
    encoder_path: Union[Unset, None, str] = UNSET
    encoder_protocol: Union[Unset, None, MediaProtocol] = UNSET
    type: Union[Unset, MediaSourceType] = UNSET
    container: Union[Unset, None, str] = UNSET
    size: Union[Unset, None, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_remote: Union[Unset, bool] = UNSET
    e_tag: Union[Unset, None, str] = UNSET
    run_time_ticks: Union[Unset, None, int] = UNSET
    read_at_native_framerate: Union[Unset, bool] = UNSET
    ignore_dts: Union[Unset, bool] = UNSET
    ignore_index: Union[Unset, bool] = UNSET
    gen_pts_input: Union[Unset, bool] = UNSET
    supports_transcoding: Union[Unset, bool] = UNSET
    supports_direct_stream: Union[Unset, bool] = UNSET
    supports_direct_play: Union[Unset, bool] = UNSET
    is_infinite_stream: Union[Unset, bool] = UNSET
    requires_opening: Union[Unset, bool] = UNSET
    open_token: Union[Unset, None, str] = UNSET
    requires_closing: Union[Unset, bool] = UNSET
    live_stream_id: Union[Unset, None, str] = UNSET
    buffer_ms: Union[Unset, None, int] = UNSET
    requires_looping: Union[Unset, bool] = UNSET
    supports_probing: Union[Unset, bool] = UNSET
    video_type: Union[Unset, None, VideoType] = UNSET
    iso_type: Union[Unset, None, IsoType] = UNSET
    video_3d_format: Union[Unset, None, Video3DFormat] = UNSET
    media_streams: Union[Unset, None, List["MediaStream"]] = UNSET
    media_attachments: Union[Unset, None, List["MediaAttachment"]] = UNSET
    formats: Union[Unset, None, List[str]] = UNSET
    bitrate: Union[Unset, None, int] = UNSET
    timestamp: Union[Unset, None, TransportStreamTimestamp] = UNSET
    required_http_headers: Union[Unset, None, "MediaSourceInfoRequiredHttpHeaders"] = UNSET
    transcoding_url: Union[Unset, None, str] = UNSET
    transcoding_sub_protocol: Union[Unset, None, str] = UNSET
    transcoding_container: Union[Unset, None, str] = UNSET
    analyze_duration_ms: Union[Unset, None, int] = UNSET
    default_audio_stream_index: Union[Unset, None, int] = UNSET
    default_subtitle_stream_index: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        id = self.id
        path = self.path
        encoder_path = self.encoder_path
        encoder_protocol: Union[Unset, None, str] = UNSET
        if not isinstance(self.encoder_protocol, Unset):
            encoder_protocol = self.encoder_protocol.value if self.encoder_protocol else None

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        container = self.container
        size = self.size
        name = self.name
        is_remote = self.is_remote
        e_tag = self.e_tag
        run_time_ticks = self.run_time_ticks
        read_at_native_framerate = self.read_at_native_framerate
        ignore_dts = self.ignore_dts
        ignore_index = self.ignore_index
        gen_pts_input = self.gen_pts_input
        supports_transcoding = self.supports_transcoding
        supports_direct_stream = self.supports_direct_stream
        supports_direct_play = self.supports_direct_play
        is_infinite_stream = self.is_infinite_stream
        requires_opening = self.requires_opening
        open_token = self.open_token
        requires_closing = self.requires_closing
        live_stream_id = self.live_stream_id
        buffer_ms = self.buffer_ms
        requires_looping = self.requires_looping
        supports_probing = self.supports_probing
        video_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.video_type, Unset):
            video_type = self.video_type.value if self.video_type else None

        iso_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.iso_type, Unset):
            iso_type = self.iso_type.value if self.iso_type else None

        video_3d_format: Union[Unset, None, str] = UNSET
        if not isinstance(self.video_3d_format, Unset):
            video_3d_format = self.video_3d_format.value if self.video_3d_format else None

        media_streams: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media_streams, Unset):
            if self.media_streams is None:
                media_streams = None
            else:
                media_streams = []
                for media_streams_item_data in self.media_streams:
                    media_streams_item = media_streams_item_data.to_dict()

                    media_streams.append(media_streams_item)

        media_attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media_attachments, Unset):
            if self.media_attachments is None:
                media_attachments = None
            else:
                media_attachments = []
                for media_attachments_item_data in self.media_attachments:
                    media_attachments_item = media_attachments_item_data.to_dict()

                    media_attachments.append(media_attachments_item)

        formats: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.formats, Unset):
            if self.formats is None:
                formats = None
            else:
                formats = self.formats

        bitrate = self.bitrate
        timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.value if self.timestamp else None

        required_http_headers: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.required_http_headers, Unset):
            required_http_headers = self.required_http_headers.to_dict() if self.required_http_headers else None

        transcoding_url = self.transcoding_url
        transcoding_sub_protocol = self.transcoding_sub_protocol
        transcoding_container = self.transcoding_container
        analyze_duration_ms = self.analyze_duration_ms
        default_audio_stream_index = self.default_audio_stream_index
        default_subtitle_stream_index = self.default_subtitle_stream_index

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["Protocol"] = protocol
        if id is not UNSET:
            field_dict["Id"] = id
        if path is not UNSET:
            field_dict["Path"] = path
        if encoder_path is not UNSET:
            field_dict["EncoderPath"] = encoder_path
        if encoder_protocol is not UNSET:
            field_dict["EncoderProtocol"] = encoder_protocol
        if type is not UNSET:
            field_dict["Type"] = type
        if container is not UNSET:
            field_dict["Container"] = container
        if size is not UNSET:
            field_dict["Size"] = size
        if name is not UNSET:
            field_dict["Name"] = name
        if is_remote is not UNSET:
            field_dict["IsRemote"] = is_remote
        if e_tag is not UNSET:
            field_dict["ETag"] = e_tag
        if run_time_ticks is not UNSET:
            field_dict["RunTimeTicks"] = run_time_ticks
        if read_at_native_framerate is not UNSET:
            field_dict["ReadAtNativeFramerate"] = read_at_native_framerate
        if ignore_dts is not UNSET:
            field_dict["IgnoreDts"] = ignore_dts
        if ignore_index is not UNSET:
            field_dict["IgnoreIndex"] = ignore_index
        if gen_pts_input is not UNSET:
            field_dict["GenPtsInput"] = gen_pts_input
        if supports_transcoding is not UNSET:
            field_dict["SupportsTranscoding"] = supports_transcoding
        if supports_direct_stream is not UNSET:
            field_dict["SupportsDirectStream"] = supports_direct_stream
        if supports_direct_play is not UNSET:
            field_dict["SupportsDirectPlay"] = supports_direct_play
        if is_infinite_stream is not UNSET:
            field_dict["IsInfiniteStream"] = is_infinite_stream
        if requires_opening is not UNSET:
            field_dict["RequiresOpening"] = requires_opening
        if open_token is not UNSET:
            field_dict["OpenToken"] = open_token
        if requires_closing is not UNSET:
            field_dict["RequiresClosing"] = requires_closing
        if live_stream_id is not UNSET:
            field_dict["LiveStreamId"] = live_stream_id
        if buffer_ms is not UNSET:
            field_dict["BufferMs"] = buffer_ms
        if requires_looping is not UNSET:
            field_dict["RequiresLooping"] = requires_looping
        if supports_probing is not UNSET:
            field_dict["SupportsProbing"] = supports_probing
        if video_type is not UNSET:
            field_dict["VideoType"] = video_type
        if iso_type is not UNSET:
            field_dict["IsoType"] = iso_type
        if video_3d_format is not UNSET:
            field_dict["Video3DFormat"] = video_3d_format
        if media_streams is not UNSET:
            field_dict["MediaStreams"] = media_streams
        if media_attachments is not UNSET:
            field_dict["MediaAttachments"] = media_attachments
        if formats is not UNSET:
            field_dict["Formats"] = formats
        if bitrate is not UNSET:
            field_dict["Bitrate"] = bitrate
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp
        if required_http_headers is not UNSET:
            field_dict["RequiredHttpHeaders"] = required_http_headers
        if transcoding_url is not UNSET:
            field_dict["TranscodingUrl"] = transcoding_url
        if transcoding_sub_protocol is not UNSET:
            field_dict["TranscodingSubProtocol"] = transcoding_sub_protocol
        if transcoding_container is not UNSET:
            field_dict["TranscodingContainer"] = transcoding_container
        if analyze_duration_ms is not UNSET:
            field_dict["AnalyzeDurationMs"] = analyze_duration_ms
        if default_audio_stream_index is not UNSET:
            field_dict["DefaultAudioStreamIndex"] = default_audio_stream_index
        if default_subtitle_stream_index is not UNSET:
            field_dict["DefaultSubtitleStreamIndex"] = default_subtitle_stream_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_attachment import MediaAttachment
        from ..models.media_source_info_required_http_headers import MediaSourceInfoRequiredHttpHeaders
        from ..models.media_stream import MediaStream

        d = src_dict.copy()
        _protocol = d.pop("Protocol", UNSET)
        protocol: Union[Unset, MediaProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = MediaProtocol(_protocol)

        id = d.pop("Id", UNSET)

        path = d.pop("Path", UNSET)

        encoder_path = d.pop("EncoderPath", UNSET)

        _encoder_protocol = d.pop("EncoderProtocol", UNSET)
        encoder_protocol: Union[Unset, None, MediaProtocol]
        if _encoder_protocol is None:
            encoder_protocol = None
        elif isinstance(_encoder_protocol, Unset):
            encoder_protocol = UNSET
        else:
            encoder_protocol = MediaProtocol(_encoder_protocol)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, MediaSourceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MediaSourceType(_type)

        container = d.pop("Container", UNSET)

        size = d.pop("Size", UNSET)

        name = d.pop("Name", UNSET)

        is_remote = d.pop("IsRemote", UNSET)

        e_tag = d.pop("ETag", UNSET)

        run_time_ticks = d.pop("RunTimeTicks", UNSET)

        read_at_native_framerate = d.pop("ReadAtNativeFramerate", UNSET)

        ignore_dts = d.pop("IgnoreDts", UNSET)

        ignore_index = d.pop("IgnoreIndex", UNSET)

        gen_pts_input = d.pop("GenPtsInput", UNSET)

        supports_transcoding = d.pop("SupportsTranscoding", UNSET)

        supports_direct_stream = d.pop("SupportsDirectStream", UNSET)

        supports_direct_play = d.pop("SupportsDirectPlay", UNSET)

        is_infinite_stream = d.pop("IsInfiniteStream", UNSET)

        requires_opening = d.pop("RequiresOpening", UNSET)

        open_token = d.pop("OpenToken", UNSET)

        requires_closing = d.pop("RequiresClosing", UNSET)

        live_stream_id = d.pop("LiveStreamId", UNSET)

        buffer_ms = d.pop("BufferMs", UNSET)

        requires_looping = d.pop("RequiresLooping", UNSET)

        supports_probing = d.pop("SupportsProbing", UNSET)

        _video_type = d.pop("VideoType", UNSET)
        video_type: Union[Unset, None, VideoType]
        if _video_type is None:
            video_type = None
        elif isinstance(_video_type, Unset):
            video_type = UNSET
        else:
            video_type = VideoType(_video_type)

        _iso_type = d.pop("IsoType", UNSET)
        iso_type: Union[Unset, None, IsoType]
        if _iso_type is None:
            iso_type = None
        elif isinstance(_iso_type, Unset):
            iso_type = UNSET
        else:
            iso_type = IsoType(_iso_type)

        _video_3d_format = d.pop("Video3DFormat", UNSET)
        video_3d_format: Union[Unset, None, Video3DFormat]
        if _video_3d_format is None:
            video_3d_format = None
        elif isinstance(_video_3d_format, Unset):
            video_3d_format = UNSET
        else:
            video_3d_format = Video3DFormat(_video_3d_format)

        media_streams = []
        _media_streams = d.pop("MediaStreams", UNSET)
        for media_streams_item_data in _media_streams or []:
            media_streams_item = MediaStream.from_dict(media_streams_item_data)

            media_streams.append(media_streams_item)

        media_attachments = []
        _media_attachments = d.pop("MediaAttachments", UNSET)
        for media_attachments_item_data in _media_attachments or []:
            media_attachments_item = MediaAttachment.from_dict(media_attachments_item_data)

            media_attachments.append(media_attachments_item)

        formats = cast(List[str], d.pop("Formats", UNSET))

        bitrate = d.pop("Bitrate", UNSET)

        _timestamp = d.pop("Timestamp", UNSET)
        timestamp: Union[Unset, None, TransportStreamTimestamp]
        if _timestamp is None:
            timestamp = None
        elif isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = TransportStreamTimestamp(_timestamp)

        _required_http_headers = d.pop("RequiredHttpHeaders", UNSET)
        required_http_headers: Union[Unset, None, MediaSourceInfoRequiredHttpHeaders]
        if _required_http_headers is None:
            required_http_headers = None
        elif isinstance(_required_http_headers, Unset):
            required_http_headers = UNSET
        else:
            required_http_headers = MediaSourceInfoRequiredHttpHeaders.from_dict(_required_http_headers)

        transcoding_url = d.pop("TranscodingUrl", UNSET)

        transcoding_sub_protocol = d.pop("TranscodingSubProtocol", UNSET)

        transcoding_container = d.pop("TranscodingContainer", UNSET)

        analyze_duration_ms = d.pop("AnalyzeDurationMs", UNSET)

        default_audio_stream_index = d.pop("DefaultAudioStreamIndex", UNSET)

        default_subtitle_stream_index = d.pop("DefaultSubtitleStreamIndex", UNSET)

        media_source_info = cls(
            protocol=protocol,
            id=id,
            path=path,
            encoder_path=encoder_path,
            encoder_protocol=encoder_protocol,
            type=type,
            container=container,
            size=size,
            name=name,
            is_remote=is_remote,
            e_tag=e_tag,
            run_time_ticks=run_time_ticks,
            read_at_native_framerate=read_at_native_framerate,
            ignore_dts=ignore_dts,
            ignore_index=ignore_index,
            gen_pts_input=gen_pts_input,
            supports_transcoding=supports_transcoding,
            supports_direct_stream=supports_direct_stream,
            supports_direct_play=supports_direct_play,
            is_infinite_stream=is_infinite_stream,
            requires_opening=requires_opening,
            open_token=open_token,
            requires_closing=requires_closing,
            live_stream_id=live_stream_id,
            buffer_ms=buffer_ms,
            requires_looping=requires_looping,
            supports_probing=supports_probing,
            video_type=video_type,
            iso_type=iso_type,
            video_3d_format=video_3d_format,
            media_streams=media_streams,
            media_attachments=media_attachments,
            formats=formats,
            bitrate=bitrate,
            timestamp=timestamp,
            required_http_headers=required_http_headers,
            transcoding_url=transcoding_url,
            transcoding_sub_protocol=transcoding_sub_protocol,
            transcoding_container=transcoding_container,
            analyze_duration_ms=analyze_duration_ms,
            default_audio_stream_index=default_audio_stream_index,
            default_subtitle_stream_index=default_subtitle_stream_index,
        )

        return media_source_info
