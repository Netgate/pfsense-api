from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.packages import Packages
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    remote_check: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["remote_check"] = remote_check

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/system/package/installed",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Packages | None:
    if response.status_code == 200:
        response_200 = Packages.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Packages]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    remote_check: bool | Unset = UNSET,
) -> Response[Error | Packages]:
    """Get list of installed packages

    Args:
        remote_check (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Packages]
    """

    kwargs = _get_kwargs(
        remote_check=remote_check,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    remote_check: bool | Unset = UNSET,
) -> Error | Packages | None:
    """Get list of installed packages

    Args:
        remote_check (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Packages
    """

    return sync_detailed(
        client=client,
        remote_check=remote_check,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    remote_check: bool | Unset = UNSET,
) -> Response[Error | Packages]:
    """Get list of installed packages

    Args:
        remote_check (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Packages]
    """

    kwargs = _get_kwargs(
        remote_check=remote_check,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    remote_check: bool | Unset = UNSET,
) -> Error | Packages | None:
    """Get list of installed packages

    Args:
        remote_check (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Packages
    """

    return (
        await asyncio_detailed(
            client=client,
            remote_check=remote_check,
        )
    ).parsed
