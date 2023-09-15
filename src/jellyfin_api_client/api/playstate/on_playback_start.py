from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.play_method import PlayMethod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    item_id: str,
    *,
    media_source_id: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    play_method: Union[Unset, None, PlayMethod] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    can_seek: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["mediaSourceId"] = media_source_id

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    json_play_method: Union[Unset, None, str] = UNSET
    if not isinstance(play_method, Unset):
        json_play_method = play_method.value if play_method else None

    params["playMethod"] = json_play_method

    params["liveStreamId"] = live_stream_id

    params["playSessionId"] = play_session_id

    params["canSeek"] = can_seek

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Users/{userId}/PlayingItems/{itemId}".format(
            userId=user_id,
            itemId=item_id,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
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
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    media_source_id: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    play_method: Union[Unset, None, PlayMethod] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    can_seek: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Reports that a user has begun playing an item.

    Args:
        user_id (str):
        item_id (str):
        media_source_id (Union[Unset, None, str]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        play_method (Union[Unset, None, PlayMethod]):
        live_stream_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        can_seek (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        can_seek=can_seek,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    media_source_id: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    play_method: Union[Unset, None, PlayMethod] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
    can_seek: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Reports that a user has begun playing an item.

    Args:
        user_id (str):
        item_id (str):
        media_source_id (Union[Unset, None, str]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        play_method (Union[Unset, None, PlayMethod]):
        live_stream_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):
        can_seek (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        play_method=play_method,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
        can_seek=can_seek,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
