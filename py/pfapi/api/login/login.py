from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.login_credentials import LoginCredentials
from ...models.login_response import LoginResponse
from ...types import Response


def _get_kwargs(
    *,
    body: LoginCredentials,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/login",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LoginResponse]]:
    if response.status_code == 200:
        response_200 = LoginResponse.from_dict(response.json())

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
) -> Response[Union[Error, LoginResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginCredentials,
) -> Response[Union[Error, LoginResponse]]:
    """Authenticate with the controller.

     Login to pfSense. If the JWT access token is not provided, then a new
    one is allocated. A JWT refresh token is also applied to cookie. The client
    can refresh the access token, while the refresh token is still valid, by
    calling RefreshAccessToken (POST /login/refresh).

    Args:
        body (LoginCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LoginResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginCredentials,
) -> Optional[Union[Error, LoginResponse]]:
    """Authenticate with the controller.

     Login to pfSense. If the JWT access token is not provided, then a new
    one is allocated. A JWT refresh token is also applied to cookie. The client
    can refresh the access token, while the refresh token is still valid, by
    calling RefreshAccessToken (POST /login/refresh).

    Args:
        body (LoginCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LoginResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginCredentials,
) -> Response[Union[Error, LoginResponse]]:
    """Authenticate with the controller.

     Login to pfSense. If the JWT access token is not provided, then a new
    one is allocated. A JWT refresh token is also applied to cookie. The client
    can refresh the access token, while the refresh token is still valid, by
    calling RefreshAccessToken (POST /login/refresh).

    Args:
        body (LoginCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LoginResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: LoginCredentials,
) -> Optional[Union[Error, LoginResponse]]:
    """Authenticate with the controller.

     Login to pfSense. If the JWT access token is not provided, then a new
    one is allocated. A JWT refresh token is also applied to cookie. The client
    can refresh the access token, while the refresh token is still valid, by
    calling RefreshAccessToken (POST /login/refresh).

    Args:
        body (LoginCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LoginResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed