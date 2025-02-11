from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.diag_dns_record import DiagDnsRecord
    from ..models.diag_dns_server_timing import DiagDnsServerTiming


T = TypeVar("T", bound="DiagDnsLookupResult")


@_attrs_define
class DiagDnsLookupResult:
    """
    Attributes:
        results (List['DiagDnsRecord']):
        timings (List['DiagDnsServerTiming']):
    """

    results: List["DiagDnsRecord"]
    timings: List["DiagDnsServerTiming"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        timings = []
        for timings_item_data in self.timings:
            timings_item = timings_item_data.to_dict()
            timings.append(timings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "timings": timings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.diag_dns_record import DiagDnsRecord
        from ..models.diag_dns_server_timing import DiagDnsServerTiming

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = DiagDnsRecord.from_dict(results_item_data)

            results.append(results_item)

        timings = []
        _timings = d.pop("timings")
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
