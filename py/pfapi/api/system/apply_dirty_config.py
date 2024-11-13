from http import HTTPStatus
from typing import Any, Dict, Optional, Union

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
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/system/config/dirty",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DirtySubsystems, Error]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DirtySubsystems, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplyDirtyConfigRequest,
) -> Response[Union[DirtySubsystems, Error]]:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DirtySubsystems, Error]]
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
    client: Union[AuthenticatedClient, Client],
    body: ApplyDirtyConfigRequest,
) -> Optional[Union[DirtySubsystems, Error]]:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DirtySubsystems, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplyDirtyConfigRequest,
) -> Response[Union[DirtySubsystems, Error]]:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DirtySubsystems, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplyDirtyConfigRequest,
) -> Optional[Union[DirtySubsystems, Error]]:
    """Apply pending subsystem changes to the system.

     The configuration has pending changes that require a series of being applied.
    It returns the list of subsystems that are still dirty.

    Args:
        body (ApplyDirtyConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DirtySubsystems, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
