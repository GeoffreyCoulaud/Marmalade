from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    item_id: Union[Unset, None, str] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    index: Union[Unset, None, int] = UNSET,
    start_position_ticks: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, str] = UNSET,
    end_position_ticks: Union[Unset, None, int] = UNSET,
    copy_timestamps: Union[Unset, None, bool] = False,
    add_vtt_time_map: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["itemId"] = item_id

    params["mediaSourceId"] = media_source_id

    params["index"] = index

    params["startPositionTicks"] = start_position_ticks

    params["format"] = format_

    params["endPositionTicks"] = end_position_ticks

    params["copyTimestamps"] = copy_timestamps

    params["addVttTimeMap"] = add_vtt_time_map

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/{routeStartPositionTicks}/Stream.{routeFormat}".format(
            routeItemId=route_item_id,
            routeMediaSourceId=route_media_source_id,
            routeIndex=route_index,
            routeStartPositionTicks=route_start_position_ticks,
            routeFormat=route_format,
        ),
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
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: Union[AuthenticatedClient, Client],
    item_id: Union[Unset, None, str] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    index: Union[Unset, None, int] = UNSET,
    start_position_ticks: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, str] = UNSET,
    end_position_ticks: Union[Unset, None, int] = UNSET,
    copy_timestamps: Union[Unset, None, bool] = False,
    add_vtt_time_map: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (str):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (Union[Unset, None, str]):
        media_source_id (Union[Unset, None, str]):
        index (Union[Unset, None, int]):
        start_position_ticks (Union[Unset, None, int]):
        format_ (Union[Unset, None, str]):
        end_position_ticks (Union[Unset, None, int]):
        copy_timestamps (Union[Unset, None, bool]):
        add_vtt_time_map (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: Union[AuthenticatedClient, Client],
    item_id: Union[Unset, None, str] = UNSET,
    media_source_id: Union[Unset, None, str] = UNSET,
    index: Union[Unset, None, int] = UNSET,
    start_position_ticks: Union[Unset, None, int] = UNSET,
    format_: Union[Unset, None, str] = UNSET,
    end_position_ticks: Union[Unset, None, int] = UNSET,
    copy_timestamps: Union[Unset, None, bool] = False,
    add_vtt_time_map: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (str):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (Union[Unset, None, str]):
        media_source_id (Union[Unset, None, str]):
        index (Union[Unset, None, int]):
        start_position_ticks (Union[Unset, None, int]):
        format_ (Union[Unset, None, str]):
        end_position_ticks (Union[Unset, None, int]):
        copy_timestamps (Union[Unset, None, bool]):
        add_vtt_time_map (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
