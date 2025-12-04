from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceSimple")


@_attrs_define
class InterfaceSimple:
    """Basic interface details.

    Attributes:
        name (str): alias to identity
        identity (str | Unset): interface identity
        assigned (str | Unset): assigned interface name
        if_ (str | Unset): operating system device name
        descr (str | Unset): interface description
        ipaddr (str | Unset):
        ipaddrv6 (str | Unset):
        mac (str | Unset):
        tag (int | Unset):
        member (str | Unset):
        addresses (list[str] | Unset):
        enable (bool | Unset):
    """

    name: str
    identity: str | Unset = UNSET
    assigned: str | Unset = UNSET
    if_: str | Unset = UNSET
    descr: str | Unset = UNSET
    ipaddr: str | Unset = UNSET
    ipaddrv6: str | Unset = UNSET
    mac: str | Unset = UNSET
    tag: int | Unset = UNSET
    member: str | Unset = UNSET
    addresses: list[str] | Unset = UNSET
    enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identity = self.identity

        assigned = self.assigned

        if_ = self.if_

        descr = self.descr

        ipaddr = self.ipaddr

        ipaddrv6 = self.ipaddrv6

        mac = self.mac

        tag = self.tag

        member = self.member

        addresses: list[str] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if identity is not UNSET:
            field_dict["identity"] = identity
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if if_ is not UNSET:
            field_dict["if"] = if_
        if descr is not UNSET:
            field_dict["descr"] = descr
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if ipaddrv6 is not UNSET:
            field_dict["ipaddrv6"] = ipaddrv6
        if mac is not UNSET:
            field_dict["mac"] = mac
        if tag is not UNSET:
            field_dict["tag"] = tag
        if member is not UNSET:
            field_dict["member"] = member
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        identity = d.pop("identity", UNSET)

        assigned = d.pop("assigned", UNSET)

        if_ = d.pop("if", UNSET)

        descr = d.pop("descr", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        ipaddrv6 = d.pop("ipaddrv6", UNSET)

        mac = d.pop("mac", UNSET)

        tag = d.pop("tag", UNSET)

        member = d.pop("member", UNSET)

        addresses = cast(list[str], d.pop("addresses", UNSET))

        enable = d.pop("enable", UNSET)

        interface_simple = cls(
            name=name,
            identity=identity,
            assigned=assigned,
            if_=if_,
            descr=descr,
            ipaddr=ipaddr,
            ipaddrv6=ipaddrv6,
            mac=mac,
            tag=tag,
            member=member,
            addresses=addresses,
            enable=enable,
        )

        interface_simple.additional_properties = d
        return interface_simple

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
