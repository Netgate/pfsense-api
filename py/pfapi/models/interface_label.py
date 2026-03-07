from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceLabel")


@_attrs_define
class InterfaceLabel:
    """
    Attributes:
        ident (str | Unset):
        device (str | Unset):
        assigned (str | Unset):
        type_ (str | Unset): interface type - device, group, vpn, other
    """

    ident: str | Unset = UNSET
    device: str | Unset = UNSET
    assigned: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ident = self.ident

        device = self.device

        assigned = self.assigned

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ident is not UNSET:
            field_dict["ident"] = ident
        if device is not UNSET:
            field_dict["device"] = device
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ident = d.pop("ident", UNSET)

        device = d.pop("device", UNSET)

        assigned = d.pop("assigned", UNSET)

        type_ = d.pop("type", UNSET)

        interface_label = cls(
            ident=ident,
            device=device,
            assigned=assigned,
            type_=type_,
        )

        interface_label.additional_properties = d
        return interface_label

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
