from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SysNetIf")


@_attrs_define
class SysNetIf:
    """network interface on the device

    Attributes:
        name (Union[Unset, str]): device name of the device
        identity (Union[Unset, str]): interface identity, e.g. wan, lan, opt1
        device (Union[Unset, str]): device driver name, e..g vtnet1
        assigned (Union[Unset, str]): user assigned name of the device, WAN, LAN, LANOPT
        link_speed (Union[Unset, int]): bps speed negotiated
        phy_speed (Union[Unset, int]): bps max speed of port
        state (Union[Unset, str]): on, off, error
        vlan (Union[Unset, int]): vlan number, if VLAN
        device_info (Union[Unset, str]): device hardware, model name
        is_physical (Union[Unset, bool]): device is a physical port
        addresses (Union[Unset, List[str]]):
        label (Union[Unset, str]): description (user-defined name) of device
    """

    name: Union[Unset, str] = UNSET
    identity: Union[Unset, str] = UNSET
    device: Union[Unset, str] = UNSET
    assigned: Union[Unset, str] = UNSET
    link_speed: Union[Unset, int] = UNSET
    phy_speed: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    vlan: Union[Unset, int] = UNSET
    device_info: Union[Unset, str] = UNSET
    is_physical: Union[Unset, bool] = UNSET
    addresses: Union[Unset, List[str]] = UNSET
    label: Union[Unset, str] = UNSET
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

        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if identity is not UNSET:
            field_dict["identity"] = identity
        if device is not UNSET:
            field_dict["device"] = device
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if link_speed is not UNSET:
            field_dict["link_speed"] = link_speed
        if phy_speed is not UNSET:
            field_dict["phy_speed"] = phy_speed
        if state is not UNSET:
            field_dict["state"] = state
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if device_info is not UNSET:
            field_dict["device_info"] = device_info
        if is_physical is not UNSET:
            field_dict["is_physical"] = is_physical
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        identity = d.pop("identity", UNSET)

        device = d.pop("device", UNSET)

        assigned = d.pop("assigned", UNSET)

        link_speed = d.pop("link_speed", UNSET)

        phy_speed = d.pop("phy_speed", UNSET)

        state = d.pop("state", UNSET)

        vlan = d.pop("vlan", UNSET)

        device_info = d.pop("device_info", UNSET)

        is_physical = d.pop("is_physical", UNSET)

        addresses = cast(List[str], d.pop("addresses", UNSET))

        label = d.pop("label", UNSET)

        sys_net_if = cls(
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
            addresses=addresses,
            label=label,
        )

        sys_net_if.additional_properties = d
        return sys_net_if

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
