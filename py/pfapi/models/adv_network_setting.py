from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdvNetworkSetting")


@_attrs_define
class AdvNetworkSetting:
    """
    Attributes:
        disablechecksumoffloading (bool):
        disablesegmentationoffloading (bool):
        disablelargereceiveoffloading (bool):
        dhcp6debug (bool):
        dhcp6norelease (bool):
        hnaltqenable (bool):
        ignoreiscwarning (bool):
        ip_change_kill_states (bool):
        ipv6allow (bool):
        ipv6dontcreatelocaldns (bool):
        ipv6nat_enable (bool):
        prefer_ipv4 (bool):
        sharednet (bool):
        duid (str):
        global_v6duid (str):
        ipv6duiden_en (str):
        ipv6duiden_id (str):
        ipv6duidll (str):
        ipv6duidllt_ll (str):
        ipv6duidllt_time (str):
        ipv6duidtype (str):
        ipv6duiduuid (str):
        ipv6nat_ipaddr (str):
        dhcpbackend (str):
    """

    disablechecksumoffloading: bool
    disablesegmentationoffloading: bool
    disablelargereceiveoffloading: bool
    dhcp6debug: bool
    dhcp6norelease: bool
    hnaltqenable: bool
    ignoreiscwarning: bool
    ip_change_kill_states: bool
    ipv6allow: bool
    ipv6dontcreatelocaldns: bool
    ipv6nat_enable: bool
    prefer_ipv4: bool
    sharednet: bool
    duid: str
    global_v6duid: str
    ipv6duiden_en: str
    ipv6duiden_id: str
    ipv6duidll: str
    ipv6duidllt_ll: str
    ipv6duidllt_time: str
    ipv6duidtype: str
    ipv6duiduuid: str
    ipv6nat_ipaddr: str
    dhcpbackend: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disablechecksumoffloading": disablechecksumoffloading,
                "disablesegmentationoffloading": disablesegmentationoffloading,
                "disablelargereceiveoffloading": disablelargereceiveoffloading,
                "dhcp6debug": dhcp6debug,
                "dhcp6norelease": dhcp6norelease,
                "hnaltqenable": hnaltqenable,
                "ignoreiscwarning": ignoreiscwarning,
                "ip_change_kill_states": ip_change_kill_states,
                "ipv6allow": ipv6allow,
                "ipv6dontcreatelocaldns": ipv6dontcreatelocaldns,
                "ipv6nat_enable": ipv6nat_enable,
                "prefer_ipv4": prefer_ipv4,
                "sharednet": sharednet,
                "duid": duid,
                "global_v6duid": global_v6duid,
                "ipv6duiden_en": ipv6duiden_en,
                "ipv6duiden_id": ipv6duiden_id,
                "ipv6duidll": ipv6duidll,
                "ipv6duidllt_ll": ipv6duidllt_ll,
                "ipv6duidllt_time": ipv6duidllt_time,
                "ipv6duidtype": ipv6duidtype,
                "ipv6duiduuid": ipv6duiduuid,
                "ipv6nat_ipaddr": ipv6nat_ipaddr,
                "dhcpbackend": dhcpbackend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disablechecksumoffloading = d.pop("disablechecksumoffloading")

        disablesegmentationoffloading = d.pop("disablesegmentationoffloading")

        disablelargereceiveoffloading = d.pop("disablelargereceiveoffloading")

        dhcp6debug = d.pop("dhcp6debug")

        dhcp6norelease = d.pop("dhcp6norelease")

        hnaltqenable = d.pop("hnaltqenable")

        ignoreiscwarning = d.pop("ignoreiscwarning")

        ip_change_kill_states = d.pop("ip_change_kill_states")

        ipv6allow = d.pop("ipv6allow")

        ipv6dontcreatelocaldns = d.pop("ipv6dontcreatelocaldns")

        ipv6nat_enable = d.pop("ipv6nat_enable")

        prefer_ipv4 = d.pop("prefer_ipv4")

        sharednet = d.pop("sharednet")

        duid = d.pop("duid")

        global_v6duid = d.pop("global_v6duid")

        ipv6duiden_en = d.pop("ipv6duiden_en")

        ipv6duiden_id = d.pop("ipv6duiden_id")

        ipv6duidll = d.pop("ipv6duidll")

        ipv6duidllt_ll = d.pop("ipv6duidllt_ll")

        ipv6duidllt_time = d.pop("ipv6duidllt_time")

        ipv6duidtype = d.pop("ipv6duidtype")

        ipv6duiduuid = d.pop("ipv6duiduuid")

        ipv6nat_ipaddr = d.pop("ipv6nat_ipaddr")

        dhcpbackend = d.pop("dhcpbackend")

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
        )

        adv_network_setting.additional_properties = d
        return adv_network_setting

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
