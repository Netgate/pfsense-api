from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.arpmon_interface_state import ArpmonInterfaceState
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    intf: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/arpmon/{intf}".format(
            intf=quote(str(intf), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArpmonInterfaceState | Error | None:
    if response.status_code == 200:
        response_200 = ArpmonInterfaceState.from_dict(response.json())

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
) -> Response[ArpmonInterfaceState | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    intf: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ArpmonInterfaceState | Error]:
    """Get arpmon state for the interface

    Args:
        intf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArpmonInterfaceState | Error]
    """

    kwargs = _get_kwargs(
        intf=intf,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    intf: str,
    *,
    client: AuthenticatedClient | Client,
) -> ArpmonInterfaceState | Error | None:
    """Get arpmon state for the interface

    Args:
        intf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArpmonInterfaceState | Error
    """

    return sync_detailed(
        intf=intf,
        client=client,
    ).parsed


async def asyncio_detailed(
    intf: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ArpmonInterfaceState | Error]:
    """Get arpmon state for the interface

    Args:
        intf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArpmonInterfaceState | Error]
    """

    kwargs = _get_kwargs(
        intf=intf,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    intf: str,
    *,
    client: AuthenticatedClient | Client,
) -> ArpmonInterfaceState | Error | None:
    """Get arpmon state for the interface

    Args:
        intf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArpmonInterfaceState | Error
    """

    return (
        await asyncio_detailed(
            intf=intf,
            client=client,
        )
    ).parsed
