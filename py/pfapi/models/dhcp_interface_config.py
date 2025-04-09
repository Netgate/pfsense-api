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
        if_ident (Union[Unset, str]):
        if_assigned_name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        deny_unknown_clients (Union[Unset, str]):
        ignore_client_identifiers (Union[Unset, bool]):
        dns_reg (Union[Unset, str]):
        early_dns_reg (Union[Unset, str]):
        address_pool_range_from (Union[Unset, str]):
        address_pool_range_to (Union[Unset, str]):
        wins_servers (Union[Unset, List[str]]):
        dns_servers (Union[Unset, List[str]]):
        additional_pools (Union[Unset, List['DhcpAddressPool']]):
        gateway (Union[Unset, str]):
        domain_name (Union[Unset, str]):
        domain_search_list (Union[Unset, List[str]]):
        default_lease_time (Union[Unset, int]):
        maximum_lease_time (Union[Unset, int]):
        mac_allow (Union[Unset, List[str]]):
        mac_deny (Union[Unset, List[str]]):
        ntp_servers (Union[Unset, List[str]]):
        tftp_server (Union[Unset, str]):
        ldap_server_uri (Union[Unset, str]):
        network_booting (Union[Unset, DhcpNetworkBooting]):
        static_mappings (Union[Unset, List['DhcpStaticMapping']]):
        static_mappings_v6 (Union[Unset, List['Dhcpv6StaticMapping']]):
        subnet (Union[Unset, str]):
        subnet_range_from (Union[Unset, str]):
        subnet_range_to (Union[Unset, str]):
        backend (Union[Unset, str]):
    """

    if_ident: Union[Unset, str] = UNSET
    if_assigned_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    deny_unknown_clients: Union[Unset, str] = UNSET
    ignore_client_identifiers: Union[Unset, bool] = UNSET
    dns_reg: Union[Unset, str] = UNSET
    early_dns_reg: Union[Unset, str] = UNSET
    address_pool_range_from: Union[Unset, str] = UNSET
    address_pool_range_to: Union[Unset, str] = UNSET
    wins_servers: Union[Unset, List[str]] = UNSET
    dns_servers: Union[Unset, List[str]] = UNSET
    additional_pools: Union[Unset, List["DhcpAddressPool"]] = UNSET
    gateway: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    domain_search_list: Union[Unset, List[str]] = UNSET
    default_lease_time: Union[Unset, int] = UNSET
    maximum_lease_time: Union[Unset, int] = UNSET
    mac_allow: Union[Unset, List[str]] = UNSET
    mac_deny: Union[Unset, List[str]] = UNSET
    ntp_servers: Union[Unset, List[str]] = UNSET
    tftp_server: Union[Unset, str] = UNSET
    ldap_server_uri: Union[Unset, str] = UNSET
    network_booting: Union[Unset, "DhcpNetworkBooting"] = UNSET
    static_mappings: Union[Unset, List["DhcpStaticMapping"]] = UNSET
    static_mappings_v6: Union[Unset, List["Dhcpv6StaticMapping"]] = UNSET
    subnet: Union[Unset, str] = UNSET
    subnet_range_from: Union[Unset, str] = UNSET
    subnet_range_to: Union[Unset, str] = UNSET
    backend: Union[Unset, str] = UNSET
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

        gateway = self.gateway

        domain_name = self.domain_name

        domain_search_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.domain_search_list, Unset):
            domain_search_list = self.domain_search_list

        default_lease_time = self.default_lease_time

        maximum_lease_time = self.maximum_lease_time

        mac_allow: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mac_allow, Unset):
            mac_allow = self.mac_allow

        mac_deny: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mac_deny, Unset):
            mac_deny = self.mac_deny

        ntp_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = self.ntp_servers

        tftp_server = self.tftp_server

        ldap_server_uri = self.ldap_server_uri

        network_booting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.network_booting, Unset):
            network_booting = self.network_booting.to_dict()

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

        subnet = self.subnet

        subnet_range_from = self.subnet_range_from

        subnet_range_to = self.subnet_range_to

        backend = self.backend

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_ident is not UNSET:
            field_dict["if_ident"] = if_ident
        if if_assigned_name is not UNSET:
            field_dict["if_assigned_name"] = if_assigned_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if deny_unknown_clients is not UNSET:
            field_dict["deny_unknown_clients"] = deny_unknown_clients
        if ignore_client_identifiers is not UNSET:
            field_dict["ignore_client_identifiers"] = ignore_client_identifiers
        if dns_reg is not UNSET:
            field_dict["dns_reg"] = dns_reg
        if early_dns_reg is not UNSET:
            field_dict["early_dns_reg"] = early_dns_reg
        if address_pool_range_from is not UNSET:
            field_dict["address_pool_range_from"] = address_pool_range_from
        if address_pool_range_to is not UNSET:
            field_dict["address_pool_range_to"] = address_pool_range_to
        if wins_servers is not UNSET:
            field_dict["wins_servers"] = wins_servers
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers
        if additional_pools is not UNSET:
            field_dict["additional_pools"] = additional_pools
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if domain_search_list is not UNSET:
            field_dict["domain_search_list"] = domain_search_list
        if default_lease_time is not UNSET:
            field_dict["default_lease_time"] = default_lease_time
        if maximum_lease_time is not UNSET:
            field_dict["maximum_lease_time"] = maximum_lease_time
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
        if static_mappings is not UNSET:
            field_dict["static_mappings"] = static_mappings
        if static_mappings_v6 is not UNSET:
            field_dict["static_mappings_v6"] = static_mappings_v6
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if subnet_range_from is not UNSET:
            field_dict["subnet_range_from"] = subnet_range_from
        if subnet_range_to is not UNSET:
            field_dict["subnet_range_to"] = subnet_range_to
        if backend is not UNSET:
            field_dict["backend"] = backend

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_address_pool import DhcpAddressPool
        from ..models.dhcp_network_booting import DhcpNetworkBooting
        from ..models.dhcp_static_mapping import DhcpStaticMapping
        from ..models.dhcpv_6_static_mapping import Dhcpv6StaticMapping

        d = src_dict.copy()
        if_ident = d.pop("if_ident", UNSET)

        if_assigned_name = d.pop("if_assigned_name", UNSET)

        enabled = d.pop("enabled", UNSET)

        deny_unknown_clients = d.pop("deny_unknown_clients", UNSET)

        ignore_client_identifiers = d.pop("ignore_client_identifiers", UNSET)

        dns_reg = d.pop("dns_reg", UNSET)

        early_dns_reg = d.pop("early_dns_reg", UNSET)

        address_pool_range_from = d.pop("address_pool_range_from", UNSET)

        address_pool_range_to = d.pop("address_pool_range_to", UNSET)

        wins_servers = cast(List[str], d.pop("wins_servers", UNSET))

        dns_servers = cast(List[str], d.pop("dns_servers", UNSET))

        additional_pools = []
        _additional_pools = d.pop("additional_pools", UNSET)
        for additional_pools_item_data in _additional_pools or []:
            additional_pools_item = DhcpAddressPool.from_dict(additional_pools_item_data)

            additional_pools.append(additional_pools_item)

        gateway = d.pop("gateway", UNSET)

        domain_name = d.pop("domain_name", UNSET)

        domain_search_list = cast(List[str], d.pop("domain_search_list", UNSET))

        default_lease_time = d.pop("default_lease_time", UNSET)

        maximum_lease_time = d.pop("maximum_lease_time", UNSET)

        mac_allow = cast(List[str], d.pop("mac_allow", UNSET))

        mac_deny = cast(List[str], d.pop("mac_deny", UNSET))

        ntp_servers = cast(List[str], d.pop("ntp_servers", UNSET))

        tftp_server = d.pop("tftp_server", UNSET)

        ldap_server_uri = d.pop("ldap_server_uri", UNSET)

        _network_booting = d.pop("network_booting", UNSET)
        network_booting: Union[Unset, DhcpNetworkBooting]
        if isinstance(_network_booting, Unset):
            network_booting = UNSET
        else:
            network_booting = DhcpNetworkBooting.from_dict(_network_booting)

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

        subnet = d.pop("subnet", UNSET)

        subnet_range_from = d.pop("subnet_range_from", UNSET)

        subnet_range_to = d.pop("subnet_range_to", UNSET)

        backend = d.pop("backend", UNSET)

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
            wins_servers=wins_servers,
            dns_servers=dns_servers,
            additional_pools=additional_pools,
            gateway=gateway,
            domain_name=domain_name,
            domain_search_list=domain_search_list,
            default_lease_time=default_lease_time,
            maximum_lease_time=maximum_lease_time,
            mac_allow=mac_allow,
            mac_deny=mac_deny,
            ntp_servers=ntp_servers,
            tftp_server=tftp_server,
            ldap_server_uri=ldap_server_uri,
            network_booting=network_booting,
            static_mappings=static_mappings,
            static_mappings_v6=static_mappings_v6,
            subnet=subnet,
            subnet_range_from=subnet_range_from,
            subnet_range_to=subnet_range_to,
            backend=backend,
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
