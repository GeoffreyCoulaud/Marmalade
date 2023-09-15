from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.playstate_command import PlaystateCommand
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    command: PlaystateCommand,
    *,
    seek_position_ticks: Union[Unset, None, int] = UNSET,
    controlling_user_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["seekPositionTicks"] = seek_position_ticks

    params["controllingUserId"] = controlling_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Sessions/{sessionId}/Playing/{command}".format(
            sessionId=session_id,
            command=command,
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
    command: PlaystateCommand,
    *,
    client: AuthenticatedClient,
    seek_position_ticks: Union[Unset, None, int] = UNSET,
    controlling_user_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Issues a playstate command to a client.

    Args:
        session_id (str):
        command (PlaystateCommand): Enum PlaystateCommand.
        seek_position_ticks (Union[Unset, None, int]):
        controlling_user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        command=command,
        seek_position_ticks=seek_position_ticks,
        controlling_user_id=controlling_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    session_id: str,
    command: PlaystateCommand,
    *,
    client: AuthenticatedClient,
    seek_position_ticks: Union[Unset, None, int] = UNSET,
    controlling_user_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Issues a playstate command to a client.

    Args:
        session_id (str):
        command (PlaystateCommand): Enum PlaystateCommand.
        seek_position_ticks (Union[Unset, None, int]):
        controlling_user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        command=command,
        seek_position_ticks=seek_position_ticks,
        controlling_user_id=controlling_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
