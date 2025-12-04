from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vxlan_capable_interface import VXLANCapableInterface
    from ..models.vxlan_interface import VXLANInterface


T = TypeVar("T", bound="VXLANInterfaces")


@_attrs_define
class VXLANInterfaces:
    """
    Attributes:
        interfaces (list[VXLANInterface] | Unset):
        vxlan_capable_ifs (list[VXLANCapableInterface] | Unset):
    """

    interfaces: list[VXLANInterface] | Unset = UNSET
    vxlan_capable_ifs: list[VXLANCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        vxlan_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vxlan_capable_ifs, Unset):
            vxlan_capable_ifs = []
            for vxlan_capable_ifs_item_data in self.vxlan_capable_ifs:
                vxlan_capable_ifs_item = vxlan_capable_ifs_item_data.to_dict()
                vxlan_capable_ifs.append(vxlan_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if vxlan_capable_ifs is not UNSET:
            field_dict["vxlan_capable_ifs"] = vxlan_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vxlan_capable_interface import VXLANCapableInterface
        from ..models.vxlan_interface import VXLANInterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[VXLANInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = VXLANInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _vxlan_capable_ifs = d.pop("vxlan_capable_ifs", UNSET)
        vxlan_capable_ifs: list[VXLANCapableInterface] | Unset = UNSET
        if _vxlan_capable_ifs is not UNSET:
            vxlan_capable_ifs = []
            for vxlan_capable_ifs_item_data in _vxlan_capable_ifs:
                vxlan_capable_ifs_item = VXLANCapableInterface.from_dict(vxlan_capable_ifs_item_data)

                vxlan_capable_ifs.append(vxlan_capable_ifs_item)

        vxlan_interfaces = cls(
            interfaces=interfaces,
            vxlan_capable_ifs=vxlan_capable_ifs,
        )

        vxlan_interfaces.additional_properties = d
        return vxlan_interfaces

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
