from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.controllers_list import ControllersList
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    detailed: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["detailed"] = detailed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/mim/controllers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ControllersList, Error]]:
    if response.status_code == 200:
        response_200 = ControllersList.from_dict(response.json())

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
) -> Response[Union[ControllersList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    detailed: Union[Unset, bool] = UNSET,
) -> Response[Union[ControllersList, Error]]:
    """Get a list of configured controllers managing this device and information about this device

    Args:
        detailed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ControllersList, Error]]
    """

    kwargs = _get_kwargs(
        detailed=detailed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    detailed: Union[Unset, bool] = UNSET,
) -> Optional[Union[ControllersList, Error]]:
    """Get a list of configured controllers managing this device and information about this device

    Args:
        detailed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ControllersList, Error]
    """

    return sync_detailed(
        client=client,
        detailed=detailed,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    detailed: Union[Unset, bool] = UNSET,
) -> Response[Union[ControllersList, Error]]:
    """Get a list of configured controllers managing this device and information about this device

    Args:
        detailed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ControllersList, Error]]
    """

    kwargs = _get_kwargs(
        detailed=detailed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    detailed: Union[Unset, bool] = UNSET,
) -> Optional[Union[ControllersList, Error]]:
    """Get a list of configured controllers managing this device and information about this device

    Args:
        detailed (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ControllersList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            detailed=detailed,
        )
    ).parsed
