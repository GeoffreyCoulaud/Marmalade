from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.play_command import PlayCommand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    play_command: PlayCommand,
    item_ids: List[str],
    start_position_ticks: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_play_command = play_command.value

    params["playCommand"] = json_play_command

    json_item_ids = item_ids

    params["itemIds"] = json_item_ids

    params["startPositionTicks"] = start_position_ticks

    params["mediaSourceId"] = media_source_id

    params["audioStreamIndex"] = audio_stream_index

    params["subtitleStreamIndex"] = subtitle_stream_index

    params["startIndex"] = start_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Sessions/{sessionId}/Playing".format(
            sessionId=session_id,
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
    session_id: str,
    *,
    client: AuthenticatedClient,
    play_command: PlayCommand,
    item_ids: List[str],
    start_position_ticks: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Instructs a session to play an item.

    Args:
        session_id (str):
        play_command (PlayCommand): Enum PlayCommand.
        item_ids (List[str]):
        start_position_ticks (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        start_index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        play_command=play_command,
        item_ids=item_ids,
        start_position_ticks=start_position_ticks,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        start_index=start_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
    play_command: PlayCommand,
    item_ids: List[str],
    start_position_ticks: Union[Unset, None, int] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    audio_stream_index: Union[Unset, None, int] = UNSET,
    subtitle_stream_index: Union[Unset, None, int] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """Instructs a session to play an item.

    Args:
        session_id (str):
        play_command (PlayCommand): Enum PlayCommand.
        item_ids (List[str]):
        start_position_ticks (Union[Unset, None, int]):
        media_source_id (Union[Unset, None, str]):
        audio_stream_index (Union[Unset, None, int]):
        subtitle_stream_index (Union[Unset, None, int]):
        start_index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        play_command=play_command,
        item_ids=item_ids,
        start_position_ticks=start_position_ticks,
        media_source_id=media_source_id,
        audio_stream_index=audio_stream_index,
        subtitle_stream_index=subtitle_stream_index,
        start_index=start_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
