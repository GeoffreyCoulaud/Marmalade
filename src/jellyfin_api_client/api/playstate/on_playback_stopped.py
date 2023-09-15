from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    item_id: str,
    *,
    media_source_id: Union[Unset, None, str] = UNSET,
    next_media_type: Union[Unset, None, str] = UNSET,
    position_ticks: Union[Unset, None, int] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["mediaSourceId"] = media_source_id

    params["nextMediaType"] = next_media_type

    params["positionTicks"] = position_ticks

    params["liveStreamId"] = live_stream_id

    params["playSessionId"] = play_session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
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
    next_media_type: Union[Unset, None, str] = UNSET,
    position_ticks: Union[Unset, None, int] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Reports that a user has stopped playing an item.

    Args:
        user_id (str):
        item_id (str):
        media_source_id (Union[Unset, None, str]):
        next_media_type (Union[Unset, None, str]):
        position_ticks (Union[Unset, None, int]):
        live_stream_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):

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
        next_media_type=next_media_type,
        position_ticks=position_ticks,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
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
    next_media_type: Union[Unset, None, str] = UNSET,
    position_ticks: Union[Unset, None, int] = UNSET,
    live_stream_id: Union[Unset, None, str] = UNSET,
    play_session_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Reports that a user has stopped playing an item.

    Args:
        user_id (str):
        item_id (str):
        media_source_id (Union[Unset, None, str]):
        next_media_type (Union[Unset, None, str]):
        position_ticks (Union[Unset, None, int]):
        live_stream_id (Union[Unset, None, str]):
        play_session_id (Union[Unset, None, str]):

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
        next_media_type=next_media_type,
        position_ticks=position_ticks,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
