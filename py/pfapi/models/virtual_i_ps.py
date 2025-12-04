from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_interface import SimpleInterface
    from ..models.virtual_ip import VirtualIP


T = TypeVar("T", bound="VirtualIPs")


@_attrs_define
class VirtualIPs:
    """
    Attributes:
        virtualips (list[VirtualIP] | Unset):
        interfaces (list[SimpleInterface] | Unset):
    """

    virtualips: list[VirtualIP] | Unset = UNSET
    interfaces: list[SimpleInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtualips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.virtualips, Unset):
            virtualips = []
            for virtualips_item_data in self.virtualips:
                virtualips_item = virtualips_item_data.to_dict()
                virtualips.append(virtualips_item)

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtualips is not UNSET:
            field_dict["virtualips"] = virtualips
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_interface import SimpleInterface
        from ..models.virtual_ip import VirtualIP

        d = dict(src_dict)
        _virtualips = d.pop("virtualips", UNSET)
        virtualips: list[VirtualIP] | Unset = UNSET
        if _virtualips is not UNSET:
            virtualips = []
            for virtualips_item_data in _virtualips:
                virtualips_item = VirtualIP.from_dict(virtualips_item_data)

                virtualips.append(virtualips_item)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[SimpleInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = SimpleInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        virtual_i_ps = cls(
            virtualips=virtualips,
            interfaces=interfaces,
        )

        virtual_i_ps.additional_properties = d
        return virtual_i_ps

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
