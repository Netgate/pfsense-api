from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.controlled_device import ControlledDevice
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    device_id: str,
    *,
    body: ControlledDevice,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/mim/devices/device/{device_id}".format(
            device_id=quote(str(device_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ControlledDevice | Error | None:
    if response.status_code == 200:
        response_200 = ControlledDevice.from_dict(response.json())

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
) -> Response[ControlledDevice | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ControlledDevice,
) -> Response[ControlledDevice | Error]:
    """Update device's settings, which can include its VPN keys or tags.
    Only parameters provided will be updated

    Args:
        device_id (str):
        body (ControlledDevice): Parameters for adding the device

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlledDevice | Error]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ControlledDevice,
) -> ControlledDevice | Error | None:
    """Update device's settings, which can include its VPN keys or tags.
    Only parameters provided will be updated

    Args:
        device_id (str):
        body (ControlledDevice): Parameters for adding the device

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlledDevice | Error
    """

    return sync_detailed(
        device_id=device_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ControlledDevice,
) -> Response[ControlledDevice | Error]:
    """Update device's settings, which can include its VPN keys or tags.
    Only parameters provided will be updated

    Args:
        device_id (str):
        body (ControlledDevice): Parameters for adding the device

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ControlledDevice | Error]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    device_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ControlledDevice,
) -> ControlledDevice | Error | None:
    """Update device's settings, which can include its VPN keys or tags.
    Only parameters provided will be updated

    Args:
        device_id (str):
        body (ControlledDevice): Parameters for adding the device

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ControlledDevice | Error
    """

    return (
        await asyncio_detailed(
            device_id=device_id,
            client=client,
            body=body,
        )
    ).parsed
