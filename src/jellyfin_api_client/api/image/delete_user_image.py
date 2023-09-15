from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    image_type: ImageType,
    *,
    index: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["index"] = index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": "/Users/{userId}/Images/{imageType}".format(
            userId=user_id,
            imageType=image_type,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
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
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient,
    index: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        image_type=image_type,
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient,
    index: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        user_id=user_id,
        image_type=image_type,
        client=client,
        index=index,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient,
    index: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        image_type=image_type,
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient,
    index: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            image_type=image_type,
            client=client,
            index=index,
        )
    ).parsed
