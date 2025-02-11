from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        logfile (str):
        filter_summary (FilterLogSummary): Summary of filter log entries. These are dictionaries of keys to counts
        alerts (Result):
        logs (Union[Unset, List['StdLog']]):
        filter_logs (Union[Unset, List['FilterLog']]):
    """

    logfile: str
    filter_summary: "FilterLogSummary"
    alerts: "Result"
    logs: Union[Unset, List["StdLog"]] = UNSET
    filter_logs: Union[Unset, List["FilterLog"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logfile = self.logfile

        filter_summary = self.filter_summary.to_dict()

        alerts = self.alerts.to_dict()

        logs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        filter_logs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filter_logs, Unset):
            filter_logs = []
            for filter_logs_item_data in self.filter_logs:
                filter_logs_item = filter_logs_item_data.to_dict()
                filter_logs.append(filter_logs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logfile": logfile,
                "filter_summary": filter_summary,
                "alerts": alerts,
            }
        )
        if logs is not UNSET:
            field_dict["logs"] = logs
        if filter_logs is not UNSET:
            field_dict["filter_logs"] = filter_logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_log import FilterLog
        from ..models.filter_log_summary import FilterLogSummary
        from ..models.result import Result
        from ..models.std_log import StdLog

        d = src_dict.copy()
        logfile = d.pop("logfile")

        filter_summary = FilterLogSummary.from_dict(d.pop("filter_summary"))

        alerts = Result.from_dict(d.pop("alerts"))

        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = StdLog.from_dict(logs_item_data)

            logs.append(logs_item)

        filter_logs = []
        _filter_logs = d.pop("filter_logs", UNSET)
        for filter_logs_item_data in _filter_logs or []:
            filter_logs_item = FilterLog.from_dict(filter_logs_item_data)

            filter_logs.append(filter_logs_item)

        std_logs = cls(
            logfile=logfile,
            filter_summary=filter_summary,
            alerts=alerts,
            logs=logs,
            filter_logs=filter_logs,
        )

        std_logs.additional_properties = d
        return std_logs

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
