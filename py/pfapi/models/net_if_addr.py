from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NetIfAddr")


@_attrs_define
class NetIfAddr:
    """
    Attributes:
        ipaddr (str):
        gateway_ip (str):
        gateway_name (str):
        alias_address (str):
        ipaddrv6 (str):
        default_gw6 (bool):
        gateway_ip6 (str):
        gateway_descr6 (str):
        gateway_name6 (str):
        ipv6_usev4_iface (bool):
        slaac_usev4_iface (bool):
    """

    ipaddr: str
    gateway_ip: str
    gateway_name: str
    alias_address: str
    ipaddrv6: str
    default_gw6: bool
    gateway_ip6: str
    gateway_descr6: str
    gateway_name6: str
    ipv6_usev4_iface: bool
    slaac_usev4_iface: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ipaddr = self.ipaddr

        gateway_ip = self.gateway_ip

        gateway_name = self.gateway_name

        alias_address = self.alias_address

        ipaddrv6 = self.ipaddrv6

        default_gw6 = self.default_gw6

        gateway_ip6 = self.gateway_ip6

        gateway_descr6 = self.gateway_descr6

        gateway_name6 = self.gateway_name6

        ipv6_usev4_iface = self.ipv6_usev4_iface

        slaac_usev4_iface = self.slaac_usev4_iface

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipaddr": ipaddr,
                "gateway_ip": gateway_ip,
                "gateway_name": gateway_name,
                "alias_address": alias_address,
                "ipaddrv6": ipaddrv6,
                "default_gw6": default_gw6,
                "gateway_ip6": gateway_ip6,
                "gateway_descr6": gateway_descr6,
                "gateway_name6": gateway_name6,
                "ipv6_usev4_iface": ipv6_usev4_iface,
                "slaac_usev4_iface": slaac_usev4_iface,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ipaddr = d.pop("ipaddr")

        gateway_ip = d.pop("gateway_ip")

        gateway_name = d.pop("gateway_name")

        alias_address = d.pop("alias_address")

        ipaddrv6 = d.pop("ipaddrv6")

        default_gw6 = d.pop("default_gw6")

        gateway_ip6 = d.pop("gateway_ip6")

        gateway_descr6 = d.pop("gateway_descr6")

        gateway_name6 = d.pop("gateway_name6")

        ipv6_usev4_iface = d.pop("ipv6_usev4_iface")

        slaac_usev4_iface = d.pop("slaac_usev4_iface")

        net_if_addr = cls(
            ipaddr=ipaddr,
            gateway_ip=gateway_ip,
            gateway_name=gateway_name,
            alias_address=alias_address,
            ipaddrv6=ipaddrv6,
            default_gw6=default_gw6,
            gateway_ip6=gateway_ip6,
            gateway_descr6=gateway_descr6,
            gateway_name6=gateway_name6,
            ipv6_usev4_iface=ipv6_usev4_iface,
            slaac_usev4_iface=slaac_usev4_iface,
        )

        net_if_addr.additional_properties = d
        return net_if_addr

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
