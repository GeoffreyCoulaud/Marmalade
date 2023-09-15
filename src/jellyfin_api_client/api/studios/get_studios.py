from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.base_item_kind import BaseItemKind
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["startIndex"] = start_index

    params["limit"] = limit

    params["searchTerm"] = search_term

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

    json_exclude_item_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_item_types, Unset):
        if exclude_item_types is None:
            json_exclude_item_types = None
        else:
            json_exclude_item_types = []
            for exclude_item_types_item_data in exclude_item_types:
                exclude_item_types_item = exclude_item_types_item_data.value

                json_exclude_item_types.append(exclude_item_types_item)

    params["excludeItemTypes"] = json_exclude_item_types

    json_include_item_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_item_types, Unset):
        if include_item_types is None:
            json_include_item_types = None
        else:
            json_include_item_types = []
            for include_item_types_item_data in include_item_types:
                include_item_types_item = include_item_types_item_data.value

                json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    params["isFavorite"] = is_favorite

    params["enableUserData"] = enable_user_data

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

    params["userId"] = user_id

    params["nameStartsWithOrGreater"] = name_starts_with_or_greater

    params["nameStartsWith"] = name_starts_with

    params["nameLessThan"] = name_less_than

    params["enableImages"] = enable_images

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Studios",
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
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all studios from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all studios from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all studios from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all studios from a given item, folder, or the entire library.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_index=start_index,
            limit=limit,
            search_term=search_term,
            parent_id=parent_id,
            fields=fields,
            exclude_item_types=exclude_item_types,
            include_item_types=include_item_types,
            is_favorite=is_favorite,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            user_id=user_id,
            name_starts_with_or_greater=name_starts_with_or_greater,
            name_starts_with=name_starts_with,
            name_less_than=name_less_than,
            enable_images=enable_images,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
