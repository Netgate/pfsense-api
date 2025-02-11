from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HAXMLRPCSync")


@_attrs_define
class HAXMLRPCSync:
    """
    Attributes:
        sync_to_ip (str): addres of device to sync the selected config sections
        username (str): username to authenticate with sync_to_ip device
        password (str): authentication password
        sync_admin_acct (bool): sync admin accounts and autoupdate sync password
        sync_users (bool): sync user manager users and groups
        sync_auth_servers (bool):
        sync_certs (bool):
        sync_fw_rules (bool):
        sync_fw_schedules (bool):
        sync_fw_aliases (bool):
        sync_nat (bool):
        sync_ipsec (bool):
        sync_ovpn (bool):
        sync_dhcp_server (bool):
        sync_dhcp_relay (bool):
        sync_dhcp6_server (bool):
        sync_dhcp6_relay (bool):
        sync_static_routes (bool):
        sync_wol (bool):
        sync_virtual_ips (bool):
        sync_traffic_shaper (bool):
        sync_traffic_shaper_limiters (bool):
        sync_dns (bool):
        sync_cap_portal (bool):
    """

    sync_to_ip: str
    username: str
    password: str
    sync_admin_acct: bool
    sync_users: bool
    sync_auth_servers: bool
    sync_certs: bool
    sync_fw_rules: bool
    sync_fw_schedules: bool
    sync_fw_aliases: bool
    sync_nat: bool
    sync_ipsec: bool
    sync_ovpn: bool
    sync_dhcp_server: bool
    sync_dhcp_relay: bool
    sync_dhcp6_server: bool
    sync_dhcp6_relay: bool
    sync_static_routes: bool
    sync_wol: bool
    sync_virtual_ips: bool
    sync_traffic_shaper: bool
    sync_traffic_shaper_limiters: bool
    sync_dns: bool
    sync_cap_portal: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sync_to_ip = self.sync_to_ip

        username = self.username

        password = self.password

        sync_admin_acct = self.sync_admin_acct

        sync_users = self.sync_users

        sync_auth_servers = self.sync_auth_servers

        sync_certs = self.sync_certs

        sync_fw_rules = self.sync_fw_rules

        sync_fw_schedules = self.sync_fw_schedules

        sync_fw_aliases = self.sync_fw_aliases

        sync_nat = self.sync_nat

        sync_ipsec = self.sync_ipsec

        sync_ovpn = self.sync_ovpn

        sync_dhcp_server = self.sync_dhcp_server

        sync_dhcp_relay = self.sync_dhcp_relay

        sync_dhcp6_server = self.sync_dhcp6_server

        sync_dhcp6_relay = self.sync_dhcp6_relay

        sync_static_routes = self.sync_static_routes

        sync_wol = self.sync_wol

        sync_virtual_ips = self.sync_virtual_ips

        sync_traffic_shaper = self.sync_traffic_shaper

        sync_traffic_shaper_limiters = self.sync_traffic_shaper_limiters

        sync_dns = self.sync_dns

        sync_cap_portal = self.sync_cap_portal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_to_ip": sync_to_ip,
                "username": username,
                "password": password,
                "sync_admin_acct": sync_admin_acct,
                "sync_users": sync_users,
                "sync_auth_servers": sync_auth_servers,
                "sync_certs": sync_certs,
                "sync_fw_rules": sync_fw_rules,
                "sync_fw_schedules": sync_fw_schedules,
                "sync_fw_aliases": sync_fw_aliases,
                "sync_nat": sync_nat,
                "sync_ipsec": sync_ipsec,
                "sync_ovpn": sync_ovpn,
                "sync_dhcp_server": sync_dhcp_server,
                "sync_dhcp_relay": sync_dhcp_relay,
                "sync_dhcp6_server": sync_dhcp6_server,
                "sync_dhcp6_relay": sync_dhcp6_relay,
                "sync_static_routes": sync_static_routes,
                "sync_wol": sync_wol,
                "sync_virtual_ips": sync_virtual_ips,
                "sync_traffic_shaper": sync_traffic_shaper,
                "sync_traffic_shaper_limiters": sync_traffic_shaper_limiters,
                "sync_dns": sync_dns,
                "sync_cap_portal": sync_cap_portal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sync_to_ip = d.pop("sync_to_ip")

        username = d.pop("username")

        password = d.pop("password")

        sync_admin_acct = d.pop("sync_admin_acct")

        sync_users = d.pop("sync_users")

        sync_auth_servers = d.pop("sync_auth_servers")

        sync_certs = d.pop("sync_certs")

        sync_fw_rules = d.pop("sync_fw_rules")

        sync_fw_schedules = d.pop("sync_fw_schedules")

        sync_fw_aliases = d.pop("sync_fw_aliases")

        sync_nat = d.pop("sync_nat")

        sync_ipsec = d.pop("sync_ipsec")

        sync_ovpn = d.pop("sync_ovpn")

        sync_dhcp_server = d.pop("sync_dhcp_server")

        sync_dhcp_relay = d.pop("sync_dhcp_relay")

        sync_dhcp6_server = d.pop("sync_dhcp6_server")

        sync_dhcp6_relay = d.pop("sync_dhcp6_relay")

        sync_static_routes = d.pop("sync_static_routes")

        sync_wol = d.pop("sync_wol")

        sync_virtual_ips = d.pop("sync_virtual_ips")

        sync_traffic_shaper = d.pop("sync_traffic_shaper")

        sync_traffic_shaper_limiters = d.pop("sync_traffic_shaper_limiters")

        sync_dns = d.pop("sync_dns")

        sync_cap_portal = d.pop("sync_cap_portal")

        haxmlrpc_sync = cls(
            sync_to_ip=sync_to_ip,
            username=username,
            password=password,
            sync_admin_acct=sync_admin_acct,
            sync_users=sync_users,
            sync_auth_servers=sync_auth_servers,
            sync_certs=sync_certs,
            sync_fw_rules=sync_fw_rules,
            sync_fw_schedules=sync_fw_schedules,
            sync_fw_aliases=sync_fw_aliases,
            sync_nat=sync_nat,
            sync_ipsec=sync_ipsec,
            sync_ovpn=sync_ovpn,
            sync_dhcp_server=sync_dhcp_server,
            sync_dhcp_relay=sync_dhcp_relay,
            sync_dhcp6_server=sync_dhcp6_server,
            sync_dhcp6_relay=sync_dhcp6_relay,
            sync_static_routes=sync_static_routes,
            sync_wol=sync_wol,
            sync_virtual_ips=sync_virtual_ips,
            sync_traffic_shaper=sync_traffic_shaper,
            sync_traffic_shaper_limiters=sync_traffic_shaper_limiters,
            sync_dns=sync_dns,
            sync_cap_portal=sync_cap_portal,
        )

        haxmlrpc_sync.additional_properties = d
        return haxmlrpc_sync

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
