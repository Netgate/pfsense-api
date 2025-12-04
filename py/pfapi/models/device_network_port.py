from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceNetworkPort")


@_attrs_define
class DeviceNetworkPort:
    """network interface on the device

    Attributes:
        name (str | Unset): device name of the device
        identity (str | Unset): interface identity, e.g. wan, lan, opt1
        device (str | Unset): device driver name, e..g vtnet1
        assigned (str | Unset): user assigned name of the device, WAN, LAN, LANOPT
        link_speed (int | Unset): bps speed negotiated
        phy_speed (int | Unset): bps max speed of port
        state (str | Unset): on, off, error
        vlan (int | Unset): vlan number, if VLAN
        device_info (str | Unset): device hardware, model name
        is_physical (bool | Unset): device is a physical port
        is_switchport (bool | Unset): device is a port on an embedded NIC switch
        addresses (list[str] | Unset):
        label (str | Unset): description (user-defined name) of device
    """

    name: str | Unset = UNSET
    identity: str | Unset = UNSET
    device: str | Unset = UNSET
    assigned: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    phy_speed: int | Unset = UNSET
    state: str | Unset = UNSET
    vlan: int | Unset = UNSET
    device_info: str | Unset = UNSET
    is_physical: bool | Unset = UNSET
    is_switchport: bool | Unset = UNSET
    addresses: list[str] | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        is_switchport = self.is_switchport

        addresses: list[str] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        label = self.label

        field_dict: dict[str, Any] = {}
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
        if is_switchport is not UNSET:
            field_dict["is_switchport"] = is_switchport
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        is_switchport = d.pop("is_switchport", UNSET)

        addresses = cast(list[str], d.pop("addresses", UNSET))

        label = d.pop("label", UNSET)

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
            is_switchport=is_switchport,
            addresses=addresses,
            label=label,
        )

        device_network_port.additional_properties = d
        return device_network_port

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
