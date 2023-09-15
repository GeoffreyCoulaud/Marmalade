from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_creation_result import CollectionCreationResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = False,
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

    params["parentId"] = parent_id

    params["isLocked"] = is_locked

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Collections",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CollectionCreationResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CollectionCreationResult.from_dict(response.json())

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
) -> Response[Union[Any, CollectionCreationResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = False,
) -> Response[Union[Any, CollectionCreationResult]]:
    """Creates a new collection.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CollectionCreationResult]]
    """

    kwargs = _get_kwargs(
        name=name,
        ids=ids,
        parent_id=parent_id,
        is_locked=is_locked,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, CollectionCreationResult]]:
    """Creates a new collection.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CollectionCreationResult]
    """

    return sync_detailed(
        client=client,
        name=name,
        ids=ids,
        parent_id=parent_id,
        is_locked=is_locked,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = False,
) -> Response[Union[Any, CollectionCreationResult]]:
    """Creates a new collection.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CollectionCreationResult]]
    """

    kwargs = _get_kwargs(
        name=name,
        ids=ids,
        parent_id=parent_id,
        is_locked=is_locked,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, CollectionCreationResult]]:
    """Creates a new collection.

    Args:
        name (Union[Unset, None, str]):
        ids (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CollectionCreationResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            ids=ids,
            parent_id=parent_id,
            is_locked=is_locked,
        )
    ).parsed
