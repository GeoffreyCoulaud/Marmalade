from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: str,
    *,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(ids, Unset):
        if ids is None:
            json_ids = None
        else:
            json_ids = ids

    params["ids"] = json_ids

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Playlists/{playlistId}/Items".format(
            playlistId=playlist_id,
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
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Adds items to a playlist.

    Args:
        playlist_id (str):
        ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        ids=ids,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Adds items to a playlist.

    Args:
        playlist_id (str):
        ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        ids=ids,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
