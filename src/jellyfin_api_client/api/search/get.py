from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_kind import BaseItemKind
from ...models.search_hint_result import SearchHintResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    search_term: str,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    include_people: Union[Unset, None, bool] = True,
    include_media: Union[Unset, None, bool] = True,
    include_genres: Union[Unset, None, bool] = True,
    include_studios: Union[Unset, None, bool] = True,
    include_artists: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["startIndex"] = start_index

    params["limit"] = limit

    params["userId"] = user_id

    params["searchTerm"] = search_term

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

    json_media_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(media_types, Unset):
        if media_types is None:
            json_media_types = None
        else:
            json_media_types = media_types

    params["mediaTypes"] = json_media_types

    params["parentId"] = parent_id

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    params["includePeople"] = include_people

    params["includeMedia"] = include_media

    params["includeGenres"] = include_genres

    params["includeStudios"] = include_studios

    params["includeArtists"] = include_artists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Search/Hints",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SearchHintResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchHintResult.from_dict(response.json())

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
) -> Response[Union[Any, SearchHintResult]]:
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
    user_id: Union[Unset, None, str] = UNSET,
    search_term: str,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    include_people: Union[Unset, None, bool] = True,
    include_media: Union[Unset, None, bool] = True,
    include_genres: Union[Unset, None, bool] = True,
    include_studios: Union[Unset, None, bool] = True,
    include_artists: Union[Unset, None, bool] = True,
) -> Response[Union[Any, SearchHintResult]]:
    """Gets the search hint result.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        search_term (str):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        media_types (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        include_people (Union[Unset, None, bool]):  Default: True.
        include_media (Union[Unset, None, bool]):  Default: True.
        include_genres (Union[Unset, None, bool]):  Default: True.
        include_studios (Union[Unset, None, bool]):  Default: True.
        include_artists (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchHintResult]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        user_id=user_id,
        search_term=search_term,
        include_item_types=include_item_types,
        exclude_item_types=exclude_item_types,
        media_types=media_types,
        parent_id=parent_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        include_people=include_people,
        include_media=include_media,
        include_genres=include_genres,
        include_studios=include_studios,
        include_artists=include_artists,
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
    user_id: Union[Unset, None, str] = UNSET,
    search_term: str,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    include_people: Union[Unset, None, bool] = True,
    include_media: Union[Unset, None, bool] = True,
    include_genres: Union[Unset, None, bool] = True,
    include_studios: Union[Unset, None, bool] = True,
    include_artists: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, SearchHintResult]]:
    """Gets the search hint result.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        search_term (str):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        media_types (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        include_people (Union[Unset, None, bool]):  Default: True.
        include_media (Union[Unset, None, bool]):  Default: True.
        include_genres (Union[Unset, None, bool]):  Default: True.
        include_studios (Union[Unset, None, bool]):  Default: True.
        include_artists (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchHintResult]
    """

    return sync_detailed(
        client=client,
        start_index=start_index,
        limit=limit,
        user_id=user_id,
        search_term=search_term,
        include_item_types=include_item_types,
        exclude_item_types=exclude_item_types,
        media_types=media_types,
        parent_id=parent_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        include_people=include_people,
        include_media=include_media,
        include_genres=include_genres,
        include_studios=include_studios,
        include_artists=include_artists,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    search_term: str,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    include_people: Union[Unset, None, bool] = True,
    include_media: Union[Unset, None, bool] = True,
    include_genres: Union[Unset, None, bool] = True,
    include_studios: Union[Unset, None, bool] = True,
    include_artists: Union[Unset, None, bool] = True,
) -> Response[Union[Any, SearchHintResult]]:
    """Gets the search hint result.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        search_term (str):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        media_types (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        include_people (Union[Unset, None, bool]):  Default: True.
        include_media (Union[Unset, None, bool]):  Default: True.
        include_genres (Union[Unset, None, bool]):  Default: True.
        include_studios (Union[Unset, None, bool]):  Default: True.
        include_artists (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SearchHintResult]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        user_id=user_id,
        search_term=search_term,
        include_item_types=include_item_types,
        exclude_item_types=exclude_item_types,
        media_types=media_types,
        parent_id=parent_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        include_people=include_people,
        include_media=include_media,
        include_genres=include_genres,
        include_studios=include_studios,
        include_artists=include_artists,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    search_term: str,
    include_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    include_people: Union[Unset, None, bool] = True,
    include_media: Union[Unset, None, bool] = True,
    include_genres: Union[Unset, None, bool] = True,
    include_studios: Union[Unset, None, bool] = True,
    include_artists: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, SearchHintResult]]:
    """Gets the search hint result.

    Args:
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        search_term (str):
        include_item_types (Union[Unset, None, List[BaseItemKind]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        media_types (Union[Unset, None, List[str]]):
        parent_id (Union[Unset, None, str]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        include_people (Union[Unset, None, bool]):  Default: True.
        include_media (Union[Unset, None, bool]):  Default: True.
        include_genres (Union[Unset, None, bool]):  Default: True.
        include_studios (Union[Unset, None, bool]):  Default: True.
        include_artists (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SearchHintResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_index=start_index,
            limit=limit,
            user_id=user_id,
            search_term=search_term,
            include_item_types=include_item_types,
            exclude_item_types=exclude_item_types,
            media_types=media_types,
            parent_id=parent_id,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            include_people=include_people,
            include_media=include_media,
            include_genres=include_genres,
            include_studios=include_studios,
            include_artists=include_artists,
        )
    ).parsed
