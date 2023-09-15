from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.live_stream_response import LiveStreamResponse
from ...models.open_live_stream_dto import OpenLiveStreamDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: OpenLiveStreamDto,
    open_token: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    item_id: Union[Unset, None, str] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["openToken"] = open_token

    params["userId"] = user_id

    params["playSessionId"] = play_session_id

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["startTimeTicks"] = start_time_ticks

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    params["maxAudioChannels"] = max_audio_channels

    params["itemId"] = item_id

    params["enableDirectPlay"] = enable_direct_play

    params["enableDirectStream"] = enable_direct_stream

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/LiveStreams/Open",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LiveStreamResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LiveStreamResponse.from_dict(response.json())

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
) -> Response[Union[Any, LiveStreamResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: OpenLiveStreamDto,
    open_token: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    item_id: Union[Unset, None, str] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        item_id (Union[Unset, None, str]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        json_body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LiveStreamResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: OpenLiveStreamDto,
    open_token: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    item_id: Union[Unset, None, str] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        item_id (Union[Unset, None, str]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        json_body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LiveStreamResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: OpenLiveStreamDto,
    open_token: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    item_id: Union[Unset, None, str] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        item_id (Union[Unset, None, str]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        json_body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LiveStreamResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: OpenLiveStreamDto,
    open_token: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    item_id: Union[Unset, None, str] = UNSET,
    enable_direct_play: Union[Unset, None, bool] = UNSET,
    enable_direct_stream: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, LiveStreamResponse]]:
    """Opens a media source.

    Args:
        open_token (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        max_streaming_bitrate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        max_audio_channels (Union[Unset, None, int]):
        item_id (Union[Unset, None, str]):
        enable_direct_play (Union[Unset, None, bool]):
        enable_direct_stream (Union[Unset, None, bool]):
        json_body (OpenLiveStreamDto): Open live stream dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LiveStreamResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
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
        )
    ).parsed
