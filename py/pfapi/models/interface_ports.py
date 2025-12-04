from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interface_ports_lists import InterfacePortsLists


T = TypeVar("T", bound="InterfacePorts")


@_attrs_define
class InterfacePorts:
    """
    Attributes:
        ports (InterfacePortsLists | Unset):
        modems (list[str] | Unset):
    """

    ports: InterfacePortsLists | Unset = UNSET
    modems: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports.to_dict()

        modems: list[str] | Unset = UNSET
        if not isinstance(self.modems, Unset):
            modems = self.modems

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ports is not UNSET:
            field_dict["ports"] = ports
        if modems is not UNSET:
            field_dict["modems"] = modems

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interface_ports_lists import InterfacePortsLists

        d = dict(src_dict)
        _ports = d.pop("ports", UNSET)
        ports: InterfacePortsLists | Unset
        if isinstance(_ports, Unset):
            ports = UNSET
        else:
            ports = InterfacePortsLists.from_dict(_ports)

        modems = cast(list[str], d.pop("modems", UNSET))

        interface_ports = cls(
            ports=ports,
            modems=modems,
        )

        interface_ports.additional_properties = d
        return interface_ports

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
