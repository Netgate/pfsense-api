from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_log import FilterLog
    from ..models.filter_log_summary import FilterLogSummary
    from ..models.result import Result
    from ..models.std_log import StdLog


T = TypeVar("T", bound="StdLogs")


@_attrs_define
class StdLogs:
    """
    Attributes:
        logfile (str | Unset):
        logs (list[StdLog] | Unset):
        filter_logs (list[FilterLog] | Unset):
        filter_summary (FilterLogSummary | Unset): Summary of filter log entries. These are dictionaries of keys to
            counts
        alerts (Result | Unset):
    """

    logfile: str | Unset = UNSET
    logs: list[StdLog] | Unset = UNSET
    filter_logs: list[FilterLog] | Unset = UNSET
    filter_summary: FilterLogSummary | Unset = UNSET
    alerts: Result | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logfile = self.logfile

        logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        filter_logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_logs, Unset):
            filter_logs = []
            for filter_logs_item_data in self.filter_logs:
                filter_logs_item = filter_logs_item_data.to_dict()
                filter_logs.append(filter_logs_item)

        filter_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_summary, Unset):
            filter_summary = self.filter_summary.to_dict()

        alerts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = self.alerts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logfile is not UNSET:
            field_dict["logfile"] = logfile
        if logs is not UNSET:
            field_dict["logs"] = logs
        if filter_logs is not UNSET:
            field_dict["filter_logs"] = filter_logs
        if filter_summary is not UNSET:
            field_dict["filter_summary"] = filter_summary
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_log import FilterLog
        from ..models.filter_log_summary import FilterLogSummary
        from ..models.result import Result
        from ..models.std_log import StdLog

        d = dict(src_dict)
        logfile = d.pop("logfile", UNSET)

        _logs = d.pop("logs", UNSET)
        logs: list[StdLog] | Unset = UNSET
        if _logs is not UNSET:
            logs = []
            for logs_item_data in _logs:
                logs_item = StdLog.from_dict(logs_item_data)

                logs.append(logs_item)

        _filter_logs = d.pop("filter_logs", UNSET)
        filter_logs: list[FilterLog] | Unset = UNSET
        if _filter_logs is not UNSET:
            filter_logs = []
            for filter_logs_item_data in _filter_logs:
                filter_logs_item = FilterLog.from_dict(filter_logs_item_data)

                filter_logs.append(filter_logs_item)

        _filter_summary = d.pop("filter_summary", UNSET)
        filter_summary: FilterLogSummary | Unset
        if isinstance(_filter_summary, Unset):
            filter_summary = UNSET
        else:
            filter_summary = FilterLogSummary.from_dict(_filter_summary)

        _alerts = d.pop("alerts", UNSET)
        alerts: Result | Unset
        if isinstance(_alerts, Unset):
            alerts = UNSET
        else:
            alerts = Result.from_dict(_alerts)

        std_logs = cls(
            logfile=logfile,
            logs=logs,
            filter_logs=filter_logs,
            filter_summary=filter_summary,
            alerts=alerts,
        )

        std_logs.additional_properties = d
        return std_logs

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
