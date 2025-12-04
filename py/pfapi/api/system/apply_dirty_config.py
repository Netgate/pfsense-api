from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apply_dirty_config_request import ApplyDirtyConfigRequest
from ...models.dirty_subsystems import DirtySubsystems
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: ApplyDirtyConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/system/config/dirty",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DirtySubsystems | Error | None:
    if response.status_code == 200:
        response_200 = DirtySubsystems.from_dict(response.json())

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
) -> Response[DirtySubsystems | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ApplyDirtyConfigRequest,
) -> Response[DirtySubsystems | Error]:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirtySubsystems | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ApplyDirtyConfigRequest,
) -> DirtySubsystems | Error | None:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirtySubsystems | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ApplyDirtyConfigRequest,
) -> Response[DirtySubsystems | Error]:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirtySubsystems | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ApplyDirtyConfigRequest,
) -> DirtySubsystems | Error | None:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirtySubsystems | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
