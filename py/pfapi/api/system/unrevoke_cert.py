from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crl_entries import CRLEntries
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    refid: str,
    certid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/system/crl/{refid}/cert/{certid}".format(
            refid=quote(str(refid), safe=""),
            certid=quote(str(certid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CRLEntries | Error | None:
    if response.status_code == 200:
        response_200 = CRLEntries.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CRLEntries | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    refid: str,
    certid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CRLEntries | Error]:
    """Unrevoke certificate by its ID.

     Unrevokes the certificate by removing it from the CRL.

    Args:
        refid (str):
        certid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CRLEntries | Error]
    """

    kwargs = _get_kwargs(
        refid=refid,
        certid=certid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    refid: str,
    certid: str,
    *,
    client: AuthenticatedClient | Client,
) -> CRLEntries | Error | None:
    """Unrevoke certificate by its ID.

     Unrevokes the certificate by removing it from the CRL.

    Args:
        refid (str):
        certid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CRLEntries | Error
    """

    return sync_detailed(
        refid=refid,
        certid=certid,
        client=client,
    ).parsed


async def asyncio_detailed(
    refid: str,
    certid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CRLEntries | Error]:
    """Unrevoke certificate by its ID.

     Unrevokes the certificate by removing it from the CRL.

    Args:
        refid (str):
        certid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CRLEntries | Error]
    """

    kwargs = _get_kwargs(
        refid=refid,
        certid=certid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    refid: str,
    certid: str,
    *,
    client: AuthenticatedClient | Client,
) -> CRLEntries | Error | None:
    """Unrevoke certificate by its ID.

     Unrevokes the certificate by removing it from the CRL.

    Args:
        refid (str):
        certid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CRLEntries | Error
    """

    return (
        await asyncio_detailed(
            refid=refid,
            certid=certid,
            client=client,
        )
    ).parsed
