from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.result import Result
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    port: Union[Unset, int] = UNSET,
    remipp: Union[Unset, str] = UNSET,
    clientid: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["port"] = port

    params["remipp"] = remipp

    params["clientid"] = clientid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/vpn/openvpn/killclient",
        "params": params,
    }

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
    *,
    client: Union[AuthenticatedClient, Client],
    port: Union[Unset, int] = UNSET,
    remipp: Union[Unset, str] = UNSET,
    clientid: Union[Unset, str] = UNSET,
) -> Response[Union[Error, Result]]:
    """Kill a client by host, IP or client ID

    Args:
        port (Union[Unset, int]):
        remipp (Union[Unset, str]):
        clientid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Result]]
    """

    kwargs = _get_kwargs(
        port=port,
        remipp=remipp,
        clientid=clientid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    port: Union[Unset, int] = UNSET,
    remipp: Union[Unset, str] = UNSET,
    clientid: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, Result]]:
    """Kill a client by host, IP or client ID

    Args:
        port (Union[Unset, int]):
        remipp (Union[Unset, str]):
        clientid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Result]
    """

    return sync_detailed(
        client=client,
        port=port,
        remipp=remipp,
        clientid=clientid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    port: Union[Unset, int] = UNSET,
    remipp: Union[Unset, str] = UNSET,
    clientid: Union[Unset, str] = UNSET,
) -> Response[Union[Error, Result]]:
    """Kill a client by host, IP or client ID

    Args:
        port (Union[Unset, int]):
        remipp (Union[Unset, str]):
        clientid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Result]]
    """

    kwargs = _get_kwargs(
        port=port,
        remipp=remipp,
        clientid=clientid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    port: Union[Unset, int] = UNSET,
    remipp: Union[Unset, str] = UNSET,
    clientid: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, Result]]:
    """Kill a client by host, IP or client ID

    Args:
        port (Union[Unset, int]):
        remipp (Union[Unset, str]):
        clientid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Result]
    """

    return (
        await asyncio_detailed(
            client=client,
            port=port,
            remipp=remipp,
            clientid=clientid,
        )
    ).parsed
