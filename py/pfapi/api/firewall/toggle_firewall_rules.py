from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.fw_bulk_toggle import FwBulkToggle
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    interface: str,
    *,
    body: FwBulkToggle,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/firewall/rules/interface/{interface}/toggle".format(
            interface=quote(str(interface), safe=""),
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
    interface: str,
    *,
    client: AuthenticatedClient | Client,
    body: FwBulkToggle,
) -> Response[Error | Result]:
    """Bulk toggle of rules

    Args:
        interface (str):
        body (FwBulkToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        interface=interface,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    interface: str,
    *,
    client: AuthenticatedClient | Client,
    body: FwBulkToggle,
) -> Error | Result | None:
    """Bulk toggle of rules

    Args:
        interface (str):
        body (FwBulkToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return sync_detailed(
        interface=interface,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    interface: str,
    *,
    client: AuthenticatedClient | Client,
    body: FwBulkToggle,
) -> Response[Error | Result]:
    """Bulk toggle of rules

    Args:
        interface (str):
        body (FwBulkToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        interface=interface,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    interface: str,
    *,
    client: AuthenticatedClient | Client,
    body: FwBulkToggle,
) -> Error | Result | None:
    """Bulk toggle of rules

    Args:
        interface (str):
        body (FwBulkToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return (
        await asyncio_detailed(
            interface=interface,
            client=client,
            body=body,
        )
    ).parsed
