from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.fw_rule_toggle import FwRuleToggle
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    interface: str,
    id: str,
    *,
    body: FwRuleToggle,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/firewall/rules/interface/{interface}/toggle/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Result]]:
    if response.status_code == 200:
        response_200 = Result.from_dict(response.json())

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
) -> Response[Union[Error, Result]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    interface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FwRuleToggle,
) -> Response[Union[Error, Result]]:
    """Toggle rule by id

    Args:
        interface (str):
        id (str):
        body (FwRuleToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Result]]
    """

    kwargs = _get_kwargs(
        interface=interface,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    interface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FwRuleToggle,
) -> Optional[Union[Error, Result]]:
    """Toggle rule by id

    Args:
        interface (str):
        id (str):
        body (FwRuleToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Result]
    """

    return sync_detailed(
        interface=interface,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    interface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FwRuleToggle,
) -> Response[Union[Error, Result]]:
    """Toggle rule by id

    Args:
        interface (str):
        id (str):
        body (FwRuleToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Result]]
    """

    kwargs = _get_kwargs(
        interface=interface,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    interface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FwRuleToggle,
) -> Optional[Union[Error, Result]]:
    """Toggle rule by id

    Args:
        interface (str):
        id (str):
        body (FwRuleToggle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Result]
    """

    return (
        await asyncio_detailed(
            interface=interface,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
