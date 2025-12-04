from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.net_if import NetIf
from ...types import Response


def _get_kwargs(
    devname: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/interfaces/by-device/{devname}".format(
            devname=quote(str(devname), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | NetIf | None:
    if response.status_code == 200:
        response_200 = NetIf.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | NetIf]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    devname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | NetIf]:
    """Get interface by its host interface name

     Host interfaces are those defined by the operating system's drivers.
    It also includes pseudo interfaces, which are software created, such as
    TUN, TAP and bridges. This function gets the information of the {devname} specified.

    Args:
        devname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | NetIf]
    """

    kwargs = _get_kwargs(
        devname=devname,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    devname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | NetIf | None:
    """Get interface by its host interface name

     Host interfaces are those defined by the operating system's drivers.
    It also includes pseudo interfaces, which are software created, such as
    TUN, TAP and bridges. This function gets the information of the {devname} specified.

    Args:
        devname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | NetIf
    """

    return sync_detailed(
        devname=devname,
        client=client,
    ).parsed


async def asyncio_detailed(
    devname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | NetIf]:
    """Get interface by its host interface name

     Host interfaces are those defined by the operating system's drivers.
    It also includes pseudo interfaces, which are software created, such as
    TUN, TAP and bridges. This function gets the information of the {devname} specified.

    Args:
        devname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | NetIf]
    """

    kwargs = _get_kwargs(
        devname=devname,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    devname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | NetIf | None:
    """Get interface by its host interface name

     Host interfaces are those defined by the operating system's drivers.
    It also includes pseudo interfaces, which are software created, such as
    TUN, TAP and bridges. This function gets the information of the {devname} specified.

    Args:
        devname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | NetIf
    """

    return (
        await asyncio_detailed(
            devname=devname,
            client=client,
        )
    ).parsed
