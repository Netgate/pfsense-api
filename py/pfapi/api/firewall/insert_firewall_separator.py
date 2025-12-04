from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.insert_filter_separator import InsertFilterSeparator
from ...models.separator import Separator
from ...types import Response


def _get_kwargs(
    interface: str,
    *,
    body: InsertFilterSeparator,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/firewall/rules/interface/{interface}/separators".format(
            interface=quote(str(interface), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Separator | None:
    if response.status_code == 200:
        response_200 = Separator.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Separator]:
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
    body: InsertFilterSeparator,
) -> Response[Error | Separator]:
    """Create separator before/after a rule identified by its id

    Args:
        interface (str):
        body (InsertFilterSeparator):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Separator]
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
    body: InsertFilterSeparator,
) -> Error | Separator | None:
    """Create separator before/after a rule identified by its id

    Args:
        interface (str):
        body (InsertFilterSeparator):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Separator
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
    body: InsertFilterSeparator,
) -> Response[Error | Separator]:
    """Create separator before/after a rule identified by its id

    Args:
        interface (str):
        body (InsertFilterSeparator):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Separator]
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
    body: InsertFilterSeparator,
) -> Error | Separator | None:
    """Create separator before/after a rule identified by its id

    Args:
        interface (str):
        body (InsertFilterSeparator):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Separator
    """

    return (
        await asyncio_detailed(
            interface=interface,
            client=client,
            body=body,
        )
    ).parsed
