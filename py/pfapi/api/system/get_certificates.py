from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certs_config import CertsConfig
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    csr_only: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["csr_only"] = csr_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/system/certificates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CertsConfig, Error]]:
    if response.status_code == 200:
        response_200 = CertsConfig.from_dict(response.json())

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
) -> Response[Union[CertsConfig, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    csr_only: Union[Unset, bool] = UNSET,
) -> Response[Union[CertsConfig, Error]]:
    """Get certificates, or CSRs only (if ?csr_only=true)

    Args:
        csr_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CertsConfig, Error]]
    """

    kwargs = _get_kwargs(
        csr_only=csr_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    csr_only: Union[Unset, bool] = UNSET,
) -> Optional[Union[CertsConfig, Error]]:
    """Get certificates, or CSRs only (if ?csr_only=true)

    Args:
        csr_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CertsConfig, Error]
    """

    return sync_detailed(
        client=client,
        csr_only=csr_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    csr_only: Union[Unset, bool] = UNSET,
) -> Response[Union[CertsConfig, Error]]:
    """Get certificates, or CSRs only (if ?csr_only=true)

    Args:
        csr_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CertsConfig, Error]]
    """

    kwargs = _get_kwargs(
        csr_only=csr_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    csr_only: Union[Unset, bool] = UNSET,
) -> Optional[Union[CertsConfig, Error]]:
    """Get certificates, or CSRs only (if ?csr_only=true)

    Args:
        csr_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CertsConfig, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            csr_only=csr_only,
        )
    ).parsed
