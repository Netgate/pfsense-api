from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.intf_router_adv_setting import IntfRouterAdvSetting
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    intf: str,
    *,
    body: IntfRouterAdvSetting,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/services/radv/{intf}".format(
            intf=quote(str(intf), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    intf: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntfRouterAdvSetting,
) -> Response[Error | Result]:
    """Configure router advertisement for assigned interface

    Args:
        intf (str):
        body (IntfRouterAdvSetting):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        intf=intf,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    intf: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntfRouterAdvSetting,
) -> Error | Result | None:
    """Configure router advertisement for assigned interface

    Args:
        intf (str):
        body (IntfRouterAdvSetting):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return sync_detailed(
        intf=intf,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    intf: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntfRouterAdvSetting,
) -> Response[Error | Result]:
    """Configure router advertisement for assigned interface

    Args:
        intf (str):
        body (IntfRouterAdvSetting):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        intf=intf,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    intf: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntfRouterAdvSetting,
) -> Error | Result | None:
    """Configure router advertisement for assigned interface

    Args:
        intf (str):
        body (IntfRouterAdvSetting):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return (
        await asyncio_detailed(
            intf=intf,
            client=client,
            body=body,
        )
    ).parsed
