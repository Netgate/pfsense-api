from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceLabelToName")


@_attrs_define
class InterfaceLabelToName:
    """Mapping of friendly interface label to the configuration name
    and the underlying device name. For example:

    friendly: LANOPT
    name:     lanopt (assigned)
    ident:    opt1
    if:       eth0

        Attributes:
            friendly (str | Unset):
            name (str | Unset):
            ident (str | Unset):
            if_ (str | Unset):
    """

    friendly: str | Unset = UNSET
    name: str | Unset = UNSET
    ident: str | Unset = UNSET
    if_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        friendly = self.friendly

        name = self.name

        ident = self.ident

        if_ = self.if_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if friendly is not UNSET:
            field_dict["friendly"] = friendly
        if name is not UNSET:
            field_dict["name"] = name
        if ident is not UNSET:
            field_dict["ident"] = ident
        if if_ is not UNSET:
            field_dict["if"] = if_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        friendly = d.pop("friendly", UNSET)

        name = d.pop("name", UNSET)

        ident = d.pop("ident", UNSET)

        if_ = d.pop("if", UNSET)

        interface_label_to_name = cls(
            friendly=friendly,
            name=name,
            ident=ident,
            if_=if_,
        )

        interface_label_to_name.additional_properties = d
        return interface_label_to_name

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
