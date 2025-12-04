from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessAddlClone")


@_attrs_define
class WirelessAddlClone:
    """
    Attributes:
        if_ (str | Unset):
        mode (str | Unset):
        descr (str | Unset):
        cloneif (str | Unset):
    """

    if_: str | Unset = UNSET
    mode: str | Unset = UNSET
    descr: str | Unset = UNSET
    cloneif: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_ = self.if_

        mode = self.mode

        descr = self.descr

        cloneif = self.cloneif

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_ is not UNSET:
            field_dict["if"] = if_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if descr is not UNSET:
            field_dict["descr"] = descr
        if cloneif is not UNSET:
            field_dict["cloneif"] = cloneif

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        if_ = d.pop("if", UNSET)

        mode = d.pop("mode", UNSET)

        descr = d.pop("descr", UNSET)

        cloneif = d.pop("cloneif", UNSET)

        wireless_addl_clone = cls(
            if_=if_,
            mode=mode,
            descr=descr,
            cloneif=cloneif,
        )

        wireless_addl_clone.additional_properties = d
        return wireless_addl_clone

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
