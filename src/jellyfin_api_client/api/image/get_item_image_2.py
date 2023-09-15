from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_format import ImageFormat
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    image_type: ImageType,
    image_index: int,
    tag: str,
    format_: ImageFormat,
    max_width: int,
    max_height: int,
    percent_played: float,
    unplayed_count: int,
    *,
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    quality: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    crop_whitespace: Union[Unset, None, bool] = UNSET,
    add_played_indicator: Union[Unset, None, bool] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["width"] = width

    params["height"] = height

    params["quality"] = quality

    params["fillWidth"] = fill_width

    params["fillHeight"] = fill_height

    params["cropWhitespace"] = crop_whitespace

    params["addPlayedIndicator"] = add_played_indicator

    params["blur"] = blur

    params["backgroundColor"] = background_color

    params["foregroundLayer"] = foreground_layer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}".format(
            itemId=item_id,
            imageType=image_type,
            imageIndex=image_index,
            tag=tag,
            format=format_,
            maxWidth=max_width,
            maxHeight=max_height,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProblemDetails]:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    image_type: ImageType,
    image_index: int,
    tag: str,
    format_: ImageFormat,
    max_width: int,
    max_height: int,
    percent_played: float,
    unplayed_count: int,
    *,
    client: Union[AuthenticatedClient, Client],
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    quality: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    crop_whitespace: Union[Unset, None, bool] = UNSET,
    add_played_indicator: Union[Unset, None, bool] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
) -> Response[ProblemDetails]:
    """Gets the item's image.

    Args:
        item_id (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (str):
        format_ (ImageFormat): Enum ImageOutputFormat.
        max_width (int):
        max_height (int):
        percent_played (float):
        unplayed_count (int):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        quality (Union[Unset, None, int]):
        fill_width (Union[Unset, None, int]):
        fill_height (Union[Unset, None, int]):
        crop_whitespace (Union[Unset, None, bool]):
        add_played_indicator (Union[Unset, None, bool]):
        blur (Union[Unset, None, int]):
        background_color (Union[Unset, None, str]):
        foreground_layer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        image_type=image_type,
        image_index=image_index,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        crop_whitespace=crop_whitespace,
        add_played_indicator=add_played_indicator,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    image_type: ImageType,
    image_index: int,
    tag: str,
    format_: ImageFormat,
    max_width: int,
    max_height: int,
    percent_played: float,
    unplayed_count: int,
    *,
    client: Union[AuthenticatedClient, Client],
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    quality: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    crop_whitespace: Union[Unset, None, bool] = UNSET,
    add_played_indicator: Union[Unset, None, bool] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
) -> Optional[ProblemDetails]:
    """Gets the item's image.

    Args:
        item_id (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (str):
        format_ (ImageFormat): Enum ImageOutputFormat.
        max_width (int):
        max_height (int):
        percent_played (float):
        unplayed_count (int):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        quality (Union[Unset, None, int]):
        fill_width (Union[Unset, None, int]):
        fill_height (Union[Unset, None, int]):
        crop_whitespace (Union[Unset, None, bool]):
        add_played_indicator (Union[Unset, None, bool]):
        blur (Union[Unset, None, int]):
        background_color (Union[Unset, None, str]):
        foreground_layer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return sync_detailed(
        item_id=item_id,
        image_type=image_type,
        image_index=image_index,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        client=client,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        crop_whitespace=crop_whitespace,
        add_played_indicator=add_played_indicator,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    image_type: ImageType,
    image_index: int,
    tag: str,
    format_: ImageFormat,
    max_width: int,
    max_height: int,
    percent_played: float,
    unplayed_count: int,
    *,
    client: Union[AuthenticatedClient, Client],
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    quality: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    crop_whitespace: Union[Unset, None, bool] = UNSET,
    add_played_indicator: Union[Unset, None, bool] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
) -> Response[ProblemDetails]:
    """Gets the item's image.

    Args:
        item_id (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (str):
        format_ (ImageFormat): Enum ImageOutputFormat.
        max_width (int):
        max_height (int):
        percent_played (float):
        unplayed_count (int):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        quality (Union[Unset, None, int]):
        fill_width (Union[Unset, None, int]):
        fill_height (Union[Unset, None, int]):
        crop_whitespace (Union[Unset, None, bool]):
        add_played_indicator (Union[Unset, None, bool]):
        blur (Union[Unset, None, int]):
        background_color (Union[Unset, None, str]):
        foreground_layer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        image_type=image_type,
        image_index=image_index,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        crop_whitespace=crop_whitespace,
        add_played_indicator=add_played_indicator,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    image_type: ImageType,
    image_index: int,
    tag: str,
    format_: ImageFormat,
    max_width: int,
    max_height: int,
    percent_played: float,
    unplayed_count: int,
    *,
    client: Union[AuthenticatedClient, Client],
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    quality: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    crop_whitespace: Union[Unset, None, bool] = UNSET,
    add_played_indicator: Union[Unset, None, bool] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
) -> Optional[ProblemDetails]:
    """Gets the item's image.

    Args:
        item_id (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (str):
        format_ (ImageFormat): Enum ImageOutputFormat.
        max_width (int):
        max_height (int):
        percent_played (float):
        unplayed_count (int):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        quality (Union[Unset, None, int]):
        fill_width (Union[Unset, None, int]):
        fill_height (Union[Unset, None, int]):
        crop_whitespace (Union[Unset, None, bool]):
        add_played_indicator (Union[Unset, None, bool]):
        blur (Union[Unset, None, int]):
        background_color (Union[Unset, None, str]):
        foreground_layer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            image_type=image_type,
            image_index=image_index,
            tag=tag,
            format_=format_,
            max_width=max_width,
            max_height=max_height,
            percent_played=percent_played,
            unplayed_count=unplayed_count,
            client=client,
            width=width,
            height=height,
            quality=quality,
            fill_width=fill_width,
            fill_height=fill_height,
            crop_whitespace=crop_whitespace,
            add_played_indicator=add_played_indicator,
            blur=blur,
            background_color=background_color,
            foreground_layer=foreground_layer,
        )
    ).parsed
