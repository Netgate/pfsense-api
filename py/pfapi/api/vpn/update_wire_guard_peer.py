from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pfsense_result import PfsenseResult
from ...models.wg_peer import WGPeer
from ...types import Response


def _get_kwargs(
    pubkey: str,
    *,
    body: WGPeer,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vpn/wg/peer/{pubkey}".format(
            pubkey=quote(str(pubkey), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PfsenseResult | None:
    if response.status_code == 200:
        response_200 = PfsenseResult.from_dict(response.json())

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
) -> Response[Error | PfsenseResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    body: WGPeer,
) -> Response[Error | PfsenseResult]:
    """Update WireGuard Peer

    Args:
        pubkey (str):
        body (WGPeer): valid values:
            enabled = "yes", "no"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PfsenseResult]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    body: WGPeer,
) -> Error | PfsenseResult | None:
    """Update WireGuard Peer

    Args:
        pubkey (str):
        body (WGPeer): valid values:
            enabled = "yes", "no"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PfsenseResult
    """

    return sync_detailed(
        pubkey=pubkey,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    body: WGPeer,
) -> Response[Error | PfsenseResult]:
    """Update WireGuard Peer

    Args:
        pubkey (str):
        body (WGPeer): valid values:
            enabled = "yes", "no"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PfsenseResult]
    """

    kwargs = _get_kwargs(
        pubkey=pubkey,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pubkey: str,
    *,
    client: AuthenticatedClient | Client,
    body: WGPeer,
) -> Error | PfsenseResult | None:
    """Update WireGuard Peer

    Args:
        pubkey (str):
        body (WGPeer): valid values:
            enabled = "yes", "no"

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PfsenseResult
    """

    return (
        await asyncio_detailed(
            pubkey=pubkey,
            client=client,
            body=body,
        )
    ).parsed
