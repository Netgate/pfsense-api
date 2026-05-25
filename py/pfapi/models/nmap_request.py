from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NmapRequest")


@_attrs_define
class NmapRequest:
    """
    Attributes:
        hostnames (str | Unset): Space-separated target IP addresses, hostnames, ranges, or networks to scan
        scan_type (str | Unset): Scan type (syn, connect, ack, window, udp, icmp, arp, ipscan, sctpinit, sctpecho,
            listscan)
        iface (str | Unset): Interface friendly name to use as the source interface
        udp_scan (bool | Unset): Combine UDP scan (-sU) with a TCP scan method
        no_ping (bool | Unset): Treat all hosts as online, skip host discovery (-Pn)
        service_version (bool | Unset): Attempt to identify service versions (-sV)
        os_detect (bool | Unset): Enable operating system detection (-O)
        exclude_hosts (str | Unset): Comma-separated IP addresses, hostnames, or ranges to exclude from scan
        ports (str | Unset): Port specification in nmap -p format (e.g. 22,80,443 or T:21-25,80,U:53)
        top_ports (int | Unset): Only scan the N most common ports (1-65535)
        no_dns (bool | Unset): Disable DNS resolution (-n)
        traceroute (bool | Unset): Trace hop path to each host (--traceroute)
    """

    hostnames: str | Unset = UNSET
    scan_type: str | Unset = UNSET
    iface: str | Unset = UNSET
    udp_scan: bool | Unset = UNSET
    no_ping: bool | Unset = UNSET
    service_version: bool | Unset = UNSET
    os_detect: bool | Unset = UNSET
    exclude_hosts: str | Unset = UNSET
    ports: str | Unset = UNSET
    top_ports: int | Unset = UNSET
    no_dns: bool | Unset = UNSET
    traceroute: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostnames = self.hostnames

        scan_type = self.scan_type

        iface = self.iface

        udp_scan = self.udp_scan

        no_ping = self.no_ping

        service_version = self.service_version

        os_detect = self.os_detect

        exclude_hosts = self.exclude_hosts

        ports = self.ports

        top_ports = self.top_ports

        no_dns = self.no_dns

        traceroute = self.traceroute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if scan_type is not UNSET:
            field_dict["scan_type"] = scan_type
        if iface is not UNSET:
            field_dict["iface"] = iface
        if udp_scan is not UNSET:
            field_dict["udp_scan"] = udp_scan
        if no_ping is not UNSET:
            field_dict["no_ping"] = no_ping
        if service_version is not UNSET:
            field_dict["service_version"] = service_version
        if os_detect is not UNSET:
            field_dict["os_detect"] = os_detect
        if exclude_hosts is not UNSET:
            field_dict["exclude_hosts"] = exclude_hosts
        if ports is not UNSET:
            field_dict["ports"] = ports
        if top_ports is not UNSET:
            field_dict["top_ports"] = top_ports
        if no_dns is not UNSET:
            field_dict["no_dns"] = no_dns
        if traceroute is not UNSET:
            field_dict["traceroute"] = traceroute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostnames = d.pop("hostnames", UNSET)

        scan_type = d.pop("scan_type", UNSET)

        iface = d.pop("iface", UNSET)

        udp_scan = d.pop("udp_scan", UNSET)

        no_ping = d.pop("no_ping", UNSET)

        service_version = d.pop("service_version", UNSET)

        os_detect = d.pop("os_detect", UNSET)

        exclude_hosts = d.pop("exclude_hosts", UNSET)

        ports = d.pop("ports", UNSET)

        top_ports = d.pop("top_ports", UNSET)

        no_dns = d.pop("no_dns", UNSET)

        traceroute = d.pop("traceroute", UNSET)

        nmap_request = cls(
            hostnames=hostnames,
            scan_type=scan_type,
            iface=iface,
            udp_scan=udp_scan,
            no_ping=no_ping,
            service_version=service_version,
            os_detect=os_detect,
            exclude_hosts=exclude_hosts,
            ports=ports,
            top_ports=top_ports,
            no_dns=no_dns,
            traceroute=traceroute,
        )

        nmap_request.additional_properties = d
        return nmap_request

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
