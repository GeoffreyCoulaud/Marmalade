from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, None, str] = UNSET,
    new_name: Union[Unset, None, str] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["name"] = name

    params["newName"] = new_name

    params["refreshLibrary"] = refresh_library

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Library/VirtualFolders/Name",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409
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
) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    new_name: Union[Unset, None, str] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Response[Union[Any, ProblemDetails]]:
    """Renames a virtual folder.

    Args:
        name (Union[Unset, None, str]):
        new_name (Union[Unset, None, str]):
        refresh_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        name=name,
        new_name=new_name,
        refresh_library=refresh_library,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    new_name: Union[Unset, None, str] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, ProblemDetails]]:
    """Renames a virtual folder.

    Args:
        name (Union[Unset, None, str]):
        new_name (Union[Unset, None, str]):
        refresh_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        name=name,
        new_name=new_name,
        refresh_library=refresh_library,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    new_name: Union[Unset, None, str] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Response[Union[Any, ProblemDetails]]:
    """Renames a virtual folder.

    Args:
        name (Union[Unset, None, str]):
        new_name (Union[Unset, None, str]):
        refresh_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        name=name,
        new_name=new_name,
        refresh_library=refresh_library,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    new_name: Union[Unset, None, str] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, ProblemDetails]]:
    """Renames a virtual folder.

    Args:
        name (Union[Unset, None, str]):
        new_name (Union[Unset, None, str]):
        refresh_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            new_name=new_name,
            refresh_library=refresh_library,
        )
    ).parsed
