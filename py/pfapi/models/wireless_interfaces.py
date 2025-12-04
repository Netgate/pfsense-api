from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wireless_addl import WirelessAddl
    from ..models.wireless_interface import WirelessInterface


T = TypeVar("T", bound="WirelessInterfaces")


@_attrs_define
class WirelessInterfaces:
    """
    Attributes:
        interfaces (list[WirelessInterface] | Unset):
        interfaces_clone (list[WirelessAddl] | Unset):
    """

    interfaces: list[WirelessInterface] | Unset = UNSET
    interfaces_clone: list[WirelessAddl] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        interfaces_clone: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces_clone, Unset):
            interfaces_clone = []
            for interfaces_clone_item_data in self.interfaces_clone:
                interfaces_clone_item = interfaces_clone_item_data.to_dict()
                interfaces_clone.append(interfaces_clone_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if interfaces_clone is not UNSET:
            field_dict["interfacesClone"] = interfaces_clone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wireless_addl import WirelessAddl
        from ..models.wireless_interface import WirelessInterface

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[WirelessInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = WirelessInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _interfaces_clone = d.pop("interfacesClone", UNSET)
        interfaces_clone: list[WirelessAddl] | Unset = UNSET
        if _interfaces_clone is not UNSET:
            interfaces_clone = []
            for interfaces_clone_item_data in _interfaces_clone:
                interfaces_clone_item = WirelessAddl.from_dict(interfaces_clone_item_data)

                interfaces_clone.append(interfaces_clone_item)

        wireless_interfaces = cls(
            interfaces=interfaces,
            interfaces_clone=interfaces_clone,
        )

        wireless_interfaces.additional_properties = d
        return wireless_interfaces

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
