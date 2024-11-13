from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.install_packages_opt import InstallPackagesOpt
from ...models.install_packages_response import InstallPackagesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: InstallPackagesOpt,
    chunked: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["chunked"] = chunked

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/system/package/install",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, InstallPackagesResponse]]:
    if response.status_code == 200:
        response_200 = InstallPackagesResponse.from_dict(response.json())

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
) -> Response[Union[Error, InstallPackagesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallPackagesOpt,
    chunked: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, InstallPackagesResponse]]:
    """Install package(s)

     Install specified list of packages. If chunked=true, then the progress of the installation is
    returned as chunks.

    Args:
        chunked (Union[Unset, bool]):
        body (InstallPackagesOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InstallPackagesResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        chunked=chunked,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallPackagesOpt,
    chunked: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, InstallPackagesResponse]]:
    """Install package(s)

     Install specified list of packages. If chunked=true, then the progress of the installation is
    returned as chunks.

    Args:
        chunked (Union[Unset, bool]):
        body (InstallPackagesOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, InstallPackagesResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        chunked=chunked,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallPackagesOpt,
    chunked: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, InstallPackagesResponse]]:
    """Install package(s)

     Install specified list of packages. If chunked=true, then the progress of the installation is
    returned as chunks.

    Args:
        chunked (Union[Unset, bool]):
        body (InstallPackagesOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, InstallPackagesResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        chunked=chunked,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallPackagesOpt,
    chunked: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, InstallPackagesResponse]]:
    """Install package(s)

     Install specified list of packages. If chunked=true, then the progress of the installation is
    returned as chunks.

    Args:
        chunked (Union[Unset, bool]):
        body (InstallPackagesOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, InstallPackagesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            chunked=chunked,
        )
    ).parsed
