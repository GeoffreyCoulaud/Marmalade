from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_virtual_folder_dto import AddVirtualFolderDto
from ...models.collection_type_options import CollectionTypeOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: AddVirtualFolderDto,
    name: Union[Unset, None, str] = UNSET,
    collection_type: Union[Unset, None, CollectionTypeOptions] = UNSET,
    paths: Union[Unset, None, List[str]] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["name"] = name

    json_collection_type: Union[Unset, None, str] = UNSET
    if not isinstance(collection_type, Unset):
        json_collection_type = collection_type.value if collection_type else None

    params["collectionType"] = json_collection_type

    json_paths: Union[Unset, None, List[str]] = UNSET
    if not isinstance(paths, Unset):
        if paths is None:
            json_paths = None
        else:
            json_paths = paths

    params["paths"] = json_paths

    params["refreshLibrary"] = refresh_library

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/Library/VirtualFolders",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
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
    *,
    client: AuthenticatedClient,
    json_body: AddVirtualFolderDto,
    name: Union[Unset, None, str] = UNSET,
    collection_type: Union[Unset, None, CollectionTypeOptions] = UNSET,
    paths: Union[Unset, None, List[str]] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Adds a virtual folder.

    Args:
        name (Union[Unset, None, str]):
        collection_type (Union[Unset, None, CollectionTypeOptions]):
        paths (Union[Unset, None, List[str]]):
        refresh_library (Union[Unset, None, bool]):
        json_body (AddVirtualFolderDto): Add virtual folder dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        name=name,
        collection_type=collection_type,
        paths=paths,
        refresh_library=refresh_library,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AddVirtualFolderDto,
    name: Union[Unset, None, str] = UNSET,
    collection_type: Union[Unset, None, CollectionTypeOptions] = UNSET,
    paths: Union[Unset, None, List[str]] = UNSET,
    refresh_library: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Adds a virtual folder.

    Args:
        name (Union[Unset, None, str]):
        collection_type (Union[Unset, None, CollectionTypeOptions]):
        paths (Union[Unset, None, List[str]]):
        refresh_library (Union[Unset, None, bool]):
        json_body (AddVirtualFolderDto): Add virtual folder dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        name=name,
        collection_type=collection_type,
        paths=paths,
        refresh_library=refresh_library,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
