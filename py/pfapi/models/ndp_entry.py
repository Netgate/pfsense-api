from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NDPEntry")


@_attrs_define
class NDPEntry:
    """
    Attributes:
        ipv6 (str | Unset):
        mac (str | Unset):
        iface (str | Unset):
        hostname (str | Unset):
        exp (str | Unset):
        status (str | Unset):
        flags (str | Unset):
    """

    ipv6: str | Unset = UNSET
    mac: str | Unset = UNSET
    iface: str | Unset = UNSET
    hostname: str | Unset = UNSET
    exp: str | Unset = UNSET
    status: str | Unset = UNSET
    flags: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv6 = self.ipv6

        mac = self.mac

        iface = self.iface

        hostname = self.hostname

        exp = self.exp

        status = self.status

        flags = self.flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if mac is not UNSET:
            field_dict["mac"] = mac
        if iface is not UNSET:
            field_dict["iface"] = iface
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if exp is not UNSET:
            field_dict["exp"] = exp
        if status is not UNSET:
            field_dict["status"] = status
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ipv6 = d.pop("ipv6", UNSET)

        mac = d.pop("mac", UNSET)

        iface = d.pop("iface", UNSET)

        hostname = d.pop("hostname", UNSET)

        exp = d.pop("exp", UNSET)

        status = d.pop("status", UNSET)

        flags = d.pop("flags", UNSET)

        ndp_entry = cls(
            ipv6=ipv6,
            mac=mac,
            iface=iface,
            hostname=hostname,
            exp=exp,
            status=status,
            flags=flags,
        )

        ndp_entry.additional_properties = d
        return ndp_entry

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
