from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IfStats")


@_attrs_define
class IfStats:
    """
    Attributes:
        time (int | Unset):
        bytesin (int | Unset):
        bytesout (int | Unset):
    """

    time: int | Unset = UNSET
    bytesin: int | Unset = UNSET
    bytesout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        bytesin = self.bytesin

        bytesout = self.bytesout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if bytesin is not UNSET:
            field_dict["bytesin"] = bytesin
        if bytesout is not UNSET:
            field_dict["bytesout"] = bytesout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        bytesin = d.pop("bytesin", UNSET)

        bytesout = d.pop("bytesout", UNSET)

        if_stats = cls(
            time=time,
            bytesin=bytesin,
            bytesout=bytesout,
        )

        if_stats.additional_properties = d
        return if_stats

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
