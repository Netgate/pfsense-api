from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortPassList")


@_attrs_define
class SnortPassList:
    """
    Attributes:
        name (str | Unset): unique name for pass list
        descr (str | Unset):
        local_networks (bool | Unset): add firewall locally-attached networks to the list
        wan_gateways (bool | Unset): add WAN gateways
        wan_dns_servers (bool | Unset): add WAN DNS servers
        virtual_ips (bool | Unset): add virtual IP addresses
        vpn_addrs (bool | Unset): add VPN addresses
        aliases (list[str] | Unset):
        addresses (list[str] | Unset):
        new_name (str | Unset): for updating with new name
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    local_networks: bool | Unset = UNSET
    wan_gateways: bool | Unset = UNSET
    wan_dns_servers: bool | Unset = UNSET
    virtual_ips: bool | Unset = UNSET
    vpn_addrs: bool | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    addresses: list[str] | Unset = UNSET
    new_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        local_networks = self.local_networks

        wan_gateways = self.wan_gateways

        wan_dns_servers = self.wan_dns_servers

        virtual_ips = self.virtual_ips

        vpn_addrs = self.vpn_addrs

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        addresses: list[str] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        new_name = self.new_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if local_networks is not UNSET:
            field_dict["local_networks"] = local_networks
        if wan_gateways is not UNSET:
            field_dict["wan_gateways"] = wan_gateways
        if wan_dns_servers is not UNSET:
            field_dict["wan_dns_servers"] = wan_dns_servers
        if virtual_ips is not UNSET:
            field_dict["virtual_ips"] = virtual_ips
        if vpn_addrs is not UNSET:
            field_dict["vpn_addrs"] = vpn_addrs
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if new_name is not UNSET:
            field_dict["new_name"] = new_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        local_networks = d.pop("local_networks", UNSET)

        wan_gateways = d.pop("wan_gateways", UNSET)

        wan_dns_servers = d.pop("wan_dns_servers", UNSET)

        virtual_ips = d.pop("virtual_ips", UNSET)

        vpn_addrs = d.pop("vpn_addrs", UNSET)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        addresses = cast(list[str], d.pop("addresses", UNSET))

        new_name = d.pop("new_name", UNSET)

        snort_pass_list = cls(
            name=name,
            descr=descr,
            local_networks=local_networks,
            wan_gateways=wan_gateways,
            wan_dns_servers=wan_dns_servers,
            virtual_ips=virtual_ips,
            vpn_addrs=vpn_addrs,
            aliases=aliases,
            addresses=addresses,
            new_name=new_name,
        )

        snort_pass_list.additional_properties = d
        return snort_pass_list

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
