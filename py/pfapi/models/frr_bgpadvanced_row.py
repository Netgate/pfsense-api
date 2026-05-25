from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrBgpadvancedRow")


@_attrs_define
class FrrBgpadvancedRow:
    """
    Attributes:
        aggregateaddr (str | Unset): Aggregate Address

            IPv4 or IPv6 Prefix
        aggregateasset (str | Unset): Generate AS Set
        aggregatesummaryonly (str | Unset): Summary Only
    """

    aggregateaddr: str | Unset = UNSET
    aggregateasset: str | Unset = UNSET
    aggregatesummaryonly: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregateaddr = self.aggregateaddr

        aggregateasset = self.aggregateasset

        aggregatesummaryonly = self.aggregatesummaryonly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregateaddr is not UNSET:
            field_dict["aggregateaddr"] = aggregateaddr
        if aggregateasset is not UNSET:
            field_dict["aggregateasset"] = aggregateasset
        if aggregatesummaryonly is not UNSET:
            field_dict["aggregatesummaryonly"] = aggregatesummaryonly

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aggregateaddr = d.pop("aggregateaddr", UNSET)

        aggregateasset = d.pop("aggregateasset", UNSET)

        aggregatesummaryonly = d.pop("aggregatesummaryonly", UNSET)

        frr_bgpadvanced_row = cls(
            aggregateaddr=aggregateaddr,
            aggregateasset=aggregateasset,
            aggregatesummaryonly=aggregatesummaryonly,
        )

        frr_bgpadvanced_row.additional_properties = d
        return frr_bgpadvanced_row

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
