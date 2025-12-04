from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_network_booting import DhcpNetworkBooting


T = TypeVar("T", bound="DhcpStaticMapping")


@_attrs_define
class DhcpStaticMapping:
    """
    Attributes:
        id (str | Unset):
        mac_address (str | Unset):
        client_identifier (str | Unset):
        ip_address (str | Unset):
        arp_table_static_entry (bool | Unset):
        hostname (str | Unset):
        description (str | Unset):
        early_dns_reg (str | Unset):
        wins_servers (list[str] | Unset):
        dns_servers (list[str] | Unset):
        gateway (str | Unset):
        domain_name (str | Unset):
        domain_search_list (list[str] | Unset):
        ntp_servers (list[str] | Unset):
        tftp_server (str | Unset):
        ldap_server_uri (str | Unset):
        network_booting (DhcpNetworkBooting | Unset):
        duid (str | Unset):
        ipv6_address (str | Unset):
        filename (str | Unset):
        rootpath (str | Unset):
    """

    id: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    client_identifier: str | Unset = UNSET
    ip_address: str | Unset = UNSET
    arp_table_static_entry: bool | Unset = UNSET
    hostname: str | Unset = UNSET
    description: str | Unset = UNSET
    early_dns_reg: str | Unset = UNSET
    wins_servers: list[str] | Unset = UNSET
    dns_servers: list[str] | Unset = UNSET
    gateway: str | Unset = UNSET
    domain_name: str | Unset = UNSET
    domain_search_list: list[str] | Unset = UNSET
    ntp_servers: list[str] | Unset = UNSET
    tftp_server: str | Unset = UNSET
    ldap_server_uri: str | Unset = UNSET
    network_booting: DhcpNetworkBooting | Unset = UNSET
    duid: str | Unset = UNSET
    ipv6_address: str | Unset = UNSET
    filename: str | Unset = UNSET
    rootpath: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac_address = self.mac_address

        client_identifier = self.client_identifier

        ip_address = self.ip_address

        arp_table_static_entry = self.arp_table_static_entry

        hostname = self.hostname

        description = self.description

        early_dns_reg = self.early_dns_reg

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

        ntp_servers: list[str] | Unset = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = self.ntp_servers

        tftp_server = self.tftp_server

        ldap_server_uri = self.ldap_server_uri

        network_booting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_booting, Unset):
            network_booting = self.network_booting.to_dict()

        duid = self.duid

        ipv6_address = self.ipv6_address

        filename = self.filename

        rootpath = self.rootpath

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if client_identifier is not UNSET:
            field_dict["client_identifier"] = client_identifier
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if arp_table_static_entry is not UNSET:
            field_dict["arp_table_static_entry"] = arp_table_static_entry
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if description is not UNSET:
            field_dict["description"] = description
        if early_dns_reg is not UNSET:
            field_dict["early_dns_reg"] = early_dns_reg
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
        if ntp_servers is not UNSET:
            field_dict["ntp_servers"] = ntp_servers
        if tftp_server is not UNSET:
            field_dict["tftp_server"] = tftp_server
        if ldap_server_uri is not UNSET:
            field_dict["ldap_server_uri"] = ldap_server_uri
        if network_booting is not UNSET:
            field_dict["network_booting"] = network_booting
        if duid is not UNSET:
            field_dict["duid"] = duid
        if ipv6_address is not UNSET:
            field_dict["ipv6_address"] = ipv6_address
        if filename is not UNSET:
            field_dict["filename"] = filename
        if rootpath is not UNSET:
            field_dict["rootpath"] = rootpath

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_network_booting import DhcpNetworkBooting

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        client_identifier = d.pop("client_identifier", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        arp_table_static_entry = d.pop("arp_table_static_entry", UNSET)

        hostname = d.pop("hostname", UNSET)

        description = d.pop("description", UNSET)

        early_dns_reg = d.pop("early_dns_reg", UNSET)

        wins_servers = cast(list[str], d.pop("wins_servers", UNSET))

        dns_servers = cast(list[str], d.pop("dns_servers", UNSET))

        gateway = d.pop("gateway", UNSET)

        domain_name = d.pop("domain_name", UNSET)

        domain_search_list = cast(list[str], d.pop("domain_search_list", UNSET))

        ntp_servers = cast(list[str], d.pop("ntp_servers", UNSET))

        tftp_server = d.pop("tftp_server", UNSET)

        ldap_server_uri = d.pop("ldap_server_uri", UNSET)

        _network_booting = d.pop("network_booting", UNSET)
        network_booting: DhcpNetworkBooting | Unset
        if isinstance(_network_booting, Unset):
            network_booting = UNSET
        else:
            network_booting = DhcpNetworkBooting.from_dict(_network_booting)

        duid = d.pop("duid", UNSET)

        ipv6_address = d.pop("ipv6_address", UNSET)

        filename = d.pop("filename", UNSET)

        rootpath = d.pop("rootpath", UNSET)

        dhcp_static_mapping = cls(
            id=id,
            mac_address=mac_address,
            client_identifier=client_identifier,
            ip_address=ip_address,
            arp_table_static_entry=arp_table_static_entry,
            hostname=hostname,
            description=description,
            early_dns_reg=early_dns_reg,
            wins_servers=wins_servers,
            dns_servers=dns_servers,
            gateway=gateway,
            domain_name=domain_name,
            domain_search_list=domain_search_list,
            ntp_servers=ntp_servers,
            tftp_server=tftp_server,
            ldap_server_uri=ldap_server_uri,
            network_booting=network_booting,
            duid=duid,
            ipv6_address=ipv6_address,
            filename=filename,
            rootpath=rootpath,
        )

        dhcp_static_mapping.additional_properties = d
        return dhcp_static_mapping

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
