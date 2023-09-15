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
    name: str,
    image_type: ImageType,
    image_index: int,
    *,
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    percent_played: Union[Unset, None, float] = UNSET,
    unplayed_count: Union[Unset, None, int] = UNSET,
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
    params["tag"] = tag

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["percentPlayed"] = percent_played

    params["unplayedCount"] = unplayed_count

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
        "url": "/MusicGenres/{name}/Images/{imageType}/{imageIndex}".format(
            name=name,
            imageType=image_type,
            imageIndex=image_index,
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
    name: str,
    image_type: ImageType,
    image_index: int,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    percent_played: Union[Unset, None, float] = UNSET,
    unplayed_count: Union[Unset, None, int] = UNSET,
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
    """Get music genre image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (Union[Unset, None, str]):
        format_ (Union[Unset, None, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        percent_played (Union[Unset, None, float]):
        unplayed_count (Union[Unset, None, int]):
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
        name=name,
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
    name: str,
    image_type: ImageType,
    image_index: int,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    percent_played: Union[Unset, None, float] = UNSET,
    unplayed_count: Union[Unset, None, int] = UNSET,
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
    """Get music genre image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (Union[Unset, None, str]):
        format_ (Union[Unset, None, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        percent_played (Union[Unset, None, float]):
        unplayed_count (Union[Unset, None, int]):
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
        name=name,
        image_type=image_type,
        image_index=image_index,
        client=client,
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
    ).parsed


async def asyncio_detailed(
    name: str,
    image_type: ImageType,
    image_index: int,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    percent_played: Union[Unset, None, float] = UNSET,
    unplayed_count: Union[Unset, None, int] = UNSET,
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
    """Get music genre image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (Union[Unset, None, str]):
        format_ (Union[Unset, None, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        percent_played (Union[Unset, None, float]):
        unplayed_count (Union[Unset, None, int]):
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
        name=name,
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
    name: str,
    image_type: ImageType,
    image_index: int,
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    percent_played: Union[Unset, None, float] = UNSET,
    unplayed_count: Union[Unset, None, int] = UNSET,
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
    """Get music genre image by name.

    Args:
        name (str):
        image_type (ImageType): Enum ImageType.
        image_index (int):
        tag (Union[Unset, None, str]):
        format_ (Union[Unset, None, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        percent_played (Union[Unset, None, float]):
        unplayed_count (Union[Unset, None, int]):
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
            name=name,
            image_type=image_type,
            image_index=image_index,
            client=client,
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
    ).parsed
