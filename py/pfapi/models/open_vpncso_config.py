from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNCSOConfig")


@_attrs_define
class OpenVPNCSOConfig:
    """
    Attributes:
        disable (Union[Unset, bool]):
        server_list (Union[Unset, str]):
        common_name (Union[Unset, str]):
        block (Union[Unset, bool]):
        description (Union[Unset, str]):
        tunnel_network (Union[Unset, str]):
        tunnel_networkv6 (Union[Unset, str]):
        local_network (Union[Unset, str]):
        local_networkv6 (Union[Unset, str]):
        remote_network (Union[Unset, str]):
        remote_networkv6 (Union[Unset, str]):
        gwredir (Union[Unset, bool]):
        push_reset (Union[Unset, bool]):
        remove_route (Union[Unset, bool]):
        dns_domain_enable (Union[Unset, bool]):
        dns_domain (Union[Unset, str]):
        dns_server_enable (Union[Unset, bool]):
        dns_server1 (Union[Unset, str]):
        dns_server2 (Union[Unset, str]):
        dns_server3 (Union[Unset, str]):
        dns_server4 (Union[Unset, str]):
        ntp_server_enable (Union[Unset, bool]):
        ntp_server1 (Union[Unset, str]):
        ntp_server2 (Union[Unset, str]):
        netbios_enable (Union[Unset, bool]):
        netbios_ntype (Union[Unset, str]):
        netbios_scope (Union[Unset, str]):
        wins_server_enable (Union[Unset, bool]):
        wins_server1 (Union[Unset, str]):
        wins_server2 (Union[Unset, str]):
        nbdd_server_enable (Union[Unset, bool]):
        nbdd_server1 (Union[Unset, str]):
        nbdd_server2 (Union[Unset, str]):
        custom_options (Union[Unset, str]):
    """

    disable: Union[Unset, bool] = UNSET
    server_list: Union[Unset, str] = UNSET
    common_name: Union[Unset, str] = UNSET
    block: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    tunnel_network: Union[Unset, str] = UNSET
    tunnel_networkv6: Union[Unset, str] = UNSET
    local_network: Union[Unset, str] = UNSET
    local_networkv6: Union[Unset, str] = UNSET
    remote_network: Union[Unset, str] = UNSET
    remote_networkv6: Union[Unset, str] = UNSET
    gwredir: Union[Unset, bool] = UNSET
    push_reset: Union[Unset, bool] = UNSET
    remove_route: Union[Unset, bool] = UNSET
    dns_domain_enable: Union[Unset, bool] = UNSET
    dns_domain: Union[Unset, str] = UNSET
    dns_server_enable: Union[Unset, bool] = UNSET
    dns_server1: Union[Unset, str] = UNSET
    dns_server2: Union[Unset, str] = UNSET
    dns_server3: Union[Unset, str] = UNSET
    dns_server4: Union[Unset, str] = UNSET
    ntp_server_enable: Union[Unset, bool] = UNSET
    ntp_server1: Union[Unset, str] = UNSET
    ntp_server2: Union[Unset, str] = UNSET
    netbios_enable: Union[Unset, bool] = UNSET
    netbios_ntype: Union[Unset, str] = UNSET
    netbios_scope: Union[Unset, str] = UNSET
    wins_server_enable: Union[Unset, bool] = UNSET
    wins_server1: Union[Unset, str] = UNSET
    wins_server2: Union[Unset, str] = UNSET
    nbdd_server_enable: Union[Unset, bool] = UNSET
    nbdd_server1: Union[Unset, str] = UNSET
    nbdd_server2: Union[Unset, str] = UNSET
    custom_options: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disable = self.disable

        server_list = self.server_list

        common_name = self.common_name

        block = self.block

        description = self.description

        tunnel_network = self.tunnel_network

        tunnel_networkv6 = self.tunnel_networkv6

        local_network = self.local_network

        local_networkv6 = self.local_networkv6

        remote_network = self.remote_network

        remote_networkv6 = self.remote_networkv6

        gwredir = self.gwredir

        push_reset = self.push_reset

        remove_route = self.remove_route

        dns_domain_enable = self.dns_domain_enable

        dns_domain = self.dns_domain

        dns_server_enable = self.dns_server_enable

        dns_server1 = self.dns_server1

        dns_server2 = self.dns_server2

        dns_server3 = self.dns_server3

        dns_server4 = self.dns_server4

        ntp_server_enable = self.ntp_server_enable

        ntp_server1 = self.ntp_server1

        ntp_server2 = self.ntp_server2

        netbios_enable = self.netbios_enable

        netbios_ntype = self.netbios_ntype

        netbios_scope = self.netbios_scope

        wins_server_enable = self.wins_server_enable

        wins_server1 = self.wins_server1

        wins_server2 = self.wins_server2

        nbdd_server_enable = self.nbdd_server_enable

        nbdd_server1 = self.nbdd_server1

        nbdd_server2 = self.nbdd_server2

        custom_options = self.custom_options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable is not UNSET:
            field_dict["disable"] = disable
        if server_list is not UNSET:
            field_dict["server_list"] = server_list
        if common_name is not UNSET:
            field_dict["common_name"] = common_name
        if block is not UNSET:
            field_dict["block"] = block
        if description is not UNSET:
            field_dict["description"] = description
        if tunnel_network is not UNSET:
            field_dict["tunnel_network"] = tunnel_network
        if tunnel_networkv6 is not UNSET:
            field_dict["tunnel_networkv6"] = tunnel_networkv6
        if local_network is not UNSET:
            field_dict["local_network"] = local_network
        if local_networkv6 is not UNSET:
            field_dict["local_networkv6"] = local_networkv6
        if remote_network is not UNSET:
            field_dict["remote_network"] = remote_network
        if remote_networkv6 is not UNSET:
            field_dict["remote_networkv6"] = remote_networkv6
        if gwredir is not UNSET:
            field_dict["gwredir"] = gwredir
        if push_reset is not UNSET:
            field_dict["push_reset"] = push_reset
        if remove_route is not UNSET:
            field_dict["remove_route"] = remove_route
        if dns_domain_enable is not UNSET:
            field_dict["dns_domain_enable"] = dns_domain_enable
        if dns_domain is not UNSET:
            field_dict["dns_domain"] = dns_domain
        if dns_server_enable is not UNSET:
            field_dict["dns_server_enable"] = dns_server_enable
        if dns_server1 is not UNSET:
            field_dict["dns_server1"] = dns_server1
        if dns_server2 is not UNSET:
            field_dict["dns_server2"] = dns_server2
        if dns_server3 is not UNSET:
            field_dict["dns_server3"] = dns_server3
        if dns_server4 is not UNSET:
            field_dict["dns_server4"] = dns_server4
        if ntp_server_enable is not UNSET:
            field_dict["ntp_server_enable"] = ntp_server_enable
        if ntp_server1 is not UNSET:
            field_dict["ntp_server1"] = ntp_server1
        if ntp_server2 is not UNSET:
            field_dict["ntp_server2"] = ntp_server2
        if netbios_enable is not UNSET:
            field_dict["netbios_enable"] = netbios_enable
        if netbios_ntype is not UNSET:
            field_dict["netbios_ntype"] = netbios_ntype
        if netbios_scope is not UNSET:
            field_dict["netbios_scope"] = netbios_scope
        if wins_server_enable is not UNSET:
            field_dict["wins_server_enable"] = wins_server_enable
        if wins_server1 is not UNSET:
            field_dict["wins_server1"] = wins_server1
        if wins_server2 is not UNSET:
            field_dict["wins_server2"] = wins_server2
        if nbdd_server_enable is not UNSET:
            field_dict["nbdd_server_enable"] = nbdd_server_enable
        if nbdd_server1 is not UNSET:
            field_dict["nbdd_server1"] = nbdd_server1
        if nbdd_server2 is not UNSET:
            field_dict["nbdd_server2"] = nbdd_server2
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disable = d.pop("disable", UNSET)

        server_list = d.pop("server_list", UNSET)

        common_name = d.pop("common_name", UNSET)

        block = d.pop("block", UNSET)

        description = d.pop("description", UNSET)

        tunnel_network = d.pop("tunnel_network", UNSET)

        tunnel_networkv6 = d.pop("tunnel_networkv6", UNSET)

        local_network = d.pop("local_network", UNSET)

        local_networkv6 = d.pop("local_networkv6", UNSET)

        remote_network = d.pop("remote_network", UNSET)

        remote_networkv6 = d.pop("remote_networkv6", UNSET)

        gwredir = d.pop("gwredir", UNSET)

        push_reset = d.pop("push_reset", UNSET)

        remove_route = d.pop("remove_route", UNSET)

        dns_domain_enable = d.pop("dns_domain_enable", UNSET)

        dns_domain = d.pop("dns_domain", UNSET)

        dns_server_enable = d.pop("dns_server_enable", UNSET)

        dns_server1 = d.pop("dns_server1", UNSET)

        dns_server2 = d.pop("dns_server2", UNSET)

        dns_server3 = d.pop("dns_server3", UNSET)

        dns_server4 = d.pop("dns_server4", UNSET)

        ntp_server_enable = d.pop("ntp_server_enable", UNSET)

        ntp_server1 = d.pop("ntp_server1", UNSET)

        ntp_server2 = d.pop("ntp_server2", UNSET)

        netbios_enable = d.pop("netbios_enable", UNSET)

        netbios_ntype = d.pop("netbios_ntype", UNSET)

        netbios_scope = d.pop("netbios_scope", UNSET)

        wins_server_enable = d.pop("wins_server_enable", UNSET)

        wins_server1 = d.pop("wins_server1", UNSET)

        wins_server2 = d.pop("wins_server2", UNSET)

        nbdd_server_enable = d.pop("nbdd_server_enable", UNSET)

        nbdd_server1 = d.pop("nbdd_server1", UNSET)

        nbdd_server2 = d.pop("nbdd_server2", UNSET)

        custom_options = d.pop("custom_options", UNSET)

        open_vpncso_config = cls(
            disable=disable,
            server_list=server_list,
            common_name=common_name,
            block=block,
            description=description,
            tunnel_network=tunnel_network,
            tunnel_networkv6=tunnel_networkv6,
            local_network=local_network,
            local_networkv6=local_networkv6,
            remote_network=remote_network,
            remote_networkv6=remote_networkv6,
            gwredir=gwredir,
            push_reset=push_reset,
            remove_route=remove_route,
            dns_domain_enable=dns_domain_enable,
            dns_domain=dns_domain,
            dns_server_enable=dns_server_enable,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            ntp_server_enable=ntp_server_enable,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            netbios_enable=netbios_enable,
            netbios_ntype=netbios_ntype,
            netbios_scope=netbios_scope,
            wins_server_enable=wins_server_enable,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            nbdd_server_enable=nbdd_server_enable,
            nbdd_server1=nbdd_server1,
            nbdd_server2=nbdd_server2,
            custom_options=custom_options,
        )

        open_vpncso_config.additional_properties = d
        return open_vpncso_config

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
