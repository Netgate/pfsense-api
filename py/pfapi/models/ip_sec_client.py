from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecClient")


@_attrs_define
class IPSecClient:
    """
    Attributes:
        enable (bool):
        radiusaccounting (bool):
        user_source (str):
        group_source (bool):
        auth_groups (str):
        pool_address (str):
        pool_netbits (str):
        pool_address_v6 (str):
        pool_netbits_v6 (str):
        net_list (bool):
        save_passwd (bool):
        dns_domain (str):
        dns_split (str):
        dns_server1 (str):
        dns_server2 (str):
        dns_server3 (str):
        dns_server4 (str):
        wins_server1 (str):
        wins_server2 (str):
        pfs_group (str):
        login_banner (str):
        radius_ip_priority_enable (bool):
        radius_retransmit_base (str):
        radius_retransmit_timeout (str):
        radius_retransmit_tries (str):
        radius_sockets (str):
        user_source_array (Union[Unset, List[str]]):
        auth_groups_array (Union[Unset, List[str]]):
    """

    enable: bool
    radiusaccounting: bool
    user_source: str
    group_source: bool
    auth_groups: str
    pool_address: str
    pool_netbits: str
    pool_address_v6: str
    pool_netbits_v6: str
    net_list: bool
    save_passwd: bool
    dns_domain: str
    dns_split: str
    dns_server1: str
    dns_server2: str
    dns_server3: str
    dns_server4: str
    wins_server1: str
    wins_server2: str
    pfs_group: str
    login_banner: str
    radius_ip_priority_enable: bool
    radius_retransmit_base: str
    radius_retransmit_timeout: str
    radius_retransmit_tries: str
    radius_sockets: str
    user_source_array: Union[Unset, List[str]] = UNSET
    auth_groups_array: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        radiusaccounting = self.radiusaccounting

        user_source = self.user_source

        group_source = self.group_source

        auth_groups = self.auth_groups

        pool_address = self.pool_address

        pool_netbits = self.pool_netbits

        pool_address_v6 = self.pool_address_v6

        pool_netbits_v6 = self.pool_netbits_v6

        net_list = self.net_list

        save_passwd = self.save_passwd

        dns_domain = self.dns_domain

        dns_split = self.dns_split

        dns_server1 = self.dns_server1

        dns_server2 = self.dns_server2

        dns_server3 = self.dns_server3

        dns_server4 = self.dns_server4

        wins_server1 = self.wins_server1

        wins_server2 = self.wins_server2

        pfs_group = self.pfs_group

        login_banner = self.login_banner

        radius_ip_priority_enable = self.radius_ip_priority_enable

        radius_retransmit_base = self.radius_retransmit_base

        radius_retransmit_timeout = self.radius_retransmit_timeout

        radius_retransmit_tries = self.radius_retransmit_tries

        radius_sockets = self.radius_sockets

        user_source_array: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_source_array, Unset):
            user_source_array = self.user_source_array

        auth_groups_array: Union[Unset, List[str]] = UNSET
        if not isinstance(self.auth_groups_array, Unset):
            auth_groups_array = self.auth_groups_array

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "radiusaccounting": radiusaccounting,
                "user_source": user_source,
                "group_source": group_source,
                "auth_groups": auth_groups,
                "pool_address": pool_address,
                "pool_netbits": pool_netbits,
                "pool_address_v6": pool_address_v6,
                "pool_netbits_v6": pool_netbits_v6,
                "net_list": net_list,
                "save_passwd": save_passwd,
                "dns_domain": dns_domain,
                "dns_split": dns_split,
                "dns_server1": dns_server1,
                "dns_server2": dns_server2,
                "dns_server3": dns_server3,
                "dns_server4": dns_server4,
                "wins_server1": wins_server1,
                "wins_server2": wins_server2,
                "pfs_group": pfs_group,
                "login_banner": login_banner,
                "radius_ip_priority_enable": radius_ip_priority_enable,
                "radius_retransmit_base": radius_retransmit_base,
                "radius_retransmit_timeout": radius_retransmit_timeout,
                "radius_retransmit_tries": radius_retransmit_tries,
                "radius_sockets": radius_sockets,
            }
        )
        if user_source_array is not UNSET:
            field_dict["user_source_array"] = user_source_array
        if auth_groups_array is not UNSET:
            field_dict["auth_groups_array"] = auth_groups_array

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        radiusaccounting = d.pop("radiusaccounting")

        user_source = d.pop("user_source")

        group_source = d.pop("group_source")

        auth_groups = d.pop("auth_groups")

        pool_address = d.pop("pool_address")

        pool_netbits = d.pop("pool_netbits")

        pool_address_v6 = d.pop("pool_address_v6")

        pool_netbits_v6 = d.pop("pool_netbits_v6")

        net_list = d.pop("net_list")

        save_passwd = d.pop("save_passwd")

        dns_domain = d.pop("dns_domain")

        dns_split = d.pop("dns_split")

        dns_server1 = d.pop("dns_server1")

        dns_server2 = d.pop("dns_server2")

        dns_server3 = d.pop("dns_server3")

        dns_server4 = d.pop("dns_server4")

        wins_server1 = d.pop("wins_server1")

        wins_server2 = d.pop("wins_server2")

        pfs_group = d.pop("pfs_group")

        login_banner = d.pop("login_banner")

        radius_ip_priority_enable = d.pop("radius_ip_priority_enable")

        radius_retransmit_base = d.pop("radius_retransmit_base")

        radius_retransmit_timeout = d.pop("radius_retransmit_timeout")

        radius_retransmit_tries = d.pop("radius_retransmit_tries")

        radius_sockets = d.pop("radius_sockets")

        user_source_array = cast(List[str], d.pop("user_source_array", UNSET))

        auth_groups_array = cast(List[str], d.pop("auth_groups_array", UNSET))

        ip_sec_client = cls(
            enable=enable,
            radiusaccounting=radiusaccounting,
            user_source=user_source,
            group_source=group_source,
            auth_groups=auth_groups,
            pool_address=pool_address,
            pool_netbits=pool_netbits,
            pool_address_v6=pool_address_v6,
            pool_netbits_v6=pool_netbits_v6,
            net_list=net_list,
            save_passwd=save_passwd,
            dns_domain=dns_domain,
            dns_split=dns_split,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            pfs_group=pfs_group,
            login_banner=login_banner,
            radius_ip_priority_enable=radius_ip_priority_enable,
            radius_retransmit_base=radius_retransmit_base,
            radius_retransmit_timeout=radius_retransmit_timeout,
            radius_retransmit_tries=radius_retransmit_tries,
            radius_sockets=radius_sockets,
            user_source_array=user_source_array,
            auth_groups_array=auth_groups_array,
        )

        ip_sec_client.additional_properties = d
        return ip_sec_client

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
