from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    exclude_person_types: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    appears_in_item_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["searchTerm"] = search_term

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

    json_exclude_person_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_person_types, Unset):
        if exclude_person_types is None:
            json_exclude_person_types = None
        else:
            json_exclude_person_types = exclude_person_types

    params["excludePersonTypes"] = json_exclude_person_types

    json_person_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(person_types, Unset):
        if person_types is None:
            json_person_types = None
        else:
            json_person_types = person_types

    params["personTypes"] = json_person_types

    params["appearsInItemId"] = appears_in_item_id

    params["userId"] = user_id

    params["enableImages"] = enable_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Persons",
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
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    exclude_person_types: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    appears_in_item_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all persons.

    Args:
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        exclude_person_types (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        appears_in_item_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search_term=search_term,
        fields=fields,
        filters=filters,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_person_types=exclude_person_types,
        person_types=person_types,
        appears_in_item_id=appears_in_item_id,
        user_id=user_id,
        enable_images=enable_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    exclude_person_types: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    appears_in_item_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all persons.

    Args:
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        exclude_person_types (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        appears_in_item_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        search_term=search_term,
        fields=fields,
        filters=filters,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_person_types=exclude_person_types,
        person_types=person_types,
        appears_in_item_id=appears_in_item_id,
        user_id=user_id,
        enable_images=enable_images,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    exclude_person_types: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    appears_in_item_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all persons.

    Args:
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        exclude_person_types (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        appears_in_item_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        search_term=search_term,
        fields=fields,
        filters=filters,
        is_favorite=is_favorite,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        exclude_person_types=exclude_person_types,
        person_types=person_types,
        appears_in_item_id=appears_in_item_id,
        user_id=user_id,
        enable_images=enable_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    exclude_person_types: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    appears_in_item_id: Union[Unset, None, str] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
    enable_images: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets all persons.

    Args:
        limit (Union[Unset, None, int]):
        search_term (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        exclude_person_types (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        appears_in_item_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            search_term=search_term,
            fields=fields,
            filters=filters,
            is_favorite=is_favorite,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            exclude_person_types=exclude_person_types,
            person_types=person_types,
            appears_in_item_id=appears_in_item_id,
            user_id=user_id,
            enable_images=enable_images,
        )
    ).parsed
