from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cert_authorities import CertAuthorities
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    withprivkey: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["withprivkey"] = withprivkey

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/system/certauth",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CertAuthorities | Error | None:
    if response.status_code == 200:
        response_200 = CertAuthorities.from_dict(response.json())

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
) -> Response[CertAuthorities | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    withprivkey: bool | Unset = UNSET,
) -> Response[CertAuthorities | Error]:
    """Get a list of Certificate Authorities

    Args:
        withprivkey (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertAuthorities | Error]
    """

    kwargs = _get_kwargs(
        withprivkey=withprivkey,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    withprivkey: bool | Unset = UNSET,
) -> CertAuthorities | Error | None:
    """Get a list of Certificate Authorities

    Args:
        withprivkey (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertAuthorities | Error
    """

    return sync_detailed(
        client=client,
        withprivkey=withprivkey,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    withprivkey: bool | Unset = UNSET,
) -> Response[CertAuthorities | Error]:
    """Get a list of Certificate Authorities

    Args:
        withprivkey (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertAuthorities | Error]
    """

    kwargs = _get_kwargs(
        withprivkey=withprivkey,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    withprivkey: bool | Unset = UNSET,
) -> CertAuthorities | Error | None:
    """Get a list of Certificate Authorities

    Args:
        withprivkey (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertAuthorities | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            withprivkey=withprivkey,
        )
    ).parsed
