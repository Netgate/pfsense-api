from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspPortScanTcpSweep")


@_attrs_define
class SnortInspPortScanTcpSweep:
    """
    Attributes:
        scans (int | Unset): scan attempts { 0:65535 }; default 100
        rejects (int | Unset): scan attempts with negative response { 0:65535 }; default 15
        nets (int | Unset): number of times address changed from prior attempt { 0:65535 }; default 25
        ports (int | Unset): number of times port (or proto) changed from prior attempt { 0:65535 }; default 25
    """

    scans: int | Unset = UNSET
    rejects: int | Unset = UNSET
    nets: int | Unset = UNSET
    ports: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scans = self.scans

        rejects = self.rejects

        nets = self.nets

        ports = self.ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scans is not UNSET:
            field_dict["scans"] = scans
        if rejects is not UNSET:
            field_dict["rejects"] = rejects
        if nets is not UNSET:
            field_dict["nets"] = nets
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scans = d.pop("scans", UNSET)

        rejects = d.pop("rejects", UNSET)

        nets = d.pop("nets", UNSET)

        ports = d.pop("ports", UNSET)

        snort_insp_port_scan_tcp_sweep = cls(
            scans=scans,
            rejects=rejects,
            nets=nets,
            ports=ports,
        )

        snort_insp_port_scan_tcp_sweep.additional_properties = d
        return snort_insp_port_scan_tcp_sweep

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
