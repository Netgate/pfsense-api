from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.events import Events
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    last_id: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Events]]:
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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, Events]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    last_id: Union[Unset, int] = UNSET,
) -> Response[Union[Error, Events]]:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be placed on a a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the nest set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Events]]
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
    client: Union[AuthenticatedClient, Client],
    last_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, Events]]:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be placed on a a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the nest set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Events]
    """

    return sync_detailed(
        client=client,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    last_id: Union[Unset, int] = UNSET,
) -> Response[Union[Error, Events]]:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be placed on a a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the nest set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Events]]
    """

    kwargs = _get_kwargs(
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    last_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Error, Events]]:
    """Long poll to wait for events from the system

     Detect system events or alerts that need to be attended to.
    Calling this function will block the client, and it should therefore
    be placed on a a dedicated connection from other API requests.
    Each event returned in the events list has an event_id, which
    can be used as a tracker for retrieving the nest set of events.

    parameters:
      - last_id: the ID of the event that was last retrieved by the client.

    Args:
        last_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Events]
    """

    return (
        await asyncio_detailed(
            client=client,
            last_id=last_id,
        )
    ).parsed
