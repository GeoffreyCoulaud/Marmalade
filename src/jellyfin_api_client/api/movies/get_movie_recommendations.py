from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.item_fields import ItemFields
from ...models.recommendation_dto import RecommendationDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    category_limit: Union[Unset, None, int] = 5,
    item_limit: Union[Unset, None, int] = 8,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["parentId"] = parent_id

    json_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(fields, Unset):
        if fields is None:
            json_fields = None
        else:
            json_fields = []
            for fields_item_data in fields:
                fields_item = fields_item_data.value

                json_fields.append(fields_item)

    params["fields"] = json_fields

    params["categoryLimit"] = category_limit

    params["itemLimit"] = item_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Movies/Recommendations",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["RecommendationDto"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RecommendationDto.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["RecommendationDto"]]]:
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
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    category_limit: Union[Unset, None, int] = 5,
    item_limit: Union[Unset, None, int] = 8,
) -> Response[Union[Any, List["RecommendationDto"]]]:
    """Gets movie recommendations.

    Args:
        user_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        category_limit (Union[Unset, None, int]):  Default: 5.
        item_limit (Union[Unset, None, int]):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['RecommendationDto']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        category_limit=category_limit,
        item_limit=item_limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    category_limit: Union[Unset, None, int] = 5,
    item_limit: Union[Unset, None, int] = 8,
) -> Optional[Union[Any, List["RecommendationDto"]]]:
    """Gets movie recommendations.

    Args:
        user_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        category_limit (Union[Unset, None, int]):  Default: 5.
        item_limit (Union[Unset, None, int]):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['RecommendationDto']]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        category_limit=category_limit,
        item_limit=item_limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    category_limit: Union[Unset, None, int] = 5,
    item_limit: Union[Unset, None, int] = 8,
) -> Response[Union[Any, List["RecommendationDto"]]]:
    """Gets movie recommendations.

    Args:
        user_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        category_limit (Union[Unset, None, int]):  Default: 5.
        item_limit (Union[Unset, None, int]):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['RecommendationDto']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        fields=fields,
        category_limit=category_limit,
        item_limit=item_limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    category_limit: Union[Unset, None, int] = 5,
    item_limit: Union[Unset, None, int] = 8,
) -> Optional[Union[Any, List["RecommendationDto"]]]:
    """Gets movie recommendations.

    Args:
        user_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        category_limit (Union[Unset, None, int]):  Default: 5.
        item_limit (Union[Unset, None, int]):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['RecommendationDto']]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            parent_id=parent_id,
            fields=fields,
            category_limit=category_limit,
            item_limit=item_limit,
        )
    ).parsed
