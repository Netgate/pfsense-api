from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.open_vpn_server_config import OpenVPNServerConfig
from ...models.pfsense_result import PfsenseResult
from ...types import Response


def _get_kwargs(
    vpnid: str,
    *,
    body: OpenVPNServerConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vpn/openvpn/servers/{vpnid}".format(
            vpnid=quote(str(vpnid), safe=""),
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
    vpnid: str,
    *,
    client: AuthenticatedClient | Client,
    body: OpenVPNServerConfig,
) -> Response[Error | PfsenseResult]:
    """Update OpenVPN server

    Args:
        vpnid (str):
        body (OpenVPNServerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PfsenseResult]
    """

    kwargs = _get_kwargs(
        vpnid=vpnid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vpnid: str,
    *,
    client: AuthenticatedClient | Client,
    body: OpenVPNServerConfig,
) -> Error | PfsenseResult | None:
    """Update OpenVPN server

    Args:
        vpnid (str):
        body (OpenVPNServerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PfsenseResult
    """

    return sync_detailed(
        vpnid=vpnid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    vpnid: str,
    *,
    client: AuthenticatedClient | Client,
    body: OpenVPNServerConfig,
) -> Response[Error | PfsenseResult]:
    """Update OpenVPN server

    Args:
        vpnid (str):
        body (OpenVPNServerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PfsenseResult]
    """

    kwargs = _get_kwargs(
        vpnid=vpnid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vpnid: str,
    *,
    client: AuthenticatedClient | Client,
    body: OpenVPNServerConfig,
) -> Error | PfsenseResult | None:
    """Update OpenVPN server

    Args:
        vpnid (str):
        body (OpenVPNServerConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PfsenseResult
    """

    return (
        await asyncio_detailed(
            vpnid=vpnid,
            client=client,
            body=body,
        )
    ).parsed
