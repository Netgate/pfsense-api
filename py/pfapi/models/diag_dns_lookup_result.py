from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diag_dns_record import DiagDnsRecord
    from ..models.diag_dns_server_timing import DiagDnsServerTiming


T = TypeVar("T", bound="DiagDnsLookupResult")


@_attrs_define
class DiagDnsLookupResult:
    """
    Attributes:
        results (list[DiagDnsRecord] | Unset):
        timings (list[DiagDnsServerTiming] | Unset):
    """

    results: list[DiagDnsRecord] | Unset = UNSET
    timings: list[DiagDnsServerTiming] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        timings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timings, Unset):
            timings = []
            for timings_item_data in self.timings:
                timings_item = timings_item_data.to_dict()
                timings.append(timings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if timings is not UNSET:
            field_dict["timings"] = timings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diag_dns_record import DiagDnsRecord
        from ..models.diag_dns_server_timing import DiagDnsServerTiming

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[DiagDnsRecord] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = DiagDnsRecord.from_dict(results_item_data)

                results.append(results_item)

        _timings = d.pop("timings", UNSET)
        timings: list[DiagDnsServerTiming] | Unset = UNSET
        if _timings is not UNSET:
            timings = []
            for timings_item_data in _timings:
                timings_item = DiagDnsServerTiming.from_dict(timings_item_data)

                timings.append(timings_item)

        diag_dns_lookup_result = cls(
            results=results,
            timings=timings,
        )

        diag_dns_lookup_result.additional_properties = d
        return diag_dns_lookup_result

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
