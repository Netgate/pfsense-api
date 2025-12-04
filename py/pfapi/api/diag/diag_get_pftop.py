from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pftop_response import PftopResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    viewtype: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sorttype: str | Unset = UNSET,
    states: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["viewtype"] = viewtype

    params["filter"] = filter_

    params["sorttype"] = sorttype

    params["states"] = states

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/diag/pftop",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PftopResponse | None:
    if response.status_code == 200:
        response_200 = PftopResponse.from_dict(response.json())

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
) -> Response[Error | PftopResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    viewtype: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sorttype: str | Unset = UNSET,
    states: str | Unset = UNSET,
) -> Response[Error | PftopResponse]:
    """Get pftop output

    Args:
        viewtype (str | Unset):
        filter_ (str | Unset):
        sorttype (str | Unset):
        states (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PftopResponse]
    """

    kwargs = _get_kwargs(
        viewtype=viewtype,
        filter_=filter_,
        sorttype=sorttype,
        states=states,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    viewtype: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sorttype: str | Unset = UNSET,
    states: str | Unset = UNSET,
) -> Error | PftopResponse | None:
    """Get pftop output

    Args:
        viewtype (str | Unset):
        filter_ (str | Unset):
        sorttype (str | Unset):
        states (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PftopResponse
    """

    return sync_detailed(
        client=client,
        viewtype=viewtype,
        filter_=filter_,
        sorttype=sorttype,
        states=states,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    viewtype: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sorttype: str | Unset = UNSET,
    states: str | Unset = UNSET,
) -> Response[Error | PftopResponse]:
    """Get pftop output

    Args:
        viewtype (str | Unset):
        filter_ (str | Unset):
        sorttype (str | Unset):
        states (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PftopResponse]
    """

    kwargs = _get_kwargs(
        viewtype=viewtype,
        filter_=filter_,
        sorttype=sorttype,
        states=states,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    viewtype: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sorttype: str | Unset = UNSET,
    states: str | Unset = UNSET,
) -> Error | PftopResponse | None:
    """Get pftop output

    Args:
        viewtype (str | Unset):
        filter_ (str | Unset):
        sorttype (str | Unset):
        states (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PftopResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            viewtype=viewtype,
            filter_=filter_,
            sorttype=sorttype,
            states=states,
        )
    ).parsed
