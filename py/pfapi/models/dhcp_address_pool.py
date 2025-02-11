from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        id (str):
        deny_unknown_clients (str):
        description (str):
        address_pool_range_from (str):
        address_pool_range_to (str):
        gateway (str):
        domain_name (str):
        tftp_server (str):
        ldap_server_uri (str):
        network_booting (DhcpNetworkBooting):
        subnet (str):
        subnet_range_from (str):
        subnet_range_to (str):
        wins_servers (Union[Unset, List[str]]):
        dns_servers (Union[Unset, List[str]]):
        domain_search_list (Union[Unset, List[str]]):
        mac_allow (Union[Unset, List[str]]):
        mac_deny (Union[Unset, List[str]]):
        ntp_servers (Union[Unset, List[str]]):
    """

    id: str
    deny_unknown_clients: str
    description: str
    address_pool_range_from: str
    address_pool_range_to: str
    gateway: str
    domain_name: str
    tftp_server: str
    ldap_server_uri: str
    network_booting: "DhcpNetworkBooting"
    subnet: str
    subnet_range_from: str
    subnet_range_to: str
    wins_servers: Union[Unset, List[str]] = UNSET
    dns_servers: Union[Unset, List[str]] = UNSET
    domain_search_list: Union[Unset, List[str]] = UNSET
    mac_allow: Union[Unset, List[str]] = UNSET
    mac_deny: Union[Unset, List[str]] = UNSET
    ntp_servers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        deny_unknown_clients = self.deny_unknown_clients

        description = self.description

        address_pool_range_from = self.address_pool_range_from

        address_pool_range_to = self.address_pool_range_to

        gateway = self.gateway

        domain_name = self.domain_name

        tftp_server = self.tftp_server

        ldap_server_uri = self.ldap_server_uri

        network_booting = self.network_booting.to_dict()

        subnet = self.subnet

        subnet_range_from = self.subnet_range_from

        subnet_range_to = self.subnet_range_to

        wins_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wins_servers, Unset):
            wins_servers = self.wins_servers

        dns_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        domain_search_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.domain_search_list, Unset):
            domain_search_list = self.domain_search_list

        mac_allow: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mac_allow, Unset):
            mac_allow = self.mac_allow

        mac_deny: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mac_deny, Unset):
            mac_deny = self.mac_deny

        ntp_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = self.ntp_servers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deny_unknown_clients": deny_unknown_clients,
                "description": description,
                "address_pool_range_from": address_pool_range_from,
                "address_pool_range_to": address_pool_range_to,
                "gateway": gateway,
                "domain_name": domain_name,
                "tftp_server": tftp_server,
                "ldap_server_uri": ldap_server_uri,
                "network_booting": network_booting,
                "subnet": subnet,
                "subnet_range_from": subnet_range_from,
                "subnet_range_to": subnet_range_to,
            }
        )
        if wins_servers is not UNSET:
            field_dict["wins_servers"] = wins_servers
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers
        if domain_search_list is not UNSET:
            field_dict["domain_search_list"] = domain_search_list
        if mac_allow is not UNSET:
            field_dict["mac_allow"] = mac_allow
        if mac_deny is not UNSET:
            field_dict["mac_deny"] = mac_deny
        if ntp_servers is not UNSET:
            field_dict["ntp_servers"] = ntp_servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_network_booting import DhcpNetworkBooting

        d = src_dict.copy()
        id = d.pop("id")

        deny_unknown_clients = d.pop("deny_unknown_clients")

        description = d.pop("description")

        address_pool_range_from = d.pop("address_pool_range_from")

        address_pool_range_to = d.pop("address_pool_range_to")

        gateway = d.pop("gateway")

        domain_name = d.pop("domain_name")

        tftp_server = d.pop("tftp_server")

        ldap_server_uri = d.pop("ldap_server_uri")

        network_booting = DhcpNetworkBooting.from_dict(d.pop("network_booting"))

        subnet = d.pop("subnet")

        subnet_range_from = d.pop("subnet_range_from")

        subnet_range_to = d.pop("subnet_range_to")

        wins_servers = cast(List[str], d.pop("wins_servers", UNSET))

        dns_servers = cast(List[str], d.pop("dns_servers", UNSET))

        domain_search_list = cast(List[str], d.pop("domain_search_list", UNSET))

        mac_allow = cast(List[str], d.pop("mac_allow", UNSET))

        mac_deny = cast(List[str], d.pop("mac_deny", UNSET))

        ntp_servers = cast(List[str], d.pop("ntp_servers", UNSET))

        dhcp_address_pool = cls(
            id=id,
            deny_unknown_clients=deny_unknown_clients,
            description=description,
            address_pool_range_from=address_pool_range_from,
            address_pool_range_to=address_pool_range_to,
            gateway=gateway,
            domain_name=domain_name,
            tftp_server=tftp_server,
            ldap_server_uri=ldap_server_uri,
            network_booting=network_booting,
            subnet=subnet,
            subnet_range_from=subnet_range_from,
            subnet_range_to=subnet_range_to,
            wins_servers=wins_servers,
            dns_servers=dns_servers,
            domain_search_list=domain_search_list,
            mac_allow=mac_allow,
            mac_deny=mac_deny,
            ntp_servers=ntp_servers,
        )

        dhcp_address_pool.additional_properties = d
        return dhcp_address_pool

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
