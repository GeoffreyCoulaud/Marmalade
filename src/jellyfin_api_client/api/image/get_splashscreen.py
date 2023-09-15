from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_format import ImageFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
    quality: Union[Unset, None, int] = 90,
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

    params["width"] = width

    params["height"] = height

    params["fillWidth"] = fill_width

    params["fillHeight"] = fill_height

    params["blur"] = blur

    params["backgroundColor"] = background_color

    params["foregroundLayer"] = foreground_layer

    params["quality"] = quality

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Branding/Splashscreen",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
    quality: Union[Unset, None, int] = 90,
) -> Response[Any]:
    """Generates or gets the splashscreen.

    Args:
        tag (Union[Unset, None, str]):
        format_ (Union[Unset, None, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        fill_width (Union[Unset, None, int]):
        fill_height (Union[Unset, None, int]):
        blur (Union[Unset, None, int]):
        background_color (Union[Unset, None, str]):
        foreground_layer (Union[Unset, None, str]):
        quality (Union[Unset, None, int]):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        width=width,
        height=height,
        fill_width=fill_width,
        fill_height=fill_height,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        quality=quality,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    tag: Union[Unset, None, str] = UNSET,
    format_: Union[Unset, None, ImageFormat] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    width: Union[Unset, None, int] = UNSET,
    height: Union[Unset, None, int] = UNSET,
    fill_width: Union[Unset, None, int] = UNSET,
    fill_height: Union[Unset, None, int] = UNSET,
    blur: Union[Unset, None, int] = UNSET,
    background_color: Union[Unset, None, str] = UNSET,
    foreground_layer: Union[Unset, None, str] = UNSET,
    quality: Union[Unset, None, int] = 90,
) -> Response[Any]:
    """Generates or gets the splashscreen.

    Args:
        tag (Union[Unset, None, str]):
        format_ (Union[Unset, None, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        width (Union[Unset, None, int]):
        height (Union[Unset, None, int]):
        fill_width (Union[Unset, None, int]):
        fill_height (Union[Unset, None, int]):
        blur (Union[Unset, None, int]):
        background_color (Union[Unset, None, str]):
        foreground_layer (Union[Unset, None, str]):
        quality (Union[Unset, None, int]):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        width=width,
        height=height,
        fill_width=fill_width,
        fill_height=fill_height,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        quality=quality,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
