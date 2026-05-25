from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disk_usage import DiskUsage


T = TypeVar("T", bound="SysinfoTelemetry")


@_attrs_define
class SysinfoTelemetry:
    """Compact, frequently-pushed resource telemetry

    Attributes:
        cpu_load (int | Unset): CPU usage percentage (0-100)
        mem_total (int | Unset):
        mem_used (int | Unset):
        loadavg (list[int] | Unset):
        disks (list[DiskUsage] | Unset):
    """

    cpu_load: int | Unset = UNSET
    mem_total: int | Unset = UNSET
    mem_used: int | Unset = UNSET
    loadavg: list[int] | Unset = UNSET
    disks: list[DiskUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_load = self.cpu_load

        mem_total = self.mem_total

        mem_used = self.mem_used

        loadavg: list[int] | Unset = UNSET
        if not isinstance(self.loadavg, Unset):
            loadavg = self.loadavg

        disks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disks, Unset):
            disks = []
            for disks_item_data in self.disks:
                disks_item = disks_item_data.to_dict()
                disks.append(disks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_load is not UNSET:
            field_dict["cpu_load"] = cpu_load
        if mem_total is not UNSET:
            field_dict["mem_total"] = mem_total
        if mem_used is not UNSET:
            field_dict["mem_used"] = mem_used
        if loadavg is not UNSET:
            field_dict["loadavg"] = loadavg
        if disks is not UNSET:
            field_dict["disks"] = disks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disk_usage import DiskUsage

        d = dict(src_dict)
        cpu_load = d.pop("cpu_load", UNSET)

        mem_total = d.pop("mem_total", UNSET)

        mem_used = d.pop("mem_used", UNSET)

        loadavg = cast(list[int], d.pop("loadavg", UNSET))

        _disks = d.pop("disks", UNSET)
        disks: list[DiskUsage] | Unset = UNSET
        if _disks is not UNSET:
            disks = []
            for disks_item_data in _disks:
                disks_item = DiskUsage.from_dict(disks_item_data)

                disks.append(disks_item)

        sysinfo_telemetry = cls(
            cpu_load=cpu_load,
            mem_total=mem_total,
            mem_used=mem_used,
            loadavg=loadavg,
            disks=disks,
        )

        sysinfo_telemetry.additional_properties = d
        return sysinfo_telemetry

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
