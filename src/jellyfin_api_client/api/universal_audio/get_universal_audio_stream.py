from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    container: Union[Unset, None, List[str]] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    audio_codec: Union[Unset, None, str] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    transcoding_audio_channels: Union[Unset, None, int] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    audio_bit_rate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    transcoding_container: Union[Unset, None, str] = UNSET,
    transcoding_protocol: Union[Unset, None, str] = UNSET,
    max_audio_sample_rate: Union[Unset, None, int] = UNSET,
    max_audio_bit_depth: Union[Unset, None, int] = UNSET,
    enable_remote_media: Union[Unset, None, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, None, bool] = False,
    enable_redirection: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_container: Union[Unset, None, List[str]] = UNSET
    if not isinstance(container, Unset):
        if container is None:
            json_container = None
        else:
            json_container = container

    params["container"] = json_container

    params["mediaSourceId"] = media_source_id

    params["deviceId"] = device_id

    params["userId"] = user_id

    params["audioCodec"] = audio_codec

    params["maxAudioChannels"] = max_audio_channels

    params["transcodingAudioChannels"] = transcoding_audio_channels

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["audioBitRate"] = audio_bit_rate

    params["startTimeTicks"] = start_time_ticks

    params["transcodingContainer"] = transcoding_container

    params["transcodingProtocol"] = transcoding_protocol

    params["maxAudioSampleRate"] = max_audio_sample_rate

    params["maxAudioBitDepth"] = max_audio_bit_depth

    params["enableRemoteMedia"] = enable_remote_media

    params["breakOnNonKeyFrames"] = break_on_non_key_frames

    params["enableRedirection"] = enable_redirection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Audio/{itemId}/universal".format(
            itemId=item_id,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.FOUND:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
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
    client: AuthenticatedClient,
    container: Union[Unset, None, List[str]] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    audio_codec: Union[Unset, None, str] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    transcoding_audio_channels: Union[Unset, None, int] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    audio_bit_rate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    transcoding_container: Union[Unset, None, str] = UNSET,
    transcoding_protocol: Union[Unset, None, str] = UNSET,
    max_audio_sample_rate: Union[Unset, None, int] = UNSET,
    max_audio_bit_depth: Union[Unset, None, int] = UNSET,
    enable_remote_media: Union[Unset, None, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, None, bool] = False,
    enable_redirection: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, None, List[str]]):
        media_source_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        audio_codec (Union[Unset, None, str]):
        max_audio_channels (Union[Unset, None, int]):
        transcoding_audio_channels (Union[Unset, None, int]):
        max_streaming_bitrate (Union[Unset, None, int]):
        audio_bit_rate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        transcoding_container (Union[Unset, None, str]):
        transcoding_protocol (Union[Unset, None, str]):
        max_audio_sample_rate (Union[Unset, None, int]):
        max_audio_bit_depth (Union[Unset, None, int]):
        enable_remote_media (Union[Unset, None, bool]):
        break_on_non_key_frames (Union[Unset, None, bool]):
        enable_redirection (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    container: Union[Unset, None, List[str]] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    audio_codec: Union[Unset, None, str] = UNSET,
    max_audio_channels: Union[Unset, None, int] = UNSET,
    transcoding_audio_channels: Union[Unset, None, int] = UNSET,
    max_streaming_bitrate: Union[Unset, None, int] = UNSET,
    audio_bit_rate: Union[Unset, None, int] = UNSET,
    start_time_ticks: Union[Unset, None, int] = UNSET,
    transcoding_container: Union[Unset, None, str] = UNSET,
    transcoding_protocol: Union[Unset, None, str] = UNSET,
    max_audio_sample_rate: Union[Unset, None, int] = UNSET,
    max_audio_bit_depth: Union[Unset, None, int] = UNSET,
    enable_remote_media: Union[Unset, None, bool] = UNSET,
    break_on_non_key_frames: Union[Unset, None, bool] = False,
    enable_redirection: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, None, List[str]]):
        media_source_id (Union[Unset, None, str]):
        device_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        audio_codec (Union[Unset, None, str]):
        max_audio_channels (Union[Unset, None, int]):
        transcoding_audio_channels (Union[Unset, None, int]):
        max_streaming_bitrate (Union[Unset, None, int]):
        audio_bit_rate (Union[Unset, None, int]):
        start_time_ticks (Union[Unset, None, int]):
        transcoding_container (Union[Unset, None, str]):
        transcoding_protocol (Union[Unset, None, str]):
        max_audio_sample_rate (Union[Unset, None, int]):
        max_audio_bit_depth (Union[Unset, None, int]):
        enable_remote_media (Union[Unset, None, bool]):
        break_on_non_key_frames (Union[Unset, None, bool]):
        enable_redirection (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
