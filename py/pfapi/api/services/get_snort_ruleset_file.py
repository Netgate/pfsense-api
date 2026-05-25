from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.snort_rule_file_contents import SnortRuleFileContents
from ...types import Response


def _get_kwargs(
    name: str,
    file: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/services/snort/rules/{name}/{file}".format(
            name=quote(str(name), safe=""),
            file=quote(str(file), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SnortRuleFileContents | None:
    if response.status_code == 200:
        response_200 = SnortRuleFileContents.from_dict(response.json())

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
) -> Response[Error | SnortRuleFileContents]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | SnortRuleFileContents]:
    """Get the original contents of the specified file in the ruleset

     Obtain the contents of the specified file in the ruleset. This is intended for inspecting scripts
    provided by it.

    Args:
        name (str):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortRuleFileContents]
    """

    kwargs = _get_kwargs(
        name=name,
        file=file,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | SnortRuleFileContents | None:
    """Get the original contents of the specified file in the ruleset

     Obtain the contents of the specified file in the ruleset. This is intended for inspecting scripts
    provided by it.

    Args:
        name (str):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortRuleFileContents
    """

    return sync_detailed(
        name=name,
        file=file,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | SnortRuleFileContents]:
    """Get the original contents of the specified file in the ruleset

     Obtain the contents of the specified file in the ruleset. This is intended for inspecting scripts
    provided by it.

    Args:
        name (str):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortRuleFileContents]
    """

    kwargs = _get_kwargs(
        name=name,
        file=file,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | SnortRuleFileContents | None:
    """Get the original contents of the specified file in the ruleset

     Obtain the contents of the specified file in the ruleset. This is intended for inspecting scripts
    provided by it.

    Args:
        name (str):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortRuleFileContents
    """

    return (
        await asyncio_detailed(
            name=name,
            file=file,
            client=client,
        )
    ).parsed
