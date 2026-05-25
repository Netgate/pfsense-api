from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspArpSpoofHosts")


@_attrs_define
class SnortInspArpSpoofHosts:
    """
    Attributes:
        ip (str | Unset): host ip address
        mac (str | Unset): host mac address
    """

    ip: str | Unset = UNSET
    mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        mac = self.mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mac is not UNSET:
            field_dict["mac"] = mac

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ip = d.pop("ip", UNSET)

        mac = d.pop("mac", UNSET)

        snort_insp_arp_spoof_hosts = cls(
            ip=ip,
            mac=mac,
        )

        snort_insp_arp_spoof_hosts.additional_properties = d
        return snort_insp_arp_spoof_hosts

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
