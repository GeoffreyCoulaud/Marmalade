from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_item_data_dto import UserItemDataDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    item_id: str,
    *,
    likes: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["likes"] = likes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Users/{userId}/Items/{itemId}/Rating".format(
            userId=user_id,
            itemId=item_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UserItemDataDto]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserItemDataDto.from_dict(response.json())

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
) -> Response[Union[Any, UserItemDataDto]]:
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
    likes: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, UserItemDataDto]]:
    """Updates a user's rating for an item.

    Args:
        user_id (str):
        item_id (str):
        likes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        likes=likes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    likes: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, UserItemDataDto]]:
    """Updates a user's rating for an item.

    Args:
        user_id (str):
        item_id (str):
        likes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserItemDataDto]
    """

    return sync_detailed(
        user_id=user_id,
        item_id=item_id,
        client=client,
        likes=likes,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    likes: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, UserItemDataDto]]:
    """Updates a user's rating for an item.

    Args:
        user_id (str):
        item_id (str):
        likes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        likes=likes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    likes: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, UserItemDataDto]]:
    """Updates a user's rating for an item.

    Args:
        user_id (str):
        item_id (str):
        likes (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserItemDataDto]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            item_id=item_id,
            client=client,
            likes=likes,
        )
    ).parsed
