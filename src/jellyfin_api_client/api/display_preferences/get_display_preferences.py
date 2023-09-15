from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.display_preferences_dto import DisplayPreferencesDto
from ...types import UNSET, Response


def _get_kwargs(
    display_preferences_id: str,
    *,
    user_id: str,
    client_query: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/DisplayPreferences/{displayPreferencesId}".format(
            displayPreferencesId=display_preferences_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DisplayPreferencesDto]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DisplayPreferencesDto.from_dict(response.json())

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
) -> Response[Union[Any, DisplayPreferencesDto]]:
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
    user_id: str,
    client_query: str,
) -> Response[Union[Any, DisplayPreferencesDto]]:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (str):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DisplayPreferencesDto]]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        user_id=user_id,
        client_query=client_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    client_query: str,
) -> Optional[Union[Any, DisplayPreferencesDto]]:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (str):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DisplayPreferencesDto]
    """

    return sync_detailed(
        display_preferences_id=display_preferences_id,
        client=client,
        user_id=user_id,
        client_query=client_query,
    ).parsed


async def asyncio_detailed(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    client_query: str,
) -> Response[Union[Any, DisplayPreferencesDto]]:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (str):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DisplayPreferencesDto]]
    """

    kwargs = _get_kwargs(
        display_preferences_id=display_preferences_id,
        user_id=user_id,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    display_preferences_id: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    client_query: str,
) -> Optional[Union[Any, DisplayPreferencesDto]]:
    """Get Display Preferences.

    Args:
        display_preferences_id (str):
        user_id (str):
        client_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DisplayPreferencesDto]
    """

    return (
        await asyncio_detailed(
            display_preferences_id=display_preferences_id,
            client=client,
            user_id=user_id,
            client_query=client_query,
        )
    ).parsed
