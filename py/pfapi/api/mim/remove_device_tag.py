from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.controlled_device import ControlledDevice
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    tag: str,
    device_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/mim/devices/tag/{tag}/device/{device_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ControlledDevice, Error]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ControlledDevice, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tag: str,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ControlledDevice, Error]]:
    r"""Remove the tag from the specified device. If tag == \"*\" then remove all tags from the device.

    Args:
        tag (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ControlledDevice, Error]]
    """

    kwargs = _get_kwargs(
        tag=tag,
        device_id=device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag: str,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ControlledDevice, Error]]:
    r"""Remove the tag from the specified device. If tag == \"*\" then remove all tags from the device.

    Args:
        tag (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ControlledDevice, Error]
    """

    return sync_detailed(
        tag=tag,
        device_id=device_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tag: str,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ControlledDevice, Error]]:
    r"""Remove the tag from the specified device. If tag == \"*\" then remove all tags from the device.

    Args:
        tag (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ControlledDevice, Error]]
    """

    kwargs = _get_kwargs(
        tag=tag,
        device_id=device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag: str,
    device_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ControlledDevice, Error]]:
    r"""Remove the tag from the specified device. If tag == \"*\" then remove all tags from the device.

    Args:
        tag (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ControlledDevice, Error]
    """

    return (
        await asyncio_detailed(
            tag=tag,
            device_id=device_id,
            client=client,
        )
    ).parsed
