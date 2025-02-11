from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crl_entries import CRLEntries
from ...models.error import Error
from ...models.new_crl_req import NewCRLReq
from ...types import Response


def _get_kwargs(
    *,
    body: NewCRLReq,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/system/crl",
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCRLReq,
) -> Response[Union[CRLEntries, Error]]:
    """Add new CRL, either by importing an existing X509 version or creating one.

     Add a new CRL with either an existing X509 input or values for creating a new one.
    The NewCRLReq method must contain one of:
      - method_internal:  CRLMethodNew
      - method_x509:      CRLMethodX509

    Args:
        body (NewCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CRLEntries, Error]]
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
    body: NewCRLReq,
) -> Optional[Union[CRLEntries, Error]]:
    """Add new CRL, either by importing an existing X509 version or creating one.

     Add a new CRL with either an existing X509 input or values for creating a new one.
    The NewCRLReq method must contain one of:
      - method_internal:  CRLMethodNew
      - method_x509:      CRLMethodX509

    Args:
        body (NewCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CRLEntries, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCRLReq,
) -> Response[Union[CRLEntries, Error]]:
    """Add new CRL, either by importing an existing X509 version or creating one.

     Add a new CRL with either an existing X509 input or values for creating a new one.
    The NewCRLReq method must contain one of:
      - method_internal:  CRLMethodNew
      - method_x509:      CRLMethodX509

    Args:
        body (NewCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CRLEntries, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewCRLReq,
) -> Optional[Union[CRLEntries, Error]]:
    """Add new CRL, either by importing an existing X509 version or creating one.

     Add a new CRL with either an existing X509 input or values for creating a new one.
    The NewCRLReq method must contain one of:
      - method_internal:  CRLMethodNew
      - method_x509:      CRLMethodX509

    Args:
        body (NewCRLReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CRLEntries, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
