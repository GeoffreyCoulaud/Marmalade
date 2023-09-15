import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    series_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    next_up_date_cutoff: Union[Unset, None, datetime.datetime] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    disable_first_episode: Union[Unset, None, bool] = False,
    enable_rewatching: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["startIndex"] = start_index

    params["limit"] = limit

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

    params["seriesId"] = series_id

    params["parentId"] = parent_id

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        if enable_image_types is None:
            json_enable_image_types = None
        else:
            json_enable_image_types = []
            for enable_image_types_item_data in enable_image_types:
                enable_image_types_item = enable_image_types_item_data.value

                json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["enableUserData"] = enable_user_data

    json_next_up_date_cutoff: Union[Unset, None, str] = UNSET
    if not isinstance(next_up_date_cutoff, Unset):
        json_next_up_date_cutoff = next_up_date_cutoff.isoformat() if next_up_date_cutoff else None

    params["nextUpDateCutoff"] = json_next_up_date_cutoff

    params["enableTotalRecordCount"] = enable_total_record_count

    params["disableFirstEpisode"] = disable_first_episode

    params["enableRewatching"] = enable_rewatching

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Shows/NextUp",
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
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    series_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    next_up_date_cutoff: Union[Unset, None, datetime.datetime] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    disable_first_episode: Union[Unset, None, bool] = False,
    enable_rewatching: Union[Unset, None, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets a list of next up episodes.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        fields (Union[Unset, None, List[ItemFields]]):
        series_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        next_up_date_cutoff (Union[Unset, None, datetime.datetime]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        disable_first_episode (Union[Unset, None, bool]):
        enable_rewatching (Union[Unset, None, bool]):

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
        fields=fields,
        series_id=series_id,
        parent_id=parent_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        next_up_date_cutoff=next_up_date_cutoff,
        enable_total_record_count=enable_total_record_count,
        disable_first_episode=disable_first_episode,
        enable_rewatching=enable_rewatching,
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
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    series_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    next_up_date_cutoff: Union[Unset, None, datetime.datetime] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    disable_first_episode: Union[Unset, None, bool] = False,
    enable_rewatching: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets a list of next up episodes.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        fields (Union[Unset, None, List[ItemFields]]):
        series_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        next_up_date_cutoff (Union[Unset, None, datetime.datetime]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        disable_first_episode (Union[Unset, None, bool]):
        enable_rewatching (Union[Unset, None, bool]):

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
        fields=fields,
        series_id=series_id,
        parent_id=parent_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        next_up_date_cutoff=next_up_date_cutoff,
        enable_total_record_count=enable_total_record_count,
        disable_first_episode=disable_first_episode,
        enable_rewatching=enable_rewatching,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    series_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    next_up_date_cutoff: Union[Unset, None, datetime.datetime] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    disable_first_episode: Union[Unset, None, bool] = False,
    enable_rewatching: Union[Unset, None, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets a list of next up episodes.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        fields (Union[Unset, None, List[ItemFields]]):
        series_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        next_up_date_cutoff (Union[Unset, None, datetime.datetime]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        disable_first_episode (Union[Unset, None, bool]):
        enable_rewatching (Union[Unset, None, bool]):

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
        fields=fields,
        series_id=series_id,
        parent_id=parent_id,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        next_up_date_cutoff=next_up_date_cutoff,
        enable_total_record_count=enable_total_record_count,
        disable_first_episode=disable_first_episode,
        enable_rewatching=enable_rewatching,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    series_id: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    next_up_date_cutoff: Union[Unset, None, datetime.datetime] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    disable_first_episode: Union[Unset, None, bool] = False,
    enable_rewatching: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets a list of next up episodes.

    Args:
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        fields (Union[Unset, None, List[ItemFields]]):
        series_id (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        next_up_date_cutoff (Union[Unset, None, datetime.datetime]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        disable_first_episode (Union[Unset, None, bool]):
        enable_rewatching (Union[Unset, None, bool]):

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
            fields=fields,
            series_id=series_id,
            parent_id=parent_id,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            next_up_date_cutoff=next_up_date_cutoff,
            enable_total_record_count=enable_total_record_count,
            disable_first_episode=disable_first_episode,
            enable_rewatching=enable_rewatching,
        )
    ).parsed
