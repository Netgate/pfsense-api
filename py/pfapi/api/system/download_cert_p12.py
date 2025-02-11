from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cert_pkcs_12_export_opts import CertPkcs12ExportOpts
from ...models.error import Error
from ...types import File, Response


def _get_kwargs(
    refid: str,
    *,
    body: CertPkcs12ExportOpts,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/system/certificates/{refid}/export-p12",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[Union[Error, File]]:
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
    body: CertPkcs12ExportOpts,
) -> Response[Union[Error, File]]:
    """Download the certificate and key as a unified PKCS12 file

    Args:
        refid (str):
        body (CertPkcs12ExportOpts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, File]]
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
    body: CertPkcs12ExportOpts,
) -> Optional[Union[Error, File]]:
    """Download the certificate and key as a unified PKCS12 file

    Args:
        refid (str):
        body (CertPkcs12ExportOpts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, File]
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
    body: CertPkcs12ExportOpts,
) -> Response[Union[Error, File]]:
    """Download the certificate and key as a unified PKCS12 file

    Args:
        refid (str):
        body (CertPkcs12ExportOpts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, File]]
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
    body: CertPkcs12ExportOpts,
) -> Optional[Union[Error, File]]:
    """Download the certificate and key as a unified PKCS12 file

    Args:
        refid (str):
        body (CertPkcs12ExportOpts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, File]
    """

    return (
        await asyncio_detailed(
            refid=refid,
            client=client,
            body=body,
        )
    ).parsed
