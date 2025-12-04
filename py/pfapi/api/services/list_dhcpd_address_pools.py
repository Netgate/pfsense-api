from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dhcp_address_pools import DhcpAddressPools
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    version: str,
    iface: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/dhcp-server/{version}/address-pools/{iface}".format(
            version=quote(str(version), safe=""),
            iface=quote(str(iface), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DhcpAddressPools | Error | None:
    if response.status_code == 200:
        response_200 = DhcpAddressPools.from_dict(response.json())

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
) -> Response[DhcpAddressPools | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    iface: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DhcpAddressPools | Error]:
    """List all address pools for an interface

    Args:
        version (str):
        iface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DhcpAddressPools | Error]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    iface: str,
    *,
    client: AuthenticatedClient | Client,
) -> DhcpAddressPools | Error | None:
    """List all address pools for an interface

    Args:
        version (str):
        iface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DhcpAddressPools | Error
    """

    return sync_detailed(
        version=version,
        iface=iface,
        client=client,
    ).parsed


async def asyncio_detailed(
    version: str,
    iface: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DhcpAddressPools | Error]:
    """List all address pools for an interface

    Args:
        version (str):
        iface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DhcpAddressPools | Error]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    iface: str,
    *,
    client: AuthenticatedClient | Client,
) -> DhcpAddressPools | Error | None:
    """List all address pools for an interface

    Args:
        version (str):
        iface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DhcpAddressPools | Error
    """

    return (
        await asyncio_detailed(
            version=version,
            iface=iface,
            client=client,
        )
    ).parsed
