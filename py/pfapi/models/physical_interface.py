from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhysicalInterface")


@_attrs_define
class PhysicalInterface:
    """a physical interface port

    Attributes:
        name (Union[Unset, str]):
        mac (Union[Unset, str]):
        up (Union[Unset, bool]):
        ipaddr (Union[Unset, str]):
        friendly (Union[Unset, str]):
        dmesg (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    up: Union[Unset, bool] = UNSET
    ipaddr: Union[Unset, str] = UNSET
    friendly: Union[Unset, str] = UNSET
    dmesg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        mac = self.mac

        up = self.up

        ipaddr = self.ipaddr

        friendly = self.friendly

        dmesg = self.dmesg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

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
