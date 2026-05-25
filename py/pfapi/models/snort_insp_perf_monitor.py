from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_perf_monitor_modules import SnortInspPerfMonitorModules


T = TypeVar("T", bound="SnortInspPerfMonitor")


@_attrs_define
class SnortInspPerfMonitor:
    """
    Attributes:
        base (bool | Unset): enable base statistics; default true
        cpu (bool | Unset): enable cpu statistics; default false
        flow (bool | Unset): enable traffic statistics; default false
        flow_ip (bool | Unset): enable statistics on host pairs; default false
        flow_ip_all (bool | Unset): enable every stat of flow_ip profiling on host pairs; default false
        packets (int | Unset): minimum packets to report { 0:max32 }; default 10000
        seconds (int | Unset): report interval { 0:max32 }; default 60
        flow_ip_memcap (int | Unset): maximum memory in bytes for flow tracking { 236:maxSZ }; default 52428800
        max_file_size (int | Unset): files will be rolled over if they exceed this size { 4096:max53 }; default
            1073741824
        flow_ports (int | Unset): maximum ports to track { 0:65535 }; default 1023
        output (str | Unset): output location for stats { file | console }; default file
        modules (list[SnortInspPerfMonitorModules] | Unset):
        format_ (str | Unset): output format for stats { csv | text | json }; default csv
        summary (bool | Unset): output summary at shutdown; default false
    """

    base: bool | Unset = UNSET
    cpu: bool | Unset = UNSET
    flow: bool | Unset = UNSET
    flow_ip: bool | Unset = UNSET
    flow_ip_all: bool | Unset = UNSET
    packets: int | Unset = UNSET
    seconds: int | Unset = UNSET
    flow_ip_memcap: int | Unset = UNSET
    max_file_size: int | Unset = UNSET
    flow_ports: int | Unset = UNSET
    output: str | Unset = UNSET
    modules: list[SnortInspPerfMonitorModules] | Unset = UNSET
    format_: str | Unset = UNSET
    summary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base

        cpu = self.cpu

        flow = self.flow

        flow_ip = self.flow_ip

        flow_ip_all = self.flow_ip_all

        packets = self.packets

        seconds = self.seconds

        flow_ip_memcap = self.flow_ip_memcap

        max_file_size = self.max_file_size

        flow_ports = self.flow_ports

        output = self.output

        modules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = []
            for modules_item_data in self.modules:
                modules_item = modules_item_data.to_dict()
                modules.append(modules_item)

        format_ = self.format_

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if flow is not UNSET:
            field_dict["flow"] = flow
        if flow_ip is not UNSET:
            field_dict["flow_ip"] = flow_ip
        if flow_ip_all is not UNSET:
            field_dict["flow_ip_all"] = flow_ip_all
        if packets is not UNSET:
            field_dict["packets"] = packets
        if seconds is not UNSET:
            field_dict["seconds"] = seconds
        if flow_ip_memcap is not UNSET:
            field_dict["flow_ip_memcap"] = flow_ip_memcap
        if max_file_size is not UNSET:
            field_dict["max_file_size"] = max_file_size
        if flow_ports is not UNSET:
            field_dict["flow_ports"] = flow_ports
        if output is not UNSET:
            field_dict["output"] = output
        if modules is not UNSET:
            field_dict["modules"] = modules
        if format_ is not UNSET:
            field_dict["format"] = format_
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_perf_monitor_modules import SnortInspPerfMonitorModules

        d = dict(src_dict)
        base = d.pop("base", UNSET)

        cpu = d.pop("cpu", UNSET)

        flow = d.pop("flow", UNSET)

        flow_ip = d.pop("flow_ip", UNSET)

        flow_ip_all = d.pop("flow_ip_all", UNSET)

        packets = d.pop("packets", UNSET)

        seconds = d.pop("seconds", UNSET)

        flow_ip_memcap = d.pop("flow_ip_memcap", UNSET)

        max_file_size = d.pop("max_file_size", UNSET)

        flow_ports = d.pop("flow_ports", UNSET)

        output = d.pop("output", UNSET)

        _modules = d.pop("modules", UNSET)
        modules: list[SnortInspPerfMonitorModules] | Unset = UNSET
        if _modules is not UNSET:
            modules = []
            for modules_item_data in _modules:
                modules_item = SnortInspPerfMonitorModules.from_dict(modules_item_data)

                modules.append(modules_item)

        format_ = d.pop("format", UNSET)

        summary = d.pop("summary", UNSET)

        snort_insp_perf_monitor = cls(
            base=base,
            cpu=cpu,
            flow=flow,
            flow_ip=flow_ip,
            flow_ip_all=flow_ip_all,
            packets=packets,
            seconds=seconds,
            flow_ip_memcap=flow_ip_memcap,
            max_file_size=max_file_size,
            flow_ports=flow_ports,
            output=output,
            modules=modules,
            format_=format_,
            summary=summary,
        )

        snort_insp_perf_monitor.additional_properties = d
        return snort_insp_perf_monitor

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
