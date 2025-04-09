from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PPPLinkInterface")


@_attrs_define
class PPPLinkInterface:
    """
    Attributes:
        if_device (str): device name of the interface used for the link
        bandwidth (Union[Unset, int]):
        mtu (Union[Unset, int]):
        mru (Union[Unset, int]):
        mrru (Union[Unset, int]):
        localip (Union[Unset, str]): (type pptp and l2tp only) local ip address
        subnet (Union[Unset, int]): (type pptp and l2tp only) local ip address subnet
        gateway (Union[Unset, str]): (type pptp and l2tp only) gateway ip address or hostname
    """

    if_device: str
    bandwidth: Union[Unset, int] = UNSET
    mtu: Union[Unset, int] = UNSET
    mru: Union[Unset, int] = UNSET
    mrru: Union[Unset, int] = UNSET
    localip: Union[Unset, str] = UNSET
    subnet: Union[Unset, int] = UNSET
    gateway: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_device = self.if_device

        bandwidth = self.bandwidth

        mtu = self.mtu

        mru = self.mru

        mrru = self.mrru

        localip = self.localip

        subnet = self.subnet

        gateway = self.gateway

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if_device": if_device,
            }
        )
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if mru is not UNSET:
            field_dict["mru"] = mru
        if mrru is not UNSET:
            field_dict["mrru"] = mrru
        if localip is not UNSET:
            field_dict["localip"] = localip
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_device = d.pop("if_device")

        bandwidth = d.pop("bandwidth", UNSET)

        mtu = d.pop("mtu", UNSET)

        mru = d.pop("mru", UNSET)

        mrru = d.pop("mrru", UNSET)

        localip = d.pop("localip", UNSET)

        subnet = d.pop("subnet", UNSET)

        gateway = d.pop("gateway", UNSET)

        ppp_link_interface = cls(
            if_device=if_device,
            bandwidth=bandwidth,
            mtu=mtu,
            mru=mru,
            mrru=mrru,
            localip=localip,
            subnet=subnet,
            gateway=gateway,
        )

        ppp_link_interface.additional_properties = d
        return ppp_link_interface

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
