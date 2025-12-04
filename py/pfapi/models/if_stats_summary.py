from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.if_stats import IfStats
    from ..models.if_stats_bandwidth import IfStatsBandwidth


T = TypeVar("T", bound="IfStatsSummary")


@_attrs_define
class IfStatsSummary:
    """
    Attributes:
        if_ (str | Unset):
        ifstats (IfStats | Unset):
        bandwidth (list[IfStatsBandwidth] | Unset):
    """

    if_: str | Unset = UNSET
    ifstats: IfStats | Unset = UNSET
    bandwidth: list[IfStatsBandwidth] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_ = self.if_

        ifstats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ifstats, Unset):
            ifstats = self.ifstats.to_dict()

        bandwidth: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bandwidth, Unset):
            bandwidth = []
            for bandwidth_item_data in self.bandwidth:
                bandwidth_item = bandwidth_item_data.to_dict()
                bandwidth.append(bandwidth_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_ is not UNSET:
            field_dict["if"] = if_
        if ifstats is not UNSET:
            field_dict["ifstats"] = ifstats
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.if_stats import IfStats
        from ..models.if_stats_bandwidth import IfStatsBandwidth

        d = dict(src_dict)
        if_ = d.pop("if", UNSET)

        _ifstats = d.pop("ifstats", UNSET)
        ifstats: IfStats | Unset
        if isinstance(_ifstats, Unset):
            ifstats = UNSET
        else:
            ifstats = IfStats.from_dict(_ifstats)

        _bandwidth = d.pop("bandwidth", UNSET)
        bandwidth: list[IfStatsBandwidth] | Unset = UNSET
        if _bandwidth is not UNSET:
            bandwidth = []
            for bandwidth_item_data in _bandwidth:
                bandwidth_item = IfStatsBandwidth.from_dict(bandwidth_item_data)

                bandwidth.append(bandwidth_item)

        if_stats_summary = cls(
            if_=if_,
            ifstats=ifstats,
            bandwidth=bandwidth,
        )

        if_stats_summary.additional_properties = d
        return if_stats_summary

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
