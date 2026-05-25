from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.result import Result
from ...models.store_snort_ruleset_body import StoreSnortRulesetBody
from ...types import Response


def _get_kwargs(
    *,
    body: StoreSnortRulesetBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/services/snort/rules",
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
    body: StoreSnortRulesetBody,
) -> Response[Error | Result]:
    """Upload a rule set

     Upload the rule set, specifying a name to give to it. The contents can be a single
    .rules file or an archive containing a batch of rules. Archive contents
    will be inspected to locate .rules files in the following manner:

    - locating rules/includes.rules otherwise all rules/*.rules files
    - locating precompiled rules in so_rules/precompiled/<os>/*.so and so_rules/include.rules
      - these get added to ips.states
    - locating *-ips.states for IPS rules enablement

    The request can be a regular API call with SnortRulesUploadReq provided, or
    as a multi-part piece, with the SnortRulesUploadReq in the req section, and the
    archive or rules file in the rules section.

    How the upload request is handled:
    - if a file is sent, then it is processed immediately
    - if contents is provided, then it is parsed for ruleset validity and applied
    - otherwise if a URL is provided, then the ruleset is downloaded. If the same
      URL is specified again while the download is in progress, then Result will
      contain a message indicating that status.

    Args:
        body (StoreSnortRulesetBody):

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
    body: StoreSnortRulesetBody,
) -> Error | Result | None:
    """Upload a rule set

     Upload the rule set, specifying a name to give to it. The contents can be a single
    .rules file or an archive containing a batch of rules. Archive contents
    will be inspected to locate .rules files in the following manner:

    - locating rules/includes.rules otherwise all rules/*.rules files
    - locating precompiled rules in so_rules/precompiled/<os>/*.so and so_rules/include.rules
      - these get added to ips.states
    - locating *-ips.states for IPS rules enablement

    The request can be a regular API call with SnortRulesUploadReq provided, or
    as a multi-part piece, with the SnortRulesUploadReq in the req section, and the
    archive or rules file in the rules section.

    How the upload request is handled:
    - if a file is sent, then it is processed immediately
    - if contents is provided, then it is parsed for ruleset validity and applied
    - otherwise if a URL is provided, then the ruleset is downloaded. If the same
      URL is specified again while the download is in progress, then Result will
      contain a message indicating that status.

    Args:
        body (StoreSnortRulesetBody):

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
    body: StoreSnortRulesetBody,
) -> Response[Error | Result]:
    """Upload a rule set

     Upload the rule set, specifying a name to give to it. The contents can be a single
    .rules file or an archive containing a batch of rules. Archive contents
    will be inspected to locate .rules files in the following manner:

    - locating rules/includes.rules otherwise all rules/*.rules files
    - locating precompiled rules in so_rules/precompiled/<os>/*.so and so_rules/include.rules
      - these get added to ips.states
    - locating *-ips.states for IPS rules enablement

    The request can be a regular API call with SnortRulesUploadReq provided, or
    as a multi-part piece, with the SnortRulesUploadReq in the req section, and the
    archive or rules file in the rules section.

    How the upload request is handled:
    - if a file is sent, then it is processed immediately
    - if contents is provided, then it is parsed for ruleset validity and applied
    - otherwise if a URL is provided, then the ruleset is downloaded. If the same
      URL is specified again while the download is in progress, then Result will
      contain a message indicating that status.

    Args:
        body (StoreSnortRulesetBody):

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
    body: StoreSnortRulesetBody,
) -> Error | Result | None:
    """Upload a rule set

     Upload the rule set, specifying a name to give to it. The contents can be a single
    .rules file or an archive containing a batch of rules. Archive contents
    will be inspected to locate .rules files in the following manner:

    - locating rules/includes.rules otherwise all rules/*.rules files
    - locating precompiled rules in so_rules/precompiled/<os>/*.so and so_rules/include.rules
      - these get added to ips.states
    - locating *-ips.states for IPS rules enablement

    The request can be a regular API call with SnortRulesUploadReq provided, or
    as a multi-part piece, with the SnortRulesUploadReq in the req section, and the
    archive or rules file in the rules section.

    How the upload request is handled:
    - if a file is sent, then it is processed immediately
    - if contents is provided, then it is parsed for ruleset validity and applied
    - otherwise if a URL is provided, then the ruleset is downloaded. If the same
      URL is specified again while the download is in progress, then Result will
      contain a message indicating that status.

    Args:
        body (StoreSnortRulesetBody):

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
