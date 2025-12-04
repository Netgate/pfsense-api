from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageStats")


@_attrs_define
class StorageStats:
    """
    Attributes:
        volume (str | Unset): volume name or directory
        device (str | Unset): device partition
        capacity (int | Unset):
        used (int | Unset):
    """

    volume: str | Unset = UNSET
    device: str | Unset = UNSET
    capacity: int | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume = self.volume

        device = self.device

        capacity = self.capacity

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volume is not UNSET:
            field_dict["volume"] = volume
        if device is not UNSET:
            field_dict["device"] = device
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume = d.pop("volume", UNSET)

        device = d.pop("device", UNSET)

        capacity = d.pop("capacity", UNSET)

        used = d.pop("used", UNSET)

        storage_stats = cls(
            volume=volume,
            device=device,
            capacity=capacity,
            used=used,
        )

        storage_stats.additional_properties = d
        return storage_stats

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
