from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        regdhcp (bool):
        regdhcpstatic (bool):
        dhcpfirst (bool):
        strict_order (bool):
        domain_needed (bool):
        no_private_reverse (bool):
        port (str):
        interface (str):
        strictbind (bool):
        custom_options (str):
        hosts (Union[Unset, List['DNSForwarderHost']]):
        domainoverrides (Union[Unset, List['DNSForwarderDomain']]):
    """

    enable: bool
    regdhcp: bool
    regdhcpstatic: bool
    dhcpfirst: bool
    strict_order: bool
    domain_needed: bool
    no_private_reverse: bool
    port: str
    interface: str
    strictbind: bool
    custom_options: str
    hosts: Union[Unset, List["DNSForwarderHost"]] = UNSET
    domainoverrides: Union[Unset, List["DNSForwarderDomain"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        hosts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()
                hosts.append(hosts_item)

        domainoverrides: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.domainoverrides, Unset):
            domainoverrides = []
            for domainoverrides_item_data in self.domainoverrides:
                domainoverrides_item = domainoverrides_item_data.to_dict()
                domainoverrides.append(domainoverrides_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "regdhcp": regdhcp,
                "regdhcpstatic": regdhcpstatic,
                "dhcpfirst": dhcpfirst,
                "strict_order": strict_order,
                "domain_needed": domain_needed,
                "no_private_reverse": no_private_reverse,
                "port": port,
                "interface": interface,
                "strictbind": strictbind,
                "custom_options": custom_options,
            }
        )
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if domainoverrides is not UNSET:
            field_dict["domainoverrides"] = domainoverrides

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dns_forwarder_domain import DNSForwarderDomain
        from ..models.dns_forwarder_host import DNSForwarderHost

        d = src_dict.copy()
        enable = d.pop("enable")

        regdhcp = d.pop("regdhcp")

        regdhcpstatic = d.pop("regdhcpstatic")

        dhcpfirst = d.pop("dhcpfirst")

        strict_order = d.pop("strict_order")

        domain_needed = d.pop("domain_needed")

        no_private_reverse = d.pop("no_private_reverse")

        port = d.pop("port")

        interface = d.pop("interface")

        strictbind = d.pop("strictbind")

        custom_options = d.pop("custom_options")

        hosts = []
        _hosts = d.pop("hosts", UNSET)
        for hosts_item_data in _hosts or []:
            hosts_item = DNSForwarderHost.from_dict(hosts_item_data)

            hosts.append(hosts_item)

        domainoverrides = []
        _domainoverrides = d.pop("domainoverrides", UNSET)
        for domainoverrides_item_data in _domainoverrides or []:
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
