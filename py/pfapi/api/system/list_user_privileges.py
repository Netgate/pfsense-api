from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.user_privileges import UserPrivileges
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/system/users/privs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UserPrivileges]]:
    if response.status_code == 200:
        response_200 = UserPrivileges.from_dict(response.json())

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
) -> Response[Union[Error, UserPrivileges]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, UserPrivileges]]:
    """Get definitions of user privileges

     In pfSense, the user privileges are applied to the user's login to the
    legacy user interface. When pfSense acts as a Multi-instance Management
    Controller, MIM privileges are defined by the group's name.

    When the Controller runs as a separate entity, group privileges are used
    as roles in Multi-instance management and define the entitlements of the
    user belonging to the group. Apart from the superuser (or admin) role,
    all roles can be made granular with read, modify and delete attributes.
    A role without these attributes is considered to be granted them all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UserPrivileges]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, UserPrivileges]]:
    """Get definitions of user privileges

     In pfSense, the user privileges are applied to the user's login to the
    legacy user interface. When pfSense acts as a Multi-instance Management
    Controller, MIM privileges are defined by the group's name.

    When the Controller runs as a separate entity, group privileges are used
    as roles in Multi-instance management and define the entitlements of the
    user belonging to the group. Apart from the superuser (or admin) role,
    all roles can be made granular with read, modify and delete attributes.
    A role without these attributes is considered to be granted them all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UserPrivileges]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, UserPrivileges]]:
    """Get definitions of user privileges

     In pfSense, the user privileges are applied to the user's login to the
    legacy user interface. When pfSense acts as a Multi-instance Management
    Controller, MIM privileges are defined by the group's name.

    When the Controller runs as a separate entity, group privileges are used
    as roles in Multi-instance management and define the entitlements of the
    user belonging to the group. Apart from the superuser (or admin) role,
    all roles can be made granular with read, modify and delete attributes.
    A role without these attributes is considered to be granted them all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UserPrivileges]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, UserPrivileges]]:
    """Get definitions of user privileges

     In pfSense, the user privileges are applied to the user's login to the
    legacy user interface. When pfSense acts as a Multi-instance Management
    Controller, MIM privileges are defined by the group's name.

    When the Controller runs as a separate entity, group privileges are used
    as roles in Multi-instance management and define the entitlements of the
    user belonging to the group. Apart from the superuser (or admin) role,
    all roles can be made granular with read, modify and delete attributes.
    A role without these attributes is considered to be granted them all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UserPrivileges]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
