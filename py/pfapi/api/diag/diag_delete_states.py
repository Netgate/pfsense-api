from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.result import Result
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    srcip: str | Unset = UNSET,
    dstip: str | Unset = UNSET,
    filter_str: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["srcip"] = srcip

    params["dstip"] = dstip

    params["filter_str"] = filter_str

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/diag/states",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Result | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Result]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    srcip: str | Unset = UNSET,
    dstip: str | Unset = UNSET,
    filter_str: str | Unset = UNSET,
) -> Response[Error | Result]:
    """Delete state information

    Args:
        srcip (str | Unset):
        dstip (str | Unset):
        filter_str (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        srcip=srcip,
        dstip=dstip,
        filter_str=filter_str,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    srcip: str | Unset = UNSET,
    dstip: str | Unset = UNSET,
    filter_str: str | Unset = UNSET,
) -> Error | Result | None:
    """Delete state information

    Args:
        srcip (str | Unset):
        dstip (str | Unset):
        filter_str (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return sync_detailed(
        client=client,
        srcip=srcip,
        dstip=dstip,
        filter_str=filter_str,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    srcip: str | Unset = UNSET,
    dstip: str | Unset = UNSET,
    filter_str: str | Unset = UNSET,
) -> Response[Error | Result]:
    """Delete state information

    Args:
        srcip (str | Unset):
        dstip (str | Unset):
        filter_str (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        srcip=srcip,
        dstip=dstip,
        filter_str=filter_str,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    srcip: str | Unset = UNSET,
    dstip: str | Unset = UNSET,
    filter_str: str | Unset = UNSET,
) -> Error | Result | None:
    """Delete state information

    Args:
        srcip (str | Unset):
        dstip (str | Unset):
        filter_str (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return (
        await asyncio_detailed(
            client=client,
            srcip=srcip,
            dstip=dstip,
            filter_str=filter_str,
        )
    ).parsed
