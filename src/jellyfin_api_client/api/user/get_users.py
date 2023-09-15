from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_dto import UserDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_hidden: Union[Unset, None, bool] = UNSET,
    is_disabled: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["isHidden"] = is_hidden

    params["isDisabled"] = is_disabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Users",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["UserDto"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, List["UserDto"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_hidden: Union[Unset, None, bool] = UNSET,
    is_disabled: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["UserDto"]]]:
    """Gets a list of users.

    Args:
        is_hidden (Union[Unset, None, bool]):
        is_disabled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['UserDto']]]
    """

    kwargs = _get_kwargs(
        is_hidden=is_hidden,
        is_disabled=is_disabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_hidden: Union[Unset, None, bool] = UNSET,
    is_disabled: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["UserDto"]]]:
    """Gets a list of users.

    Args:
        is_hidden (Union[Unset, None, bool]):
        is_disabled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['UserDto']]
    """

    return sync_detailed(
        client=client,
        is_hidden=is_hidden,
        is_disabled=is_disabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_hidden: Union[Unset, None, bool] = UNSET,
    is_disabled: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["UserDto"]]]:
    """Gets a list of users.

    Args:
        is_hidden (Union[Unset, None, bool]):
        is_disabled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['UserDto']]]
    """

    kwargs = _get_kwargs(
        is_hidden=is_hidden,
        is_disabled=is_disabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_hidden: Union[Unset, None, bool] = UNSET,
    is_disabled: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["UserDto"]]]:
    """Gets a list of users.

    Args:
        is_hidden (Union[Unset, None, bool]):
        is_disabled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['UserDto']]
    """

    return (
        await asyncio_detailed(
            client=client,
            is_hidden=is_hidden,
            is_disabled=is_disabled,
        )
    ).parsed
