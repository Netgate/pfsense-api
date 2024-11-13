from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.std_logs import StdLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    filename: str,
    *,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
    summary: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params["summary"] = summary

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/system/logs/{filename}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, StdLogs]]:
    if response.status_code == 200:
        response_200 = StdLogs.from_dict(response.json())

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
) -> Response[Union[Error, StdLogs]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
    summary: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, StdLogs]]:
    r"""Get log file contents

     Regular log files are returned as a list of records in StdLogs.Logs. For
    firewall logs (filename being \"filter\" or \"firewall\"), the log records
    are returned in StdLogs.filter_logs. If the query string \"summary=true\" is
    provided, then the firewall log summary is returned in StdLogs.filter_summary
    with dictionaries of each category with its tallied values.

    Args:
        filename (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StdLogs]]
    """

    kwargs = _get_kwargs(
        filename=filename,
        start=start,
        end=end,
        summary=summary,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
    summary: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, StdLogs]]:
    r"""Get log file contents

     Regular log files are returned as a list of records in StdLogs.Logs. For
    firewall logs (filename being \"filter\" or \"firewall\"), the log records
    are returned in StdLogs.filter_logs. If the query string \"summary=true\" is
    provided, then the firewall log summary is returned in StdLogs.filter_summary
    with dictionaries of each category with its tallied values.

    Args:
        filename (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StdLogs]
    """

    return sync_detailed(
        filename=filename,
        client=client,
        start=start,
        end=end,
        summary=summary,
    ).parsed


async def asyncio_detailed(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
    summary: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, StdLogs]]:
    r"""Get log file contents

     Regular log files are returned as a list of records in StdLogs.Logs. For
    firewall logs (filename being \"filter\" or \"firewall\"), the log records
    are returned in StdLogs.filter_logs. If the query string \"summary=true\" is
    provided, then the firewall log summary is returned in StdLogs.filter_summary
    with dictionaries of each category with its tallied values.

    Args:
        filename (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StdLogs]]
    """

    kwargs = _get_kwargs(
        filename=filename,
        start=start,
        end=end,
        summary=summary,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,
    summary: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, StdLogs]]:
    r"""Get log file contents

     Regular log files are returned as a list of records in StdLogs.Logs. For
    firewall logs (filename being \"filter\" or \"firewall\"), the log records
    are returned in StdLogs.filter_logs. If the query string \"summary=true\" is
    provided, then the firewall log summary is returned in StdLogs.filter_summary
    with dictionaries of each category with its tallied values.

    Args:
        filename (str):
        start (Union[Unset, str]):
        end (Union[Unset, str]):
        summary (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StdLogs]
    """

    return (
        await asyncio_detailed(
            filename=filename,
            client=client,
            start=start,
            end=end,
            summary=summary,
        )
    ).parsed
