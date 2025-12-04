from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.smart_result import SMARTResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    drive: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["drive"] = drive

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/diag/smart/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SMARTResult | None:
    if response.status_code == 200:
        response_200 = SMARTResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SMARTResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    drive: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[Error | SMARTResult]:
    """Get SMART logs

    Args:
        drive (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SMARTResult]
    """

    kwargs = _get_kwargs(
        drive=drive,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    drive: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Error | SMARTResult | None:
    """Get SMART logs

    Args:
        drive (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SMARTResult
    """

    return sync_detailed(
        client=client,
        drive=drive,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    drive: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[Error | SMARTResult]:
    """Get SMART logs

    Args:
        drive (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SMARTResult]
    """

    kwargs = _get_kwargs(
        drive=drive,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    drive: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Error | SMARTResult | None:
    """Get SMART logs

    Args:
        drive (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SMARTResult
    """

    return (
        await asyncio_detailed(
            client=client,
            drive=drive,
            type_=type_,
        )
    ).parsed
