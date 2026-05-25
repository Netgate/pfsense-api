from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.freeradiusauthorizedmac import Freeradiusauthorizedmac
from ...types import Response


def _get_kwargs(
    *,
    body: Freeradiusauthorizedmac,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ports/freeradius/macs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Freeradiusauthorizedmac | None:
    if response.status_code == 200:
        response_200 = Freeradiusauthorizedmac.from_dict(response.json())

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
) -> Response[Error | Freeradiusauthorizedmac]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Freeradiusauthorizedmac,
) -> Response[Error | Freeradiusauthorizedmac]:
    """Create a new FreeRADIUS authorized MAC

    Args:
        body (Freeradiusauthorizedmac):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Freeradiusauthorizedmac]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: Freeradiusauthorizedmac,
) -> Error | Freeradiusauthorizedmac | None:
    """Create a new FreeRADIUS authorized MAC

    Args:
        body (Freeradiusauthorizedmac):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Freeradiusauthorizedmac
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Freeradiusauthorizedmac,
) -> Response[Error | Freeradiusauthorizedmac]:
    """Create a new FreeRADIUS authorized MAC

    Args:
        body (Freeradiusauthorizedmac):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Freeradiusauthorizedmac]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: Freeradiusauthorizedmac,
) -> Error | Freeradiusauthorizedmac | None:
    """Create a new FreeRADIUS authorized MAC

    Args:
        body (Freeradiusauthorizedmac):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Freeradiusauthorizedmac
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
