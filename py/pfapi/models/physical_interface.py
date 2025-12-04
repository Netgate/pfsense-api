from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhysicalInterface")


@_attrs_define
class PhysicalInterface:
    """a physical interface port

    Attributes:
        name (str):
        mac (str | Unset):
        up (bool | Unset):
        ipaddr (str | Unset):
        friendly (str | Unset):
        dmesg (str | Unset):
    """

    name: str
    mac: str | Unset = UNSET
    up: bool | Unset = UNSET
    ipaddr: str | Unset = UNSET
    friendly: str | Unset = UNSET
    dmesg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        up = self.up

        ipaddr = self.ipaddr

        friendly = self.friendly

        dmesg = self.dmesg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if mac is not UNSET:
            field_dict["mac"] = mac
        if up is not UNSET:
            field_dict["up"] = up
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if friendly is not UNSET:
            field_dict["friendly"] = friendly
        if dmesg is not UNSET:
            field_dict["dmesg"] = dmesg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        mac = d.pop("mac", UNSET)

        up = d.pop("up", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        friendly = d.pop("friendly", UNSET)

        dmesg = d.pop("dmesg", UNSET)

        physical_interface = cls(
            name=name,
            mac=mac,
            up=up,
            ipaddr=ipaddr,
            friendly=friendly,
            dmesg=dmesg,
        )

        physical_interface.additional_properties = d
        return physical_interface

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
