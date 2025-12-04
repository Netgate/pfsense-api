from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArpTableEntry")


@_attrs_define
class ArpTableEntry:
    """
    Attributes:
        ip (str | Unset):
        mac (str | Unset):
        interface (str | Unset):
        expires (str | Unset):
        type_ (str | Unset):
        dnsresolve (str | Unset):
    """

    ip: str | Unset = UNSET
    mac: str | Unset = UNSET
    interface: str | Unset = UNSET
    expires: str | Unset = UNSET
    type_: str | Unset = UNSET
    dnsresolve: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        mac = self.mac

        interface = self.interface

        expires = self.expires

        type_ = self.type_

        dnsresolve = self.dnsresolve

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mac is not UNSET:
            field_dict["mac"] = mac
        if interface is not UNSET:
            field_dict["interface"] = interface
        if expires is not UNSET:
            field_dict["expires"] = expires
        if type_ is not UNSET:
            field_dict["type"] = type_
        if dnsresolve is not UNSET:
            field_dict["dnsresolve"] = dnsresolve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ip = d.pop("ip", UNSET)

        mac = d.pop("mac", UNSET)

        interface = d.pop("interface", UNSET)

        expires = d.pop("expires", UNSET)

        type_ = d.pop("type", UNSET)

        dnsresolve = d.pop("dnsresolve", UNSET)

        arp_table_entry = cls(
            ip=ip,
            mac=mac,
            interface=interface,
            expires=expires,
            type_=type_,
            dnsresolve=dnsresolve,
        )

        arp_table_entry.additional_properties = d
        return arp_table_entry

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
