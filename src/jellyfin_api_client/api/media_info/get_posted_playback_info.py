from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.playback_info_dto import PlaybackInfoDto
from ...models.playback_info_response import PlaybackInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    json_body: PlaybackInfoDto,
    user_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    auto_open_live_stream: Union[Unset, None, bool] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
    enable_transcoding: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["startTimeTicks"] = start_time_ticks

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    params["maxAudioChannels"] = max_audio_channels

    params["mediaSourceId"] = media_source_id

    params["liveStreamId"] = live_stream_id

    params["autoOpenLiveStream"] = auto_open_live_stream

    params["enableDirectPlay"] = enable_direct_play

    params["enableDirectStream"] = enable_direct_stream

    params["enableTranscoding"] = enable_transcoding

    params["allowVideoStreamCopy"] = allow_video_stream_copy

    params["allowAudioStreamCopy"] = allow_audio_stream_copy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/Items/{itemId}/PlaybackInfo".format(
            itemId=item_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PlaybackInfoResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PlaybackInfoResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PlaybackInfoResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PlaybackInfoDto,
    user_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    auto_open_live_stream: Union[Unset, None, bool] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
    enable_transcoding: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, PlaybackInfoResponse]]:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (str):
        user_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        live_stream_id (Union[Unset, None, str]):
        auto_open_live_stream (Union[Unset, None, bool]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        enable_transcoding (Union[Unset, None, bool]):
        allow_video_stream_copy (Union[Unset, None, bool]):
        allow_audio_stream_copy (Union[Unset, None, bool]):
        json_body (PlaybackInfoDto): Plabyback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaybackInfoResponse]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        json_body=json_body,
        user_id=user_id,
        max_streaming_bitrate=max_streaming_bitrate,
        start_time_ticks=start_time_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        max_audio_channels=max_audio_channels,
        media_source_id=media_source_id,
        live_stream_id=live_stream_id,
        auto_open_live_stream=auto_open_live_stream,
        enable_direct_play=enable_direct_play,
        enable_direct_stream=enable_direct_stream,
        enable_transcoding=enable_transcoding,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PlaybackInfoDto,
    user_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    auto_open_live_stream: Union[Unset, None, bool] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
    enable_transcoding: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, PlaybackInfoResponse]]:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (str):
        user_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        live_stream_id (Union[Unset, None, str]):
        auto_open_live_stream (Union[Unset, None, bool]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        enable_transcoding (Union[Unset, None, bool]):
        allow_video_stream_copy (Union[Unset, None, bool]):
        allow_audio_stream_copy (Union[Unset, None, bool]):
        json_body (PlaybackInfoDto): Plabyback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaybackInfoResponse]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        json_body=json_body,
        user_id=user_id,
        max_streaming_bitrate=max_streaming_bitrate,
        start_time_ticks=start_time_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        max_audio_channels=max_audio_channels,
        media_source_id=media_source_id,
        live_stream_id=live_stream_id,
        auto_open_live_stream=auto_open_live_stream,
        enable_direct_play=enable_direct_play,
        enable_direct_stream=enable_direct_stream,
        enable_transcoding=enable_transcoding,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PlaybackInfoDto,
    user_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    auto_open_live_stream: Union[Unset, None, bool] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
    enable_transcoding: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, PlaybackInfoResponse]]:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (str):
        user_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        live_stream_id (Union[Unset, None, str]):
        auto_open_live_stream (Union[Unset, None, bool]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        enable_transcoding (Union[Unset, None, bool]):
        allow_video_stream_copy (Union[Unset, None, bool]):
        allow_audio_stream_copy (Union[Unset, None, bool]):
        json_body (PlaybackInfoDto): Plabyback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaybackInfoResponse]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        json_body=json_body,
        user_id=user_id,
        max_streaming_bitrate=max_streaming_bitrate,
        start_time_ticks=start_time_ticks,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        max_audio_channels=max_audio_channels,
        media_source_id=media_source_id,
        live_stream_id=live_stream_id,
        auto_open_live_stream=auto_open_live_stream,
        enable_direct_play=enable_direct_play,
        enable_direct_stream=enable_direct_stream,
        enable_transcoding=enable_transcoding,
        allow_video_stream_copy=allow_video_stream_copy,
        allow_audio_stream_copy=allow_audio_stream_copy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PlaybackInfoDto,
    user_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    auto_open_live_stream: Union[Unset, None, bool] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
    enable_transcoding: Union[Unset, None, bool] = UNSET,
    allow_video_stream_copy: Union[Unset, None, bool] = UNSET,
    allow_audio_stream_copy: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, PlaybackInfoResponse]]:
    """Gets live playback media info for an item.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        item_id (str):
        user_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        live_stream_id (Union[Unset, None, str]):
        auto_open_live_stream (Union[Unset, None, bool]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        enable_transcoding (Union[Unset, None, bool]):
        allow_video_stream_copy (Union[Unset, None, bool]):
        allow_audio_stream_copy (Union[Unset, None, bool]):
        json_body (PlaybackInfoDto): Plabyback info dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaybackInfoResponse]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            json_body=json_body,
            user_id=user_id,
            max_streaming_bitrate=max_streaming_bitrate,
            start_time_ticks=start_time_ticks,
            audio_stream_index=audio_stream_index,
            subtitle_stream_index=subtitle_stream_index,
            max_audio_channels=max_audio_channels,
            media_source_id=media_source_id,
            live_stream_id=live_stream_id,
            auto_open_live_stream=auto_open_live_stream,
            enable_direct_play=enable_direct_play,
            enable_direct_stream=enable_direct_stream,
            enable_transcoding=enable_transcoding,
            allow_video_stream_copy=allow_video_stream_copy,
            allow_audio_stream_copy=allow_audio_stream_copy,
        )
    ).parsed
