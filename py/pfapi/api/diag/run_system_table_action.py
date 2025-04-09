from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.diag_table_action import DiagTableAction
from ...models.diag_table_detailed import DiagTableDetailed
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    table_name: str,
    *,
    body: DiagTableAction,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/diag/tables/{table_name}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DiagTableDetailed, Error]]:
    if response.status_code == 200:
        response_200 = DiagTableDetailed.from_dict(response.json())

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
) -> Response[Union[DiagTableDetailed, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DiagTableAction,
) -> Response[Union[DiagTableDetailed, Error]]:
    """Perform an action on the table, from its avail_action.

    Args:
        table_name (str):
        body (DiagTableAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DiagTableDetailed, Error]]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DiagTableAction,
) -> Optional[Union[DiagTableDetailed, Error]]:
    """Perform an action on the table, from its avail_action.

    Args:
        table_name (str):
        body (DiagTableAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DiagTableDetailed, Error]
    """

    return sync_detailed(
        table_name=table_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DiagTableAction,
) -> Response[Union[DiagTableDetailed, Error]]:
    """Perform an action on the table, from its avail_action.

    Args:
        table_name (str):
        body (DiagTableAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DiagTableDetailed, Error]]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DiagTableAction,
) -> Optional[Union[DiagTableDetailed, Error]]:
    """Perform an action on the table, from its avail_action.

    Args:
        table_name (str):
        body (DiagTableAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DiagTableDetailed, Error]
    """

    return (
        await asyncio_detailed(
            table_name=table_name,
            client=client,
            body=body,
        )
    ).parsed
