from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyStickTable")


@_attrs_define
class HaproxyStickTable:
    """
    Attributes:
        name (str | Unset): Stick-table name
        type_ (str | Unset): Key type
        size (int | Unset): Maximum entries
        used (int | Unset): Entries currently used
    """

    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    size: int | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        size = self.size

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if size is not UNSET:
            field_dict["size"] = size
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        size = d.pop("size", UNSET)

        used = d.pop("used", UNSET)

        haproxy_stick_table = cls(
            name=name,
            type_=type_,
            size=size,
            used=used,
        )

        haproxy_stick_table.additional_properties = d
        return haproxy_stick_table

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
