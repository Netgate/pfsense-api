from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.provider_country import ProviderCountry
from ...types import Response


def _get_kwargs(
    country: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/system/serviceproviders/{country}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ProviderCountry]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, ProviderCountry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    country: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, ProviderCountry]]:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ProviderCountry]]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, ProviderCountry]]:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ProviderCountry]
    """

    return sync_detailed(
        country=country,
        client=client,
    ).parsed


async def asyncio_detailed(
    country: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, ProviderCountry]]:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ProviderCountry]]
    """

    kwargs = _get_kwargs(
        country=country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    country: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, ProviderCountry]]:
    """Get Service Provider by Country

    Args:
        country (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ProviderCountry]
    """

    return (
        await asyncio_detailed(
            country=country,
            client=client,
        )
    ).parsed
