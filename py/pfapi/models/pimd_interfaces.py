from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pimd_interface import PimdInterface
    from ..models.text_value import TextValue


T = TypeVar("T", bound="PimdInterfaces")


@_attrs_define
class PimdInterfaces:
    """
    Attributes:
        interfaces (list[PimdInterface] | Unset):
        intf_options (list[TextValue] | Unset):
    """

    interfaces: list[PimdInterface] | Unset = UNSET
    intf_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        intf_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intf_options, Unset):
            intf_options = []
            for intf_options_item_data in self.intf_options:
                intf_options_item = intf_options_item_data.to_dict()
                intf_options.append(intf_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if intf_options is not UNSET:
            field_dict["intf_options"] = intf_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pimd_interface import PimdInterface
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[PimdInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = PimdInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _intf_options = d.pop("intf_options", UNSET)
        intf_options: list[TextValue] | Unset = UNSET
        if _intf_options is not UNSET:
            intf_options = []
            for intf_options_item_data in _intf_options:
                intf_options_item = TextValue.from_dict(intf_options_item_data)

                intf_options.append(intf_options_item)

        pimd_interfaces = cls(
            interfaces=interfaces,
            intf_options=intf_options,
        )

        pimd_interfaces.additional_properties = d
        return pimd_interfaces

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
