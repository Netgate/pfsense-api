from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dhcp_static_mapping import DhcpStaticMapping
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    version: str,
    iface: str,
    *,
    body: DhcpStaticMapping,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/services/dhcp-server/{version}/static-mappings/{iface}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DhcpStaticMapping, Error]]:
    if response.status_code == 200:
        response_200 = DhcpStaticMapping.from_dict(response.json())

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
) -> Response[Union[DhcpStaticMapping, Error]]:
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
    client: Union[AuthenticatedClient, Client],
    body: DhcpStaticMapping,
) -> Response[Union[DhcpStaticMapping, Error]]:
    """Create a static mapping for a given interface

    Args:
        version (str):
        iface (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DhcpStaticMapping, Error]]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    iface: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DhcpStaticMapping,
) -> Optional[Union[DhcpStaticMapping, Error]]:
    """Create a static mapping for a given interface

    Args:
        version (str):
        iface (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DhcpStaticMapping, Error]
    """

    return sync_detailed(
        version=version,
        iface=iface,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    version: str,
    iface: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DhcpStaticMapping,
) -> Response[Union[DhcpStaticMapping, Error]]:
    """Create a static mapping for a given interface

    Args:
        version (str):
        iface (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DhcpStaticMapping, Error]]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    iface: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DhcpStaticMapping,
) -> Optional[Union[DhcpStaticMapping, Error]]:
    """Create a static mapping for a given interface

    Args:
        version (str):
        iface (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DhcpStaticMapping, Error]
    """

    return (
        await asyncio_detailed(
            version=version,
            iface=iface,
            client=client,
            body=body,
        )
    ).parsed
