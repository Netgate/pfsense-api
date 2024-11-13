from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        timestamp (Union[Unset, float]):
        interfacestats (Union[Unset, List['QueueStats']]):
    """

    timestamp: Union[Unset, float] = UNSET
    interfacestats: Union[Unset, List["QueueStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp

        interfacestats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfacestats, Unset):
            interfacestats = []
            for interfacestats_item_data in self.interfacestats:
                interfacestats_item = interfacestats_item_data.to_dict()
                interfacestats.append(interfacestats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if interfacestats is not UNSET:
            field_dict["interfacestats"] = interfacestats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.queue_stats import QueueStats

        d = src_dict.copy()
        timestamp = d.pop("timestamp", UNSET)

        interfacestats = []
        _interfacestats = d.pop("interfacestats", UNSET)
        for interfacestats_item_data in _interfacestats or []:
            interfacestats_item = QueueStats.from_dict(interfacestats_item_data)

            interfacestats.append(interfacestats_item)

        traffic_queue_stats = cls(
            timestamp=timestamp,
            interfacestats=interfacestats,
        )

        traffic_queue_stats.additional_properties = d
        return traffic_queue_stats

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
