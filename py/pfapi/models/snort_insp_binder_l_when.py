from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspBinderLWhen")


@_attrs_define
class SnortInspBinderLWhen:
    """
    Attributes:
        ips_policy_id (int | Unset): unique ID for selection of this config by external logic { 0:max32 }
        vlans (list[str] | Unset):
        nets (list[str] | Unset):
        src_nets (list[str] | Unset):
        dst_nets (list[str] | Unset):
        proto (str | Unset): protocol { any | ip | icmp | tcp | udp | user | file }
        ports (list[str] | Unset):
        src_ports (list[str] | Unset):
        dst_ports (list[str] | Unset):
        intfs (str | Unset): list of interface IDs
        src_intfs (str | Unset): list of source interface IDs
        dst_intfs (str | Unset): list of destination interface IDs
        groups (str | Unset): list of interface group IDs
        src_groups (str | Unset): list of source interface group IDs
        dst_groups (str | Unset): list of destination group IDs
        addr_spaces (str | Unset): list of address space IDs
        tenants (str | Unset): list of tenants
        role (str | Unset): use the given configuration on one or any end of a session { client | server | any };
            default any
        service (str | Unset): name of service to match
    """

    ips_policy_id: int | Unset = UNSET
    vlans: list[str] | Unset = UNSET
    nets: list[str] | Unset = UNSET
    src_nets: list[str] | Unset = UNSET
    dst_nets: list[str] | Unset = UNSET
    proto: str | Unset = UNSET
    ports: list[str] | Unset = UNSET
    src_ports: list[str] | Unset = UNSET
    dst_ports: list[str] | Unset = UNSET
    intfs: str | Unset = UNSET
    src_intfs: str | Unset = UNSET
    dst_intfs: str | Unset = UNSET
    groups: str | Unset = UNSET
    src_groups: str | Unset = UNSET
    dst_groups: str | Unset = UNSET
    addr_spaces: str | Unset = UNSET
    tenants: str | Unset = UNSET
    role: str | Unset = UNSET
    service: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ips_policy_id = self.ips_policy_id

        vlans: list[str] | Unset = UNSET
        if not isinstance(self.vlans, Unset):
            vlans = self.vlans

        nets: list[str] | Unset = UNSET
        if not isinstance(self.nets, Unset):
            nets = self.nets

        src_nets: list[str] | Unset = UNSET
        if not isinstance(self.src_nets, Unset):
            src_nets = self.src_nets

        dst_nets: list[str] | Unset = UNSET
        if not isinstance(self.dst_nets, Unset):
            dst_nets = self.dst_nets

        proto = self.proto

        ports: list[str] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        src_ports: list[str] | Unset = UNSET
        if not isinstance(self.src_ports, Unset):
            src_ports = self.src_ports

        dst_ports: list[str] | Unset = UNSET
        if not isinstance(self.dst_ports, Unset):
            dst_ports = self.dst_ports

        intfs = self.intfs

        src_intfs = self.src_intfs

        dst_intfs = self.dst_intfs

        groups = self.groups

        src_groups = self.src_groups

        dst_groups = self.dst_groups

        addr_spaces = self.addr_spaces

        tenants = self.tenants

        role = self.role

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ips_policy_id is not UNSET:
            field_dict["ips_policy_id"] = ips_policy_id
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if nets is not UNSET:
            field_dict["nets"] = nets
        if src_nets is not UNSET:
            field_dict["src_nets"] = src_nets
        if dst_nets is not UNSET:
            field_dict["dst_nets"] = dst_nets
        if proto is not UNSET:
            field_dict["proto"] = proto
        if ports is not UNSET:
            field_dict["ports"] = ports
        if src_ports is not UNSET:
            field_dict["src_ports"] = src_ports
        if dst_ports is not UNSET:
            field_dict["dst_ports"] = dst_ports
        if intfs is not UNSET:
            field_dict["intfs"] = intfs
        if src_intfs is not UNSET:
            field_dict["src_intfs"] = src_intfs
        if dst_intfs is not UNSET:
            field_dict["dst_intfs"] = dst_intfs
        if groups is not UNSET:
            field_dict["groups"] = groups
        if src_groups is not UNSET:
            field_dict["src_groups"] = src_groups
        if dst_groups is not UNSET:
            field_dict["dst_groups"] = dst_groups
        if addr_spaces is not UNSET:
            field_dict["addr_spaces"] = addr_spaces
        if tenants is not UNSET:
            field_dict["tenants"] = tenants
        if role is not UNSET:
            field_dict["role"] = role
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ips_policy_id = d.pop("ips_policy_id", UNSET)

        vlans = cast(list[str], d.pop("vlans", UNSET))

        nets = cast(list[str], d.pop("nets", UNSET))

        src_nets = cast(list[str], d.pop("src_nets", UNSET))

        dst_nets = cast(list[str], d.pop("dst_nets", UNSET))

        proto = d.pop("proto", UNSET)

        ports = cast(list[str], d.pop("ports", UNSET))

        src_ports = cast(list[str], d.pop("src_ports", UNSET))

        dst_ports = cast(list[str], d.pop("dst_ports", UNSET))

        intfs = d.pop("intfs", UNSET)

        src_intfs = d.pop("src_intfs", UNSET)

        dst_intfs = d.pop("dst_intfs", UNSET)

        groups = d.pop("groups", UNSET)

        src_groups = d.pop("src_groups", UNSET)

        dst_groups = d.pop("dst_groups", UNSET)

        addr_spaces = d.pop("addr_spaces", UNSET)

        tenants = d.pop("tenants", UNSET)

        role = d.pop("role", UNSET)

        service = d.pop("service", UNSET)

        snort_insp_binder_l_when = cls(
            ips_policy_id=ips_policy_id,
            vlans=vlans,
            nets=nets,
            src_nets=src_nets,
            dst_nets=dst_nets,
            proto=proto,
            ports=ports,
            src_ports=src_ports,
            dst_ports=dst_ports,
            intfs=intfs,
            src_intfs=src_intfs,
            dst_intfs=dst_intfs,
            groups=groups,
            src_groups=src_groups,
            dst_groups=dst_groups,
            addr_spaces=addr_spaces,
            tenants=tenants,
            role=role,
            service=service,
        )

        snort_insp_binder_l_when.additional_properties = d
        return snort_insp_binder_l_when

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
