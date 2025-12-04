from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.service_provider import ServiceProvider
from ...types import Response


def _get_kwargs(
    country: str,
    provider: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/system/serviceproviders/{country}/{provider}".format(
            country=quote(str(country), safe=""),
            provider=quote(str(provider), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ServiceProvider | None:
    if response.status_code == 200:
        response_200 = ServiceProvider.from_dict(response.json())

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
) -> Response[Error | ServiceProvider]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    country: str,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | ServiceProvider]:
    """Get Service Provider by Provider

    Args:
        country (str):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ServiceProvider]
    """

    kwargs = _get_kwargs(
        country=country,
        provider=provider,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    country: str,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | ServiceProvider | None:
    """Get Service Provider by Provider

    Args:
        country (str):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ServiceProvider
    """

    return sync_detailed(
        country=country,
        provider=provider,
        client=client,
    ).parsed


async def asyncio_detailed(
    country: str,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | ServiceProvider]:
    """Get Service Provider by Provider

    Args:
        country (str):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ServiceProvider]
    """

    kwargs = _get_kwargs(
        country=country,
        provider=provider,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    country: str,
    provider: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | ServiceProvider | None:
    """Get Service Provider by Provider

    Args:
        country (str):
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ServiceProvider
    """

    return (
        await asyncio_detailed(
            country=country,
            provider=provider,
            client=client,
        )
    ).parsed
