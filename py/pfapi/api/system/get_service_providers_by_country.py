from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.provider_country import ProviderCountry
from ...types import Response


def _get_kwargs(
    country: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/system/serviceproviders/{country}".format(
            country=quote(str(country), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ProviderCountry | None:
    if response.status_code == 200:
        response_200 = ProviderCountry.from_dict(response.json())

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
) -> Response[Error | ProviderCountry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    country: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | ProviderCountry]:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProviderCountry]
    """

    kwargs = _get_kwargs(
        country=country,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    country: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | ProviderCountry | None:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProviderCountry
    """

    return sync_detailed(
        country=country,
        client=client,
    ).parsed


async def asyncio_detailed(
    country: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | ProviderCountry]:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ProviderCountry]
    """

    kwargs = _get_kwargs(
        country=country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    country: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | ProviderCountry | None:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ProviderCountry
    """

    return (
        await asyncio_detailed(
            country=country,
            client=client,
        )
    ).parsed
