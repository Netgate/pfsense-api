from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.snort_pass_list import SnortPassList
from ...models.snort_pass_lists import SnortPassLists
from ...types import Response


def _get_kwargs(
    *,
    body: SnortPassList,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/services/snort/passlist",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SnortPassLists | None:
    if response.status_code == 200:
        response_200 = SnortPassLists.from_dict(response.json())

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
) -> Response[Error | SnortPassLists]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SnortPassList,
) -> Response[Error | SnortPassLists]:
    """Add Snort pass list.

     Pass Lists are lists of IP addresses that Snort should never block.
    Pass lists can be created and managed on the Pass Lists tab.
    When an IP address is listed on a Pass List, Snort will never
    insert a block on that address even when malicious traffic is detected.

    When a pass list is applied to an interface configuration, it will white
    list those addresses in Snort as part of the reputation allowlist.

    Args:
        body (SnortPassList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortPassLists]
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
    client: AuthenticatedClient | Client,
    body: SnortPassList,
) -> Error | SnortPassLists | None:
    """Add Snort pass list.

     Pass Lists are lists of IP addresses that Snort should never block.
    Pass lists can be created and managed on the Pass Lists tab.
    When an IP address is listed on a Pass List, Snort will never
    insert a block on that address even when malicious traffic is detected.

    When a pass list is applied to an interface configuration, it will white
    list those addresses in Snort as part of the reputation allowlist.

    Args:
        body (SnortPassList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortPassLists
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SnortPassList,
) -> Response[Error | SnortPassLists]:
    """Add Snort pass list.

     Pass Lists are lists of IP addresses that Snort should never block.
    Pass lists can be created and managed on the Pass Lists tab.
    When an IP address is listed on a Pass List, Snort will never
    insert a block on that address even when malicious traffic is detected.

    When a pass list is applied to an interface configuration, it will white
    list those addresses in Snort as part of the reputation allowlist.

    Args:
        body (SnortPassList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortPassLists]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SnortPassList,
) -> Error | SnortPassLists | None:
    """Add Snort pass list.

     Pass Lists are lists of IP addresses that Snort should never block.
    Pass lists can be created and managed on the Pass Lists tab.
    When an IP address is listed on a Pass List, Snort will never
    insert a block on that address even when malicious traffic is detected.

    When a pass list is applied to an interface configuration, it will white
    list those addresses in Snort as part of the reputation allowlist.

    Args:
        body (SnortPassList):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortPassLists
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
