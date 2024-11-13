from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.nat_rule import NATRule
from ...models.nat_update_result import NATUpdateResult
from ...types import Response


def _get_kwargs(
    ids: str,
    *,
    body: NATRule,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/firewall/nat/{ids}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, NATUpdateResult]]:
    if response.status_code == 200:
        response_200 = NATUpdateResult.from_dict(response.json())

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
) -> Response[Union[Error, NATUpdateResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ids: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NATRule,
) -> Response[Union[Error, NATUpdateResult]]:
    """Update NAT rule

    Args:
        ids (str):
        body (NATRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, NATUpdateResult]]
    """

    kwargs = _get_kwargs(
        ids=ids,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ids: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NATRule,
) -> Optional[Union[Error, NATUpdateResult]]:
    """Update NAT rule

    Args:
        ids (str):
        body (NATRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, NATUpdateResult]
    """

    return sync_detailed(
        ids=ids,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ids: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NATRule,
) -> Response[Union[Error, NATUpdateResult]]:
    """Update NAT rule

    Args:
        ids (str):
        body (NATRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, NATUpdateResult]]
    """

    kwargs = _get_kwargs(
        ids=ids,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ids: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NATRule,
) -> Optional[Union[Error, NATUpdateResult]]:
    """Update NAT rule

    Args:
        ids (str):
        body (NATRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, NATUpdateResult]
    """

    return (
        await asyncio_detailed(
            ids=ids,
            client=client,
            body=body,
        )
    ).parsed
