from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.filter_log_summary_actions import FilterLogSummaryActions
    from ..models.filter_log_summary_dest_ips import FilterLogSummaryDestIps
    from ..models.filter_log_summary_dest_ports import FilterLogSummaryDestPorts
    from ..models.filter_log_summary_interfaces import FilterLogSummaryInterfaces
    from ..models.filter_log_summary_protocols import FilterLogSummaryProtocols
    from ..models.filter_log_summary_src_ips import FilterLogSummarySrcIps
    from ..models.filter_log_summary_src_ports import FilterLogSummarySrcPorts
    from ..models.filter_log_summary_tracker_hits import FilterLogSummaryTrackerHits


T = TypeVar("T", bound="FilterLogSummary")


@_attrs_define
class FilterLogSummary:
    """Summary of filter log entries. These are dictionaries of keys to counts

    Attributes:
        total_records (int):
        actions (FilterLogSummaryActions):
        interfaces (FilterLogSummaryInterfaces):
        protocols (FilterLogSummaryProtocols):
        src_ips (FilterLogSummarySrcIps):
        dest_ips (FilterLogSummaryDestIps):
        src_ports (FilterLogSummarySrcPorts):
        dest_ports (FilterLogSummaryDestPorts):
        tracker_hits (FilterLogSummaryTrackerHits):
    """

    total_records: int
    actions: "FilterLogSummaryActions"
    interfaces: "FilterLogSummaryInterfaces"
    protocols: "FilterLogSummaryProtocols"
    src_ips: "FilterLogSummarySrcIps"
    dest_ips: "FilterLogSummaryDestIps"
    src_ports: "FilterLogSummarySrcPorts"
    dest_ports: "FilterLogSummaryDestPorts"
    tracker_hits: "FilterLogSummaryTrackerHits"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_records = self.total_records

        actions = self.actions.to_dict()

        interfaces = self.interfaces.to_dict()

        protocols = self.protocols.to_dict()

        src_ips = self.src_ips.to_dict()

        dest_ips = self.dest_ips.to_dict()

        src_ports = self.src_ports.to_dict()

        dest_ports = self.dest_ports.to_dict()

        tracker_hits = self.tracker_hits.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_records": total_records,
                "actions": actions,
                "interfaces": interfaces,
                "protocols": protocols,
                "src_ips": src_ips,
                "dest_ips": dest_ips,
                "src_ports": src_ports,
                "dest_ports": dest_ports,
                "tracker_hits": tracker_hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_log_summary_actions import FilterLogSummaryActions
        from ..models.filter_log_summary_dest_ips import FilterLogSummaryDestIps
        from ..models.filter_log_summary_dest_ports import FilterLogSummaryDestPorts
        from ..models.filter_log_summary_interfaces import FilterLogSummaryInterfaces
        from ..models.filter_log_summary_protocols import FilterLogSummaryProtocols
        from ..models.filter_log_summary_src_ips import FilterLogSummarySrcIps
        from ..models.filter_log_summary_src_ports import FilterLogSummarySrcPorts
        from ..models.filter_log_summary_tracker_hits import FilterLogSummaryTrackerHits

        d = src_dict.copy()
        total_records = d.pop("total_records")

        actions = FilterLogSummaryActions.from_dict(d.pop("actions"))

        interfaces = FilterLogSummaryInterfaces.from_dict(d.pop("interfaces"))

        protocols = FilterLogSummaryProtocols.from_dict(d.pop("protocols"))

        src_ips = FilterLogSummarySrcIps.from_dict(d.pop("src_ips"))

        dest_ips = FilterLogSummaryDestIps.from_dict(d.pop("dest_ips"))

        src_ports = FilterLogSummarySrcPorts.from_dict(d.pop("src_ports"))

        dest_ports = FilterLogSummaryDestPorts.from_dict(d.pop("dest_ports"))

        tracker_hits = FilterLogSummaryTrackerHits.from_dict(d.pop("tracker_hits"))

        filter_log_summary = cls(
            total_records=total_records,
            actions=actions,
            interfaces=interfaces,
            protocols=protocols,
            src_ips=src_ips,
            dest_ips=dest_ips,
            src_ports=src_ports,
            dest_ports=dest_ports,
            tracker_hits=tracker_hits,
        )

        filter_log_summary.additional_properties = d
        return filter_log_summary

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
