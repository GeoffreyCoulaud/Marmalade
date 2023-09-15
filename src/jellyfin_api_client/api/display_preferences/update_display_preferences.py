from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.display_preferences_dto import DisplayPreferencesDto
from ...types import UNSET, Response


def _get_kwargs(
    display_preferences_id: str,
    *,
    json_body: DisplayPreferencesDto,
    user_id: str,
    client_query: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/DisplayPreferences/{displayPreferencesId}".format(
            displayPreferencesId=display_preferences_id,
        ),
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
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DisplayPreferencesDto,
    user_id: str,
    client_query: str,
) -> Response[Any]:
    """Update Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (str):
        client_query (str):
        json_body (DisplayPreferencesDto): Defines the display preferences for any item that
            supports them (usually Folders).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        json_body=json_body,
        user_id=user_id,
        client_query=client_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    json_body: DisplayPreferencesDto,
    user_id: str,
    client_query: str,
) -> Response[Any]:
    """Update Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (str):
        client_query (str):
        json_body (DisplayPreferencesDto): Defines the display preferences for any item that
            supports them (usually Folders).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        json_body=json_body,
        user_id=user_id,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
