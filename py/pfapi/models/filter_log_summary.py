from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        total_records (int | Unset):
        actions (FilterLogSummaryActions | Unset):
        interfaces (FilterLogSummaryInterfaces | Unset):
        protocols (FilterLogSummaryProtocols | Unset):
        src_ips (FilterLogSummarySrcIps | Unset):
        dest_ips (FilterLogSummaryDestIps | Unset):
        src_ports (FilterLogSummarySrcPorts | Unset):
        dest_ports (FilterLogSummaryDestPorts | Unset):
        tracker_hits (FilterLogSummaryTrackerHits | Unset):
    """

    total_records: int | Unset = UNSET
    actions: FilterLogSummaryActions | Unset = UNSET
    interfaces: FilterLogSummaryInterfaces | Unset = UNSET
    protocols: FilterLogSummaryProtocols | Unset = UNSET
    src_ips: FilterLogSummarySrcIps | Unset = UNSET
    dest_ips: FilterLogSummaryDestIps | Unset = UNSET
    src_ports: FilterLogSummarySrcPorts | Unset = UNSET
    dest_ports: FilterLogSummaryDestPorts | Unset = UNSET
    tracker_hits: FilterLogSummaryTrackerHits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_records = self.total_records

        actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        interfaces: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces.to_dict()

        protocols: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protocols, Unset):
            protocols = self.protocols.to_dict()

        src_ips: dict[str, Any] | Unset = UNSET
        if not isinstance(self.src_ips, Unset):
            src_ips = self.src_ips.to_dict()

        dest_ips: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dest_ips, Unset):
            dest_ips = self.dest_ips.to_dict()

        src_ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.src_ports, Unset):
            src_ports = self.src_ports.to_dict()

        dest_ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dest_ports, Unset):
            dest_ports = self.dest_ports.to_dict()

        tracker_hits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tracker_hits, Unset):
            tracker_hits = self.tracker_hits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_records is not UNSET:
            field_dict["total_records"] = total_records
        if actions is not UNSET:
            field_dict["actions"] = actions
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if protocols is not UNSET:
            field_dict["protocols"] = protocols
        if src_ips is not UNSET:
            field_dict["src_ips"] = src_ips
        if dest_ips is not UNSET:
            field_dict["dest_ips"] = dest_ips
        if src_ports is not UNSET:
            field_dict["src_ports"] = src_ports
        if dest_ports is not UNSET:
            field_dict["dest_ports"] = dest_ports
        if tracker_hits is not UNSET:
            field_dict["tracker_hits"] = tracker_hits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_log_summary_actions import FilterLogSummaryActions
        from ..models.filter_log_summary_dest_ips import FilterLogSummaryDestIps
        from ..models.filter_log_summary_dest_ports import FilterLogSummaryDestPorts
        from ..models.filter_log_summary_interfaces import FilterLogSummaryInterfaces
        from ..models.filter_log_summary_protocols import FilterLogSummaryProtocols
        from ..models.filter_log_summary_src_ips import FilterLogSummarySrcIps
        from ..models.filter_log_summary_src_ports import FilterLogSummarySrcPorts
        from ..models.filter_log_summary_tracker_hits import FilterLogSummaryTrackerHits

        d = dict(src_dict)
        total_records = d.pop("total_records", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: FilterLogSummaryActions | Unset
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = FilterLogSummaryActions.from_dict(_actions)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: FilterLogSummaryInterfaces | Unset
        if isinstance(_interfaces, Unset):
            interfaces = UNSET
        else:
            interfaces = FilterLogSummaryInterfaces.from_dict(_interfaces)

        _protocols = d.pop("protocols", UNSET)
        protocols: FilterLogSummaryProtocols | Unset
        if isinstance(_protocols, Unset):
            protocols = UNSET
        else:
            protocols = FilterLogSummaryProtocols.from_dict(_protocols)

        _src_ips = d.pop("src_ips", UNSET)
        src_ips: FilterLogSummarySrcIps | Unset
        if isinstance(_src_ips, Unset):
            src_ips = UNSET
        else:
            src_ips = FilterLogSummarySrcIps.from_dict(_src_ips)

        _dest_ips = d.pop("dest_ips", UNSET)
        dest_ips: FilterLogSummaryDestIps | Unset
        if isinstance(_dest_ips, Unset):
            dest_ips = UNSET
        else:
            dest_ips = FilterLogSummaryDestIps.from_dict(_dest_ips)

        _src_ports = d.pop("src_ports", UNSET)
        src_ports: FilterLogSummarySrcPorts | Unset
        if isinstance(_src_ports, Unset):
            src_ports = UNSET
        else:
            src_ports = FilterLogSummarySrcPorts.from_dict(_src_ports)

        _dest_ports = d.pop("dest_ports", UNSET)
        dest_ports: FilterLogSummaryDestPorts | Unset
        if isinstance(_dest_ports, Unset):
            dest_ports = UNSET
        else:
            dest_ports = FilterLogSummaryDestPorts.from_dict(_dest_ports)

        _tracker_hits = d.pop("tracker_hits", UNSET)
        tracker_hits: FilterLogSummaryTrackerHits | Unset
        if isinstance(_tracker_hits, Unset):
            tracker_hits = UNSET
        else:
            tracker_hits = FilterLogSummaryTrackerHits.from_dict(_tracker_hits)

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
