from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.media_stream_type import MediaStreamType
from ..models.subtitle_delivery_method import SubtitleDeliveryMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaStream")


@_attrs_define
class MediaStream:
    """Class MediaStream.

    Attributes:
        codec (Union[Unset, None, str]): Gets or sets the codec.
        codec_tag (Union[Unset, None, str]): Gets or sets the codec tag.
        language (Union[Unset, None, str]): Gets or sets the language.
        color_range (Union[Unset, None, str]): Gets or sets the color range.
        color_space (Union[Unset, None, str]): Gets or sets the color space.
        color_transfer (Union[Unset, None, str]): Gets or sets the color transfer.
        color_primaries (Union[Unset, None, str]): Gets or sets the color primaries.
        dv_version_major (Union[Unset, None, int]): Gets or sets the Dolby Vision version major.
        dv_version_minor (Union[Unset, None, int]): Gets or sets the Dolby Vision version minor.
        dv_profile (Union[Unset, None, int]): Gets or sets the Dolby Vision profile.
        dv_level (Union[Unset, None, int]): Gets or sets the Dolby Vision level.
        rpu_present_flag (Union[Unset, None, int]): Gets or sets the Dolby Vision rpu present flag.
        el_present_flag (Union[Unset, None, int]): Gets or sets the Dolby Vision el present flag.
        bl_present_flag (Union[Unset, None, int]): Gets or sets the Dolby Vision bl present flag.
        dv_bl_signal_compatibility_id (Union[Unset, None, int]): Gets or sets the Dolby Vision bl signal compatibility
            id.
        comment (Union[Unset, None, str]): Gets or sets the comment.
        time_base (Union[Unset, None, str]): Gets or sets the time base.
        codec_time_base (Union[Unset, None, str]): Gets or sets the codec time base.
        title (Union[Unset, None, str]): Gets or sets the title.
        video_range (Union[Unset, None, str]): Gets the video range.
        video_range_type (Union[Unset, None, str]): Gets the video range type.
        video_do_vi_title (Union[Unset, None, str]): Gets the video dovi title.
        localized_undefined (Union[Unset, None, str]):
        localized_default (Union[Unset, None, str]):
        localized_forced (Union[Unset, None, str]):
        localized_external (Union[Unset, None, str]):
        display_title (Union[Unset, None, str]):
        nal_length_size (Union[Unset, None, str]):
        is_interlaced (Union[Unset, bool]): Gets or sets a value indicating whether this instance is interlaced.
        is_avc (Union[Unset, None, bool]):
        channel_layout (Union[Unset, None, str]): Gets or sets the channel layout.
        bit_rate (Union[Unset, None, int]): Gets or sets the bit rate.
        bit_depth (Union[Unset, None, int]): Gets or sets the bit depth.
        ref_frames (Union[Unset, None, int]): Gets or sets the reference frames.
        packet_length (Union[Unset, None, int]): Gets or sets the length of the packet.
        channels (Union[Unset, None, int]): Gets or sets the channels.
        sample_rate (Union[Unset, None, int]): Gets or sets the sample rate.
        is_default (Union[Unset, bool]): Gets or sets a value indicating whether this instance is default.
        is_forced (Union[Unset, bool]): Gets or sets a value indicating whether this instance is forced.
        height (Union[Unset, None, int]): Gets or sets the height.
        width (Union[Unset, None, int]): Gets or sets the width.
        average_frame_rate (Union[Unset, None, float]): Gets or sets the average frame rate.
        real_frame_rate (Union[Unset, None, float]): Gets or sets the real frame rate.
        profile (Union[Unset, None, str]): Gets or sets the profile.
        type (Union[Unset, MediaStreamType]): Enum MediaStreamType.
        aspect_ratio (Union[Unset, None, str]): Gets or sets the aspect ratio.
        index (Union[Unset, int]): Gets or sets the index.
        score (Union[Unset, None, int]): Gets or sets the score.
        is_external (Union[Unset, bool]): Gets or sets a value indicating whether this instance is external.
        delivery_method (Union[Unset, None, SubtitleDeliveryMethod]): Delivery method to use during playback of a
            specific subtitle format.
        delivery_url (Union[Unset, None, str]): Gets or sets the delivery URL.
        is_external_url (Union[Unset, None, bool]): Gets or sets a value indicating whether this instance is external
            URL.
        is_text_subtitle_stream (Union[Unset, bool]):
        supports_external_stream (Union[Unset, bool]): Gets or sets a value indicating whether [supports external
            stream].
        path (Union[Unset, None, str]): Gets or sets the filename.
        pixel_format (Union[Unset, None, str]): Gets or sets the pixel format.
        level (Union[Unset, None, float]): Gets or sets the level.
        is_anamorphic (Union[Unset, None, bool]): Gets or sets whether this instance is anamorphic.
    """

    codec: Union[Unset, None, str] = UNSET
    codec_tag: Union[Unset, None, str] = UNSET
    language: Union[Unset, None, str] = UNSET
    color_range: Union[Unset, None, str] = UNSET
    color_space: Union[Unset, None, str] = UNSET
    color_transfer: Union[Unset, None, str] = UNSET
    color_primaries: Union[Unset, None, str] = UNSET
    dv_version_major: Union[Unset, None, int] = UNSET
    dv_version_minor: Union[Unset, None, int] = UNSET
    dv_profile: Union[Unset, None, int] = UNSET
    dv_level: Union[Unset, None, int] = UNSET
    rpu_present_flag: Union[Unset, None, int] = UNSET
    el_present_flag: Union[Unset, None, int] = UNSET
    bl_present_flag: Union[Unset, None, int] = UNSET
    dv_bl_signal_compatibility_id: Union[Unset, None, int] = UNSET
    comment: Union[Unset, None, str] = UNSET
    time_base: Union[Unset, None, str] = UNSET
    codec_time_base: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    video_range: Union[Unset, None, str] = UNSET
    video_range_type: Union[Unset, None, str] = UNSET
    video_do_vi_title: Union[Unset, None, str] = UNSET
    localized_undefined: Union[Unset, None, str] = UNSET
    localized_default: Union[Unset, None, str] = UNSET
    localized_forced: Union[Unset, None, str] = UNSET
    localized_external: Union[Unset, None, str] = UNSET
    display_title: Union[Unset, None, str] = UNSET
    nal_length_size: Union[Unset, None, str] = UNSET
    is_interlaced: Union[Unset, bool] = UNSET
    is_avc: Union[Unset, None, bool] = UNSET
    channel_layout: Union[Unset, None, str] = UNSET
    bit_rate: Union[Unset, None, int] = UNSET
    bit_depth: Union[Unset, None, int] = UNSET
    ref_frames: Union[Unset, None, int] = UNSET
    packet_length: Union[Unset, None, int] = UNSET
    channels: Union[Unset, None, int] = UNSET
    sample_rate: Union[Unset, None, int] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_forced: Union[Unset, bool] = UNSET
    height: Union[Unset, None, int] = UNSET
    width: Union[Unset, None, int] = UNSET
    average_frame_rate: Union[Unset, None, float] = UNSET
    real_frame_rate: Union[Unset, None, float] = UNSET
    profile: Union[Unset, None, str] = UNSET
    type: Union[Unset, MediaStreamType] = UNSET
    aspect_ratio: Union[Unset, None, str] = UNSET
    index: Union[Unset, int] = UNSET
    score: Union[Unset, None, int] = UNSET
    is_external: Union[Unset, bool] = UNSET
    delivery_method: Union[Unset, None, SubtitleDeliveryMethod] = UNSET
    delivery_url: Union[Unset, None, str] = UNSET
    is_external_url: Union[Unset, None, bool] = UNSET
    is_text_subtitle_stream: Union[Unset, bool] = UNSET
    supports_external_stream: Union[Unset, bool] = UNSET
    path: Union[Unset, None, str] = UNSET
    pixel_format: Union[Unset, None, str] = UNSET
    level: Union[Unset, None, float] = UNSET
    is_anamorphic: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        codec = self.codec
        codec_tag = self.codec_tag
        language = self.language
        color_range = self.color_range
        color_space = self.color_space
        color_transfer = self.color_transfer
        color_primaries = self.color_primaries
        dv_version_major = self.dv_version_major
        dv_version_minor = self.dv_version_minor
        dv_profile = self.dv_profile
        dv_level = self.dv_level
        rpu_present_flag = self.rpu_present_flag
        el_present_flag = self.el_present_flag
        bl_present_flag = self.bl_present_flag
        dv_bl_signal_compatibility_id = self.dv_bl_signal_compatibility_id
        comment = self.comment
        time_base = self.time_base
        codec_time_base = self.codec_time_base
        title = self.title
        video_range = self.video_range
        video_range_type = self.video_range_type
        video_do_vi_title = self.video_do_vi_title
        localized_undefined = self.localized_undefined
        localized_default = self.localized_default
        localized_forced = self.localized_forced
        localized_external = self.localized_external
        display_title = self.display_title
        nal_length_size = self.nal_length_size
        is_interlaced = self.is_interlaced
        is_avc = self.is_avc
        channel_layout = self.channel_layout
        bit_rate = self.bit_rate
        bit_depth = self.bit_depth
        ref_frames = self.ref_frames
        packet_length = self.packet_length
        channels = self.channels
        sample_rate = self.sample_rate
        is_default = self.is_default
        is_forced = self.is_forced
        height = self.height
        width = self.width
        average_frame_rate = self.average_frame_rate
        real_frame_rate = self.real_frame_rate
        profile = self.profile
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        aspect_ratio = self.aspect_ratio
        index = self.index
        score = self.score
        is_external = self.is_external
        delivery_method: Union[Unset, None, str] = UNSET
        if not isinstance(self.delivery_method, Unset):
            delivery_method = self.delivery_method.value if self.delivery_method else None

        delivery_url = self.delivery_url
        is_external_url = self.is_external_url
        is_text_subtitle_stream = self.is_text_subtitle_stream
        supports_external_stream = self.supports_external_stream
        path = self.path
        pixel_format = self.pixel_format
        level = self.level
        is_anamorphic = self.is_anamorphic

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if codec_tag is not UNSET:
            field_dict["CodecTag"] = codec_tag
        if language is not UNSET:
            field_dict["Language"] = language
        if color_range is not UNSET:
            field_dict["ColorRange"] = color_range
        if color_space is not UNSET:
            field_dict["ColorSpace"] = color_space
        if color_transfer is not UNSET:
            field_dict["ColorTransfer"] = color_transfer
        if color_primaries is not UNSET:
            field_dict["ColorPrimaries"] = color_primaries
        if dv_version_major is not UNSET:
            field_dict["DvVersionMajor"] = dv_version_major
        if dv_version_minor is not UNSET:
            field_dict["DvVersionMinor"] = dv_version_minor
        if dv_profile is not UNSET:
            field_dict["DvProfile"] = dv_profile
        if dv_level is not UNSET:
            field_dict["DvLevel"] = dv_level
        if rpu_present_flag is not UNSET:
            field_dict["RpuPresentFlag"] = rpu_present_flag
        if el_present_flag is not UNSET:
            field_dict["ElPresentFlag"] = el_present_flag
        if bl_present_flag is not UNSET:
            field_dict["BlPresentFlag"] = bl_present_flag
        if dv_bl_signal_compatibility_id is not UNSET:
            field_dict["DvBlSignalCompatibilityId"] = dv_bl_signal_compatibility_id
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if time_base is not UNSET:
            field_dict["TimeBase"] = time_base
        if codec_time_base is not UNSET:
            field_dict["CodecTimeBase"] = codec_time_base
        if title is not UNSET:
            field_dict["Title"] = title
        if video_range is not UNSET:
            field_dict["VideoRange"] = video_range
        if video_range_type is not UNSET:
            field_dict["VideoRangeType"] = video_range_type
        if video_do_vi_title is not UNSET:
            field_dict["VideoDoViTitle"] = video_do_vi_title
        if localized_undefined is not UNSET:
            field_dict["LocalizedUndefined"] = localized_undefined
        if localized_default is not UNSET:
            field_dict["LocalizedDefault"] = localized_default
        if localized_forced is not UNSET:
            field_dict["LocalizedForced"] = localized_forced
        if localized_external is not UNSET:
            field_dict["LocalizedExternal"] = localized_external
        if display_title is not UNSET:
            field_dict["DisplayTitle"] = display_title
        if nal_length_size is not UNSET:
            field_dict["NalLengthSize"] = nal_length_size
        if is_interlaced is not UNSET:
            field_dict["IsInterlaced"] = is_interlaced
        if is_avc is not UNSET:
            field_dict["IsAVC"] = is_avc
        if channel_layout is not UNSET:
            field_dict["ChannelLayout"] = channel_layout
        if bit_rate is not UNSET:
            field_dict["BitRate"] = bit_rate
        if bit_depth is not UNSET:
            field_dict["BitDepth"] = bit_depth
        if ref_frames is not UNSET:
            field_dict["RefFrames"] = ref_frames
        if packet_length is not UNSET:
            field_dict["PacketLength"] = packet_length
        if channels is not UNSET:
            field_dict["Channels"] = channels
        if sample_rate is not UNSET:
            field_dict["SampleRate"] = sample_rate
        if is_default is not UNSET:
            field_dict["IsDefault"] = is_default
        if is_forced is not UNSET:
            field_dict["IsForced"] = is_forced
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if average_frame_rate is not UNSET:
            field_dict["AverageFrameRate"] = average_frame_rate
        if real_frame_rate is not UNSET:
            field_dict["RealFrameRate"] = real_frame_rate
        if profile is not UNSET:
            field_dict["Profile"] = profile
        if type is not UNSET:
            field_dict["Type"] = type
        if aspect_ratio is not UNSET:
            field_dict["AspectRatio"] = aspect_ratio
        if index is not UNSET:
            field_dict["Index"] = index
        if score is not UNSET:
            field_dict["Score"] = score
        if is_external is not UNSET:
            field_dict["IsExternal"] = is_external
        if delivery_method is not UNSET:
            field_dict["DeliveryMethod"] = delivery_method
        if delivery_url is not UNSET:
            field_dict["DeliveryUrl"] = delivery_url
        if is_external_url is not UNSET:
            field_dict["IsExternalUrl"] = is_external_url
        if is_text_subtitle_stream is not UNSET:
            field_dict["IsTextSubtitleStream"] = is_text_subtitle_stream
        if supports_external_stream is not UNSET:
            field_dict["SupportsExternalStream"] = supports_external_stream
        if path is not UNSET:
            field_dict["Path"] = path
        if pixel_format is not UNSET:
            field_dict["PixelFormat"] = pixel_format
        if level is not UNSET:
            field_dict["Level"] = level
        if is_anamorphic is not UNSET:
            field_dict["IsAnamorphic"] = is_anamorphic

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        codec = d.pop("Codec", UNSET)

        codec_tag = d.pop("CodecTag", UNSET)

        language = d.pop("Language", UNSET)

        color_range = d.pop("ColorRange", UNSET)

        color_space = d.pop("ColorSpace", UNSET)

        color_transfer = d.pop("ColorTransfer", UNSET)

        color_primaries = d.pop("ColorPrimaries", UNSET)

        dv_version_major = d.pop("DvVersionMajor", UNSET)

        dv_version_minor = d.pop("DvVersionMinor", UNSET)

        dv_profile = d.pop("DvProfile", UNSET)

        dv_level = d.pop("DvLevel", UNSET)

        rpu_present_flag = d.pop("RpuPresentFlag", UNSET)

        el_present_flag = d.pop("ElPresentFlag", UNSET)

        bl_present_flag = d.pop("BlPresentFlag", UNSET)

        dv_bl_signal_compatibility_id = d.pop("DvBlSignalCompatibilityId", UNSET)

        comment = d.pop("Comment", UNSET)

        time_base = d.pop("TimeBase", UNSET)

        codec_time_base = d.pop("CodecTimeBase", UNSET)

        title = d.pop("Title", UNSET)

        video_range = d.pop("VideoRange", UNSET)

        video_range_type = d.pop("VideoRangeType", UNSET)

        video_do_vi_title = d.pop("VideoDoViTitle", UNSET)

        localized_undefined = d.pop("LocalizedUndefined", UNSET)

        localized_default = d.pop("LocalizedDefault", UNSET)

        localized_forced = d.pop("LocalizedForced", UNSET)

        localized_external = d.pop("LocalizedExternal", UNSET)

        display_title = d.pop("DisplayTitle", UNSET)

        nal_length_size = d.pop("NalLengthSize", UNSET)

        is_interlaced = d.pop("IsInterlaced", UNSET)

        is_avc = d.pop("IsAVC", UNSET)

        channel_layout = d.pop("ChannelLayout", UNSET)

        bit_rate = d.pop("BitRate", UNSET)

        bit_depth = d.pop("BitDepth", UNSET)

        ref_frames = d.pop("RefFrames", UNSET)

        packet_length = d.pop("PacketLength", UNSET)

        channels = d.pop("Channels", UNSET)

        sample_rate = d.pop("SampleRate", UNSET)

        is_default = d.pop("IsDefault", UNSET)

        is_forced = d.pop("IsForced", UNSET)

        height = d.pop("Height", UNSET)

        width = d.pop("Width", UNSET)

        average_frame_rate = d.pop("AverageFrameRate", UNSET)

        real_frame_rate = d.pop("RealFrameRate", UNSET)

        profile = d.pop("Profile", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, MediaStreamType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MediaStreamType(_type)

        aspect_ratio = d.pop("AspectRatio", UNSET)

        index = d.pop("Index", UNSET)

        score = d.pop("Score", UNSET)

        is_external = d.pop("IsExternal", UNSET)

        _delivery_method = d.pop("DeliveryMethod", UNSET)
        delivery_method: Union[Unset, None, SubtitleDeliveryMethod]
        if _delivery_method is None:
            delivery_method = None
        elif isinstance(_delivery_method, Unset):
            delivery_method = UNSET
        else:
            delivery_method = SubtitleDeliveryMethod(_delivery_method)

        delivery_url = d.pop("DeliveryUrl", UNSET)

        is_external_url = d.pop("IsExternalUrl", UNSET)

        is_text_subtitle_stream = d.pop("IsTextSubtitleStream", UNSET)

        supports_external_stream = d.pop("SupportsExternalStream", UNSET)

        path = d.pop("Path", UNSET)

        pixel_format = d.pop("PixelFormat", UNSET)

        level = d.pop("Level", UNSET)

        is_anamorphic = d.pop("IsAnamorphic", UNSET)

        media_stream = cls(
            codec=codec,
            codec_tag=codec_tag,
            language=language,
            color_range=color_range,
            color_space=color_space,
            color_transfer=color_transfer,
            color_primaries=color_primaries,
            dv_version_major=dv_version_major,
            dv_version_minor=dv_version_minor,
            dv_profile=dv_profile,
            dv_level=dv_level,
            rpu_present_flag=rpu_present_flag,
            el_present_flag=el_present_flag,
            bl_present_flag=bl_present_flag,
            dv_bl_signal_compatibility_id=dv_bl_signal_compatibility_id,
            comment=comment,
            time_base=time_base,
            codec_time_base=codec_time_base,
            title=title,
            video_range=video_range,
            video_range_type=video_range_type,
            video_do_vi_title=video_do_vi_title,
            localized_undefined=localized_undefined,
            localized_default=localized_default,
            localized_forced=localized_forced,
            localized_external=localized_external,
            display_title=display_title,
            nal_length_size=nal_length_size,
            is_interlaced=is_interlaced,
            is_avc=is_avc,
            channel_layout=channel_layout,
            bit_rate=bit_rate,
            bit_depth=bit_depth,
            ref_frames=ref_frames,
            packet_length=packet_length,
            channels=channels,
            sample_rate=sample_rate,
            is_default=is_default,
            is_forced=is_forced,
            height=height,
            width=width,
            average_frame_rate=average_frame_rate,
            real_frame_rate=real_frame_rate,
            profile=profile,
            type=type,
            aspect_ratio=aspect_ratio,
            index=index,
            score=score,
            is_external=is_external,
            delivery_method=delivery_method,
            delivery_url=delivery_url,
            is_external_url=is_external_url,
            is_text_subtitle_stream=is_text_subtitle_stream,
            supports_external_stream=supports_external_stream,
            path=path,
            pixel_format=pixel_format,
            level=level,
            is_anamorphic=is_anamorphic,
        )

        return media_stream
