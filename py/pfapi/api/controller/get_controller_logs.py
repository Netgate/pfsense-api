from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.log_entries import LogEntries
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    device_name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    from_ts: Union[Unset, int] = UNSET,
    to_ts: Union[Unset, int] = UNSET,
    class_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["device_name"] = device_name

    params["type"] = type

    params["from_ts"] = from_ts

    params["to_ts"] = to_ts

    params["class"] = class_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/controller/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LogEntries]]:
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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, LogEntries]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    from_ts: Union[Unset, int] = UNSET,
    to_ts: Union[Unset, int] = UNSET,
    class_: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LogEntries]]:
    """Get controller logs

    Args:
        device_name (Union[Unset, str]):
        type (Union[Unset, str]):
        from_ts (Union[Unset, int]):
        to_ts (Union[Unset, int]):
        class_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LogEntries]]
    """

    kwargs = _get_kwargs(
        device_name=device_name,
        type=type,
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
    client: Union[AuthenticatedClient, Client],
    device_name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    from_ts: Union[Unset, int] = UNSET,
    to_ts: Union[Unset, int] = UNSET,
    class_: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LogEntries]]:
    """Get controller logs

    Args:
        device_name (Union[Unset, str]):
        type (Union[Unset, str]):
        from_ts (Union[Unset, int]):
        to_ts (Union[Unset, int]):
        class_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LogEntries]
    """

    return sync_detailed(
        client=client,
        device_name=device_name,
        type=type,
        from_ts=from_ts,
        to_ts=to_ts,
        class_=class_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    from_ts: Union[Unset, int] = UNSET,
    to_ts: Union[Unset, int] = UNSET,
    class_: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LogEntries]]:
    """Get controller logs

    Args:
        device_name (Union[Unset, str]):
        type (Union[Unset, str]):
        from_ts (Union[Unset, int]):
        to_ts (Union[Unset, int]):
        class_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LogEntries]]
    """

    kwargs = _get_kwargs(
        device_name=device_name,
        type=type,
        from_ts=from_ts,
        to_ts=to_ts,
        class_=class_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    device_name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    from_ts: Union[Unset, int] = UNSET,
    to_ts: Union[Unset, int] = UNSET,
    class_: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LogEntries]]:
    """Get controller logs

    Args:
        device_name (Union[Unset, str]):
        type (Union[Unset, str]):
        from_ts (Union[Unset, int]):
        to_ts (Union[Unset, int]):
        class_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LogEntries]
    """

    return (
        await asyncio_detailed(
            client=client,
            device_name=device_name,
            type=type,
            from_ts=from_ts,
            to_ts=to_ts,
            class_=class_,
        )
    ).parsed
