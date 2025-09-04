from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.intf_router_adv_setting_mode import IntfRouterAdvSettingMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="IntfRouterAdvSetting")


@_attrs_define
class IntfRouterAdvSetting:
    """
    Attributes:
        assigned_interface (str): assigned name of network interface
        mode (IntfRouterAdvSettingMode): disabled, router, unmanaged, managed, assist, stateless_dhcp
        priority (Union[Unset, str]): low, normal, high
        lifetime_secs (Union[Unset, int]): length of time in seconds, default is 86400
        pref_lifetime_secs (Union[Unset, int]): length of time from SLAAC addresses remain preferred, default 14400
        min_ra_interval (Union[Unset, int]): minimum time allowed between sending unsolicited multicast RA in seconds,
            default 200
        max_ra_interval (Union[Unset, int]): maximum time allowed between sending unsolicited multicast RA in seconds,
            default 600
        router_lifetime (Union[Unset, int]): lifetime associated wi th default router in seconds, default 3x max RA
        nat64_enable (Union[Unset, bool]): advertise a NAT64 prefix
        nat64_prefix (Union[Unset, str]): NAT 64 prefix to enable PREF64 support
        nat64_prefix_life (Union[Unset, int]): length of time in seconds that the prefix is valid for NAT64, default is
            3x RA
        ra_subnets (Union[Unset, List[str]]):
        enable_dns (Union[Unset, bool]): provide DNS configuration via RA service
        mirror_dhcp6 (Union[Unset, bool]): copy DNS configuration from primary DHCPv6 options
        dns_servers (Union[Unset, List[str]]):
        dns_searchlist (Union[Unset, List[str]]):
    """

    assigned_interface: str
    mode: IntfRouterAdvSettingMode
    priority: Union[Unset, str] = UNSET
    lifetime_secs: Union[Unset, int] = UNSET
    pref_lifetime_secs: Union[Unset, int] = UNSET
    min_ra_interval: Union[Unset, int] = UNSET
    max_ra_interval: Union[Unset, int] = UNSET
    router_lifetime: Union[Unset, int] = UNSET
    nat64_enable: Union[Unset, bool] = UNSET
    nat64_prefix: Union[Unset, str] = UNSET
    nat64_prefix_life: Union[Unset, int] = UNSET
    ra_subnets: Union[Unset, List[str]] = UNSET
    enable_dns: Union[Unset, bool] = UNSET
    mirror_dhcp6: Union[Unset, bool] = UNSET
    dns_servers: Union[Unset, List[str]] = UNSET
    dns_searchlist: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assigned_interface = self.assigned_interface

        mode = self.mode.value

        priority = self.priority

        lifetime_secs = self.lifetime_secs

        pref_lifetime_secs = self.pref_lifetime_secs

        min_ra_interval = self.min_ra_interval

        max_ra_interval = self.max_ra_interval

        router_lifetime = self.router_lifetime

        nat64_enable = self.nat64_enable

        nat64_prefix = self.nat64_prefix

        nat64_prefix_life = self.nat64_prefix_life

        ra_subnets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ra_subnets, Unset):
            ra_subnets = self.ra_subnets

        enable_dns = self.enable_dns

        mirror_dhcp6 = self.mirror_dhcp6

        dns_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        dns_searchlist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dns_searchlist, Unset):
            dns_searchlist = self.dns_searchlist

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assigned_interface": assigned_interface,
                "mode": mode,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if lifetime_secs is not UNSET:
            field_dict["lifetime_secs"] = lifetime_secs
        if pref_lifetime_secs is not UNSET:
            field_dict["pref_lifetime_secs"] = pref_lifetime_secs
        if min_ra_interval is not UNSET:
            field_dict["min_ra_interval"] = min_ra_interval
        if max_ra_interval is not UNSET:
            field_dict["max_ra_interval"] = max_ra_interval
        if router_lifetime is not UNSET:
            field_dict["router_lifetime"] = router_lifetime
        if nat64_enable is not UNSET:
            field_dict["nat64_enable"] = nat64_enable
        if nat64_prefix is not UNSET:
            field_dict["nat64_prefix"] = nat64_prefix
        if nat64_prefix_life is not UNSET:
            field_dict["nat64_prefix_life"] = nat64_prefix_life
        if ra_subnets is not UNSET:
            field_dict["ra_subnets"] = ra_subnets
        if enable_dns is not UNSET:
            field_dict["enable_dns"] = enable_dns
        if mirror_dhcp6 is not UNSET:
            field_dict["mirror_dhcp6"] = mirror_dhcp6
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers
        if dns_searchlist is not UNSET:
            field_dict["dns_searchlist"] = dns_searchlist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assigned_interface = d.pop("assigned_interface")

        mode = IntfRouterAdvSettingMode(d.pop("mode"))

        priority = d.pop("priority", UNSET)

        lifetime_secs = d.pop("lifetime_secs", UNSET)

        pref_lifetime_secs = d.pop("pref_lifetime_secs", UNSET)

        min_ra_interval = d.pop("min_ra_interval", UNSET)

        max_ra_interval = d.pop("max_ra_interval", UNSET)

        router_lifetime = d.pop("router_lifetime", UNSET)

        nat64_enable = d.pop("nat64_enable", UNSET)

        nat64_prefix = d.pop("nat64_prefix", UNSET)

        nat64_prefix_life = d.pop("nat64_prefix_life", UNSET)

        ra_subnets = cast(List[str], d.pop("ra_subnets", UNSET))

        enable_dns = d.pop("enable_dns", UNSET)

        mirror_dhcp6 = d.pop("mirror_dhcp6", UNSET)

        dns_servers = cast(List[str], d.pop("dns_servers", UNSET))

        dns_searchlist = cast(List[str], d.pop("dns_searchlist", UNSET))

        intf_router_adv_setting = cls(
            assigned_interface=assigned_interface,
            mode=mode,
            priority=priority,
            lifetime_secs=lifetime_secs,
            pref_lifetime_secs=pref_lifetime_secs,
            min_ra_interval=min_ra_interval,
            max_ra_interval=max_ra_interval,
            router_lifetime=router_lifetime,
            nat64_enable=nat64_enable,
            nat64_prefix=nat64_prefix,
            nat64_prefix_life=nat64_prefix_life,
            ra_subnets=ra_subnets,
            enable_dns=enable_dns,
            mirror_dhcp6=mirror_dhcp6,
            dns_servers=dns_servers,
            dns_searchlist=dns_searchlist,
        )

        intf_router_adv_setting.additional_properties = d
        return intf_router_adv_setting

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
