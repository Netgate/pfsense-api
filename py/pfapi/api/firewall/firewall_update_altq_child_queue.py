from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.altq_child_queue import ALTQChildQueue
from ...models.error import Error
from ...models.pfsense_result import PfsenseResult
from ...types import Response


def _get_kwargs(
    name: str,
    parentname: str,
    qname: str,
    *,
    body: ALTQChildQueue,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/firewall/traffic-shaper/altq/{name}/queue/{parentname}/{qname}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PfsenseResult]]:
    if response.status_code == 200:
        response_200 = PfsenseResult.from_dict(response.json())

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
) -> Response[Union[Error, PfsenseResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    parentname: str,
    qname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ALTQChildQueue,
) -> Response[Union[Error, PfsenseResult]]:
    """Update ALTQ Child Queue

    Args:
        name (str):
        parentname (str):
        qname (str):
        body (ALTQChildQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PfsenseResult]]
    """

    kwargs = _get_kwargs(
        name=name,
        parentname=parentname,
        qname=qname,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    parentname: str,
    qname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ALTQChildQueue,
) -> Optional[Union[Error, PfsenseResult]]:
    """Update ALTQ Child Queue

    Args:
        name (str):
        parentname (str):
        qname (str):
        body (ALTQChildQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PfsenseResult]
    """

    return sync_detailed(
        name=name,
        parentname=parentname,
        qname=qname,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    parentname: str,
    qname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ALTQChildQueue,
) -> Response[Union[Error, PfsenseResult]]:
    """Update ALTQ Child Queue

    Args:
        name (str):
        parentname (str):
        qname (str):
        body (ALTQChildQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PfsenseResult]]
    """

    kwargs = _get_kwargs(
        name=name,
        parentname=parentname,
        qname=qname,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    parentname: str,
    qname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ALTQChildQueue,
) -> Optional[Union[Error, PfsenseResult]]:
    """Update ALTQ Child Queue

    Args:
        name (str):
        parentname (str):
        qname (str):
        body (ALTQChildQueue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PfsenseResult]
    """

    return (
        await asyncio_detailed(
            name=name,
            parentname=parentname,
            qname=qname,
            client=client,
            body=body,
        )
    ).parsed
