from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.log_entries import LogEntries
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    device_name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    class_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["device_name"] = device_name

    params["type"] = type_

    params["from_ts"] = from_ts

    params["to_ts"] = to_ts

    params["class"] = class_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/controller/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | LogEntries | None:
    if response.status_code == 200:
        response_200 = LogEntries.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | LogEntries]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    device_name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    class_: str | Unset = UNSET,
) -> Response[Error | LogEntries]:
    """Get controller logs

    Args:
        device_name (str | Unset):
        type_ (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        class_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LogEntries]
    """

    kwargs = _get_kwargs(
        device_name=device_name,
        type_=type_,
        from_ts=from_ts,
        to_ts=to_ts,
        class_=class_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    device_name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    class_: str | Unset = UNSET,
) -> Error | LogEntries | None:
    """Get controller logs

    Args:
        device_name (str | Unset):
        type_ (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        class_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LogEntries
    """

    return sync_detailed(
        client=client,
        device_name=device_name,
        type_=type_,
        from_ts=from_ts,
        to_ts=to_ts,
        class_=class_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    device_name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    class_: str | Unset = UNSET,
) -> Response[Error | LogEntries]:
    """Get controller logs

    Args:
        device_name (str | Unset):
        type_ (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        class_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LogEntries]
    """

    kwargs = _get_kwargs(
        device_name=device_name,
        type_=type_,
        from_ts=from_ts,
        to_ts=to_ts,
        class_=class_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    device_name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    from_ts: int | Unset = UNSET,
    to_ts: int | Unset = UNSET,
    class_: str | Unset = UNSET,
) -> Error | LogEntries | None:
    """Get controller logs

    Args:
        device_name (str | Unset):
        type_ (str | Unset):
        from_ts (int | Unset):
        to_ts (int | Unset):
        class_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LogEntries
    """

    return (
        await asyncio_detailed(
            client=client,
            device_name=device_name,
            type_=type_,
            from_ts=from_ts,
            to_ts=to_ts,
            class_=class_,
        )
    ).parsed
