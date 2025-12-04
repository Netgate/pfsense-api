from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.events import Events
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    last_id: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Events | None:
    if response.status_code == 200:
        response_200 = Events.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Events]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    last_id: int | Unset = UNSET,
) -> Response[Error | Events]:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be done on a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the next set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Events]
    """

    kwargs = _get_kwargs(
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    last_id: int | Unset = UNSET,
) -> Error | Events | None:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be done on a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the next set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Events
    """

    return sync_detailed(
        client=client,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    last_id: int | Unset = UNSET,
) -> Response[Error | Events]:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be done on a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the next set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Events]
    """

    kwargs = _get_kwargs(
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    last_id: int | Unset = UNSET,
) -> Error | Events | None:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be done on a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the next set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Events
    """

    return (
        await asyncio_detailed(
            client=client,
            last_id=last_id,
        )
    ).parsed
