from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CRLMethodNew")


@_attrs_define
class CRLMethodNew:
    """
    Attributes:
        lifetime (int | Unset): lifetime days
        serial (int | Unset):
    """

    lifetime: int | Unset = UNSET
    serial: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lifetime = self.lifetime

        serial = self.serial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if serial is not UNSET:
            field_dict["serial"] = serial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lifetime = d.pop("lifetime", UNSET)

        serial = d.pop("serial", UNSET)

        crl_method_new = cls(
            lifetime=lifetime,
            serial=serial,
        )

        crl_method_new.additional_properties = d
        return crl_method_new

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
