from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.snort_interface_config import SnortInterfaceConfig
from ...types import Response


def _get_kwargs(
    *,
    body: SnortInterfaceConfig,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/services/snort/intf",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SnortInterfaceConfig | None:
    if response.status_code == 200:
        response_200 = SnortInterfaceConfig.from_dict(response.json())

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
) -> Response[Error | SnortInterfaceConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SnortInterfaceConfig,
) -> Response[Error | SnortInterfaceConfig]:
    """Apply the specified configuration.

     Apply snort configuration for the specified interfaces in the SnortInterfaceConfig argument. The
    interfaces must not already be bound to another SnortInterfaceConfig.
    If Talos LightSPD rules are used, then the interface configuration will limit the number of
    customizations that are applied. Most of the changes are for overriding the LigthSPD defaults.
    The `id` of the configuration will be automatically assigned by the handler and guaranteed to be
    unique.

    Args:
        body (SnortInterfaceConfig): Per-interface group Snort configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortInterfaceConfig]
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
    body: SnortInterfaceConfig,
) -> Error | SnortInterfaceConfig | None:
    """Apply the specified configuration.

     Apply snort configuration for the specified interfaces in the SnortInterfaceConfig argument. The
    interfaces must not already be bound to another SnortInterfaceConfig.
    If Talos LightSPD rules are used, then the interface configuration will limit the number of
    customizations that are applied. Most of the changes are for overriding the LigthSPD defaults.
    The `id` of the configuration will be automatically assigned by the handler and guaranteed to be
    unique.

    Args:
        body (SnortInterfaceConfig): Per-interface group Snort configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortInterfaceConfig
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SnortInterfaceConfig,
) -> Response[Error | SnortInterfaceConfig]:
    """Apply the specified configuration.

     Apply snort configuration for the specified interfaces in the SnortInterfaceConfig argument. The
    interfaces must not already be bound to another SnortInterfaceConfig.
    If Talos LightSPD rules are used, then the interface configuration will limit the number of
    customizations that are applied. Most of the changes are for overriding the LigthSPD defaults.
    The `id` of the configuration will be automatically assigned by the handler and guaranteed to be
    unique.

    Args:
        body (SnortInterfaceConfig): Per-interface group Snort configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortInterfaceConfig]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SnortInterfaceConfig,
) -> Error | SnortInterfaceConfig | None:
    """Apply the specified configuration.

     Apply snort configuration for the specified interfaces in the SnortInterfaceConfig argument. The
    interfaces must not already be bound to another SnortInterfaceConfig.
    If Talos LightSPD rules are used, then the interface configuration will limit the number of
    customizations that are applied. Most of the changes are for overriding the LigthSPD defaults.
    The `id` of the configuration will be automatically assigned by the handler and guaranteed to be
    unique.

    Args:
        body (SnortInterfaceConfig): Per-interface group Snort configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortInterfaceConfig
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
