from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device_public_key_option import DevicePublicKeyOption
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: DevicePublicKeyOption,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/mim/device/pubkey",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DevicePublicKeyOption, Error]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DevicePublicKeyOption, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DevicePublicKeyOption,
) -> Response[Union[DevicePublicKeyOption, Error]]:
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
        Response[Union[DevicePublicKeyOption, Error]]
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
    body: DevicePublicKeyOption,
) -> Optional[Union[DevicePublicKeyOption, Error]]:
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
        Union[DevicePublicKeyOption, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DevicePublicKeyOption,
) -> Response[Union[DevicePublicKeyOption, Error]]:
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
        Response[Union[DevicePublicKeyOption, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DevicePublicKeyOption,
) -> Optional[Union[DevicePublicKeyOption, Error]]:
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
        Union[DevicePublicKeyOption, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
