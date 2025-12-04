from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.retrieved_backup import RetrievedBackup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    userkey: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userkey"] = userkey

    params["revision"] = revision

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/acb/bkp",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | RetrievedBackup | None:
    if response.status_code == 200:
        response_200 = RetrievedBackup.from_dict(response.json())

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
) -> Response[Error | RetrievedBackup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    userkey: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Response[Error | RetrievedBackup]:
    """Retrieve backup

    Args:
        userkey (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RetrievedBackup]
    """

    kwargs = _get_kwargs(
        userkey=userkey,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    userkey: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Error | RetrievedBackup | None:
    """Retrieve backup

    Args:
        userkey (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RetrievedBackup
    """

    return sync_detailed(
        client=client,
        userkey=userkey,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    userkey: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Response[Error | RetrievedBackup]:
    """Retrieve backup

    Args:
        userkey (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RetrievedBackup]
    """

    kwargs = _get_kwargs(
        userkey=userkey,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    userkey: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Error | RetrievedBackup | None:
    """Retrieve backup

    Args:
        userkey (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RetrievedBackup
    """

    return (
        await asyncio_detailed(
            client=client,
            userkey=userkey,
            revision=revision,
        )
    ).parsed
