from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetIfOwnerHost")


@_attrs_define
class NetIfOwnerHost:
    """
    Attributes:
        wol (bool | Unset):
        hw_flags (str | Unset): comma-separated flags configured on interface, e.g. TSO, LRO, etc
    """

    wol: bool | Unset = UNSET
    hw_flags: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wol = self.wol

        hw_flags = self.hw_flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wol is not UNSET:
            field_dict["wol"] = wol
        if hw_flags is not UNSET:
            field_dict["hw_flags"] = hw_flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wol = d.pop("wol", UNSET)

        hw_flags = d.pop("hw_flags", UNSET)

        net_if_owner_host = cls(
            wol=wol,
            hw_flags=hw_flags,
        )

        net_if_owner_host.additional_properties = d
        return net_if_owner_host

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
