from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.channel_type import ChannelType
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type: Union[Unset, None, ChannelType] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_liked: Union[Unset, None, bool] = UNSET,
    is_disliked: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    enable_favorite_sorting: Union[Unset, None, bool] = False,
    add_current_program: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["userId"] = user_id

    params["startIndex"] = start_index

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    params["limit"] = limit

    params["isFavorite"] = is_favorite

    params["isLiked"] = is_liked

    params["isDisliked"] = is_disliked

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

    params["enableUserData"] = enable_user_data

    json_sort_by: Union[Unset, None, List[str]] = UNSET
    if not isinstance(sort_by, Unset):
        if sort_by is None:
            json_sort_by = None
        else:
            json_sort_by = sort_by

    params["sortBy"] = json_sort_by

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    params["enableFavoriteSorting"] = enable_favorite_sorting

    params["addCurrentProgram"] = add_current_program

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/LiveTv/Channels",
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
    type: Union[Unset, None, ChannelType] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_liked: Union[Unset, None, bool] = UNSET,
    is_disliked: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    enable_favorite_sorting: Union[Unset, None, bool] = False,
    add_current_program: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv channels.

    Args:
        type (Union[Unset, None, ChannelType]): Enum ChannelType.
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        is_favorite (Union[Unset, None, bool]):
        is_liked (Union[Unset, None, bool]):
        is_disliked (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, SortOrder]): An enum representing the sorting order.
        enable_favorite_sorting (Union[Unset, None, bool]):
        add_current_program (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        type=type,
        user_id=user_id,
        start_index=start_index,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        limit=limit,
        is_favorite=is_favorite,
        is_liked=is_liked,
        is_disliked=is_disliked,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_favorite_sorting=enable_favorite_sorting,
        add_current_program=add_current_program,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type: Union[Unset, None, ChannelType] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_liked: Union[Unset, None, bool] = UNSET,
    is_disliked: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    enable_favorite_sorting: Union[Unset, None, bool] = False,
    add_current_program: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv channels.

    Args:
        type (Union[Unset, None, ChannelType]): Enum ChannelType.
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        is_favorite (Union[Unset, None, bool]):
        is_liked (Union[Unset, None, bool]):
        is_disliked (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, SortOrder]): An enum representing the sorting order.
        enable_favorite_sorting (Union[Unset, None, bool]):
        add_current_program (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        type=type,
        user_id=user_id,
        start_index=start_index,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        limit=limit,
        is_favorite=is_favorite,
        is_liked=is_liked,
        is_disliked=is_disliked,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_favorite_sorting=enable_favorite_sorting,
        add_current_program=add_current_program,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type: Union[Unset, None, ChannelType] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_liked: Union[Unset, None, bool] = UNSET,
    is_disliked: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    enable_favorite_sorting: Union[Unset, None, bool] = False,
    add_current_program: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv channels.

    Args:
        type (Union[Unset, None, ChannelType]): Enum ChannelType.
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        is_favorite (Union[Unset, None, bool]):
        is_liked (Union[Unset, None, bool]):
        is_disliked (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, SortOrder]): An enum representing the sorting order.
        enable_favorite_sorting (Union[Unset, None, bool]):
        add_current_program (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        type=type,
        user_id=user_id,
        start_index=start_index,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        limit=limit,
        is_favorite=is_favorite,
        is_liked=is_liked,
        is_disliked=is_disliked,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        fields=fields,
        enable_user_data=enable_user_data,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_favorite_sorting=enable_favorite_sorting,
        add_current_program=add_current_program,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type: Union[Unset, None, ChannelType] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    is_liked: Union[Unset, None, bool] = UNSET,
    is_disliked: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, SortOrder] = UNSET,
    enable_favorite_sorting: Union[Unset, None, bool] = False,
    add_current_program: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv channels.

    Args:
        type (Union[Unset, None, ChannelType]): Enum ChannelType.
        user_id (Union[Unset, None, str]):
        start_index (Union[Unset, None, int]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        is_favorite (Union[Unset, None, bool]):
        is_liked (Union[Unset, None, bool]):
        is_disliked (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, SortOrder]): An enum representing the sorting order.
        enable_favorite_sorting (Union[Unset, None, bool]):
        add_current_program (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
            user_id=user_id,
            start_index=start_index,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            limit=limit,
            is_favorite=is_favorite,
            is_liked=is_liked,
            is_disliked=is_disliked,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            fields=fields,
            enable_user_data=enable_user_data,
            sort_by=sort_by,
            sort_order=sort_order,
            enable_favorite_sorting=enable_favorite_sorting,
            add_current_program=add_current_program,
        )
    ).parsed
