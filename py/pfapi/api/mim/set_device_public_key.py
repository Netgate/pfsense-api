from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device_public_key_option import DevicePublicKeyOption
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: DevicePublicKeyOption,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mim/device/pubkey",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DevicePublicKeyOption | Error | None:
    if response.status_code == 200:
        response_200 = DevicePublicKeyOption.from_dict(response.json())

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
) -> Response[DevicePublicKeyOption | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DevicePublicKeyOption,
) -> Response[DevicePublicKeyOption | Error]:
    """Sets the pfSense device's public key which is used by a controller to manage it.

     The ED25519 public key set to the device is used for secure Noise handshaking
    between the controller and the device to ensure the establish trust. The public
    key part is exported in the `DeviceIdentity` structure and is what should be
    updated on the controller when this device's key is changed.

    This function is intended to be used on the device to change its ED25519 public key.

    Args:
        body (DevicePublicKeyOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DevicePublicKeyOption | Error]
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
    body: DevicePublicKeyOption,
) -> DevicePublicKeyOption | Error | None:
    """Sets the pfSense device's public key which is used by a controller to manage it.

     The ED25519 public key set to the device is used for secure Noise handshaking
    between the controller and the device to ensure the establish trust. The public
    key part is exported in the `DeviceIdentity` structure and is what should be
    updated on the controller when this device's key is changed.

    This function is intended to be used on the device to change its ED25519 public key.

    Args:
        body (DevicePublicKeyOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DevicePublicKeyOption | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DevicePublicKeyOption,
) -> Response[DevicePublicKeyOption | Error]:
    """Sets the pfSense device's public key which is used by a controller to manage it.

     The ED25519 public key set to the device is used for secure Noise handshaking
    between the controller and the device to ensure the establish trust. The public
    key part is exported in the `DeviceIdentity` structure and is what should be
    updated on the controller when this device's key is changed.

    This function is intended to be used on the device to change its ED25519 public key.

    Args:
        body (DevicePublicKeyOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DevicePublicKeyOption | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DevicePublicKeyOption,
) -> DevicePublicKeyOption | Error | None:
    """Sets the pfSense device's public key which is used by a controller to manage it.

     The ED25519 public key set to the device is used for secure Noise handshaking
    between the controller and the device to ensure the establish trust. The public
    key part is exported in the `DeviceIdentity` structure and is what should be
    updated on the controller when this device's key is changed.

    This function is intended to be used on the device to change its ED25519 public key.

    Args:
        body (DevicePublicKeyOption):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DevicePublicKeyOption | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
