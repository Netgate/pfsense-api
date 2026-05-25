from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ospf_6d_interface import FrrOspf6DInterface
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrOspf6DInterfacesList")


@_attrs_define
class FrrOspf6DInterfacesList:
    """
    Attributes:
        ospf6dinterfaces (list[FrrOspf6DInterface] | Unset):
        interface_options (list[TextValue] | Unset):
    """

    ospf6dinterfaces: list[FrrOspf6DInterface] | Unset = UNSET
    interface_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ospf6dinterfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ospf6dinterfaces, Unset):
            ospf6dinterfaces = []
            for ospf6dinterfaces_item_data in self.ospf6dinterfaces:
                ospf6dinterfaces_item = ospf6dinterfaces_item_data.to_dict()
                ospf6dinterfaces.append(ospf6dinterfaces_item)

        interface_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interface_options, Unset):
            interface_options = []
            for interface_options_item_data in self.interface_options:
                interface_options_item = interface_options_item_data.to_dict()
                interface_options.append(interface_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ospf6dinterfaces is not UNSET:
            field_dict["ospf6dinterfaces"] = ospf6dinterfaces
        if interface_options is not UNSET:
            field_dict["interface_options"] = interface_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ospf_6d_interface import FrrOspf6DInterface
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _ospf6dinterfaces = d.pop("ospf6dinterfaces", UNSET)
        ospf6dinterfaces: list[FrrOspf6DInterface] | Unset = UNSET
        if _ospf6dinterfaces is not UNSET:
            ospf6dinterfaces = []
            for ospf6dinterfaces_item_data in _ospf6dinterfaces:
                ospf6dinterfaces_item = FrrOspf6DInterface.from_dict(ospf6dinterfaces_item_data)

                ospf6dinterfaces.append(ospf6dinterfaces_item)

        _interface_options = d.pop("interface_options", UNSET)
        interface_options: list[TextValue] | Unset = UNSET
        if _interface_options is not UNSET:
            interface_options = []
            for interface_options_item_data in _interface_options:
                interface_options_item = TextValue.from_dict(interface_options_item_data)

                interface_options.append(interface_options_item)

        frr_ospf_6d_interfaces_list = cls(
            ospf6dinterfaces=ospf6dinterfaces,
            interface_options=interface_options,
        )

        frr_ospf_6d_interfaces_list.additional_properties = d
        return frr_ospf_6d_interfaces_list

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
