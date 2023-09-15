from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.package_info import PackageInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    assembly_guid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["assemblyGuid"] = assembly_guid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Packages/{name}".format(
            name=name,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PackageInfo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PackageInfo.from_dict(response.json())

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
) -> Response[Union[Any, PackageInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, PackageInfo]]:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PackageInfo]]
    """

    kwargs = _get_kwargs(
        name=name,
        assembly_guid=assembly_guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, PackageInfo]]:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PackageInfo]
    """

    return sync_detailed(
        name=name,
        client=client,
        assembly_guid=assembly_guid,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, PackageInfo]]:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PackageInfo]]
    """

    kwargs = _get_kwargs(
        name=name,
        assembly_guid=assembly_guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, PackageInfo]]:
    """Gets a package by name or assembly GUID.

    Args:
        name (str):
        assembly_guid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PackageInfo]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            assembly_guid=assembly_guid,
        )
    ).parsed
