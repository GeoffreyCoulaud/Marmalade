from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device_info_query_result import DeviceInfoQueryResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    supports_sync: Union[Unset, None, bool] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["supportsSync"] = supports_sync

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Devices",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeviceInfoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeviceInfoQueryResult.from_dict(response.json())

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
) -> Response[Union[Any, DeviceInfoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    supports_sync: Union[Unset, None, bool] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, DeviceInfoQueryResult]]:
    """Get Devices.

    Args:
        supports_sync (Union[Unset, None, bool]):
        user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeviceInfoQueryResult]]
    """

    kwargs = _get_kwargs(
        supports_sync=supports_sync,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    supports_sync: Union[Unset, None, bool] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, DeviceInfoQueryResult]]:
    """Get Devices.

    Args:
        supports_sync (Union[Unset, None, bool]):
        user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeviceInfoQueryResult]
    """

    return sync_detailed(
        client=client,
        supports_sync=supports_sync,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    supports_sync: Union[Unset, None, bool] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, DeviceInfoQueryResult]]:
    """Get Devices.

    Args:
        supports_sync (Union[Unset, None, bool]):
        user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeviceInfoQueryResult]]
    """

    kwargs = _get_kwargs(
        supports_sync=supports_sync,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    supports_sync: Union[Unset, None, bool] = UNSET,
    user_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, DeviceInfoQueryResult]]:
    """Get Devices.

    Args:
        supports_sync (Union[Unset, None, bool]):
        user_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeviceInfoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            supports_sync=supports_sync,
            user_id=user_id,
        )
    ).parsed
