from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.sso_services import SSOServices
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/login/ssoauth",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SSOServices | None:
    if response.status_code == 200:
        response_200 = SSOServices.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SSOServices]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | SSOServices]:
    """Retrieve the list of single sign-on authenticators for logging into the controller

     Fetch the list of external login service providers that have been configured on this
    controller, such as: SAML, OAuth. The returned data is a list of labels to for the
    service and its associated URL to proceed with the login.

    If no service has been configured, then an empty list is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SSOServices]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | SSOServices | None:
    """Retrieve the list of single sign-on authenticators for logging into the controller

     Fetch the list of external login service providers that have been configured on this
    controller, such as: SAML, OAuth. The returned data is a list of labels to for the
    service and its associated URL to proceed with the login.

    If no service has been configured, then an empty list is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SSOServices
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | SSOServices]:
    """Retrieve the list of single sign-on authenticators for logging into the controller

     Fetch the list of external login service providers that have been configured on this
    controller, such as: SAML, OAuth. The returned data is a list of labels to for the
    service and its associated URL to proceed with the login.

    If no service has been configured, then an empty list is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SSOServices]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | SSOServices | None:
    """Retrieve the list of single sign-on authenticators for logging into the controller

     Fetch the list of external login service providers that have been configured on this
    controller, such as: SAML, OAuth. The returned data is a list of labels to for the
    service and its associated URL to proceed with the login.

    If no service has been configured, then an empty list is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SSOServices
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
