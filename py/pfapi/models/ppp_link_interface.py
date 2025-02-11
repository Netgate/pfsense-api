from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PPPLinkInterface")


@_attrs_define
class PPPLinkInterface:
    """
    Attributes:
        if_device (str): device name of the interface used for the link
        bandwidth (int):
        mtu (int):
        mru (int):
        mrru (int):
        localip (str): (type pptp and l2tp only) local ip address
        subnet (int): (type pptp and l2tp only) local ip address subnet
        gateway (str): (type pptp and l2tp only) gateway ip address or hostname
    """

    if_device: str
    bandwidth: int
    mtu: int
    mru: int
    mrru: int
    localip: str
    subnet: int
    gateway: str
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
                "bandwidth": bandwidth,
                "mtu": mtu,
                "mru": mru,
                "mrru": mrru,
                "localip": localip,
                "subnet": subnet,
                "gateway": gateway,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_device = d.pop("if_device")

        bandwidth = d.pop("bandwidth")

        mtu = d.pop("mtu")

        mru = d.pop("mru")

        mrru = d.pop("mrru")

        localip = d.pop("localip")

        subnet = d.pop("subnet")

        gateway = d.pop("gateway")

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
