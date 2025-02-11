from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenVPNCSOConfig")


@_attrs_define
class OpenVPNCSOConfig:
    """
    Attributes:
        disable (bool):
        server_list (str):
        common_name (str):
        block (bool):
        description (str):
        tunnel_network (str):
        tunnel_networkv6 (str):
        local_network (str):
        local_networkv6 (str):
        remote_network (str):
        remote_networkv6 (str):
        gwredir (bool):
        push_reset (bool):
        remove_route (bool):
        dns_domain_enable (bool):
        dns_domain (str):
        dns_server_enable (bool):
        dns_server1 (str):
        dns_server2 (str):
        dns_server3 (str):
        dns_server4 (str):
        ntp_server_enable (bool):
        ntp_server1 (str):
        ntp_server2 (str):
        netbios_enable (bool):
        netbios_ntype (str):
        netbios_scope (str):
        wins_server_enable (bool):
        wins_server1 (str):
        wins_server2 (str):
        nbdd_server_enable (bool):
        nbdd_server1 (str):
        nbdd_server2 (str):
        custom_options (str):
    """

    disable: bool
    server_list: str
    common_name: str
    block: bool
    description: str
    tunnel_network: str
    tunnel_networkv6: str
    local_network: str
    local_networkv6: str
    remote_network: str
    remote_networkv6: str
    gwredir: bool
    push_reset: bool
    remove_route: bool
    dns_domain_enable: bool
    dns_domain: str
    dns_server_enable: bool
    dns_server1: str
    dns_server2: str
    dns_server3: str
    dns_server4: str
    ntp_server_enable: bool
    ntp_server1: str
    ntp_server2: str
    netbios_enable: bool
    netbios_ntype: str
    netbios_scope: str
    wins_server_enable: bool
    wins_server1: str
    wins_server2: str
    nbdd_server_enable: bool
    nbdd_server1: str
    nbdd_server2: str
    custom_options: str
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
        field_dict.update(
            {
                "disable": disable,
                "server_list": server_list,
                "common_name": common_name,
                "block": block,
                "description": description,
                "tunnel_network": tunnel_network,
                "tunnel_networkv6": tunnel_networkv6,
                "local_network": local_network,
                "local_networkv6": local_networkv6,
                "remote_network": remote_network,
                "remote_networkv6": remote_networkv6,
                "gwredir": gwredir,
                "push_reset": push_reset,
                "remove_route": remove_route,
                "dns_domain_enable": dns_domain_enable,
                "dns_domain": dns_domain,
                "dns_server_enable": dns_server_enable,
                "dns_server1": dns_server1,
                "dns_server2": dns_server2,
                "dns_server3": dns_server3,
                "dns_server4": dns_server4,
                "ntp_server_enable": ntp_server_enable,
                "ntp_server1": ntp_server1,
                "ntp_server2": ntp_server2,
                "netbios_enable": netbios_enable,
                "netbios_ntype": netbios_ntype,
                "netbios_scope": netbios_scope,
                "wins_server_enable": wins_server_enable,
                "wins_server1": wins_server1,
                "wins_server2": wins_server2,
                "nbdd_server_enable": nbdd_server_enable,
                "nbdd_server1": nbdd_server1,
                "nbdd_server2": nbdd_server2,
                "custom_options": custom_options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disable = d.pop("disable")

        server_list = d.pop("server_list")

        common_name = d.pop("common_name")

        block = d.pop("block")

        description = d.pop("description")

        tunnel_network = d.pop("tunnel_network")

        tunnel_networkv6 = d.pop("tunnel_networkv6")

        local_network = d.pop("local_network")

        local_networkv6 = d.pop("local_networkv6")

        remote_network = d.pop("remote_network")

        remote_networkv6 = d.pop("remote_networkv6")

        gwredir = d.pop("gwredir")

        push_reset = d.pop("push_reset")

        remove_route = d.pop("remove_route")

        dns_domain_enable = d.pop("dns_domain_enable")

        dns_domain = d.pop("dns_domain")

        dns_server_enable = d.pop("dns_server_enable")

        dns_server1 = d.pop("dns_server1")

        dns_server2 = d.pop("dns_server2")

        dns_server3 = d.pop("dns_server3")

        dns_server4 = d.pop("dns_server4")

        ntp_server_enable = d.pop("ntp_server_enable")

        ntp_server1 = d.pop("ntp_server1")

        ntp_server2 = d.pop("ntp_server2")

        netbios_enable = d.pop("netbios_enable")

        netbios_ntype = d.pop("netbios_ntype")

        netbios_scope = d.pop("netbios_scope")

        wins_server_enable = d.pop("wins_server_enable")

        wins_server1 = d.pop("wins_server1")

        wins_server2 = d.pop("wins_server2")

        nbdd_server_enable = d.pop("nbdd_server_enable")

        nbdd_server1 = d.pop("nbdd_server1")

        nbdd_server2 = d.pop("nbdd_server2")

        custom_options = d.pop("custom_options")

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
