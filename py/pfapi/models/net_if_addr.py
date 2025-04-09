from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetIfAddr")


@_attrs_define
class NetIfAddr:
    """
    Attributes:
        ipaddr (Union[Unset, str]):
        gateway_ip (Union[Unset, str]):
        gateway_name (Union[Unset, str]):
        alias_address (Union[Unset, str]):
        ipaddrv6 (Union[Unset, str]):
        default_gw6 (Union[Unset, bool]):
        gateway_ip6 (Union[Unset, str]):
        gateway_descr6 (Union[Unset, str]):
        gateway_name6 (Union[Unset, str]):
        ipv6_usev4_iface (Union[Unset, bool]):
        slaac_usev4_iface (Union[Unset, bool]):
    """

    ipaddr: Union[Unset, str] = UNSET
    gateway_ip: Union[Unset, str] = UNSET
    gateway_name: Union[Unset, str] = UNSET
    alias_address: Union[Unset, str] = UNSET
    ipaddrv6: Union[Unset, str] = UNSET
    default_gw6: Union[Unset, bool] = UNSET
    gateway_ip6: Union[Unset, str] = UNSET
    gateway_descr6: Union[Unset, str] = UNSET
    gateway_name6: Union[Unset, str] = UNSET
    ipv6_usev4_iface: Union[Unset, bool] = UNSET
    slaac_usev4_iface: Union[Unset, bool] = UNSET
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
        field_dict.update({})
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if gateway_ip is not UNSET:
            field_dict["gateway_ip"] = gateway_ip
        if gateway_name is not UNSET:
            field_dict["gateway_name"] = gateway_name
        if alias_address is not UNSET:
            field_dict["alias_address"] = alias_address
        if ipaddrv6 is not UNSET:
            field_dict["ipaddrv6"] = ipaddrv6
        if default_gw6 is not UNSET:
            field_dict["default_gw6"] = default_gw6
        if gateway_ip6 is not UNSET:
            field_dict["gateway_ip6"] = gateway_ip6
        if gateway_descr6 is not UNSET:
            field_dict["gateway_descr6"] = gateway_descr6
        if gateway_name6 is not UNSET:
            field_dict["gateway_name6"] = gateway_name6
        if ipv6_usev4_iface is not UNSET:
            field_dict["ipv6_usev4_iface"] = ipv6_usev4_iface
        if slaac_usev4_iface is not UNSET:
            field_dict["slaac_usev4_iface"] = slaac_usev4_iface

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ipaddr = d.pop("ipaddr", UNSET)

        gateway_ip = d.pop("gateway_ip", UNSET)

        gateway_name = d.pop("gateway_name", UNSET)

        alias_address = d.pop("alias_address", UNSET)

        ipaddrv6 = d.pop("ipaddrv6", UNSET)

        default_gw6 = d.pop("default_gw6", UNSET)

        gateway_ip6 = d.pop("gateway_ip6", UNSET)

        gateway_descr6 = d.pop("gateway_descr6", UNSET)

        gateway_name6 = d.pop("gateway_name6", UNSET)

        ipv6_usev4_iface = d.pop("ipv6_usev4_iface", UNSET)

        slaac_usev4_iface = d.pop("slaac_usev4_iface", UNSET)

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
