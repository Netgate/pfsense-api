from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_network_booting import DhcpNetworkBooting


T = TypeVar("T", bound="DhcpAddressPool")


@_attrs_define
class DhcpAddressPool:
    """
    Attributes:
        id (str | Unset): readonly (index)
        deny_unknown_clients (str | Unset): disabled | enabled | class
        description (str | Unset):
        address_pool_range_from (str | Unset):
        address_pool_range_to (str | Unset):
        wins_servers (list[str] | Unset):
        dns_servers (list[str] | Unset):
        gateway (str | Unset):
        domain_name (str | Unset):
        domain_search_list (list[str] | Unset):
        mac_allow (list[str] | Unset):
        mac_deny (list[str] | Unset):
        ntp_servers (list[str] | Unset):
        tftp_server (str | Unset):
        ldap_server_uri (str | Unset):
        network_booting (DhcpNetworkBooting | Unset):
        subnet (str | Unset):
        subnet_range_from (str | Unset):
        subnet_range_to (str | Unset):
    """

    id: str | Unset = UNSET
    deny_unknown_clients: str | Unset = UNSET
    description: str | Unset = UNSET
    address_pool_range_from: str | Unset = UNSET
    address_pool_range_to: str | Unset = UNSET
    wins_servers: list[str] | Unset = UNSET
    dns_servers: list[str] | Unset = UNSET
    gateway: str | Unset = UNSET
    domain_name: str | Unset = UNSET
    domain_search_list: list[str] | Unset = UNSET
    mac_allow: list[str] | Unset = UNSET
    mac_deny: list[str] | Unset = UNSET
    ntp_servers: list[str] | Unset = UNSET
    tftp_server: str | Unset = UNSET
    ldap_server_uri: str | Unset = UNSET
    network_booting: DhcpNetworkBooting | Unset = UNSET
    subnet: str | Unset = UNSET
    subnet_range_from: str | Unset = UNSET
    subnet_range_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        deny_unknown_clients = self.deny_unknown_clients

        description = self.description

        address_pool_range_from = self.address_pool_range_from

        address_pool_range_to = self.address_pool_range_to

        wins_servers: list[str] | Unset = UNSET
        if not isinstance(self.wins_servers, Unset):
            wins_servers = self.wins_servers

        dns_servers: list[str] | Unset = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        gateway = self.gateway

        domain_name = self.domain_name

        domain_search_list: list[str] | Unset = UNSET
        if not isinstance(self.domain_search_list, Unset):
            domain_search_list = self.domain_search_list

        mac_allow: list[str] | Unset = UNSET
        if not isinstance(self.mac_allow, Unset):
            mac_allow = self.mac_allow

        mac_deny: list[str] | Unset = UNSET
        if not isinstance(self.mac_deny, Unset):
            mac_deny = self.mac_deny

        ntp_servers: list[str] | Unset = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = self.ntp_servers

        tftp_server = self.tftp_server

        ldap_server_uri = self.ldap_server_uri

        network_booting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_booting, Unset):
            network_booting = self.network_booting.to_dict()

        subnet = self.subnet

        subnet_range_from = self.subnet_range_from

        subnet_range_to = self.subnet_range_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if deny_unknown_clients is not UNSET:
            field_dict["deny_unknown_clients"] = deny_unknown_clients
        if description is not UNSET:
            field_dict["description"] = description
        if address_pool_range_from is not UNSET:
            field_dict["address_pool_range_from"] = address_pool_range_from
        if address_pool_range_to is not UNSET:
            field_dict["address_pool_range_to"] = address_pool_range_to
        if wins_servers is not UNSET:
            field_dict["wins_servers"] = wins_servers
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if domain_search_list is not UNSET:
            field_dict["domain_search_list"] = domain_search_list
        if mac_allow is not UNSET:
            field_dict["mac_allow"] = mac_allow
        if mac_deny is not UNSET:
            field_dict["mac_deny"] = mac_deny
        if ntp_servers is not UNSET:
            field_dict["ntp_servers"] = ntp_servers
        if tftp_server is not UNSET:
            field_dict["tftp_server"] = tftp_server
        if ldap_server_uri is not UNSET:
            field_dict["ldap_server_uri"] = ldap_server_uri
        if network_booting is not UNSET:
            field_dict["network_booting"] = network_booting
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if subnet_range_from is not UNSET:
            field_dict["subnet_range_from"] = subnet_range_from
        if subnet_range_to is not UNSET:
            field_dict["subnet_range_to"] = subnet_range_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_network_booting import DhcpNetworkBooting

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        deny_unknown_clients = d.pop("deny_unknown_clients", UNSET)

        description = d.pop("description", UNSET)

        address_pool_range_from = d.pop("address_pool_range_from", UNSET)

        address_pool_range_to = d.pop("address_pool_range_to", UNSET)

        wins_servers = cast(list[str], d.pop("wins_servers", UNSET))

        dns_servers = cast(list[str], d.pop("dns_servers", UNSET))

        gateway = d.pop("gateway", UNSET)

        domain_name = d.pop("domain_name", UNSET)

        domain_search_list = cast(list[str], d.pop("domain_search_list", UNSET))

        mac_allow = cast(list[str], d.pop("mac_allow", UNSET))

        mac_deny = cast(list[str], d.pop("mac_deny", UNSET))

        ntp_servers = cast(list[str], d.pop("ntp_servers", UNSET))

        tftp_server = d.pop("tftp_server", UNSET)

        ldap_server_uri = d.pop("ldap_server_uri", UNSET)

        _network_booting = d.pop("network_booting", UNSET)
        network_booting: DhcpNetworkBooting | Unset
        if isinstance(_network_booting, Unset):
            network_booting = UNSET
        else:
            network_booting = DhcpNetworkBooting.from_dict(_network_booting)

        subnet = d.pop("subnet", UNSET)

        subnet_range_from = d.pop("subnet_range_from", UNSET)

        subnet_range_to = d.pop("subnet_range_to", UNSET)

        dhcp_address_pool = cls(
            id=id,
            deny_unknown_clients=deny_unknown_clients,
            description=description,
            address_pool_range_from=address_pool_range_from,
            address_pool_range_to=address_pool_range_to,
            wins_servers=wins_servers,
            dns_servers=dns_servers,
            gateway=gateway,
            domain_name=domain_name,
            domain_search_list=domain_search_list,
            mac_allow=mac_allow,
            mac_deny=mac_deny,
            ntp_servers=ntp_servers,
            tftp_server=tftp_server,
            ldap_server_uri=ldap_server_uri,
            network_booting=network_booting,
            subnet=subnet,
            subnet_range_from=subnet_range_from,
            subnet_range_to=subnet_range_to,
        )

        dhcp_address_pool.additional_properties = d
        return dhcp_address_pool

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
