from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_refresh_mode import MetadataRefreshMode
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    metadata_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, None, bool] = False,
    replace_all_images: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_metadata_refresh_mode: Union[Unset, None, str] = UNSET
    if not isinstance(metadata_refresh_mode, Unset):
        json_metadata_refresh_mode = metadata_refresh_mode.value if metadata_refresh_mode else None

    params["metadataRefreshMode"] = json_metadata_refresh_mode

    json_image_refresh_mode: Union[Unset, None, str] = UNSET
    if not isinstance(image_refresh_mode, Unset):
        json_image_refresh_mode = image_refresh_mode.value if image_refresh_mode else None

    params["imageRefreshMode"] = json_image_refresh_mode

    params["replaceAllMetadata"] = replace_all_metadata

    params["replaceAllImages"] = replace_all_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Items/{itemId}/Refresh".format(
            itemId=item_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
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
) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    metadata_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, None, bool] = False,
    replace_all_images: Union[Unset, None, bool] = False,
) -> Response[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (str):
        metadata_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, None, bool]):
        replace_all_images (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        metadata_refresh_mode=metadata_refresh_mode,
        image_refresh_mode=image_refresh_mode,
        replace_all_metadata=replace_all_metadata,
        replace_all_images=replace_all_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    metadata_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, None, bool] = False,
    replace_all_images: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (str):
        metadata_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, None, bool]):
        replace_all_images (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        metadata_refresh_mode=metadata_refresh_mode,
        image_refresh_mode=image_refresh_mode,
        replace_all_metadata=replace_all_metadata,
        replace_all_images=replace_all_images,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    metadata_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, None, bool] = False,
    replace_all_images: Union[Unset, None, bool] = False,
) -> Response[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (str):
        metadata_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, None, bool]):
        replace_all_images (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        metadata_refresh_mode=metadata_refresh_mode,
        image_refresh_mode=image_refresh_mode,
        replace_all_metadata=replace_all_metadata,
        replace_all_images=replace_all_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    metadata_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, None, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, None, bool] = False,
    replace_all_images: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (str):
        metadata_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, None, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, None, bool]):
        replace_all_images (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            metadata_refresh_mode=metadata_refresh_mode,
            image_refresh_mode=image_refresh_mode,
            replace_all_metadata=replace_all_metadata,
            replace_all_images=replace_all_images,
        )
    ).parsed
