from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timer_info_dto_query_result import TimerInfoDtoQueryResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel_id: Union[Unset, None, str] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    is_scheduled: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["channelId"] = channel_id

    params["seriesTimerId"] = series_timer_id

    params["isActive"] = is_active

    params["isScheduled"] = is_scheduled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/LiveTv/Timers",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TimerInfoDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TimerInfoDtoQueryResult.from_dict(response.json())

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
) -> Response[Union[Any, TimerInfoDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: Union[Unset, None, str] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    is_scheduled: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, TimerInfoDtoQueryResult]]:
    """Gets the live tv timers.

    Args:
        channel_id (Union[Unset, None, str]):
        series_timer_id (Union[Unset, None, str]):
        is_active (Union[Unset, None, bool]):
        is_scheduled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TimerInfoDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        series_timer_id=series_timer_id,
        is_active=is_active,
        is_scheduled=is_scheduled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_id: Union[Unset, None, str] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    is_scheduled: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, TimerInfoDtoQueryResult]]:
    """Gets the live tv timers.

    Args:
        channel_id (Union[Unset, None, str]):
        series_timer_id (Union[Unset, None, str]):
        is_active (Union[Unset, None, bool]):
        is_scheduled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TimerInfoDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        series_timer_id=series_timer_id,
        is_active=is_active,
        is_scheduled=is_scheduled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: Union[Unset, None, str] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    is_scheduled: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, TimerInfoDtoQueryResult]]:
    """Gets the live tv timers.

    Args:
        channel_id (Union[Unset, None, str]):
        series_timer_id (Union[Unset, None, str]):
        is_active (Union[Unset, None, bool]):
        is_scheduled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TimerInfoDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        series_timer_id=series_timer_id,
        is_active=is_active,
        is_scheduled=is_scheduled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_id: Union[Unset, None, str] = UNSET,
    series_timer_id: Union[Unset, None, str] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    is_scheduled: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, TimerInfoDtoQueryResult]]:
    """Gets the live tv timers.

    Args:
        channel_id (Union[Unset, None, str]):
        series_timer_id (Union[Unset, None, str]):
        is_active (Union[Unset, None, bool]):
        is_scheduled (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TimerInfoDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            series_timer_id=series_timer_id,
            is_active=is_active,
            is_scheduled=is_scheduled,
        )
    ).parsed
