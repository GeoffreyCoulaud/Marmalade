from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remote_subtitle_info import RemoteSubtitleInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    language: str,
    *,
    is_perfect_match: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["isPerfectMatch"] = is_perfect_match

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Items/{itemId}/RemoteSearch/Subtitles/{language}".format(
            itemId=item_id,
            language=language,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["RemoteSubtitleInfo"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RemoteSubtitleInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, List["RemoteSubtitleInfo"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["RemoteSubtitleInfo"]]]:
    """Search remote subtitles.

    Args:
        item_id (str):
        language (str):
        is_perfect_match (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['RemoteSubtitleInfo']]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        language=language,
        is_perfect_match=is_perfect_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["RemoteSubtitleInfo"]]]:
    """Search remote subtitles.

    Args:
        item_id (str):
        language (str):
        is_perfect_match (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['RemoteSubtitleInfo']]
    """

    return sync_detailed(
        item_id=item_id,
        language=language,
        client=client,
        is_perfect_match=is_perfect_match,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["RemoteSubtitleInfo"]]]:
    """Search remote subtitles.

    Args:
        item_id (str):
        language (str):
        is_perfect_match (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['RemoteSubtitleInfo']]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        language=language,
        is_perfect_match=is_perfect_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    language: str,
    *,
    client: AuthenticatedClient,
    is_perfect_match: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["RemoteSubtitleInfo"]]]:
    """Search remote subtitles.

    Args:
        item_id (str):
        language (str):
        is_perfect_match (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['RemoteSubtitleInfo']]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            language=language,
            client=client,
            is_perfect_match=is_perfect_match,
        )
    ).parsed
