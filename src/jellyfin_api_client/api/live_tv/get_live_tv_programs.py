import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    min_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    max_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    max_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    library_series_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_channel_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(channel_ids, Unset):
        if channel_ids is None:
            json_channel_ids = None
        else:
            json_channel_ids = channel_ids

    params["channelIds"] = json_channel_ids

    params["userId"] = user_id

    json_min_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(min_start_date, Unset):
        json_min_start_date = min_start_date.isoformat() if min_start_date else None

    params["minStartDate"] = json_min_start_date

    params["hasAired"] = has_aired

    params["isAiring"] = is_airing

    json_max_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(max_start_date, Unset):
        json_max_start_date = max_start_date.isoformat() if max_start_date else None

    params["maxStartDate"] = json_max_start_date

    json_min_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(min_end_date, Unset):
        json_min_end_date = min_end_date.isoformat() if min_end_date else None

    params["minEndDate"] = json_min_end_date

    json_max_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(max_end_date, Unset):
        json_max_end_date = max_end_date.isoformat() if max_end_date else None

    params["maxEndDate"] = json_max_end_date

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    params["startIndex"] = start_index

    params["limit"] = limit

    json_sort_by: Union[Unset, None, List[str]] = UNSET
    if not isinstance(sort_by, Unset):
        if sort_by is None:
            json_sort_by = None
        else:
            json_sort_by = sort_by

    params["sortBy"] = json_sort_by

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

    json_genres: Union[Unset, None, List[str]] = UNSET
    if not isinstance(genres, Unset):
        if genres is None:
            json_genres = None
        else:
            json_genres = genres

    params["genres"] = json_genres

    json_genre_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(genre_ids, Unset):
        if genre_ids is None:
            json_genre_ids = None
        else:
            json_genre_ids = genre_ids

    params["genreIds"] = json_genre_ids

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

    params["seriesTimerId"] = series_timer_id

    params["librarySeriesId"] = library_series_id

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

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/LiveTv/Programs",
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
    channel_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    min_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    max_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    max_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    library_series_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv epgs.

    Args:
        channel_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        min_start_date (Union[Unset, None, datetime.datetime]):
        has_aired (Union[Unset, None, bool]):
        is_airing (Union[Unset, None, bool]):
        max_start_date (Union[Unset, None, datetime.datetime]):
        min_end_date (Union[Unset, None, datetime.datetime]):
        max_end_date (Union[Unset, None, datetime.datetime]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        series_timer_id (Union[Unset, None, str]):
        library_series_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_ids=channel_ids,
        user_id=user_id,
        min_start_date=min_start_date,
        has_aired=has_aired,
        is_airing=is_airing,
        max_start_date=max_start_date,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        start_index=start_index,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
        genres=genres,
        genre_ids=genre_ids,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        series_timer_id=series_timer_id,
        library_series_id=library_series_id,
        fields=fields,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    min_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    max_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    max_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    library_series_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv epgs.

    Args:
        channel_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        min_start_date (Union[Unset, None, datetime.datetime]):
        has_aired (Union[Unset, None, bool]):
        is_airing (Union[Unset, None, bool]):
        max_start_date (Union[Unset, None, datetime.datetime]):
        min_end_date (Union[Unset, None, datetime.datetime]):
        max_end_date (Union[Unset, None, datetime.datetime]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        series_timer_id (Union[Unset, None, str]):
        library_series_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        channel_ids=channel_ids,
        user_id=user_id,
        min_start_date=min_start_date,
        has_aired=has_aired,
        is_airing=is_airing,
        max_start_date=max_start_date,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        start_index=start_index,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
        genres=genres,
        genre_ids=genre_ids,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        series_timer_id=series_timer_id,
        library_series_id=library_series_id,
        fields=fields,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    min_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    max_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    max_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    library_series_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv epgs.

    Args:
        channel_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        min_start_date (Union[Unset, None, datetime.datetime]):
        has_aired (Union[Unset, None, bool]):
        is_airing (Union[Unset, None, bool]):
        max_start_date (Union[Unset, None, datetime.datetime]):
        min_end_date (Union[Unset, None, datetime.datetime]):
        max_end_date (Union[Unset, None, datetime.datetime]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        series_timer_id (Union[Unset, None, str]):
        library_series_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_ids=channel_ids,
        user_id=user_id,
        min_start_date=min_start_date,
        has_aired=has_aired,
        is_airing=is_airing,
        max_start_date=max_start_date,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        start_index=start_index,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
        genres=genres,
        genre_ids=genre_ids,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
        series_timer_id=series_timer_id,
        library_series_id=library_series_id,
        fields=fields,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    min_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    max_start_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    max_end_date: Union[Unset, None, datetime.datetime] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    library_series_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets available live tv epgs.

    Args:
        channel_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        min_start_date (Union[Unset, None, datetime.datetime]):
        has_aired (Union[Unset, None, bool]):
        is_airing (Union[Unset, None, bool]):
        max_start_date (Union[Unset, None, datetime.datetime]):
        min_end_date (Union[Unset, None, datetime.datetime]):
        max_end_date (Union[Unset, None, datetime.datetime]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        enable_user_data (Union[Unset, None, bool]):
        series_timer_id (Union[Unset, None, str]):
        library_series_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
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
            channel_ids=channel_ids,
            user_id=user_id,
            min_start_date=min_start_date,
            has_aired=has_aired,
            is_airing=is_airing,
            max_start_date=max_start_date,
            min_end_date=min_end_date,
            max_end_date=max_end_date,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            start_index=start_index,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            genres=genres,
            genre_ids=genre_ids,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            series_timer_id=series_timer_id,
            library_series_id=library_series_id,
            fields=fields,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
