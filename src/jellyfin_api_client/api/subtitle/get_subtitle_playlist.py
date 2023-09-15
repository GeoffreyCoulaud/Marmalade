from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    item_id: str,
    media_source_id: str,
    index: int,
    *,
    segment_length: int,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["segmentLength"] = segment_length

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8".format(
            itemId=item_id,
            mediaSourceId=media_source_id,
            index=index,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
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
    item_id: str,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient,
    segment_length: int,
) -> Response[Any]:
    """Gets an HLS subtitle playlist.

    Args:
        item_id (str):
        media_source_id (str):
        index (int):
        segment_length (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        segment_length=segment_length,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    media_source_id: str,
    index: int,
    *,
    client: AuthenticatedClient,
    segment_length: int,
) -> Response[Any]:
    """Gets an HLS subtitle playlist.

    Args:
        item_id (str):
        media_source_id (str):
        index (int):
        segment_length (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        segment_length=segment_length,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
