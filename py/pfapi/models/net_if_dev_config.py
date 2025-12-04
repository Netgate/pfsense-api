from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetIfDevConfig")


@_attrs_define
class NetIfDevConfig:
    """
    Attributes:
        device (str | Unset): original name of the device
        bus_path (str | Unset): BUS path of the device
        mac (str | Unset): original MAC address
        parent_device (str | Unset): parent device
        parent_path (str | Unset): parent device bus path
        iftype (str | Unset): interface type
        members (list[str] | Unset):
    """

    device: str | Unset = UNSET
    bus_path: str | Unset = UNSET
    mac: str | Unset = UNSET
    parent_device: str | Unset = UNSET
    parent_path: str | Unset = UNSET
    iftype: str | Unset = UNSET
    members: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device

        bus_path = self.bus_path

        mac = self.mac

        parent_device = self.parent_device

        parent_path = self.parent_path

        iftype = self.iftype

        members: list[str] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if bus_path is not UNSET:
            field_dict["bus_path"] = bus_path
        if mac is not UNSET:
            field_dict["mac"] = mac
        if parent_device is not UNSET:
            field_dict["parent_device"] = parent_device
        if parent_path is not UNSET:
            field_dict["parent_path"] = parent_path
        if iftype is not UNSET:
            field_dict["iftype"] = iftype
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device = d.pop("device", UNSET)

        bus_path = d.pop("bus_path", UNSET)

        mac = d.pop("mac", UNSET)

        parent_device = d.pop("parent_device", UNSET)

        parent_path = d.pop("parent_path", UNSET)

        iftype = d.pop("iftype", UNSET)

        members = cast(list[str], d.pop("members", UNSET))

        net_if_dev_config = cls(
            device=device,
            bus_path=bus_path,
            mac=mac,
            parent_device=parent_device,
            parent_path=parent_path,
            iftype=iftype,
            members=members,
        )

        net_if_dev_config.additional_properties = d
        return net_if_dev_config

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
