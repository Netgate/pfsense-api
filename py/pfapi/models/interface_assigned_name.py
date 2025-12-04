from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceAssignedName")


@_attrs_define
class InterfaceAssignedName:
    """
    Attributes:
        device (str | Unset): interface device, e.g. igbe0
        ident (str | Unset): identity, e.g. wan, lan, opt1
        assigned (str | Unset): user assigned name, e.g. WAN, LAN, MYLAN
    """

    device: str | Unset = UNSET
    ident: str | Unset = UNSET
    assigned: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device

        ident = self.ident

        assigned = self.assigned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if ident is not UNSET:
            field_dict["ident"] = ident
        if assigned is not UNSET:
            field_dict["assigned"] = assigned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device = d.pop("device", UNSET)

        ident = d.pop("ident", UNSET)

        assigned = d.pop("assigned", UNSET)

        interface_assigned_name = cls(
            device=device,
            ident=ident,
            assigned=assigned,
        )

        interface_assigned_name.additional_properties = d
        return interface_assigned_name

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
