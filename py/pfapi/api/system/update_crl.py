from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crl_entries import CRLEntries
from ...models.error import Error
from ...models.update_crl_req import UpdateCRLReq
from ...types import Response


def _get_kwargs(
    refid: str,
    *,
    body: UpdateCRLReq,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/system/crl/{refid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CRLEntries, Error]]:
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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CRLEntries, Error]]:
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
    body: UpdateCRLReq,
) -> Response[Union[CRLEntries, Error]]:
    """Update CRL, and add certs to be revoked

     Update CRL details, with option to add certificates to be revoked (if the CRL
    is an internal one). The update request must provide the complete CRL information
    including its description, just like creating a new CRL.

    Args:
        refid (str):
        body (UpdateCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CRLEntries, Error]]
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
    body: UpdateCRLReq,
) -> Optional[Union[CRLEntries, Error]]:
    """Update CRL, and add certs to be revoked

     Update CRL details, with option to add certificates to be revoked (if the CRL
    is an internal one). The update request must provide the complete CRL information
    including its description, just like creating a new CRL.

    Args:
        refid (str):
        body (UpdateCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CRLEntries, Error]
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
    body: UpdateCRLReq,
) -> Response[Union[CRLEntries, Error]]:
    """Update CRL, and add certs to be revoked

     Update CRL details, with option to add certificates to be revoked (if the CRL
    is an internal one). The update request must provide the complete CRL information
    including its description, just like creating a new CRL.

    Args:
        refid (str):
        body (UpdateCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CRLEntries, Error]]
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
    body: UpdateCRLReq,
) -> Optional[Union[CRLEntries, Error]]:
    """Update CRL, and add certs to be revoked

     Update CRL details, with option to add certificates to be revoked (if the CRL
    is an internal one). The update request must provide the complete CRL information
    including its description, just like creating a new CRL.

    Args:
        refid (str):
        body (UpdateCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CRLEntries, Error]
    """

    return (
        await asyncio_detailed(
            refid=refid,
            client=client,
            body=body,
        )
    ).parsed
