from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.quick_connect_result import QuickConnectResult
from ...types import UNSET, Response


def _get_kwargs(
    *,
    secret: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["secret"] = secret

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/QuickConnect/Connect",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, QuickConnectResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QuickConnectResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ProblemDetails, QuickConnectResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    secret: str,
) -> Response[Union[ProblemDetails, QuickConnectResult]]:
    """Attempts to retrieve authentication information.

    Args:
        secret (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, QuickConnectResult]]
    """

    kwargs = _get_kwargs(
        secret=secret,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    secret: str,
) -> Optional[Union[ProblemDetails, QuickConnectResult]]:
    """Attempts to retrieve authentication information.

    Args:
        secret (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, QuickConnectResult]
    """

    return sync_detailed(
        client=client,
        secret=secret,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    secret: str,
) -> Response[Union[ProblemDetails, QuickConnectResult]]:
    """Attempts to retrieve authentication information.

    Args:
        secret (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, QuickConnectResult]]
    """

    kwargs = _get_kwargs(
        secret=secret,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    secret: str,
) -> Optional[Union[ProblemDetails, QuickConnectResult]]:
    """Attempts to retrieve authentication information.

    Args:
        secret (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, QuickConnectResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            secret=secret,
        )
    ).parsed
