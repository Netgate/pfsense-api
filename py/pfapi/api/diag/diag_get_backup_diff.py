from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.diag_backup_diff import DiagBackupDiff
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    t1: Union[Unset, int] = UNSET,
    t2: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["t1"] = t1

    params["t2"] = t2

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/diag/backup/diff",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DiagBackupDiff, Error]]:
    if response.status_code == 200:
        response_200 = DiagBackupDiff.from_dict(response.json())

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
) -> Response[Union[DiagBackupDiff, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    t1: Union[Unset, int] = UNSET,
    t2: Union[Unset, int] = UNSET,
) -> Response[Union[DiagBackupDiff, Error]]:
    """Get a diff of two backups

    Args:
        t1 (Union[Unset, int]):
        t2 (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DiagBackupDiff, Error]]
    """

    kwargs = _get_kwargs(
        t1=t1,
        t2=t2,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    t1: Union[Unset, int] = UNSET,
    t2: Union[Unset, int] = UNSET,
) -> Optional[Union[DiagBackupDiff, Error]]:
    """Get a diff of two backups

    Args:
        t1 (Union[Unset, int]):
        t2 (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DiagBackupDiff, Error]
    """

    return sync_detailed(
        client=client,
        t1=t1,
        t2=t2,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    t1: Union[Unset, int] = UNSET,
    t2: Union[Unset, int] = UNSET,
) -> Response[Union[DiagBackupDiff, Error]]:
    """Get a diff of two backups

    Args:
        t1 (Union[Unset, int]):
        t2 (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DiagBackupDiff, Error]]
    """

    kwargs = _get_kwargs(
        t1=t1,
        t2=t2,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    t1: Union[Unset, int] = UNSET,
    t2: Union[Unset, int] = UNSET,
) -> Optional[Union[DiagBackupDiff, Error]]:
    """Get a diff of two backups

    Args:
        t1 (Union[Unset, int]):
        t2 (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DiagBackupDiff, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            t1=t1,
            t2=t2,
        )
    ).parsed
