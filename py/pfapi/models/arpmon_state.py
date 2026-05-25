from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arpmon_state_interfaces import ArpmonStateInterfaces
    from ..models.text_value import TextValue


T = TypeVar("T", bound="ArpmonState")


@_attrs_define
class ArpmonState:
    """
    Attributes:
        interfaces (ArpmonStateInterfaces | Unset):
        intf_names (list[TextValue] | Unset):
    """

    interfaces: ArpmonStateInterfaces | Unset = UNSET
    intf_names: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces.to_dict()

        intf_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intf_names, Unset):
            intf_names = []
            for intf_names_item_data in self.intf_names:
                intf_names_item = intf_names_item_data.to_dict()
                intf_names.append(intf_names_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if intf_names is not UNSET:
            field_dict["intf_names"] = intf_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arpmon_state_interfaces import ArpmonStateInterfaces
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: ArpmonStateInterfaces | Unset
        if isinstance(_interfaces, Unset):
            interfaces = UNSET
        else:
            interfaces = ArpmonStateInterfaces.from_dict(_interfaces)

        _intf_names = d.pop("intf_names", UNSET)
        intf_names: list[TextValue] | Unset = UNSET
        if _intf_names is not UNSET:
            intf_names = []
            for intf_names_item_data in _intf_names:
                intf_names_item = TextValue.from_dict(intf_names_item_data)

                intf_names.append(intf_names_item)

        arpmon_state = cls(
            interfaces=interfaces,
            intf_names=intf_names,
        )

        arpmon_state.additional_properties = d
        return arpmon_state

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
