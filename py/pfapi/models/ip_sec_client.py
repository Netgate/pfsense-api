from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecClient")


@_attrs_define
class IPSecClient:
    """
    Attributes:
        enable (Union[Unset, bool]):
        radiusaccounting (Union[Unset, bool]):
        user_source (Union[Unset, str]):
        user_source_array (Union[Unset, List[str]]):
        group_source (Union[Unset, bool]):
        auth_groups (Union[Unset, str]):
        auth_groups_array (Union[Unset, List[str]]):
        pool_address (Union[Unset, str]):
        pool_netbits (Union[Unset, str]):
        pool_address_v6 (Union[Unset, str]):
        pool_netbits_v6 (Union[Unset, str]):
        net_list (Union[Unset, bool]):
        save_passwd (Union[Unset, bool]):
        dns_domain (Union[Unset, str]):
        dns_split (Union[Unset, str]):
        dns_server1 (Union[Unset, str]):
        dns_server2 (Union[Unset, str]):
        dns_server3 (Union[Unset, str]):
        dns_server4 (Union[Unset, str]):
        wins_server1 (Union[Unset, str]):
        wins_server2 (Union[Unset, str]):
        pfs_group (Union[Unset, str]):
        login_banner (Union[Unset, str]):
        radius_ip_priority_enable (Union[Unset, bool]):
        radius_retransmit_base (Union[Unset, str]):
        radius_retransmit_timeout (Union[Unset, str]):
        radius_retransmit_tries (Union[Unset, str]):
        radius_sockets (Union[Unset, str]):
    """

    enable: Union[Unset, bool] = UNSET
    radiusaccounting: Union[Unset, bool] = UNSET
    user_source: Union[Unset, str] = UNSET
    user_source_array: Union[Unset, List[str]] = UNSET
    group_source: Union[Unset, bool] = UNSET
    auth_groups: Union[Unset, str] = UNSET
    auth_groups_array: Union[Unset, List[str]] = UNSET
    pool_address: Union[Unset, str] = UNSET
    pool_netbits: Union[Unset, str] = UNSET
    pool_address_v6: Union[Unset, str] = UNSET
    pool_netbits_v6: Union[Unset, str] = UNSET
    net_list: Union[Unset, bool] = UNSET
    save_passwd: Union[Unset, bool] = UNSET
    dns_domain: Union[Unset, str] = UNSET
    dns_split: Union[Unset, str] = UNSET
    dns_server1: Union[Unset, str] = UNSET
    dns_server2: Union[Unset, str] = UNSET
    dns_server3: Union[Unset, str] = UNSET
    dns_server4: Union[Unset, str] = UNSET
    wins_server1: Union[Unset, str] = UNSET
    wins_server2: Union[Unset, str] = UNSET
    pfs_group: Union[Unset, str] = UNSET
    login_banner: Union[Unset, str] = UNSET
    radius_ip_priority_enable: Union[Unset, bool] = UNSET
    radius_retransmit_base: Union[Unset, str] = UNSET
    radius_retransmit_timeout: Union[Unset, str] = UNSET
    radius_retransmit_tries: Union[Unset, str] = UNSET
    radius_sockets: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        radiusaccounting = self.radiusaccounting

        user_source = self.user_source

        user_source_array: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_source_array, Unset):
            user_source_array = self.user_source_array

        group_source = self.group_source

        auth_groups = self.auth_groups

        auth_groups_array: Union[Unset, List[str]] = UNSET
        if not isinstance(self.auth_groups_array, Unset):
            auth_groups_array = self.auth_groups_array

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if radiusaccounting is not UNSET:
            field_dict["radiusaccounting"] = radiusaccounting
        if user_source is not UNSET:
            field_dict["user_source"] = user_source
        if user_source_array is not UNSET:
            field_dict["user_source_array"] = user_source_array
        if group_source is not UNSET:
            field_dict["group_source"] = group_source
        if auth_groups is not UNSET:
            field_dict["auth_groups"] = auth_groups
        if auth_groups_array is not UNSET:
            field_dict["auth_groups_array"] = auth_groups_array
        if pool_address is not UNSET:
            field_dict["pool_address"] = pool_address
        if pool_netbits is not UNSET:
            field_dict["pool_netbits"] = pool_netbits
        if pool_address_v6 is not UNSET:
            field_dict["pool_address_v6"] = pool_address_v6
        if pool_netbits_v6 is not UNSET:
            field_dict["pool_netbits_v6"] = pool_netbits_v6
        if net_list is not UNSET:
            field_dict["net_list"] = net_list
        if save_passwd is not UNSET:
            field_dict["save_passwd"] = save_passwd
        if dns_domain is not UNSET:
            field_dict["dns_domain"] = dns_domain
        if dns_split is not UNSET:
            field_dict["dns_split"] = dns_split
        if dns_server1 is not UNSET:
            field_dict["dns_server1"] = dns_server1
        if dns_server2 is not UNSET:
            field_dict["dns_server2"] = dns_server2
        if dns_server3 is not UNSET:
            field_dict["dns_server3"] = dns_server3
        if dns_server4 is not UNSET:
            field_dict["dns_server4"] = dns_server4
        if wins_server1 is not UNSET:
            field_dict["wins_server1"] = wins_server1
        if wins_server2 is not UNSET:
            field_dict["wins_server2"] = wins_server2
        if pfs_group is not UNSET:
            field_dict["pfs_group"] = pfs_group
        if login_banner is not UNSET:
            field_dict["login_banner"] = login_banner
        if radius_ip_priority_enable is not UNSET:
            field_dict["radius_ip_priority_enable"] = radius_ip_priority_enable
        if radius_retransmit_base is not UNSET:
            field_dict["radius_retransmit_base"] = radius_retransmit_base
        if radius_retransmit_timeout is not UNSET:
            field_dict["radius_retransmit_timeout"] = radius_retransmit_timeout
        if radius_retransmit_tries is not UNSET:
            field_dict["radius_retransmit_tries"] = radius_retransmit_tries
        if radius_sockets is not UNSET:
            field_dict["radius_sockets"] = radius_sockets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        radiusaccounting = d.pop("radiusaccounting", UNSET)

        user_source = d.pop("user_source", UNSET)

        user_source_array = cast(List[str], d.pop("user_source_array", UNSET))

        group_source = d.pop("group_source", UNSET)

        auth_groups = d.pop("auth_groups", UNSET)

        auth_groups_array = cast(List[str], d.pop("auth_groups_array", UNSET))

        pool_address = d.pop("pool_address", UNSET)

        pool_netbits = d.pop("pool_netbits", UNSET)

        pool_address_v6 = d.pop("pool_address_v6", UNSET)

        pool_netbits_v6 = d.pop("pool_netbits_v6", UNSET)

        net_list = d.pop("net_list", UNSET)

        save_passwd = d.pop("save_passwd", UNSET)

        dns_domain = d.pop("dns_domain", UNSET)

        dns_split = d.pop("dns_split", UNSET)

        dns_server1 = d.pop("dns_server1", UNSET)

        dns_server2 = d.pop("dns_server2", UNSET)

        dns_server3 = d.pop("dns_server3", UNSET)

        dns_server4 = d.pop("dns_server4", UNSET)

        wins_server1 = d.pop("wins_server1", UNSET)

        wins_server2 = d.pop("wins_server2", UNSET)

        pfs_group = d.pop("pfs_group", UNSET)

        login_banner = d.pop("login_banner", UNSET)

        radius_ip_priority_enable = d.pop("radius_ip_priority_enable", UNSET)

        radius_retransmit_base = d.pop("radius_retransmit_base", UNSET)

        radius_retransmit_timeout = d.pop("radius_retransmit_timeout", UNSET)

        radius_retransmit_tries = d.pop("radius_retransmit_tries", UNSET)

        radius_sockets = d.pop("radius_sockets", UNSET)

        ip_sec_client = cls(
            enable=enable,
            radiusaccounting=radiusaccounting,
            user_source=user_source,
            user_source_array=user_source_array,
            group_source=group_source,
            auth_groups=auth_groups,
            auth_groups_array=auth_groups_array,
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
