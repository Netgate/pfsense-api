from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certificate_detailed import CertificateDetailed
from ...models.error import Error
from ...models.new_cert_req import NewCertReq
from ...types import Response


def _get_kwargs(
    *,
    body: NewCertReq,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/system/certificates",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CertificateDetailed, Error]]:
    if response.status_code == 200:
        response_200 = CertificateDetailed.from_dict(response.json())

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
) -> Response[Union[CertificateDetailed, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCertReq,
) -> Response[Union[CertificateDetailed, Error]]:
    """Add certificate, certificate signing request or sign a certificate.

     Add a certificate, CSR or sign CSR request. The NewCertReq method can contain one of:
      - method_internal:        CertMethodNew
      - method_existing_pem:    CertMethodExistingPEM
      - method_existing_pkcs12: CertMethodExistingPkcs12
      - method_csr:             CertMethodSigningRequest
      - method_sign:            CertMethodSignCSR

    Args:
        body (NewCertReq): Request for creating a cert or updating an existing one.
            - name: short description about certificate
            - userid: user-ID for user-specific certificate, eg for VPN
            - description:  Descriptive name
            - one of the method_xxxx

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CertificateDetailed, Error]]
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
    client: Union[AuthenticatedClient, Client],
    body: NewCertReq,
) -> Optional[Union[CertificateDetailed, Error]]:
    """Add certificate, certificate signing request or sign a certificate.

     Add a certificate, CSR or sign CSR request. The NewCertReq method can contain one of:
      - method_internal:        CertMethodNew
      - method_existing_pem:    CertMethodExistingPEM
      - method_existing_pkcs12: CertMethodExistingPkcs12
      - method_csr:             CertMethodSigningRequest
      - method_sign:            CertMethodSignCSR

    Args:
        body (NewCertReq): Request for creating a cert or updating an existing one.
            - name: short description about certificate
            - userid: user-ID for user-specific certificate, eg for VPN
            - description:  Descriptive name
            - one of the method_xxxx

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CertificateDetailed, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCertReq,
) -> Response[Union[CertificateDetailed, Error]]:
    """Add certificate, certificate signing request or sign a certificate.

     Add a certificate, CSR or sign CSR request. The NewCertReq method can contain one of:
      - method_internal:        CertMethodNew
      - method_existing_pem:    CertMethodExistingPEM
      - method_existing_pkcs12: CertMethodExistingPkcs12
      - method_csr:             CertMethodSigningRequest
      - method_sign:            CertMethodSignCSR

    Args:
        body (NewCertReq): Request for creating a cert or updating an existing one.
            - name: short description about certificate
            - userid: user-ID for user-specific certificate, eg for VPN
            - description:  Descriptive name
            - one of the method_xxxx

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CertificateDetailed, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCertReq,
) -> Optional[Union[CertificateDetailed, Error]]:
    """Add certificate, certificate signing request or sign a certificate.

     Add a certificate, CSR or sign CSR request. The NewCertReq method can contain one of:
      - method_internal:        CertMethodNew
      - method_existing_pem:    CertMethodExistingPEM
      - method_existing_pkcs12: CertMethodExistingPkcs12
      - method_csr:             CertMethodSigningRequest
      - method_sign:            CertMethodSignCSR

    Args:
        body (NewCertReq): Request for creating a cert or updating an existing one.
            - name: short description about certificate
            - userid: user-ID for user-specific certificate, eg for VPN
            - description:  Descriptive name
            - one of the method_xxxx

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CertificateDetailed, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed