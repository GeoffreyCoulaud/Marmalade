from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_playlist_dto import CreatePlaylistDto
from ...models.playlist_creation_result import PlaylistCreationResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: CreatePlaylistDto,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    media_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["name"] = name

    json_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(ids, Unset):
        if ids is None:
            json_ids = None
        else:
            json_ids = ids

    params["ids"] = json_ids

    params["userId"] = user_id

    params["mediaType"] = media_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/Playlists",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PlaylistCreationResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PlaylistCreationResult.from_dict(response.json())

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
) -> Response[Union[Any, PlaylistCreationResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreatePlaylistDto,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    media_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        media_type (Union[Unset, None, str]):
        json_body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaylistCreationResult]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreatePlaylistDto,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    media_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        media_type (Union[Unset, None, str]):
        json_body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaylistCreationResult]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreatePlaylistDto,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    media_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        media_type (Union[Unset, None, str]):
        json_body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaylistCreationResult]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreatePlaylistDto,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    media_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        media_type (Union[Unset, None, str]):
        json_body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaylistCreationResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
        )
    ).parsed
