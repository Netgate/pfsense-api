from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PacketCaptureFilter")


@_attrs_define
class PacketCaptureFilter:
    """Additional packet capture filter. These are common options for both
    tagged and untagged filters, with the exception of the vlan_*
    values which are only used by the tagged_filter.

        Attributes:
            exclude (bool | Unset): if false, then the other parameters operate as "include any of"
            vlan_tag_op (str | Unset): any_of, none_of, or_any_of
            vlan_tag (str | Unset): space or comma separated list of vlan tags
            vlan_level (int | Unset): tag level - 1-9
            host_addr_op (str | Unset): any_of, all_of, none_of, or_all_of, or_any_of
            host_addr (str | Unset): list of host addresses or CIDR subnets
            host_mac_op (str | Unset): any_of, all_of, none_of, or_all_of, or_any_of
            host_mac (str | Unset): list of mac addresses
            protocol_op (str | Unset): any_of, or_any_of, none_of, or name of protocol (ping, ipsec, tcp, udp, carp, pfsync,
                ospf)
            protocol (str | Unset): list of protocols numbers or names (if protocol_op is not a protocol name)
            port_op (str | Unset): any_of, all_of, none_of, or_all_of, or_any_of
            port (str | Unset): list of port numbers
            ether_op (str | Unset): any_of, or_any_of, none_of, or name of ethernet protocol (ipv4, ipv6, arp)
            ether (str | Unset): list of ethernet protocol names or hex values
    """

    exclude: bool | Unset = UNSET
    vlan_tag_op: str | Unset = UNSET
    vlan_tag: str | Unset = UNSET
    vlan_level: int | Unset = UNSET
    host_addr_op: str | Unset = UNSET
    host_addr: str | Unset = UNSET
    host_mac_op: str | Unset = UNSET
    host_mac: str | Unset = UNSET
    protocol_op: str | Unset = UNSET
    protocol: str | Unset = UNSET
    port_op: str | Unset = UNSET
    port: str | Unset = UNSET
    ether_op: str | Unset = UNSET
    ether: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude = self.exclude

        vlan_tag_op = self.vlan_tag_op

        vlan_tag = self.vlan_tag

        vlan_level = self.vlan_level

        host_addr_op = self.host_addr_op

        host_addr = self.host_addr

        host_mac_op = self.host_mac_op

        host_mac = self.host_mac

        protocol_op = self.protocol_op

        protocol = self.protocol

        port_op = self.port_op

        port = self.port

        ether_op = self.ether_op

        ether = self.ether

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if vlan_tag_op is not UNSET:
            field_dict["vlan_tag_op"] = vlan_tag_op
        if vlan_tag is not UNSET:
            field_dict["vlan_tag"] = vlan_tag
        if vlan_level is not UNSET:
            field_dict["vlan_level"] = vlan_level
        if host_addr_op is not UNSET:
            field_dict["host_addr_op"] = host_addr_op
        if host_addr is not UNSET:
            field_dict["host_addr"] = host_addr
        if host_mac_op is not UNSET:
            field_dict["host_mac_op"] = host_mac_op
        if host_mac is not UNSET:
            field_dict["host_mac"] = host_mac
        if protocol_op is not UNSET:
            field_dict["protocol_op"] = protocol_op
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if port_op is not UNSET:
            field_dict["port_op"] = port_op
        if port is not UNSET:
            field_dict["port"] = port
        if ether_op is not UNSET:
            field_dict["ether_op"] = ether_op
        if ether is not UNSET:
            field_dict["ether"] = ether

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exclude = d.pop("exclude", UNSET)

        vlan_tag_op = d.pop("vlan_tag_op", UNSET)

        vlan_tag = d.pop("vlan_tag", UNSET)

        vlan_level = d.pop("vlan_level", UNSET)

        host_addr_op = d.pop("host_addr_op", UNSET)

        host_addr = d.pop("host_addr", UNSET)

        host_mac_op = d.pop("host_mac_op", UNSET)

        host_mac = d.pop("host_mac", UNSET)

        protocol_op = d.pop("protocol_op", UNSET)

        protocol = d.pop("protocol", UNSET)

        port_op = d.pop("port_op", UNSET)

        port = d.pop("port", UNSET)

        ether_op = d.pop("ether_op", UNSET)

        ether = d.pop("ether", UNSET)

        packet_capture_filter = cls(
            exclude=exclude,
            vlan_tag_op=vlan_tag_op,
            vlan_tag=vlan_tag,
            vlan_level=vlan_level,
            host_addr_op=host_addr_op,
            host_addr=host_addr,
            host_mac_op=host_mac_op,
            host_mac=host_mac,
            protocol_op=protocol_op,
            protocol=protocol,
            port_op=port_op,
            port=port,
            ether_op=ether_op,
            ether=ether,
        )

        packet_capture_filter.additional_properties = d
        return packet_capture_filter

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
