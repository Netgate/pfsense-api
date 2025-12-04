from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.controlled_devices import ControlledDevices
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tags: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["tags"] = tags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mim/devices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ControlledDevices | Error | None:
    if response.status_code == 200:
        response_200 = ControlledDevices.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ControlledDevices | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    tags: str | Unset = UNSET,
) -> Response[ControlledDevices | Error]:
    """Get controlled devices

    Args:
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlledDevices | Error]
    """

    kwargs = _get_kwargs(
        tags=tags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    tags: str | Unset = UNSET,
) -> ControlledDevices | Error | None:
    """Get controlled devices

    Args:
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlledDevices | Error
    """

    return sync_detailed(
        client=client,
        tags=tags,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    tags: str | Unset = UNSET,
) -> Response[ControlledDevices | Error]:
    """Get controlled devices

    Args:
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlledDevices | Error]
    """

    kwargs = _get_kwargs(
        tags=tags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    tags: str | Unset = UNSET,
) -> ControlledDevices | Error | None:
    """Get controlled devices

    Args:
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlledDevices | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            tags=tags,
        )
    ).parsed
