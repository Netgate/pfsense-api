from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_forwarder_domain import DNSForwarderDomain
    from ..models.dns_forwarder_host import DNSForwarderHost


T = TypeVar("T", bound="DNSForwarderConfig")


@_attrs_define
class DNSForwarderConfig:
    """
    Attributes:
        enable (bool):
        regdhcp (bool | Unset):
        regdhcpstatic (bool | Unset):
        dhcpfirst (bool | Unset):
        strict_order (bool | Unset):
        domain_needed (bool | Unset):
        no_private_reverse (bool | Unset):
        port (str | Unset):
        interface (str | Unset):
        strictbind (bool | Unset):
        custom_options (str | Unset):
        hosts (list[DNSForwarderHost] | Unset):
        domainoverrides (list[DNSForwarderDomain] | Unset):
    """

    enable: bool
    regdhcp: bool | Unset = UNSET
    regdhcpstatic: bool | Unset = UNSET
    dhcpfirst: bool | Unset = UNSET
    strict_order: bool | Unset = UNSET
    domain_needed: bool | Unset = UNSET
    no_private_reverse: bool | Unset = UNSET
    port: str | Unset = UNSET
    interface: str | Unset = UNSET
    strictbind: bool | Unset = UNSET
    custom_options: str | Unset = UNSET
    hosts: list[DNSForwarderHost] | Unset = UNSET
    domainoverrides: list[DNSForwarderDomain] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        regdhcp = self.regdhcp

        regdhcpstatic = self.regdhcpstatic

        dhcpfirst = self.dhcpfirst

        strict_order = self.strict_order

        domain_needed = self.domain_needed

        no_private_reverse = self.no_private_reverse

        port = self.port

        interface = self.interface

        strictbind = self.strictbind

        custom_options = self.custom_options

        hosts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()
                hosts.append(hosts_item)

        domainoverrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domainoverrides, Unset):
            domainoverrides = []
            for domainoverrides_item_data in self.domainoverrides:
                domainoverrides_item = domainoverrides_item_data.to_dict()
                domainoverrides.append(domainoverrides_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if regdhcp is not UNSET:
            field_dict["regdhcp"] = regdhcp
        if regdhcpstatic is not UNSET:
            field_dict["regdhcpstatic"] = regdhcpstatic
        if dhcpfirst is not UNSET:
            field_dict["dhcpfirst"] = dhcpfirst
        if strict_order is not UNSET:
            field_dict["strict_order"] = strict_order
        if domain_needed is not UNSET:
            field_dict["domain_needed"] = domain_needed
        if no_private_reverse is not UNSET:
            field_dict["no_private_reverse"] = no_private_reverse
        if port is not UNSET:
            field_dict["port"] = port
        if interface is not UNSET:
            field_dict["interface"] = interface
        if strictbind is not UNSET:
            field_dict["strictbind"] = strictbind
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if domainoverrides is not UNSET:
            field_dict["domainoverrides"] = domainoverrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_forwarder_domain import DNSForwarderDomain
        from ..models.dns_forwarder_host import DNSForwarderHost

        d = dict(src_dict)
        enable = d.pop("enable")

        regdhcp = d.pop("regdhcp", UNSET)

        regdhcpstatic = d.pop("regdhcpstatic", UNSET)

        dhcpfirst = d.pop("dhcpfirst", UNSET)

        strict_order = d.pop("strict_order", UNSET)

        domain_needed = d.pop("domain_needed", UNSET)

        no_private_reverse = d.pop("no_private_reverse", UNSET)

        port = d.pop("port", UNSET)

        interface = d.pop("interface", UNSET)

        strictbind = d.pop("strictbind", UNSET)

        custom_options = d.pop("custom_options", UNSET)

        _hosts = d.pop("hosts", UNSET)
        hosts: list[DNSForwarderHost] | Unset = UNSET
        if _hosts is not UNSET:
            hosts = []
            for hosts_item_data in _hosts:
                hosts_item = DNSForwarderHost.from_dict(hosts_item_data)

                hosts.append(hosts_item)

        _domainoverrides = d.pop("domainoverrides", UNSET)
        domainoverrides: list[DNSForwarderDomain] | Unset = UNSET
        if _domainoverrides is not UNSET:
            domainoverrides = []
            for domainoverrides_item_data in _domainoverrides:
                domainoverrides_item = DNSForwarderDomain.from_dict(domainoverrides_item_data)

                domainoverrides.append(domainoverrides_item)

        dns_forwarder_config = cls(
            enable=enable,
            regdhcp=regdhcp,
            regdhcpstatic=regdhcpstatic,
            dhcpfirst=dhcpfirst,
            strict_order=strict_order,
            domain_needed=domain_needed,
            no_private_reverse=no_private_reverse,
            port=port,
            interface=interface,
            strictbind=strictbind,
            custom_options=custom_options,
            hosts=hosts,
            domainoverrides=domainoverrides,
        )

        dns_forwarder_config.additional_properties = d
        return dns_forwarder_config

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
