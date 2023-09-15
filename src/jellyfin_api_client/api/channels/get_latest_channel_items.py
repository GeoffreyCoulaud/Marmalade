from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["startIndex"] = start_index

    params["limit"] = limit

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

    json_channel_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(channel_ids, Unset):
        if channel_ids is None:
            json_channel_ids = None
        else:
            json_channel_ids = channel_ids

    params["channelIds"] = json_channel_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Channels/Items/Latest",
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
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        filters (Union[Unset, None, List[ItemFilter]]):
        fields (Union[Unset, None, List[ItemFields]]):
        channel_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        filters (Union[Unset, None, List[ItemFilter]]):
        fields (Union[Unset, None, List[ItemFields]]):
        channel_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        filters (Union[Unset, None, List[ItemFilter]]):
        fields (Union[Unset, None, List[ItemFields]]):
        channel_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        filters (Union[Unset, None, List[ItemFilter]]):
        fields (Union[Unset, None, List[ItemFields]]):
        channel_ids (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            filters=filters,
            fields=fields,
            channel_ids=channel_ids,
        )
    ).parsed
