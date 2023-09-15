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
    limit: Union[Unset, None, int] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["limit"] = limit

    params["isAiring"] = is_airing

    params["hasAired"] = has_aired

    params["isSeries"] = is_series

    params["isMovie"] = is_movie

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

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

    json_genre_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(genre_ids, Unset):
        if genre_ids is None:
            json_genre_ids = None
        else:
            json_genre_ids = genre_ids

    params["genreIds"] = json_genre_ids

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

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/LiveTv/Programs/Recommended",
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
    limit: Union[Unset, None, int] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets recommended live tv epgs.

    Args:
        user_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        is_airing (Union[Unset, None, bool]):
        has_aired (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        genre_ids (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        limit=limit,
        is_airing=is_airing,
        has_aired=has_aired,
        is_series=is_series,
        is_movie=is_movie,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        genre_ids=genre_ids,
        fields=fields,
        enable_user_data=enable_user_data,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets recommended live tv epgs.

    Args:
        user_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        is_airing (Union[Unset, None, bool]):
        has_aired (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        genre_ids (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        limit=limit,
        is_airing=is_airing,
        has_aired=has_aired,
        is_series=is_series,
        is_movie=is_movie,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        genre_ids=genre_ids,
        fields=fields,
        enable_user_data=enable_user_data,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets recommended live tv epgs.

    Args:
        user_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        is_airing (Union[Unset, None, bool]):
        has_aired (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        genre_ids (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        limit=limit,
        is_airing=is_airing,
        has_aired=has_aired,
        is_series=is_series,
        is_movie=is_movie,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        genre_ids=genre_ids,
        fields=fields,
        enable_user_data=enable_user_data,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    is_airing: Union[Unset, None, bool] = UNSET,
    has_aired: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    enable_images: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets recommended live tv epgs.

    Args:
        user_id (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        is_airing (Union[Unset, None, bool]):
        has_aired (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        enable_images (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        genre_ids (Union[Unset, None, List[str]]):
        fields (Union[Unset, None, List[ItemFields]]):
        enable_user_data (Union[Unset, None, bool]):
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
            user_id=user_id,
            limit=limit,
            is_airing=is_airing,
            has_aired=has_aired,
            is_series=is_series,
            is_movie=is_movie,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            genre_ids=genre_ids,
            fields=fields,
            enable_user_data=enable_user_data,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
