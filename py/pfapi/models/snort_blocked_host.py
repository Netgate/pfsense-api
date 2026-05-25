from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortBlockedHost")


@_attrs_define
class SnortBlockedHost:
    """
    Attributes:
        id (int | Unset):
        address (str | Unset):
        descr (str | Unset):
    """

    id: int | Unset = UNSET
    address: str | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address = self.address

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address is not UNSET:
            field_dict["address"] = address
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        address = d.pop("address", UNSET)

        descr = d.pop("descr", UNSET)

        snort_blocked_host = cls(
            id=id,
            address=address,
            descr=descr,
        )

        snort_blocked_host.additional_properties = d
        return snort_blocked_host

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
