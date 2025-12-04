from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IfStatsBandwidth")


@_attrs_define
class IfStatsBandwidth:
    """
    Attributes:
        host (str | Unset):
        bitsin (str | Unset):
        bitsout (str | Unset):
    """

    host: str | Unset = UNSET
    bitsin: str | Unset = UNSET
    bitsout: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        bitsin = self.bitsin

        bitsout = self.bitsout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if bitsin is not UNSET:
            field_dict["bitsin"] = bitsin
        if bitsout is not UNSET:
            field_dict["bitsout"] = bitsout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        bitsin = d.pop("bitsin", UNSET)

        bitsout = d.pop("bitsout", UNSET)

        if_stats_bandwidth = cls(
            host=host,
            bitsin=bitsin,
            bitsout=bitsout,
        )

        if_stats_bandwidth.additional_properties = d
        return if_stats_bandwidth

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
