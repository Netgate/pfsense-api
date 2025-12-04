from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvNetworkSetting")


@_attrs_define
class AdvNetworkSetting:
    """
    Attributes:
        disablechecksumoffloading (bool | Unset):
        disablesegmentationoffloading (bool | Unset):
        disablelargereceiveoffloading (bool | Unset):
        dhcp6debug (bool | Unset):
        dhcp6norelease (bool | Unset):
        hnaltqenable (bool | Unset):
        ignoreiscwarning (bool | Unset):
        ip_change_kill_states (bool | Unset):
        ipv6allow (bool | Unset):
        ipv6dontcreatelocaldns (bool | Unset):
        ipv6nat_enable (bool | Unset):
        prefer_ipv4 (bool | Unset):
        sharednet (bool | Unset):
        radvddebug (bool | Unset):
        duid (str | Unset):
        global_v6duid (str | Unset):
        ipv6duiden_en (str | Unset):
        ipv6duiden_id (str | Unset):
        ipv6duidll (str | Unset):
        ipv6duidllt_ll (str | Unset):
        ipv6duidllt_time (str | Unset):
        ipv6duidtype (str | Unset):
        ipv6duiduuid (str | Unset):
        ipv6nat_ipaddr (str | Unset):
        dhcpbackend (str | Unset):
        use_if_pppoe (bool | Unset):
    """

    disablechecksumoffloading: bool | Unset = UNSET
    disablesegmentationoffloading: bool | Unset = UNSET
    disablelargereceiveoffloading: bool | Unset = UNSET
    dhcp6debug: bool | Unset = UNSET
    dhcp6norelease: bool | Unset = UNSET
    hnaltqenable: bool | Unset = UNSET
    ignoreiscwarning: bool | Unset = UNSET
    ip_change_kill_states: bool | Unset = UNSET
    ipv6allow: bool | Unset = UNSET
    ipv6dontcreatelocaldns: bool | Unset = UNSET
    ipv6nat_enable: bool | Unset = UNSET
    prefer_ipv4: bool | Unset = UNSET
    sharednet: bool | Unset = UNSET
    radvddebug: bool | Unset = UNSET
    duid: str | Unset = UNSET
    global_v6duid: str | Unset = UNSET
    ipv6duiden_en: str | Unset = UNSET
    ipv6duiden_id: str | Unset = UNSET
    ipv6duidll: str | Unset = UNSET
    ipv6duidllt_ll: str | Unset = UNSET
    ipv6duidllt_time: str | Unset = UNSET
    ipv6duidtype: str | Unset = UNSET
    ipv6duiduuid: str | Unset = UNSET
    ipv6nat_ipaddr: str | Unset = UNSET
    dhcpbackend: str | Unset = UNSET
    use_if_pppoe: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disablechecksumoffloading = self.disablechecksumoffloading

        disablesegmentationoffloading = self.disablesegmentationoffloading

        disablelargereceiveoffloading = self.disablelargereceiveoffloading

        dhcp6debug = self.dhcp6debug

        dhcp6norelease = self.dhcp6norelease

        hnaltqenable = self.hnaltqenable

        ignoreiscwarning = self.ignoreiscwarning

        ip_change_kill_states = self.ip_change_kill_states

        ipv6allow = self.ipv6allow

        ipv6dontcreatelocaldns = self.ipv6dontcreatelocaldns

        ipv6nat_enable = self.ipv6nat_enable

        prefer_ipv4 = self.prefer_ipv4

        sharednet = self.sharednet

        radvddebug = self.radvddebug

        duid = self.duid

        global_v6duid = self.global_v6duid

        ipv6duiden_en = self.ipv6duiden_en

        ipv6duiden_id = self.ipv6duiden_id

        ipv6duidll = self.ipv6duidll

        ipv6duidllt_ll = self.ipv6duidllt_ll

        ipv6duidllt_time = self.ipv6duidllt_time

        ipv6duidtype = self.ipv6duidtype

        ipv6duiduuid = self.ipv6duiduuid

        ipv6nat_ipaddr = self.ipv6nat_ipaddr

        dhcpbackend = self.dhcpbackend

        use_if_pppoe = self.use_if_pppoe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disablechecksumoffloading is not UNSET:
            field_dict["disablechecksumoffloading"] = disablechecksumoffloading
        if disablesegmentationoffloading is not UNSET:
            field_dict["disablesegmentationoffloading"] = disablesegmentationoffloading
        if disablelargereceiveoffloading is not UNSET:
            field_dict["disablelargereceiveoffloading"] = disablelargereceiveoffloading
        if dhcp6debug is not UNSET:
            field_dict["dhcp6debug"] = dhcp6debug
        if dhcp6norelease is not UNSET:
            field_dict["dhcp6norelease"] = dhcp6norelease
        if hnaltqenable is not UNSET:
            field_dict["hnaltqenable"] = hnaltqenable
        if ignoreiscwarning is not UNSET:
            field_dict["ignoreiscwarning"] = ignoreiscwarning
        if ip_change_kill_states is not UNSET:
            field_dict["ip_change_kill_states"] = ip_change_kill_states
        if ipv6allow is not UNSET:
            field_dict["ipv6allow"] = ipv6allow
        if ipv6dontcreatelocaldns is not UNSET:
            field_dict["ipv6dontcreatelocaldns"] = ipv6dontcreatelocaldns
        if ipv6nat_enable is not UNSET:
            field_dict["ipv6nat_enable"] = ipv6nat_enable
        if prefer_ipv4 is not UNSET:
            field_dict["prefer_ipv4"] = prefer_ipv4
        if sharednet is not UNSET:
            field_dict["sharednet"] = sharednet
        if radvddebug is not UNSET:
            field_dict["radvddebug"] = radvddebug
        if duid is not UNSET:
            field_dict["duid"] = duid
        if global_v6duid is not UNSET:
            field_dict["global_v6duid"] = global_v6duid
        if ipv6duiden_en is not UNSET:
            field_dict["ipv6duiden_en"] = ipv6duiden_en
        if ipv6duiden_id is not UNSET:
            field_dict["ipv6duiden_id"] = ipv6duiden_id
        if ipv6duidll is not UNSET:
            field_dict["ipv6duidll"] = ipv6duidll
        if ipv6duidllt_ll is not UNSET:
            field_dict["ipv6duidllt_ll"] = ipv6duidllt_ll
        if ipv6duidllt_time is not UNSET:
            field_dict["ipv6duidllt_time"] = ipv6duidllt_time
        if ipv6duidtype is not UNSET:
            field_dict["ipv6duidtype"] = ipv6duidtype
        if ipv6duiduuid is not UNSET:
            field_dict["ipv6duiduuid"] = ipv6duiduuid
        if ipv6nat_ipaddr is not UNSET:
            field_dict["ipv6nat_ipaddr"] = ipv6nat_ipaddr
        if dhcpbackend is not UNSET:
            field_dict["dhcpbackend"] = dhcpbackend
        if use_if_pppoe is not UNSET:
            field_dict["use_if_pppoe"] = use_if_pppoe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disablechecksumoffloading = d.pop("disablechecksumoffloading", UNSET)

        disablesegmentationoffloading = d.pop("disablesegmentationoffloading", UNSET)

        disablelargereceiveoffloading = d.pop("disablelargereceiveoffloading", UNSET)

        dhcp6debug = d.pop("dhcp6debug", UNSET)

        dhcp6norelease = d.pop("dhcp6norelease", UNSET)

        hnaltqenable = d.pop("hnaltqenable", UNSET)

        ignoreiscwarning = d.pop("ignoreiscwarning", UNSET)

        ip_change_kill_states = d.pop("ip_change_kill_states", UNSET)

        ipv6allow = d.pop("ipv6allow", UNSET)

        ipv6dontcreatelocaldns = d.pop("ipv6dontcreatelocaldns", UNSET)

        ipv6nat_enable = d.pop("ipv6nat_enable", UNSET)

        prefer_ipv4 = d.pop("prefer_ipv4", UNSET)

        sharednet = d.pop("sharednet", UNSET)

        radvddebug = d.pop("radvddebug", UNSET)

        duid = d.pop("duid", UNSET)

        global_v6duid = d.pop("global_v6duid", UNSET)

        ipv6duiden_en = d.pop("ipv6duiden_en", UNSET)

        ipv6duiden_id = d.pop("ipv6duiden_id", UNSET)

        ipv6duidll = d.pop("ipv6duidll", UNSET)

        ipv6duidllt_ll = d.pop("ipv6duidllt_ll", UNSET)

        ipv6duidllt_time = d.pop("ipv6duidllt_time", UNSET)

        ipv6duidtype = d.pop("ipv6duidtype", UNSET)

        ipv6duiduuid = d.pop("ipv6duiduuid", UNSET)

        ipv6nat_ipaddr = d.pop("ipv6nat_ipaddr", UNSET)

        dhcpbackend = d.pop("dhcpbackend", UNSET)

        use_if_pppoe = d.pop("use_if_pppoe", UNSET)

        adv_network_setting = cls(
            disablechecksumoffloading=disablechecksumoffloading,
            disablesegmentationoffloading=disablesegmentationoffloading,
            disablelargereceiveoffloading=disablelargereceiveoffloading,
            dhcp6debug=dhcp6debug,
            dhcp6norelease=dhcp6norelease,
            hnaltqenable=hnaltqenable,
            ignoreiscwarning=ignoreiscwarning,
            ip_change_kill_states=ip_change_kill_states,
            ipv6allow=ipv6allow,
            ipv6dontcreatelocaldns=ipv6dontcreatelocaldns,
            ipv6nat_enable=ipv6nat_enable,
            prefer_ipv4=prefer_ipv4,
            sharednet=sharednet,
            radvddebug=radvddebug,
            duid=duid,
            global_v6duid=global_v6duid,
            ipv6duiden_en=ipv6duiden_en,
            ipv6duiden_id=ipv6duiden_id,
            ipv6duidll=ipv6duidll,
            ipv6duidllt_ll=ipv6duidllt_ll,
            ipv6duidllt_time=ipv6duidllt_time,
            ipv6duidtype=ipv6duidtype,
            ipv6duiduuid=ipv6duiduuid,
            ipv6nat_ipaddr=ipv6nat_ipaddr,
            dhcpbackend=dhcpbackend,
            use_if_pppoe=use_if_pppoe,
        )

        adv_network_setting.additional_properties = d
        return adv_network_setting

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
