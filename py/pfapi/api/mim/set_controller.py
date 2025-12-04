from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.controller_identity import ControllerIdentity
from ...models.controller_info import ControllerInfo
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: ControllerIdentity,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mim/controllers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ControllerInfo | Error | None:
    if response.status_code == 200:
        response_200 = ControllerInfo.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ControllerInfo | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ControllerIdentity,
) -> Response[ControllerInfo | Error]:
    """Add/change a management controller with its public key on the pfsense host

     Adding the controller will initiate a Netgard connection to it. The device will
    continue to issue a connection request every 10 seconds while the Controller
    has not added the device to its configuration.

    Args:
        body (ControllerIdentity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControllerInfo | Error]
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
    client: AuthenticatedClient | Client,
    body: ControllerIdentity,
) -> ControllerInfo | Error | None:
    """Add/change a management controller with its public key on the pfsense host

     Adding the controller will initiate a Netgard connection to it. The device will
    continue to issue a connection request every 10 seconds while the Controller
    has not added the device to its configuration.

    Args:
        body (ControllerIdentity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControllerInfo | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ControllerIdentity,
) -> Response[ControllerInfo | Error]:
    """Add/change a management controller with its public key on the pfsense host

     Adding the controller will initiate a Netgard connection to it. The device will
    continue to issue a connection request every 10 seconds while the Controller
    has not added the device to its configuration.

    Args:
        body (ControllerIdentity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControllerInfo | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ControllerIdentity,
) -> ControllerInfo | Error | None:
    """Add/change a management controller with its public key on the pfsense host

     Adding the controller will initiate a Netgard connection to it. The device will
    continue to issue a connection request every 10 seconds while the Controller
    has not added the device to its configuration.

    Args:
        body (ControllerIdentity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControllerInfo | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
