from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.general_command_type import GeneralCommandType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, None, str] = UNSET,
    playable_media_types: Union[Unset, None, List[str]] = UNSET,
    supported_commands: Union[Unset, None, List[GeneralCommandType]] = UNSET,
    supports_media_control: Union[Unset, None, bool] = False,
    supports_sync: Union[Unset, None, bool] = False,
    supports_persistent_identifier: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["id"] = id

    json_playable_media_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(playable_media_types, Unset):
        if playable_media_types is None:
            json_playable_media_types = None
        else:
            json_playable_media_types = playable_media_types

    params["playableMediaTypes"] = json_playable_media_types

    json_supported_commands: Union[Unset, None, List[str]] = UNSET
    if not isinstance(supported_commands, Unset):
        if supported_commands is None:
            json_supported_commands = None
        else:
            json_supported_commands = []
            for supported_commands_item_data in supported_commands:
                supported_commands_item = supported_commands_item_data.value

                json_supported_commands.append(supported_commands_item)

    params["supportedCommands"] = json_supported_commands

    params["supportsMediaControl"] = supports_media_control

    params["supportsSync"] = supports_sync

    params["supportsPersistentIdentifier"] = supports_persistent_identifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/Sessions/Capabilities",
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
    id: Union[Unset, None, str] = UNSET,
    playable_media_types: Union[Unset, None, List[str]] = UNSET,
    supported_commands: Union[Unset, None, List[GeneralCommandType]] = UNSET,
    supports_media_control: Union[Unset, None, bool] = False,
    supports_sync: Union[Unset, None, bool] = False,
    supports_persistent_identifier: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """Updates capabilities for a device.

    Args:
        id (Union[Unset, None, str]):
        playable_media_types (Union[Unset, None, List[str]]):
        supported_commands (Union[Unset, None, List[GeneralCommandType]]):
        supports_media_control (Union[Unset, None, bool]):
        supports_sync (Union[Unset, None, bool]):
        supports_persistent_identifier (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        playable_media_types=playable_media_types,
        supported_commands=supported_commands,
        supports_media_control=supports_media_control,
        supports_sync=supports_sync,
        supports_persistent_identifier=supports_persistent_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, None, str] = UNSET,
    playable_media_types: Union[Unset, None, List[str]] = UNSET,
    supported_commands: Union[Unset, None, List[GeneralCommandType]] = UNSET,
    supports_media_control: Union[Unset, None, bool] = False,
    supports_sync: Union[Unset, None, bool] = False,
    supports_persistent_identifier: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """Updates capabilities for a device.

    Args:
        id (Union[Unset, None, str]):
        playable_media_types (Union[Unset, None, List[str]]):
        supported_commands (Union[Unset, None, List[GeneralCommandType]]):
        supports_media_control (Union[Unset, None, bool]):
        supports_sync (Union[Unset, None, bool]):
        supports_persistent_identifier (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        playable_media_types=playable_media_types,
        supported_commands=supported_commands,
        supports_media_control=supports_media_control,
        supports_sync=supports_sync,
        supports_persistent_identifier=supports_persistent_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
