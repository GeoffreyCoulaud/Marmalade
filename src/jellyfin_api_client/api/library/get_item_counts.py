from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.item_counts import ItemCounts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["isFavorite"] = is_favorite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Items/Counts",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ItemCounts]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ItemCounts.from_dict(response.json())

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
) -> Response[Union[Any, ItemCounts]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ItemCounts]]:
    """Get item counts.

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ItemCounts]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        is_favorite=is_favorite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ItemCounts]]:
    """Get item counts.

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ItemCounts]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        is_favorite=is_favorite,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ItemCounts]]:
    """Get item counts.

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ItemCounts]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        is_favorite=is_favorite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ItemCounts]]:
    """Get item counts.

    Args:
        user_id (Union[Unset, None, str]):
        is_favorite (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ItemCounts]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            is_favorite=is_favorite,
        )
    ).parsed
