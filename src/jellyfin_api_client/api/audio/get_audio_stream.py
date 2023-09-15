from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.encoding_context import EncodingContext
from ...models.get_audio_stream_stream_options import GetAudioStreamStreamOptions
from ...models.subtitle_delivery_method import SubtitleDeliveryMethod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    container: Union[Unset, None, str] = UNSET,
    static: Union[Unset, None, bool] = UNSET,
    params: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    device_profile_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    segment_container: Union[Unset, None, str] = UNSET,
    segment_length: Union[Unset, None, int] = UNSET,
    min_segments: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    audio_codec: Union[Unset, None, str] = UNSET,
    enable_auto_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, None, bool] = UNSET,
    audio_sample_rate: Union[Unset, None, int] = UNSET,
    max_audio_bit_depth: Union[Unset, None, int] = UNSET,
    audio_bit_rate: Union[Unset, None, int] = UNSET,
    audio_channels: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    profile: Union[Unset, None, str] = UNSET,
    level: Union[Unset, None, str] = UNSET,
    framerate: Union[Unset, None, float] = UNSET,
    max_framerate: Union[Unset, None, float] = UNSET,
    copy_timestamps: Union[Unset, None, bool] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    video_bit_rate: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_method: Union[Unset, None, SubtitleDeliveryMethod] = UNSET,
    max_ref_frames: Union[Unset, None, int] = UNSET,
    max_video_bit_depth: Union[Unset, None, int] = UNSET,
    require_avc: Union[Unset, None, bool] = UNSET,
    de_interlace: Union[Unset, None, bool] = UNSET,
    require_non_anamorphic: Union[Unset, None, bool] = UNSET,
    transcoding_max_audio_channels: Union[Unset, None, int] = UNSET,
    cpu_core_limit: Union[Unset, None, int] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    enable_mpegts_m2_ts_mode: Union[Unset, None, bool] = UNSET,
    video_codec: Union[Unset, None, str] = UNSET,
    subtitle_codec: Union[Unset, None, str] = UNSET,
    transcode_reasons: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    video_stream_index: Union[Unset, None, int] = UNSET,
    context: Union[Unset, None, EncodingContext] = UNSET,
    stream_options: Union[Unset, None, "GetAudioStreamStreamOptions"] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["container"] = container

    params["static"] = static

    params["params"] = params

    params["tag"] = tag

    params["deviceProfileId"] = device_profile_id

    params["playSessionId"] = play_session_id

    params["segmentContainer"] = segment_container

    params["segmentLength"] = segment_length

    params["minSegments"] = min_segments

    params["mediaSourceId"] = media_source_id

    params["deviceId"] = device_id

    params["audioCodec"] = audio_codec

    params["enableAutoStreamCopy"] = enable_auto_stream_copy

    params["allowVideoStreamCopy"] = allow_video_stream_copy

    params["allowAudioStreamCopy"] = allow_audio_stream_copy

    params["breakOnNonKeyFrames"] = break_on_non_key_frames

    params["audioSampleRate"] = audio_sample_rate

    params["maxAudioBitDepth"] = max_audio_bit_depth

    params["audioBitRate"] = audio_bit_rate

    params["audioChannels"] = audio_channels

    params["maxAudioChannels"] = max_audio_channels

    params["profile"] = profile

    params["level"] = level

    params["framerate"] = framerate

    params["maxFramerate"] = max_framerate

    params["copyTimestamps"] = copy_timestamps

    params["startTimeTicks"] = start_time_ticks

    params["width"] = width

    params["height"] = height

    params["videoBitRate"] = video_bit_rate

    params["subtitleStreamIndex"] = subtitle_stream_index

    json_subtitle_method: Union[Unset, None, str] = UNSET
    if not isinstance(subtitle_method, Unset):
        json_subtitle_method = subtitle_method.value if subtitle_method else None

    params["subtitleMethod"] = json_subtitle_method

    params["maxRefFrames"] = max_ref_frames

    params["maxVideoBitDepth"] = max_video_bit_depth

    params["requireAvc"] = require_avc

    params["deInterlace"] = de_interlace

    params["requireNonAnamorphic"] = require_non_anamorphic

    params["transcodingMaxAudioChannels"] = transcoding_max_audio_channels

    params["cpuCoreLimit"] = cpu_core_limit

    params["liveStreamId"] = live_stream_id

    params["enableMpegtsM2TsMode"] = enable_mpegts_m2_ts_mode

    params["videoCodec"] = video_codec

    params["subtitleCodec"] = subtitle_codec

    params["transcodeReasons"] = transcode_reasons

    params["audioStreamIndex"] = audio_stream_index

    params["videoStreamIndex"] = video_stream_index

    json_context: Union[Unset, None, str] = UNSET
    if not isinstance(context, Unset):
        json_context = context.value if context else None

    params["context"] = json_context

    json_stream_options: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(stream_options, Unset):
        json_stream_options = stream_options.to_dict() if stream_options else None

    if not isinstance(json_stream_options, Unset) and json_stream_options is not None:
        params.update(json_stream_options)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Audio/{itemId}/stream".format(
            itemId=item_id,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    container: Union[Unset, None, str] = UNSET,
    static: Union[Unset, None, bool] = UNSET,
    params: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    device_profile_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    segment_container: Union[Unset, None, str] = UNSET,
    segment_length: Union[Unset, None, int] = UNSET,
    min_segments: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    audio_codec: Union[Unset, None, str] = UNSET,
    enable_auto_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, None, bool] = UNSET,
    audio_sample_rate: Union[Unset, None, int] = UNSET,
    max_audio_bit_depth: Union[Unset, None, int] = UNSET,
    audio_bit_rate: Union[Unset, None, int] = UNSET,
    audio_channels: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    profile: Union[Unset, None, str] = UNSET,
    level: Union[Unset, None, str] = UNSET,
    framerate: Union[Unset, None, float] = UNSET,
    max_framerate: Union[Unset, None, float] = UNSET,
    copy_timestamps: Union[Unset, None, bool] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    video_bit_rate: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_method: Union[Unset, None, SubtitleDeliveryMethod] = UNSET,
    max_ref_frames: Union[Unset, None, int] = UNSET,
    max_video_bit_depth: Union[Unset, None, int] = UNSET,
    require_avc: Union[Unset, None, bool] = UNSET,
    de_interlace: Union[Unset, None, bool] = UNSET,
    require_non_anamorphic: Union[Unset, None, bool] = UNSET,
    transcoding_max_audio_channels: Union[Unset, None, int] = UNSET,
    cpu_core_limit: Union[Unset, None, int] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    enable_mpegts_m2_ts_mode: Union[Unset, None, bool] = UNSET,
    video_codec: Union[Unset, None, str] = UNSET,
    subtitle_codec: Union[Unset, None, str] = UNSET,
    transcode_reasons: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    video_stream_index: Union[Unset, None, int] = UNSET,
    context: Union[Unset, None, EncodingContext] = UNSET,
    stream_options: Union[Unset, None, "GetAudioStreamStreamOptions"] = UNSET,
) -> Response[Any]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, None, str]):
        static (Union[Unset, None, bool]):
        params (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        device_profile_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        segment_container (Union[Unset, None, str]):
        segment_length (Union[Unset, None, int]):
        min_segments (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        audio_codec (Union[Unset, None, str]):
        enable_auto_stream_copy (Union[Unset, None, bool]):
        allow_video_stream_copy (Union[Unset, None, bool]):
        allow_audio_stream_copy (Union[Unset, None, bool]):
        break_on_non_key_frames (Union[Unset, None, bool]):
        audio_sample_rate (Union[Unset, None, int]):
        max_audio_bit_depth (Union[Unset, None, int]):
        audio_bit_rate (Union[Unset, None, int]):
        audio_channels (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        profile (Union[Unset, None, str]):
        level (Union[Unset, None, str]):
        framerate (Union[Unset, None, float]):
        max_framerate (Union[Unset, None, float]):
        copy_timestamps (Union[Unset, None, bool]):
        start_time_ticks (Union[Unset, None, int]):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        video_bit_rate (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        subtitle_method (Union[Unset, None, SubtitleDeliveryMethod]): Delivery method to use
            during playback of a specific subtitle format.
        max_ref_frames (Union[Unset, None, int]):
        max_video_bit_depth (Union[Unset, None, int]):
        require_avc (Union[Unset, None, bool]):
        de_interlace (Union[Unset, None, bool]):
        require_non_anamorphic (Union[Unset, None, bool]):
        transcoding_max_audio_channels (Union[Unset, None, int]):
        cpu_core_limit (Union[Unset, None, int]):
        live_stream_id (Union[Unset, None, str]):
        enable_mpegts_m2_ts_mode (Union[Unset, None, bool]):
        video_codec (Union[Unset, None, str]):
        subtitle_codec (Union[Unset, None, str]):
        transcode_reasons (Union[Unset, None, str]):
        audio_stream_index (Union[Unset, None, int]):
        video_stream_index (Union[Unset, None, int]):
        context (Union[Unset, None, EncodingContext]):
        stream_options (Union[Unset, None, GetAudioStreamStreamOptions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        static=static,
        params=params,
        tag=tag,
        device_profile_id=device_profile_id,
        play_session_id=play_session_id,
        segment_container=segment_container,
        segment_length=segment_length,
        min_segments=min_segments,
        media_source_id=media_source_id,
        device_id=device_id,
        audio_codec=audio_codec,
        enable_auto_stream_copy=enable_auto_stream_copy,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
        break_on_non_key_frames=break_on_non_key_frames,
        audio_sample_rate=audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        audio_bit_rate=audio_bit_rate,
        audio_channels=audio_channels,
        max_audio_channels=max_audio_channels,
        profile=profile,
        level=level,
        framerate=framerate,
        max_framerate=max_framerate,
        copy_timestamps=copy_timestamps,
        start_time_ticks=start_time_ticks,
        width=width,
        height=height,
        video_bit_rate=video_bit_rate,
        subtitle_stream_index=subtitle_stream_index,
        subtitle_method=subtitle_method,
        max_ref_frames=max_ref_frames,
        max_video_bit_depth=max_video_bit_depth,
        require_avc=require_avc,
        de_interlace=de_interlace,
        require_non_anamorphic=require_non_anamorphic,
        transcoding_max_audio_channels=transcoding_max_audio_channels,
        cpu_core_limit=cpu_core_limit,
        live_stream_id=live_stream_id,
        enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
        video_codec=video_codec,
        subtitle_codec=subtitle_codec,
        transcode_reasons=transcode_reasons,
        audio_stream_index=audio_stream_index,
        video_stream_index=video_stream_index,
        context=context,
        stream_options=stream_options,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    container: Union[Unset, None, str] = UNSET,
    static: Union[Unset, None, bool] = UNSET,
    params: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, str] = UNSET,
    device_profile_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    segment_container: Union[Unset, None, str] = UNSET,
    segment_length: Union[Unset, None, int] = UNSET,
    min_segments: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    audio_codec: Union[Unset, None, str] = UNSET,
    enable_auto_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, None, bool] = UNSET,
    audio_sample_rate: Union[Unset, None, int] = UNSET,
    max_audio_bit_depth: Union[Unset, None, int] = UNSET,
    audio_bit_rate: Union[Unset, None, int] = UNSET,
    audio_channels: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    profile: Union[Unset, None, str] = UNSET,
    level: Union[Unset, None, str] = UNSET,
    framerate: Union[Unset, None, float] = UNSET,
    max_framerate: Union[Unset, None, float] = UNSET,
    copy_timestamps: Union[Unset, None, bool] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    video_bit_rate: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_method: Union[Unset, None, SubtitleDeliveryMethod] = UNSET,
    max_ref_frames: Union[Unset, None, int] = UNSET,
    max_video_bit_depth: Union[Unset, None, int] = UNSET,
    require_avc: Union[Unset, None, bool] = UNSET,
    de_interlace: Union[Unset, None, bool] = UNSET,
    require_non_anamorphic: Union[Unset, None, bool] = UNSET,
    transcoding_max_audio_channels: Union[Unset, None, int] = UNSET,
    cpu_core_limit: Union[Unset, None, int] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    enable_mpegts_m2_ts_mode: Union[Unset, None, bool] = UNSET,
    video_codec: Union[Unset, None, str] = UNSET,
    subtitle_codec: Union[Unset, None, str] = UNSET,
    transcode_reasons: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    video_stream_index: Union[Unset, None, int] = UNSET,
    context: Union[Unset, None, EncodingContext] = UNSET,
    stream_options: Union[Unset, None, "GetAudioStreamStreamOptions"] = UNSET,
) -> Response[Any]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, None, str]):
        static (Union[Unset, None, bool]):
        params (Union[Unset, None, str]):
        tag (Union[Unset, None, str]):
        device_profile_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        segment_container (Union[Unset, None, str]):
        segment_length (Union[Unset, None, int]):
        min_segments (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        audio_codec (Union[Unset, None, str]):
        enable_auto_stream_copy (Union[Unset, None, bool]):
        allow_video_stream_copy (Union[Unset, None, bool]):
        allow_audio_stream_copy (Union[Unset, None, bool]):
        break_on_non_key_frames (Union[Unset, None, bool]):
        audio_sample_rate (Union[Unset, None, int]):
        max_audio_bit_depth (Union[Unset, None, int]):
        audio_bit_rate (Union[Unset, None, int]):
        audio_channels (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        profile (Union[Unset, None, str]):
        level (Union[Unset, None, str]):
        framerate (Union[Unset, None, float]):
        max_framerate (Union[Unset, None, float]):
        copy_timestamps (Union[Unset, None, bool]):
        start_time_ticks (Union[Unset, None, int]):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        video_bit_rate (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        subtitle_method (Union[Unset, None, SubtitleDeliveryMethod]): Delivery method to use
            during playback of a specific subtitle format.
        max_ref_frames (Union[Unset, None, int]):
        max_video_bit_depth (Union[Unset, None, int]):
        require_avc (Union[Unset, None, bool]):
        de_interlace (Union[Unset, None, bool]):
        require_non_anamorphic (Union[Unset, None, bool]):
        transcoding_max_audio_channels (Union[Unset, None, int]):
        cpu_core_limit (Union[Unset, None, int]):
        live_stream_id (Union[Unset, None, str]):
        enable_mpegts_m2_ts_mode (Union[Unset, None, bool]):
        video_codec (Union[Unset, None, str]):
        subtitle_codec (Union[Unset, None, str]):
        transcode_reasons (Union[Unset, None, str]):
        audio_stream_index (Union[Unset, None, int]):
        video_stream_index (Union[Unset, None, int]):
        context (Union[Unset, None, EncodingContext]):
        stream_options (Union[Unset, None, GetAudioStreamStreamOptions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        static=static,
        params=params,
        tag=tag,
        device_profile_id=device_profile_id,
        play_session_id=play_session_id,
        segment_container=segment_container,
        segment_length=segment_length,
        min_segments=min_segments,
        media_source_id=media_source_id,
        device_id=device_id,
        audio_codec=audio_codec,
        enable_auto_stream_copy=enable_auto_stream_copy,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
        break_on_non_key_frames=break_on_non_key_frames,
        audio_sample_rate=audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        audio_bit_rate=audio_bit_rate,
        audio_channels=audio_channels,
        max_audio_channels=max_audio_channels,
        profile=profile,
        level=level,
        framerate=framerate,
        max_framerate=max_framerate,
        copy_timestamps=copy_timestamps,
        start_time_ticks=start_time_ticks,
        width=width,
        height=height,
        video_bit_rate=video_bit_rate,
        subtitle_stream_index=subtitle_stream_index,
        subtitle_method=subtitle_method,
        max_ref_frames=max_ref_frames,
        max_video_bit_depth=max_video_bit_depth,
        require_avc=require_avc,
        de_interlace=de_interlace,
        require_non_anamorphic=require_non_anamorphic,
        transcoding_max_audio_channels=transcoding_max_audio_channels,
        cpu_core_limit=cpu_core_limit,
        live_stream_id=live_stream_id,
        enable_mpegts_m2_ts_mode=enable_mpegts_m2_ts_mode,
        video_codec=video_codec,
        subtitle_codec=subtitle_codec,
        transcode_reasons=transcode_reasons,
        audio_stream_index=audio_stream_index,
        video_stream_index=video_stream_index,
        context=context,
        stream_options=stream_options,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
