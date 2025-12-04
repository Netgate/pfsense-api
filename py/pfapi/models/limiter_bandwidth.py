from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LimiterBandwidth")


@_attrs_define
class LimiterBandwidth:
    """
    Attributes:
        bw (int | Unset): bandwidth value for the limiter
        bwscale (str | Unset): units for the bw
            valid value = Kb, Mb, b
        bwsched (str | Unset): schedule (Time Based Rules) to apply this bandwidth
    """

    bw: int | Unset = UNSET
    bwscale: str | Unset = UNSET
    bwsched: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bw = self.bw

        bwscale = self.bwscale

        bwsched = self.bwsched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bw is not UNSET:
            field_dict["bw"] = bw
        if bwscale is not UNSET:
            field_dict["bwscale"] = bwscale
        if bwsched is not UNSET:
            field_dict["bwsched"] = bwsched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bw = d.pop("bw", UNSET)

        bwscale = d.pop("bwscale", UNSET)

        bwsched = d.pop("bwsched", UNSET)

        limiter_bandwidth = cls(
            bw=bw,
            bwscale=bwscale,
            bwsched=bwsched,
        )

        limiter_bandwidth.additional_properties = d
        return limiter_bandwidth

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
