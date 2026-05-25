from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ripd_interface import FrrRipdInterface
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrRipdInterfacesList")


@_attrs_define
class FrrRipdInterfacesList:
    """
    Attributes:
        ripdinterfaces (list[FrrRipdInterface] | Unset):
        interface_options (list[TextValue] | Unset):
    """

    ripdinterfaces: list[FrrRipdInterface] | Unset = UNSET
    interface_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ripdinterfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ripdinterfaces, Unset):
            ripdinterfaces = []
            for ripdinterfaces_item_data in self.ripdinterfaces:
                ripdinterfaces_item = ripdinterfaces_item_data.to_dict()
                ripdinterfaces.append(ripdinterfaces_item)

        interface_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interface_options, Unset):
            interface_options = []
            for interface_options_item_data in self.interface_options:
                interface_options_item = interface_options_item_data.to_dict()
                interface_options.append(interface_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ripdinterfaces is not UNSET:
            field_dict["ripdinterfaces"] = ripdinterfaces
        if interface_options is not UNSET:
            field_dict["interface_options"] = interface_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ripd_interface import FrrRipdInterface
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _ripdinterfaces = d.pop("ripdinterfaces", UNSET)
        ripdinterfaces: list[FrrRipdInterface] | Unset = UNSET
        if _ripdinterfaces is not UNSET:
            ripdinterfaces = []
            for ripdinterfaces_item_data in _ripdinterfaces:
                ripdinterfaces_item = FrrRipdInterface.from_dict(ripdinterfaces_item_data)

                ripdinterfaces.append(ripdinterfaces_item)

        _interface_options = d.pop("interface_options", UNSET)
        interface_options: list[TextValue] | Unset = UNSET
        if _interface_options is not UNSET:
            interface_options = []
            for interface_options_item_data in _interface_options:
                interface_options_item = TextValue.from_dict(interface_options_item_data)

                interface_options.append(interface_options_item)

        frr_ripd_interfaces_list = cls(
            ripdinterfaces=ripdinterfaces,
            interface_options=interface_options,
        )

        frr_ripd_interfaces_list.additional_properties = d
        return frr_ripd_interfaces_list

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
