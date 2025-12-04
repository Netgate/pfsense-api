from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dhcp_static_mapping import DhcpStaticMapping
from ...models.error import Error
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    version: str,
    iface: str,
    id: str,
    *,
    body: DhcpStaticMapping,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/services/dhcp-server/{version}/static-mappings/{iface}/{id}".format(
            version=quote(str(version), safe=""),
            iface=quote(str(iface), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Result | None:
    if response.status_code == 200:
        response_200 = Result.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Result]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    iface: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DhcpStaticMapping,
) -> Response[Error | Result]:
    """Update static mapping

    Args:
        version (str):
        iface (str):
        id (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    iface: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DhcpStaticMapping,
) -> Error | Result | None:
    """Update static mapping

    Args:
        version (str):
        iface (str):
        id (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return sync_detailed(
        version=version,
        iface=iface,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    version: str,
    iface: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DhcpStaticMapping,
) -> Response[Error | Result]:
    """Update static mapping

    Args:
        version (str):
        iface (str):
        id (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    iface: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DhcpStaticMapping,
) -> Error | Result | None:
    """Update static mapping

    Args:
        version (str):
        iface (str):
        id (str):
        body (DhcpStaticMapping):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return (
        await asyncio_detailed(
            version=version,
            iface=iface,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
