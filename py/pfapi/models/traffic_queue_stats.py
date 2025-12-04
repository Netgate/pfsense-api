from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.queue_stats import QueueStats


T = TypeVar("T", bound="TrafficQueueStats")


@_attrs_define
class TrafficQueueStats:
    """
    Attributes:
        timestamp (float | Unset):
        interfacestats (list[QueueStats] | Unset):
    """

    timestamp: float | Unset = UNSET
    interfacestats: list[QueueStats] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        interfacestats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfacestats, Unset):
            interfacestats = []
            for interfacestats_item_data in self.interfacestats:
                interfacestats_item = interfacestats_item_data.to_dict()
                interfacestats.append(interfacestats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if interfacestats is not UNSET:
            field_dict["interfacestats"] = interfacestats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queue_stats import QueueStats

        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        _interfacestats = d.pop("interfacestats", UNSET)
        interfacestats: list[QueueStats] | Unset = UNSET
        if _interfacestats is not UNSET:
            interfacestats = []
            for interfacestats_item_data in _interfacestats:
                interfacestats_item = QueueStats.from_dict(interfacestats_item_data)

                interfacestats.append(interfacestats_item)

        traffic_queue_stats = cls(
            timestamp=timestamp,
            interfacestats=interfacestats,
        )

        traffic_queue_stats.additional_properties = d
        return traffic_queue_stats

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
