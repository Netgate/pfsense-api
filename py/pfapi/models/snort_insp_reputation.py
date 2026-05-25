from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspReputation")


@_attrs_define
class SnortInspReputation:
    """
    Attributes:
        blocklist (str | Unset): blocklist file name with IP lists
        list_dir (str | Unset): directory for IP lists and manifest file
        memcap (int | Unset): maximum total MB of memory allocated { 1:4095 }; default 500
        nested_ip (str | Unset): IP to use when there is IP encapsulation { inner|outer|all }; default inner
        priority (str | Unset): defines priority when there is a decision conflict during run-time { blocklist|allowlist
            }; default allowlist
        scan_local (bool | Unset): inspect local address defined in RFC 1918; default false
        allow (str | Unset): specify the meaning of allowlist { do_not_block|trust }; default do_not_block
        allowlist (str | Unset): allowlist file name with IP lists
    """

    blocklist: str | Unset = UNSET
    list_dir: str | Unset = UNSET
    memcap: int | Unset = UNSET
    nested_ip: str | Unset = UNSET
    priority: str | Unset = UNSET
    scan_local: bool | Unset = UNSET
    allow: str | Unset = UNSET
    allowlist: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocklist = self.blocklist

        list_dir = self.list_dir

        memcap = self.memcap

        nested_ip = self.nested_ip

        priority = self.priority

        scan_local = self.scan_local

        allow = self.allow

        allowlist = self.allowlist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blocklist is not UNSET:
            field_dict["blocklist"] = blocklist
        if list_dir is not UNSET:
            field_dict["list_dir"] = list_dir
        if memcap is not UNSET:
            field_dict["memcap"] = memcap
        if nested_ip is not UNSET:
            field_dict["nested_ip"] = nested_ip
        if priority is not UNSET:
            field_dict["priority"] = priority
        if scan_local is not UNSET:
            field_dict["scan_local"] = scan_local
        if allow is not UNSET:
            field_dict["allow"] = allow
        if allowlist is not UNSET:
            field_dict["allowlist"] = allowlist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blocklist = d.pop("blocklist", UNSET)

        list_dir = d.pop("list_dir", UNSET)

        memcap = d.pop("memcap", UNSET)

        nested_ip = d.pop("nested_ip", UNSET)

        priority = d.pop("priority", UNSET)

        scan_local = d.pop("scan_local", UNSET)

        allow = d.pop("allow", UNSET)

        allowlist = d.pop("allowlist", UNSET)

        snort_insp_reputation = cls(
            blocklist=blocklist,
            list_dir=list_dir,
            memcap=memcap,
            nested_ip=nested_ip,
            priority=priority,
            scan_local=scan_local,
            allow=allow,
            allowlist=allowlist,
        )

        snort_insp_reputation.additional_properties = d
        return snort_insp_reputation

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
