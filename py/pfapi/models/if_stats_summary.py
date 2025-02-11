from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.if_stats import IfStats
    from ..models.if_stats_bandwidth import IfStatsBandwidth


T = TypeVar("T", bound="IfStatsSummary")


@_attrs_define
class IfStatsSummary:
    """
    Attributes:
        if_ (str):
        ifstats (IfStats):
        bandwidth (List['IfStatsBandwidth']):
    """

    if_: str
    ifstats: "IfStats"
    bandwidth: List["IfStatsBandwidth"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_ = self.if_

        ifstats = self.ifstats.to_dict()

        bandwidth = []
        for bandwidth_item_data in self.bandwidth:
            bandwidth_item = bandwidth_item_data.to_dict()
            bandwidth.append(bandwidth_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if": if_,
                "ifstats": ifstats,
                "bandwidth": bandwidth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.if_stats import IfStats
        from ..models.if_stats_bandwidth import IfStatsBandwidth

        d = src_dict.copy()
        if_ = d.pop("if")

        ifstats = IfStats.from_dict(d.pop("ifstats"))

        bandwidth = []
        _bandwidth = d.pop("bandwidth")
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
