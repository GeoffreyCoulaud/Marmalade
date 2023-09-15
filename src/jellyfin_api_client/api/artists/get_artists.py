from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.base_item_kind import BaseItemKind
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    min_community_rating: Union[Unset, None, float] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["minCommunityRating"] = min_community_rating

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

    params["isFavorite"] = is_favorite

    json_media_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(media_types, Unset):
        if media_types is None:
            json_media_types = None
        else:
            json_media_types = media_types

    params["mediaTypes"] = json_media_types

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

    json_official_ratings: Union[Unset, None, List[str]] = UNSET
    if not isinstance(official_ratings, Unset):
        if official_ratings is None:
            json_official_ratings = None
        else:
            json_official_ratings = official_ratings

    params["officialRatings"] = json_official_ratings

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    json_years: Union[Unset, None, List[int]] = UNSET
    if not isinstance(years, Unset):
        if years is None:
            json_years = None
        else:
            json_years = years

    params["years"] = json_years

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

    params["person"] = person

    json_person_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(person_ids, Unset):
        if person_ids is None:
            json_person_ids = None
        else:
            json_person_ids = person_ids

    params["personIds"] = json_person_ids

    json_person_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(person_types, Unset):
        if person_types is None:
            json_person_types = None
        else:
            json_person_types = person_types

    params["personTypes"] = json_person_types

    json_studios: Union[Unset, None, List[str]] = UNSET
    if not isinstance(studios, Unset):
        if studios is None:
            json_studios = None
        else:
            json_studios = studios

    params["studios"] = json_studios

    json_studio_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(studio_ids, Unset):
        if studio_ids is None:
            json_studio_ids = None
        else:
            json_studio_ids = studio_ids

    params["studioIds"] = json_studio_ids

    params["userId"] = user_id

    params["nameStartsWithOrGreater"] = name_starts_with_or_greater

    params["nameStartsWith"] = name_starts_with

    params["nameLessThan"] = name_less_than

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

    params["enableImages"] = enable_images

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Artists",
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
    min_community_rating: Union[Unset, None, float] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (Union[Unset, None, float]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        studio_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        enable_images (Union[Unset, None, bool]):  Default: True.
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        min_community_rating=min_community_rating,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        genres=genres,
        genre_ids=genre_ids,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        studio_ids=studio_ids,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
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
    min_community_rating: Union[Unset, None, float] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (Union[Unset, None, float]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        studio_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
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
        min_community_rating=min_community_rating,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        genres=genres,
        genre_ids=genre_ids,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        studio_ids=studio_ids,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    min_community_rating: Union[Unset, None, float] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (Union[Unset, None, float]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        studio_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        enable_images (Union[Unset, None, bool]):  Default: True.
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        min_community_rating=min_community_rating,
        start_index=start_index,
        limit=limit,
        search_term=search_term,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        include_item_types=include_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        genres=genres,
        genre_ids=genre_ids,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        studio_ids=studio_ids,
        user_id=user_id,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        sort_by=sort_by,
        sort_order=sort_order,
        enable_images=enable_images,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    min_community_rating: Union[Unset, None, float] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all artists from a given item, folder, or the entire library.

    Args:
        min_community_rating (Union[Unset, None, float]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        genres (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        studio_ids (Union[Unset, None, List[str]]):
        user_id (Union[Unset, None, str]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        sort_by (Union[Unset, None, List[str]]):
        sort_order (Union[Unset, None, List[SortOrder]]):
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
            min_community_rating=min_community_rating,
            start_index=start_index,
            limit=limit,
            search_term=search_term,
            parent_id=parent_id,
            fields=fields,
            exclude_item_types=exclude_item_types,
            include_item_types=include_item_types,
            filters=filters,
            is_favorite=is_favorite,
            media_types=media_types,
            genres=genres,
            genre_ids=genre_ids,
            official_ratings=official_ratings,
            tags=tags,
            years=years,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            person=person,
            person_ids=person_ids,
            person_types=person_types,
            studios=studios,
            studio_ids=studio_ids,
            user_id=user_id,
            name_starts_with_or_greater=name_starts_with_or_greater,
            name_starts_with=name_starts_with,
            name_less_than=name_less_than,
            sort_by=sort_by,
            sort_order=sort_order,
            enable_images=enable_images,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
