from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.configuration_page_info import ConfigurationPageInfo
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enable_in_main_menu: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["enableInMainMenu"] = enable_in_main_menu

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/web/ConfigurationPages",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["ConfigurationPageInfo"], ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ConfigurationPageInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
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
) -> Response[Union[Any, List["ConfigurationPageInfo"], ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["ConfigurationPageInfo"], ProblemDetails]]:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ConfigurationPageInfo'], ProblemDetails]]
    """

    kwargs = _get_kwargs(
        enable_in_main_menu=enable_in_main_menu,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["ConfigurationPageInfo"], ProblemDetails]]:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ConfigurationPageInfo'], ProblemDetails]
    """

    return sync_detailed(
        client=client,
        enable_in_main_menu=enable_in_main_menu,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["ConfigurationPageInfo"], ProblemDetails]]:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ConfigurationPageInfo'], ProblemDetails]]
    """

    kwargs = _get_kwargs(
        enable_in_main_menu=enable_in_main_menu,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    enable_in_main_menu: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["ConfigurationPageInfo"], ProblemDetails]]:
    """Gets the configuration pages.

    Args:
        enable_in_main_menu (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['ConfigurationPageInfo'], ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            enable_in_main_menu=enable_in_main_menu,
        )
    ).parsed
