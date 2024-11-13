from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certificate_detailed import CertificateDetailed
from ...models.error import Error
from ...models.update_cert_req import UpdateCertReq
from ...types import Response


def _get_kwargs(
    refid: str,
    *,
    body: UpdateCertReq,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/system/certificates/{refid}",
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
    refid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCertReq,
) -> Response[Union[CertificateDetailed, Error]]:
    """Update certificate with certificate and private key payloads

    Args:
        refid (str):
        body (UpdateCertReq): Update the certificate using either PEM or PKCS12 data. This
            operation is similar to
            importing a new certificate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CertificateDetailed, Error]]
    """

    kwargs = _get_kwargs(
        refid=refid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    refid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCertReq,
) -> Optional[Union[CertificateDetailed, Error]]:
    """Update certificate with certificate and private key payloads

    Args:
        refid (str):
        body (UpdateCertReq): Update the certificate using either PEM or PKCS12 data. This
            operation is similar to
            importing a new certificate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CertificateDetailed, Error]
    """

    return sync_detailed(
        refid=refid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    refid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCertReq,
) -> Response[Union[CertificateDetailed, Error]]:
    """Update certificate with certificate and private key payloads

    Args:
        refid (str):
        body (UpdateCertReq): Update the certificate using either PEM or PKCS12 data. This
            operation is similar to
            importing a new certificate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CertificateDetailed, Error]]
    """

    kwargs = _get_kwargs(
        refid=refid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    refid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCertReq,
) -> Optional[Union[CertificateDetailed, Error]]:
    """Update certificate with certificate and private key payloads

    Args:
        refid (str):
        body (UpdateCertReq): Update the certificate using either PEM or PKCS12 data. This
            operation is similar to
            importing a new certificate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CertificateDetailed, Error]
    """

    return (
        await asyncio_detailed(
            refid=refid,
            client=client,
            body=body,
        )
    ).parsed
