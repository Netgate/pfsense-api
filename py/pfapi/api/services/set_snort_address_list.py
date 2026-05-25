from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.result import Result
from ...models.set_snort_address_list_body import SetSnortAddressListBody
from ...types import Response


def _get_kwargs(
    *,
    body: SetSnortAddressListBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/services/snort/addresses",
    }

    _kwargs["files"] = body.to_multipart()

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
    *,
    client: AuthenticatedClient | Client,
    body: SetSnortAddressListBody,
) -> Response[Error | Result]:
    """Add or update the list of snort addresses

     Set the list of addresses with the file contents specified.
    If the file already exists, it will be overwritten.

    The request can be a SnortAddressList object, or a file upload
    where the filename is used for the address list.

    Multiple address lists may be uploaded at the same time using multiple
    addresslist parts.

    Args:
        body (SetSnortAddressListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
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
    body: SetSnortAddressListBody,
) -> Error | Result | None:
    """Add or update the list of snort addresses

     Set the list of addresses with the file contents specified.
    If the file already exists, it will be overwritten.

    The request can be a SnortAddressList object, or a file upload
    where the filename is used for the address list.

    Multiple address lists may be uploaded at the same time using multiple
    addresslist parts.

    Args:
        body (SetSnortAddressListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SetSnortAddressListBody,
) -> Response[Error | Result]:
    """Add or update the list of snort addresses

     Set the list of addresses with the file contents specified.
    If the file already exists, it will be overwritten.

    The request can be a SnortAddressList object, or a file upload
    where the filename is used for the address list.

    Multiple address lists may be uploaded at the same time using multiple
    addresslist parts.

    Args:
        body (SetSnortAddressListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Result]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SetSnortAddressListBody,
) -> Error | Result | None:
    """Add or update the list of snort addresses

     Set the list of addresses with the file contents specified.
    If the file already exists, it will be overwritten.

    The request can be a SnortAddressList object, or a file upload
    where the filename is used for the address list.

    Multiple address lists may be uploaded at the same time using multiple
    addresslist parts.

    Args:
        body (SetSnortAddressListBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Result
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
