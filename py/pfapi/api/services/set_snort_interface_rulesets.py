from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.snort_interface_rulesets_opt import SnortInterfaceRulesetsOpt
from ...models.snort_intf_rulesets import SnortIntfRulesets
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: SnortInterfaceRulesetsOpt,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/services/snort/intf/{id}/rules/rulesets".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SnortIntfRulesets | None:
    if response.status_code == 200:
        response_200 = SnortIntfRulesets.from_dict(response.json())

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
) -> Response[Error | SnortIntfRulesets]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SnortInterfaceRulesetsOpt,
) -> Response[Error | SnortIntfRulesets]:
    """Apply the named rulesets to the interface

     Set the interface configuration to use the specified rulesets.

    If Talos LightSPD rulesets are used, then the snort configuration will
    use the Lua scripts provided by the package, with overrides applied
    as required. All other rulesets are ignored.

    For other rulesets, select the rules file to apply.

    Note that when this API handler completes, a new Snort configuration
    will be generated for the interface and the snort Service is restarted
    (if it was running).

    Args:
        id (str):
        body (SnortInterfaceRulesetsOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortIntfRulesets]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SnortInterfaceRulesetsOpt,
) -> Error | SnortIntfRulesets | None:
    """Apply the named rulesets to the interface

     Set the interface configuration to use the specified rulesets.

    If Talos LightSPD rulesets are used, then the snort configuration will
    use the Lua scripts provided by the package, with overrides applied
    as required. All other rulesets are ignored.

    For other rulesets, select the rules file to apply.

    Note that when this API handler completes, a new Snort configuration
    will be generated for the interface and the snort Service is restarted
    (if it was running).

    Args:
        id (str):
        body (SnortInterfaceRulesetsOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortIntfRulesets
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SnortInterfaceRulesetsOpt,
) -> Response[Error | SnortIntfRulesets]:
    """Apply the named rulesets to the interface

     Set the interface configuration to use the specified rulesets.

    If Talos LightSPD rulesets are used, then the snort configuration will
    use the Lua scripts provided by the package, with overrides applied
    as required. All other rulesets are ignored.

    For other rulesets, select the rules file to apply.

    Note that when this API handler completes, a new Snort configuration
    will be generated for the interface and the snort Service is restarted
    (if it was running).

    Args:
        id (str):
        body (SnortInterfaceRulesetsOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SnortIntfRulesets]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SnortInterfaceRulesetsOpt,
) -> Error | SnortIntfRulesets | None:
    """Apply the named rulesets to the interface

     Set the interface configuration to use the specified rulesets.

    If Talos LightSPD rulesets are used, then the snort configuration will
    use the Lua scripts provided by the package, with overrides applied
    as required. All other rulesets are ignored.

    For other rulesets, select the rules file to apply.

    Note that when this API handler completes, a new Snort configuration
    will be generated for the interface and the snort Service is restarted
    (if it was running).

    Args:
        id (str):
        body (SnortInterfaceRulesetsOpt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SnortIntfRulesets
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
