from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import File, Response


def _get_kwargs(
    video_id: str,
    media_source_id: str,
    index: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/Videos/{videoId}/{mediaSourceId}/Attachments/{index}".format(
            videoId=video_id,
            mediaSourceId=media_source_id,
            index=index,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[File, ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[Union[File, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    video_id: str,
    media_source_id: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[File, ProblemDetails]]:
    """Get video attachment.

    Args:
        video_id (str):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        media_source_id=media_source_id,
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    video_id: str,
    media_source_id: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[File, ProblemDetails]]:
    """Get video attachment.

    Args:
        video_id (str):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, ProblemDetails]
    """

    return sync_detailed(
        video_id=video_id,
        media_source_id=media_source_id,
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    video_id: str,
    media_source_id: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[File, ProblemDetails]]:
    """Get video attachment.

    Args:
        video_id (str):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        media_source_id=media_source_id,
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    video_id: str,
    media_source_id: str,
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[File, ProblemDetails]]:
    """Get video attachment.

    Args:
        video_id (str):
        media_source_id (str):
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            video_id=video_id,
            media_source_id=media_source_id,
            index=index,
            client=client,
        )
    ).parsed
