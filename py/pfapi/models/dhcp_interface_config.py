from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_address_pool import DhcpAddressPool
    from ..models.dhcp_network_booting import DhcpNetworkBooting
    from ..models.dhcp_static_mapping import DhcpStaticMapping
    from ..models.dhcpv_6_static_mapping import Dhcpv6StaticMapping


T = TypeVar("T", bound="DhcpInterfaceConfig")


@_attrs_define
class DhcpInterfaceConfig:
    """
    Attributes:
        if_ident (str):
        if_assigned_name (str):
        enabled (bool):
        deny_unknown_clients (str):
        ignore_client_identifiers (bool):
        dns_reg (str):
        early_dns_reg (str):
        address_pool_range_from (str):
        address_pool_range_to (str):
        gateway (str):
        domain_name (str):
        default_lease_time (int):
        maximum_lease_time (int):
        tftp_server (str):
        ldap_server_uri (str):
        network_booting (DhcpNetworkBooting):
        subnet (str):
        subnet_range_from (str):
        subnet_range_to (str):
        backend (str):
        wins_servers (Union[Unset, List[str]]):
        dns_servers (Union[Unset, List[str]]):
        additional_pools (Union[Unset, List['DhcpAddressPool']]):
        domain_search_list (Union[Unset, List[str]]):
        mac_allow (Union[Unset, List[str]]):
        mac_deny (Union[Unset, List[str]]):
        ntp_servers (Union[Unset, List[str]]):
        static_mappings (Union[Unset, List['DhcpStaticMapping']]):
        static_mappings_v6 (Union[Unset, List['Dhcpv6StaticMapping']]):
    """

    if_ident: str
    if_assigned_name: str
    enabled: bool
    deny_unknown_clients: str
    ignore_client_identifiers: bool
    dns_reg: str
    early_dns_reg: str
    address_pool_range_from: str
    address_pool_range_to: str
    gateway: str
    domain_name: str
    default_lease_time: int
    maximum_lease_time: int
    tftp_server: str
    ldap_server_uri: str
    network_booting: "DhcpNetworkBooting"
    subnet: str
    subnet_range_from: str
    subnet_range_to: str
    backend: str
    wins_servers: Union[Unset, List[str]] = UNSET
    dns_servers: Union[Unset, List[str]] = UNSET
    additional_pools: Union[Unset, List["DhcpAddressPool"]] = UNSET
    domain_search_list: Union[Unset, List[str]] = UNSET
    mac_allow: Union[Unset, List[str]] = UNSET
    mac_deny: Union[Unset, List[str]] = UNSET
    ntp_servers: Union[Unset, List[str]] = UNSET
    static_mappings: Union[Unset, List["DhcpStaticMapping"]] = UNSET
    static_mappings_v6: Union[Unset, List["Dhcpv6StaticMapping"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_ident = self.if_ident

        if_assigned_name = self.if_assigned_name

        enabled = self.enabled

        deny_unknown_clients = self.deny_unknown_clients

        ignore_client_identifiers = self.ignore_client_identifiers

        dns_reg = self.dns_reg

        early_dns_reg = self.early_dns_reg

        address_pool_range_from = self.address_pool_range_from

        address_pool_range_to = self.address_pool_range_to

        gateway = self.gateway

        domain_name = self.domain_name

        default_lease_time = self.default_lease_time

        maximum_lease_time = self.maximum_lease_time

        tftp_server = self.tftp_server

        ldap_server_uri = self.ldap_server_uri

        network_booting = self.network_booting.to_dict()

        subnet = self.subnet

        subnet_range_from = self.subnet_range_from

        subnet_range_to = self.subnet_range_to

        backend = self.backend

        wins_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wins_servers, Unset):
            wins_servers = self.wins_servers

        dns_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        additional_pools: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_pools, Unset):
            additional_pools = []
            for additional_pools_item_data in self.additional_pools:
                additional_pools_item = additional_pools_item_data.to_dict()
                additional_pools.append(additional_pools_item)

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

        static_mappings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.static_mappings, Unset):
            static_mappings = []
            for static_mappings_item_data in self.static_mappings:
                static_mappings_item = static_mappings_item_data.to_dict()
                static_mappings.append(static_mappings_item)

        static_mappings_v6: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.static_mappings_v6, Unset):
            static_mappings_v6 = []
            for static_mappings_v6_item_data in self.static_mappings_v6:
                static_mappings_v6_item = static_mappings_v6_item_data.to_dict()
                static_mappings_v6.append(static_mappings_v6_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if_ident": if_ident,
                "if_assigned_name": if_assigned_name,
                "enabled": enabled,
                "deny_unknown_clients": deny_unknown_clients,
                "ignore_client_identifiers": ignore_client_identifiers,
                "dns_reg": dns_reg,
                "early_dns_reg": early_dns_reg,
                "address_pool_range_from": address_pool_range_from,
                "address_pool_range_to": address_pool_range_to,
                "gateway": gateway,
                "domain_name": domain_name,
                "default_lease_time": default_lease_time,
                "maximum_lease_time": maximum_lease_time,
                "tftp_server": tftp_server,
                "ldap_server_uri": ldap_server_uri,
                "network_booting": network_booting,
                "subnet": subnet,
                "subnet_range_from": subnet_range_from,
                "subnet_range_to": subnet_range_to,
                "backend": backend,
            }
        )
        if wins_servers is not UNSET:
            field_dict["wins_servers"] = wins_servers
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers
        if additional_pools is not UNSET:
            field_dict["additional_pools"] = additional_pools
        if domain_search_list is not UNSET:
            field_dict["domain_search_list"] = domain_search_list
        if mac_allow is not UNSET:
            field_dict["mac_allow"] = mac_allow
        if mac_deny is not UNSET:
            field_dict["mac_deny"] = mac_deny
        if ntp_servers is not UNSET:
            field_dict["ntp_servers"] = ntp_servers
        if static_mappings is not UNSET:
            field_dict["static_mappings"] = static_mappings
        if static_mappings_v6 is not UNSET:
            field_dict["static_mappings_v6"] = static_mappings_v6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_address_pool import DhcpAddressPool
        from ..models.dhcp_network_booting import DhcpNetworkBooting
        from ..models.dhcp_static_mapping import DhcpStaticMapping
        from ..models.dhcpv_6_static_mapping import Dhcpv6StaticMapping

        d = src_dict.copy()
        if_ident = d.pop("if_ident")

        if_assigned_name = d.pop("if_assigned_name")

        enabled = d.pop("enabled")

        deny_unknown_clients = d.pop("deny_unknown_clients")

        ignore_client_identifiers = d.pop("ignore_client_identifiers")

        dns_reg = d.pop("dns_reg")

        early_dns_reg = d.pop("early_dns_reg")

        address_pool_range_from = d.pop("address_pool_range_from")

        address_pool_range_to = d.pop("address_pool_range_to")

        gateway = d.pop("gateway")

        domain_name = d.pop("domain_name")

        default_lease_time = d.pop("default_lease_time")

        maximum_lease_time = d.pop("maximum_lease_time")

        tftp_server = d.pop("tftp_server")

        ldap_server_uri = d.pop("ldap_server_uri")

        network_booting = DhcpNetworkBooting.from_dict(d.pop("network_booting"))

        subnet = d.pop("subnet")

        subnet_range_from = d.pop("subnet_range_from")

        subnet_range_to = d.pop("subnet_range_to")

        backend = d.pop("backend")

        wins_servers = cast(List[str], d.pop("wins_servers", UNSET))

        dns_servers = cast(List[str], d.pop("dns_servers", UNSET))

        additional_pools = []
        _additional_pools = d.pop("additional_pools", UNSET)
        for additional_pools_item_data in _additional_pools or []:
            additional_pools_item = DhcpAddressPool.from_dict(additional_pools_item_data)

            additional_pools.append(additional_pools_item)

        domain_search_list = cast(List[str], d.pop("domain_search_list", UNSET))

        mac_allow = cast(List[str], d.pop("mac_allow", UNSET))

        mac_deny = cast(List[str], d.pop("mac_deny", UNSET))

        ntp_servers = cast(List[str], d.pop("ntp_servers", UNSET))

        static_mappings = []
        _static_mappings = d.pop("static_mappings", UNSET)
        for static_mappings_item_data in _static_mappings or []:
            static_mappings_item = DhcpStaticMapping.from_dict(static_mappings_item_data)

            static_mappings.append(static_mappings_item)

        static_mappings_v6 = []
        _static_mappings_v6 = d.pop("static_mappings_v6", UNSET)
        for static_mappings_v6_item_data in _static_mappings_v6 or []:
            static_mappings_v6_item = Dhcpv6StaticMapping.from_dict(static_mappings_v6_item_data)

            static_mappings_v6.append(static_mappings_v6_item)

        dhcp_interface_config = cls(
            if_ident=if_ident,
            if_assigned_name=if_assigned_name,
            enabled=enabled,
            deny_unknown_clients=deny_unknown_clients,
            ignore_client_identifiers=ignore_client_identifiers,
            dns_reg=dns_reg,
            early_dns_reg=early_dns_reg,
            address_pool_range_from=address_pool_range_from,
            address_pool_range_to=address_pool_range_to,
            gateway=gateway,
            domain_name=domain_name,
            default_lease_time=default_lease_time,
            maximum_lease_time=maximum_lease_time,
            tftp_server=tftp_server,
            ldap_server_uri=ldap_server_uri,
            network_booting=network_booting,
            subnet=subnet,
            subnet_range_from=subnet_range_from,
            subnet_range_to=subnet_range_to,
            backend=backend,
            wins_servers=wins_servers,
            dns_servers=dns_servers,
            additional_pools=additional_pools,
            domain_search_list=domain_search_list,
            mac_allow=mac_allow,
            mac_deny=mac_deny,
            ntp_servers=ntp_servers,
            static_mappings=static_mappings,
            static_mappings_v6=static_mappings_v6,
        )

        dhcp_interface_config.additional_properties = d
        return dhcp_interface_config

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
