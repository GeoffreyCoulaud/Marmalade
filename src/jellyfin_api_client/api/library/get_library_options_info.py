from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_options_result_dto import LibraryOptionsResultDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    library_content_type: Union[Unset, None, str] = UNSET,
    is_new_library: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["libraryContentType"] = library_content_type

    params["isNewLibrary"] = is_new_library

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Libraries/AvailableOptions",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LibraryOptionsResultDto]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LibraryOptionsResultDto.from_dict(response.json())

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
) -> Response[Union[Any, LibraryOptionsResultDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    library_content_type: Union[Unset, None, str] = UNSET,
    is_new_library: Union[Unset, None, bool] = False,
) -> Response[Union[Any, LibraryOptionsResultDto]]:
    """Gets the library options info.

    Args:
        library_content_type (Union[Unset, None, str]):
        is_new_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LibraryOptionsResultDto]]
    """

    kwargs = _get_kwargs(
        library_content_type=library_content_type,
        is_new_library=is_new_library,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    library_content_type: Union[Unset, None, str] = UNSET,
    is_new_library: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, LibraryOptionsResultDto]]:
    """Gets the library options info.

    Args:
        library_content_type (Union[Unset, None, str]):
        is_new_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LibraryOptionsResultDto]
    """

    return sync_detailed(
        client=client,
        library_content_type=library_content_type,
        is_new_library=is_new_library,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    library_content_type: Union[Unset, None, str] = UNSET,
    is_new_library: Union[Unset, None, bool] = False,
) -> Response[Union[Any, LibraryOptionsResultDto]]:
    """Gets the library options info.

    Args:
        library_content_type (Union[Unset, None, str]):
        is_new_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LibraryOptionsResultDto]]
    """

    kwargs = _get_kwargs(
        library_content_type=library_content_type,
        is_new_library=is_new_library,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    library_content_type: Union[Unset, None, str] = UNSET,
    is_new_library: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, LibraryOptionsResultDto]]:
    """Gets the library options info.

    Args:
        library_content_type (Union[Unset, None, str]):
        is_new_library (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LibraryOptionsResultDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            library_content_type=library_content_type,
            is_new_library=is_new_library,
        )
    ).parsed
