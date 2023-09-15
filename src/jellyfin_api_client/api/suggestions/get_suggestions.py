from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.base_item_kind import BaseItemKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    media_type: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_media_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(media_type, Unset):
        if media_type is None:
            json_media_type = None
        else:
            json_media_type = media_type

    params["mediaType"] = json_media_type

    json_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(type, Unset):
        if type is None:
            json_type = None
        else:
            json_type = []
            for type_item_data in type:
                type_item = type_item_data.value

                json_type.append(type_item)

    params["type"] = json_type

    params["startIndex"] = start_index

    params["limit"] = limit

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Users/{userId}/Suggestions".format(
            userId=user_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

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
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, None, List[str]]):
        type (Union[Unset, None, List[BaseItemKind]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_total_record_count (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, None, List[str]]):
        type (Union[Unset, None, List[BaseItemKind]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_total_record_count (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, None, List[str]]):
        type (Union[Unset, None, List[BaseItemKind]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_total_record_count (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Union[Unset, None, List[str]] = UNSET,
    type: Union[Unset, None, List[BaseItemKind]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, None, List[str]]):
        type (Union[Unset, None, List[BaseItemKind]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        enable_total_record_count (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            media_type=media_type,
            type=type,
            start_index=start_index,
            limit=limit,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
