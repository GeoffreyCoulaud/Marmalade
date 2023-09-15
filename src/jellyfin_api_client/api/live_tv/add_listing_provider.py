from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listings_provider_info import ListingsProviderInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: ListingsProviderInfo,
    pw: Union[Unset, None, str] = UNSET,
    validate_listings: Union[Unset, None, bool] = False,
    validate_login: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["pw"] = pw

    params["validateListings"] = validate_listings

    params["validateLogin"] = validate_login

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/LiveTv/ListingProviders",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListingsProviderInfo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListingsProviderInfo.from_dict(response.json())

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
) -> Response[Union[Any, ListingsProviderInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ListingsProviderInfo,
    pw: Union[Unset, None, str] = UNSET,
    validate_listings: Union[Unset, None, bool] = False,
    validate_login: Union[Unset, None, bool] = False,
) -> Response[Union[Any, ListingsProviderInfo]]:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, None, str]):
        validate_listings (Union[Unset, None, bool]):
        validate_login (Union[Unset, None, bool]):
        json_body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingsProviderInfo]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        pw=pw,
        validate_listings=validate_listings,
        validate_login=validate_login,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ListingsProviderInfo,
    pw: Union[Unset, None, str] = UNSET,
    validate_listings: Union[Unset, None, bool] = False,
    validate_login: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, ListingsProviderInfo]]:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, None, str]):
        validate_listings (Union[Unset, None, bool]):
        validate_login (Union[Unset, None, bool]):
        json_body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingsProviderInfo]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        pw=pw,
        validate_listings=validate_listings,
        validate_login=validate_login,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ListingsProviderInfo,
    pw: Union[Unset, None, str] = UNSET,
    validate_listings: Union[Unset, None, bool] = False,
    validate_login: Union[Unset, None, bool] = False,
) -> Response[Union[Any, ListingsProviderInfo]]:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, None, str]):
        validate_listings (Union[Unset, None, bool]):
        validate_login (Union[Unset, None, bool]):
        json_body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingsProviderInfo]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        pw=pw,
        validate_listings=validate_listings,
        validate_login=validate_login,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ListingsProviderInfo,
    pw: Union[Unset, None, str] = UNSET,
    validate_listings: Union[Unset, None, bool] = False,
    validate_login: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, ListingsProviderInfo]]:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, None, str]):
        validate_listings (Union[Unset, None, bool]):
        validate_login (Union[Unset, None, bool]):
        json_body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingsProviderInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            pw=pw,
            validate_listings=validate_listings,
            validate_login=validate_login,
        )
    ).parsed
