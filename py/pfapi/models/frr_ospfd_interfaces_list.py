from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ospfd_interface import FrrOspfdInterface
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrOspfdInterfacesList")


@_attrs_define
class FrrOspfdInterfacesList:
    """
    Attributes:
        ospfdinterfaces (list[FrrOspfdInterface] | Unset):
        interface_options (list[TextValue] | Unset):
    """

    ospfdinterfaces: list[FrrOspfdInterface] | Unset = UNSET
    interface_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ospfdinterfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ospfdinterfaces, Unset):
            ospfdinterfaces = []
            for ospfdinterfaces_item_data in self.ospfdinterfaces:
                ospfdinterfaces_item = ospfdinterfaces_item_data.to_dict()
                ospfdinterfaces.append(ospfdinterfaces_item)

        interface_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interface_options, Unset):
            interface_options = []
            for interface_options_item_data in self.interface_options:
                interface_options_item = interface_options_item_data.to_dict()
                interface_options.append(interface_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ospfdinterfaces is not UNSET:
            field_dict["ospfdinterfaces"] = ospfdinterfaces
        if interface_options is not UNSET:
            field_dict["interface_options"] = interface_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ospfd_interface import FrrOspfdInterface
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _ospfdinterfaces = d.pop("ospfdinterfaces", UNSET)
        ospfdinterfaces: list[FrrOspfdInterface] | Unset = UNSET
        if _ospfdinterfaces is not UNSET:
            ospfdinterfaces = []
            for ospfdinterfaces_item_data in _ospfdinterfaces:
                ospfdinterfaces_item = FrrOspfdInterface.from_dict(ospfdinterfaces_item_data)

                ospfdinterfaces.append(ospfdinterfaces_item)

        _interface_options = d.pop("interface_options", UNSET)
        interface_options: list[TextValue] | Unset = UNSET
        if _interface_options is not UNSET:
            interface_options = []
            for interface_options_item_data in _interface_options:
                interface_options_item = TextValue.from_dict(interface_options_item_data)

                interface_options.append(interface_options_item)

        frr_ospfd_interfaces_list = cls(
            ospfdinterfaces=ospfdinterfaces,
            interface_options=interface_options,
        )

        frr_ospfd_interfaces_list.additional_properties = d
        return frr_ospfd_interfaces_list

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
