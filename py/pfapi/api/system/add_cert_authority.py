from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cert_authority import CertAuthority
from ...models.error import Error
from ...models.new_ca_cert_req import NewCaCertReq
from ...types import Response


def _get_kwargs(
    *,
    body: NewCaCertReq,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/system/certauth",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CertAuthority | Error | None:
    if response.status_code == 200:
        response_200 = CertAuthority.from_dict(response.json())

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
) -> Response[CertAuthority | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewCaCertReq,
) -> Response[CertAuthority | Error]:
    """Add Certificate Authority

     Add a new Certificate Authority. The input must provide one of the method structures
    which contain the parameters to generate the certificate from. If an existing certificate
    is to be used, the method_existing must contain the certificate and the private key
    associated with it.

    The input `NewCaCertReq` object must have a name provided, and one of the `method_xxxxx`
    providing the certificate creation options.

    Args:
        body (NewCaCertReq): Request for creating a new CA cert or updating an existing one.
            - name: short description about certificate
            - trust: add to OS trusted cert store
            - randomize_serial: use random serial numbers when signing certificates
            - one of: method_internal (self-signed), mehod_existing (import), or method_intermediate
            (signed by another CA)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertAuthority | Error]
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
    body: NewCaCertReq,
) -> CertAuthority | Error | None:
    """Add Certificate Authority

     Add a new Certificate Authority. The input must provide one of the method structures
    which contain the parameters to generate the certificate from. If an existing certificate
    is to be used, the method_existing must contain the certificate and the private key
    associated with it.

    The input `NewCaCertReq` object must have a name provided, and one of the `method_xxxxx`
    providing the certificate creation options.

    Args:
        body (NewCaCertReq): Request for creating a new CA cert or updating an existing one.
            - name: short description about certificate
            - trust: add to OS trusted cert store
            - randomize_serial: use random serial numbers when signing certificates
            - one of: method_internal (self-signed), mehod_existing (import), or method_intermediate
            (signed by another CA)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertAuthority | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewCaCertReq,
) -> Response[CertAuthority | Error]:
    """Add Certificate Authority

     Add a new Certificate Authority. The input must provide one of the method structures
    which contain the parameters to generate the certificate from. If an existing certificate
    is to be used, the method_existing must contain the certificate and the private key
    associated with it.

    The input `NewCaCertReq` object must have a name provided, and one of the `method_xxxxx`
    providing the certificate creation options.

    Args:
        body (NewCaCertReq): Request for creating a new CA cert or updating an existing one.
            - name: short description about certificate
            - trust: add to OS trusted cert store
            - randomize_serial: use random serial numbers when signing certificates
            - one of: method_internal (self-signed), mehod_existing (import), or method_intermediate
            (signed by another CA)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertAuthority | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewCaCertReq,
) -> CertAuthority | Error | None:
    """Add Certificate Authority

     Add a new Certificate Authority. The input must provide one of the method structures
    which contain the parameters to generate the certificate from. If an existing certificate
    is to be used, the method_existing must contain the certificate and the private key
    associated with it.

    The input `NewCaCertReq` object must have a name provided, and one of the `method_xxxxx`
    providing the certificate creation options.

    Args:
        body (NewCaCertReq): Request for creating a new CA cert or updating an existing one.
            - name: short description about certificate
            - trust: add to OS trusted cert store
            - randomize_serial: use random serial numbers when signing certificates
            - one of: method_internal (self-signed), mehod_existing (import), or method_intermediate
            (signed by another CA)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertAuthority | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
