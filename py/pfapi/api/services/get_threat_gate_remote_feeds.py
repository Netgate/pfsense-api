from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.threat_gate_remote_feeds_array import ThreatGateRemoteFeedsArray
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    mode: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["enabled"] = enabled

    params["mode"] = mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/threatgate/remotes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ThreatGateRemoteFeedsArray | None:
    if response.status_code == 200:
        response_200 = ThreatGateRemoteFeedsArray.from_dict(response.json())

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
) -> Response[Error | ThreatGateRemoteFeedsArray]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    mode: str | Unset = UNSET,
) -> Response[Error | ThreatGateRemoteFeedsArray]:
    """Retrieves the a list of remote feeds filtered by optional query-parameters

    Args:
        name (str | Unset):
        enabled (bool | Unset):
        mode (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ThreatGateRemoteFeedsArray]
    """

    kwargs = _get_kwargs(
        name=name,
        enabled=enabled,
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    mode: str | Unset = UNSET,
) -> Error | ThreatGateRemoteFeedsArray | None:
    """Retrieves the a list of remote feeds filtered by optional query-parameters

    Args:
        name (str | Unset):
        enabled (bool | Unset):
        mode (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ThreatGateRemoteFeedsArray
    """

    return sync_detailed(
        client=client,
        name=name,
        enabled=enabled,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    mode: str | Unset = UNSET,
) -> Response[Error | ThreatGateRemoteFeedsArray]:
    """Retrieves the a list of remote feeds filtered by optional query-parameters

    Args:
        name (str | Unset):
        enabled (bool | Unset):
        mode (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ThreatGateRemoteFeedsArray]
    """

    kwargs = _get_kwargs(
        name=name,
        enabled=enabled,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    mode: str | Unset = UNSET,
) -> Error | ThreatGateRemoteFeedsArray | None:
    """Retrieves the a list of remote feeds filtered by optional query-parameters

    Args:
        name (str | Unset):
        enabled (bool | Unset):
        mode (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ThreatGateRemoteFeedsArray
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            enabled=enabled,
            mode=mode,
        )
    ).parsed
