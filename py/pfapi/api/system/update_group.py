from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.group_update_req import GroupUpdateReq
from ...models.user_groups import UserGroups
from ...types import Response


def _get_kwargs(
    groupname: str,
    *,
    body: GroupUpdateReq,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/system/users/group/{groupname}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UserGroups]]:
    if response.status_code == 200:
        response_200 = UserGroups.from_dict(response.json())

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
) -> Response[Union[Error, UserGroups]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    groupname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupUpdateReq,
) -> Response[Union[Error, UserGroups]]:
    """Update group

    Args:
        groupname (str):
        body (GroupUpdateReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UserGroups]]
    """

    kwargs = _get_kwargs(
        groupname=groupname,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    groupname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupUpdateReq,
) -> Optional[Union[Error, UserGroups]]:
    """Update group

    Args:
        groupname (str):
        body (GroupUpdateReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UserGroups]
    """

    return sync_detailed(
        groupname=groupname,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    groupname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupUpdateReq,
) -> Response[Union[Error, UserGroups]]:
    """Update group

    Args:
        groupname (str):
        body (GroupUpdateReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UserGroups]]
    """

    kwargs = _get_kwargs(
        groupname=groupname,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    groupname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupUpdateReq,
) -> Optional[Union[Error, UserGroups]]:
    """Update group

    Args:
        groupname (str):
        body (GroupUpdateReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UserGroups]
    """

    return (
        await asyncio_detailed(
            groupname=groupname,
            client=client,
            body=body,
        )
    ).parsed
