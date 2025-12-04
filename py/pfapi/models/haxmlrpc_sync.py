from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HAXMLRPCSync")


@_attrs_define
class HAXMLRPCSync:
    """
    Attributes:
        sync_to_ip (str | Unset): addres of device to sync the selected config sections
        username (str | Unset): username to authenticate with sync_to_ip device
        password (str | Unset): authentication password
        sync_admin_acct (bool | Unset): sync admin accounts and autoupdate sync password
        sync_users (bool | Unset): sync user manager users and groups
        sync_auth_servers (bool | Unset):
        sync_certs (bool | Unset):
        sync_fw_rules (bool | Unset):
        sync_fw_schedules (bool | Unset):
        sync_fw_aliases (bool | Unset):
        sync_nat (bool | Unset):
        sync_ipsec (bool | Unset):
        sync_ovpn (bool | Unset):
        sync_dhcp_server (bool | Unset):
        sync_dhcp_relay (bool | Unset):
        sync_dhcp6_server (bool | Unset):
        sync_dhcp6_relay (bool | Unset):
        sync_static_routes (bool | Unset):
        sync_wol (bool | Unset):
        sync_virtual_ips (bool | Unset):
        sync_traffic_shaper (bool | Unset):
        sync_traffic_shaper_limiters (bool | Unset):
        sync_dns (bool | Unset):
        sync_cap_portal (bool | Unset):
    """

    sync_to_ip: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    sync_admin_acct: bool | Unset = UNSET
    sync_users: bool | Unset = UNSET
    sync_auth_servers: bool | Unset = UNSET
    sync_certs: bool | Unset = UNSET
    sync_fw_rules: bool | Unset = UNSET
    sync_fw_schedules: bool | Unset = UNSET
    sync_fw_aliases: bool | Unset = UNSET
    sync_nat: bool | Unset = UNSET
    sync_ipsec: bool | Unset = UNSET
    sync_ovpn: bool | Unset = UNSET
    sync_dhcp_server: bool | Unset = UNSET
    sync_dhcp_relay: bool | Unset = UNSET
    sync_dhcp6_server: bool | Unset = UNSET
    sync_dhcp6_relay: bool | Unset = UNSET
    sync_static_routes: bool | Unset = UNSET
    sync_wol: bool | Unset = UNSET
    sync_virtual_ips: bool | Unset = UNSET
    sync_traffic_shaper: bool | Unset = UNSET
    sync_traffic_shaper_limiters: bool | Unset = UNSET
    sync_dns: bool | Unset = UNSET
    sync_cap_portal: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sync_to_ip is not UNSET:
            field_dict["sync_to_ip"] = sync_to_ip
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if sync_admin_acct is not UNSET:
            field_dict["sync_admin_acct"] = sync_admin_acct
        if sync_users is not UNSET:
            field_dict["sync_users"] = sync_users
        if sync_auth_servers is not UNSET:
            field_dict["sync_auth_servers"] = sync_auth_servers
        if sync_certs is not UNSET:
            field_dict["sync_certs"] = sync_certs
        if sync_fw_rules is not UNSET:
            field_dict["sync_fw_rules"] = sync_fw_rules
        if sync_fw_schedules is not UNSET:
            field_dict["sync_fw_schedules"] = sync_fw_schedules
        if sync_fw_aliases is not UNSET:
            field_dict["sync_fw_aliases"] = sync_fw_aliases
        if sync_nat is not UNSET:
            field_dict["sync_nat"] = sync_nat
        if sync_ipsec is not UNSET:
            field_dict["sync_ipsec"] = sync_ipsec
        if sync_ovpn is not UNSET:
            field_dict["sync_ovpn"] = sync_ovpn
        if sync_dhcp_server is not UNSET:
            field_dict["sync_dhcp_server"] = sync_dhcp_server
        if sync_dhcp_relay is not UNSET:
            field_dict["sync_dhcp_relay"] = sync_dhcp_relay
        if sync_dhcp6_server is not UNSET:
            field_dict["sync_dhcp6_server"] = sync_dhcp6_server
        if sync_dhcp6_relay is not UNSET:
            field_dict["sync_dhcp6_relay"] = sync_dhcp6_relay
        if sync_static_routes is not UNSET:
            field_dict["sync_static_routes"] = sync_static_routes
        if sync_wol is not UNSET:
            field_dict["sync_wol"] = sync_wol
        if sync_virtual_ips is not UNSET:
            field_dict["sync_virtual_ips"] = sync_virtual_ips
        if sync_traffic_shaper is not UNSET:
            field_dict["sync_traffic_shaper"] = sync_traffic_shaper
        if sync_traffic_shaper_limiters is not UNSET:
            field_dict["sync_traffic_shaper_limiters"] = sync_traffic_shaper_limiters
        if sync_dns is not UNSET:
            field_dict["sync_dns"] = sync_dns
        if sync_cap_portal is not UNSET:
            field_dict["sync_cap_portal"] = sync_cap_portal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_to_ip = d.pop("sync_to_ip", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        sync_admin_acct = d.pop("sync_admin_acct", UNSET)

        sync_users = d.pop("sync_users", UNSET)

        sync_auth_servers = d.pop("sync_auth_servers", UNSET)

        sync_certs = d.pop("sync_certs", UNSET)

        sync_fw_rules = d.pop("sync_fw_rules", UNSET)

        sync_fw_schedules = d.pop("sync_fw_schedules", UNSET)

        sync_fw_aliases = d.pop("sync_fw_aliases", UNSET)

        sync_nat = d.pop("sync_nat", UNSET)

        sync_ipsec = d.pop("sync_ipsec", UNSET)

        sync_ovpn = d.pop("sync_ovpn", UNSET)

        sync_dhcp_server = d.pop("sync_dhcp_server", UNSET)

        sync_dhcp_relay = d.pop("sync_dhcp_relay", UNSET)

        sync_dhcp6_server = d.pop("sync_dhcp6_server", UNSET)

        sync_dhcp6_relay = d.pop("sync_dhcp6_relay", UNSET)

        sync_static_routes = d.pop("sync_static_routes", UNSET)

        sync_wol = d.pop("sync_wol", UNSET)

        sync_virtual_ips = d.pop("sync_virtual_ips", UNSET)

        sync_traffic_shaper = d.pop("sync_traffic_shaper", UNSET)

        sync_traffic_shaper_limiters = d.pop("sync_traffic_shaper_limiters", UNSET)

        sync_dns = d.pop("sync_dns", UNSET)

        sync_cap_portal = d.pop("sync_cap_portal", UNSET)

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
