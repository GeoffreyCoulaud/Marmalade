from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    folder_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["folderId"] = folder_id

    params["userId"] = user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_sort_order: Union[Unset, None, List[str]] = UNSET
    if not isinstance(sort_order, Unset):
        if sort_order is None:
            json_sort_order = None
        else:
            json_sort_order = []
            for sort_order_item_data in sort_order:
                sort_order_item = sort_order_item_data.value

                json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    json_filters: Union[Unset, None, List[str]] = UNSET
    if not isinstance(filters, Unset):
        if filters is None:
            json_filters = None
        else:
            json_filters = []
            for filters_item_data in filters:
                filters_item = filters_item_data.value

                json_filters.append(filters_item)

    params["filters"] = json_filters

    json_sort_by: Union[Unset, None, List[str]] = UNSET
    if not isinstance(sort_by, Unset):
        if sort_by is None:
            json_sort_by = None
        else:
            json_sort_by = sort_by

    params["sortBy"] = json_sort_by

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Channels/{channelId}/Items".format(
            channelId=channel_id,
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
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        sort_by (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        sort_by (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        sort_by (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        sort_by (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            folder_id=folder_id,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            sort_order=sort_order,
            filters=filters,
            sort_by=sort_by,
            fields=fields,
        )
    ).parsed
