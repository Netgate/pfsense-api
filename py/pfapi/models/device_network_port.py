from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceNetworkPort")


@_attrs_define
class DeviceNetworkPort:
    """network interface on the device

    Attributes:
        name (str): device name of the device
        identity (str): interface identity, e.g. wan, lan, opt1
        device (str): device driver name, e..g vtnet1
        assigned (str): user assigned name of the device, WAN, LAN, LANOPT
        link_speed (int): bps speed negotiated
        phy_speed (int): bps max speed of port
        state (str): on, off, error
        vlan (int): vlan number, if VLAN
        device_info (str): device hardware, model name
        is_physical (bool): device is a physical port
        label (str): description (user-defined name) of device
        addresses (Union[Unset, List[str]]):
    """

    name: str
    identity: str
    device: str
    assigned: str
    link_speed: int
    phy_speed: int
    state: str
    vlan: int
    device_info: str
    is_physical: bool
    label: str
    addresses: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        identity = self.identity

        device = self.device

        assigned = self.assigned

        link_speed = self.link_speed

        phy_speed = self.phy_speed

        state = self.state

        vlan = self.vlan

        device_info = self.device_info

        is_physical = self.is_physical

        label = self.label

        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "identity": identity,
                "device": device,
                "assigned": assigned,
                "link_speed": link_speed,
                "phy_speed": phy_speed,
                "state": state,
                "vlan": vlan,
                "device_info": device_info,
                "is_physical": is_physical,
                "label": label,
            }
        )
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        identity = d.pop("identity")

        device = d.pop("device")

        assigned = d.pop("assigned")

        link_speed = d.pop("link_speed")

        phy_speed = d.pop("phy_speed")

        state = d.pop("state")

        vlan = d.pop("vlan")

        device_info = d.pop("device_info")

        is_physical = d.pop("is_physical")

        label = d.pop("label")

        addresses = cast(List[str], d.pop("addresses", UNSET))

        device_network_port = cls(
            name=name,
            identity=identity,
            device=device,
            assigned=assigned,
            link_speed=link_speed,
            phy_speed=phy_speed,
            state=state,
            vlan=vlan,
            device_info=device_info,
            is_physical=is_physical,
            label=label,
            addresses=addresses,
        )

        device_network_port.additional_properties = d
        return device_network_port

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
