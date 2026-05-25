from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortReputationConfig")


@_attrs_define
class SnortReputationConfig:
    """
    Attributes:
        enable (bool | Unset): enable reputation list on the interface
        max_mem_mb (int | Unset): maximum memory (in MB) for IP reputation list, default 500
        scan_local (bool | Unset): scan RFC1918 (private LAN) addresses
        nested_ip (str | Unset): which IP address to use for allowlist/blocklist matching of encapsulated IPs - inner,
            outer, or all
        priority_allowlist (bool | Unset): prioritize allowlist (default:true) or blocklist
        allowlist_trust (bool | Unset): unblock (default:false) address for further inspection or trust address
        blocklist_names (list[str] | Unset):
        allowlist_names (list[str] | Unset):
    """

    enable: bool | Unset = UNSET
    max_mem_mb: int | Unset = UNSET
    scan_local: bool | Unset = UNSET
    nested_ip: str | Unset = UNSET
    priority_allowlist: bool | Unset = UNSET
    allowlist_trust: bool | Unset = UNSET
    blocklist_names: list[str] | Unset = UNSET
    allowlist_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        max_mem_mb = self.max_mem_mb

        scan_local = self.scan_local

        nested_ip = self.nested_ip

        priority_allowlist = self.priority_allowlist

        allowlist_trust = self.allowlist_trust

        blocklist_names: list[str] | Unset = UNSET
        if not isinstance(self.blocklist_names, Unset):
            blocklist_names = self.blocklist_names

        allowlist_names: list[str] | Unset = UNSET
        if not isinstance(self.allowlist_names, Unset):
            allowlist_names = self.allowlist_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if max_mem_mb is not UNSET:
            field_dict["max_mem_mb"] = max_mem_mb
        if scan_local is not UNSET:
            field_dict["scan_local"] = scan_local
        if nested_ip is not UNSET:
            field_dict["nested_ip"] = nested_ip
        if priority_allowlist is not UNSET:
            field_dict["priority_allowlist"] = priority_allowlist
        if allowlist_trust is not UNSET:
            field_dict["allowlist_trust"] = allowlist_trust
        if blocklist_names is not UNSET:
            field_dict["blocklist_names"] = blocklist_names
        if allowlist_names is not UNSET:
            field_dict["allowlist_names"] = allowlist_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        max_mem_mb = d.pop("max_mem_mb", UNSET)

        scan_local = d.pop("scan_local", UNSET)

        nested_ip = d.pop("nested_ip", UNSET)

        priority_allowlist = d.pop("priority_allowlist", UNSET)

        allowlist_trust = d.pop("allowlist_trust", UNSET)

        blocklist_names = cast(list[str], d.pop("blocklist_names", UNSET))

        allowlist_names = cast(list[str], d.pop("allowlist_names", UNSET))

        snort_reputation_config = cls(
            enable=enable,
            max_mem_mb=max_mem_mb,
            scan_local=scan_local,
            nested_ip=nested_ip,
            priority_allowlist=priority_allowlist,
            allowlist_trust=allowlist_trust,
            blocklist_names=blocklist_names,
            allowlist_names=allowlist_names,
        )

        snort_reputation_config.additional_properties = d
        return snort_reputation_config

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
