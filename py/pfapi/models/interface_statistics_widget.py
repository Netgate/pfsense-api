from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceStatisticsWidget")


@_attrs_define
class InterfaceStatisticsWidget:
    """
    Attributes:
        packets_in (int | Unset):
        packets_out (int | Unset):
        bytes_in (int | Unset):
        bytes_out (int | Unset):
        errors_in (int | Unset):
        errors_out (int | Unset):
        collisions (int | Unset):
    """

    packets_in: int | Unset = UNSET
    packets_out: int | Unset = UNSET
    bytes_in: int | Unset = UNSET
    bytes_out: int | Unset = UNSET
    errors_in: int | Unset = UNSET
    errors_out: int | Unset = UNSET
    collisions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        packets_in = self.packets_in

        packets_out = self.packets_out

        bytes_in = self.bytes_in

        bytes_out = self.bytes_out

        errors_in = self.errors_in

        errors_out = self.errors_out

        collisions = self.collisions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if packets_in is not UNSET:
            field_dict["packets_in"] = packets_in
        if packets_out is not UNSET:
            field_dict["packets_out"] = packets_out
        if bytes_in is not UNSET:
            field_dict["bytes_in"] = bytes_in
        if bytes_out is not UNSET:
            field_dict["bytes_out"] = bytes_out
        if errors_in is not UNSET:
            field_dict["errors_in"] = errors_in
        if errors_out is not UNSET:
            field_dict["errors_out"] = errors_out
        if collisions is not UNSET:
            field_dict["collisions"] = collisions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        packets_in = d.pop("packets_in", UNSET)

        packets_out = d.pop("packets_out", UNSET)

        bytes_in = d.pop("bytes_in", UNSET)

        bytes_out = d.pop("bytes_out", UNSET)

        errors_in = d.pop("errors_in", UNSET)

        errors_out = d.pop("errors_out", UNSET)

        collisions = d.pop("collisions", UNSET)

        interface_statistics_widget = cls(
            packets_in=packets_in,
            packets_out=packets_out,
            bytes_in=bytes_in,
            bytes_out=bytes_out,
            errors_in=errors_in,
            errors_out=errors_out,
            collisions=collisions,
        )

        interface_statistics_widget.additional_properties = d
        return interface_statistics_widget

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
