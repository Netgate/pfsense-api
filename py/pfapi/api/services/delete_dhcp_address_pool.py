from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    version: str,
    iface: str,
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/services/dhcp-server/{version}/address-pools/{iface}/{id}",
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
    version: str,
    iface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, Result]]:
    """Delete address pool by its id

    Args:
        version (str):
        iface (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Result]]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    iface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, Result]]:
    """Delete address pool by its id

    Args:
        version (str):
        iface (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Result]
    """

    return sync_detailed(
        version=version,
        iface=iface,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    version: str,
    iface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, Result]]:
    """Delete address pool by its id

    Args:
        version (str):
        iface (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Result]]
    """

    kwargs = _get_kwargs(
        version=version,
        iface=iface,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    iface: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, Result]]:
    """Delete address pool by its id

    Args:
        version (str):
        iface (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Result]
    """

    return (
        await asyncio_detailed(
            version=version,
            iface=iface,
            id=id,
            client=client,
        )
    ).parsed
