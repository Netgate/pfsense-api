from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.open_vpn_next_port import OpenVPNNextPort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    protocol: str | Unset = UNSET,
    if_ident: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["protocol"] = protocol

    params["if_ident"] = if_ident

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vpn/openvpn/nextport",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | OpenVPNNextPort | None:
    if response.status_code == 200:
        response_200 = OpenVPNNextPort.from_dict(response.json())

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
) -> Response[Error | OpenVPNNextPort]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    protocol: str | Unset = UNSET,
    if_ident: str | Unset = UNSET,
) -> Response[Error | OpenVPNNextPort]:
    """Get the next available openvpn port

    Args:
        protocol (str | Unset):
        if_ident (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OpenVPNNextPort]
    """

    kwargs = _get_kwargs(
        protocol=protocol,
        if_ident=if_ident,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    protocol: str | Unset = UNSET,
    if_ident: str | Unset = UNSET,
) -> Error | OpenVPNNextPort | None:
    """Get the next available openvpn port

    Args:
        protocol (str | Unset):
        if_ident (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OpenVPNNextPort
    """

    return sync_detailed(
        client=client,
        protocol=protocol,
        if_ident=if_ident,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    protocol: str | Unset = UNSET,
    if_ident: str | Unset = UNSET,
) -> Response[Error | OpenVPNNextPort]:
    """Get the next available openvpn port

    Args:
        protocol (str | Unset):
        if_ident (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OpenVPNNextPort]
    """

    kwargs = _get_kwargs(
        protocol=protocol,
        if_ident=if_ident,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    protocol: str | Unset = UNSET,
    if_ident: str | Unset = UNSET,
) -> Error | OpenVPNNextPort | None:
    """Get the next available openvpn port

    Args:
        protocol (str | Unset):
        if_ident (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OpenVPNNextPort
    """

    return (
        await asyncio_detailed(
            client=client,
            protocol=protocol,
            if_ident=if_ident,
        )
    ).parsed
