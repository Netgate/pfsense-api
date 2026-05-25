from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MDNSPublishing")


@_attrs_define
class MDNSPublishing:
    """
    Attributes:
        enable (bool | Unset): enable publishing this system info
        addresses (bool | Unset): publish addresses of this system
        hostinfo (bool | Unset): publish host information (OS and CPU)
        workstation (bool | Unset): publish workstation record for this system
        domain (bool | Unset): publish domain name in use by this system
        custom_hostname (str | Unset): override host name used for publishing system's host name
        custom_domain (str | Unset): override domain name used for publishing domain record
        aaaa_over_ipv4 (bool | Unset): publish local IPv6 addresses over IPv4
        a_over_ipv6 (bool | Unset): publish local IPv4 addresses over IPv6
    """

    enable: bool | Unset = UNSET
    addresses: bool | Unset = UNSET
    hostinfo: bool | Unset = UNSET
    workstation: bool | Unset = UNSET
    domain: bool | Unset = UNSET
    custom_hostname: str | Unset = UNSET
    custom_domain: str | Unset = UNSET
    aaaa_over_ipv4: bool | Unset = UNSET
    a_over_ipv6: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        addresses = self.addresses

        hostinfo = self.hostinfo

        workstation = self.workstation

        domain = self.domain

        custom_hostname = self.custom_hostname

        custom_domain = self.custom_domain

        aaaa_over_ipv4 = self.aaaa_over_ipv4

        a_over_ipv6 = self.a_over_ipv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if hostinfo is not UNSET:
            field_dict["hostinfo"] = hostinfo
        if workstation is not UNSET:
            field_dict["workstation"] = workstation
        if domain is not UNSET:
            field_dict["domain"] = domain
        if custom_hostname is not UNSET:
            field_dict["custom_hostname"] = custom_hostname
        if custom_domain is not UNSET:
            field_dict["custom_domain"] = custom_domain
        if aaaa_over_ipv4 is not UNSET:
            field_dict["aaaa_over_ipv4"] = aaaa_over_ipv4
        if a_over_ipv6 is not UNSET:
            field_dict["a_over_ipv6"] = a_over_ipv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        addresses = d.pop("addresses", UNSET)

        hostinfo = d.pop("hostinfo", UNSET)

        workstation = d.pop("workstation", UNSET)

        domain = d.pop("domain", UNSET)

        custom_hostname = d.pop("custom_hostname", UNSET)

        custom_domain = d.pop("custom_domain", UNSET)

        aaaa_over_ipv4 = d.pop("aaaa_over_ipv4", UNSET)

        a_over_ipv6 = d.pop("a_over_ipv6", UNSET)

        mdns_publishing = cls(
            enable=enable,
            addresses=addresses,
            hostinfo=hostinfo,
            workstation=workstation,
            domain=domain,
            custom_hostname=custom_hostname,
            custom_domain=custom_domain,
            aaaa_over_ipv4=aaaa_over_ipv4,
            a_over_ipv6=a_over_ipv6,
        )

        mdns_publishing.additional_properties = d
        return mdns_publishing

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
