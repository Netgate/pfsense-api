from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_resolver_status_speed import DNSResolverStatusSpeed
    from ..models.dns_resolver_status_stats import DNSResolverStatusStats


T = TypeVar("T", bound="DNSResolverStatus")


@_attrs_define
class DNSResolverStatus:
    """
    Attributes:
        speed (Union[Unset, List['DNSResolverStatusSpeed']]):
        stats (Union[Unset, List['DNSResolverStatusStats']]):
    """

    speed: Union[Unset, List["DNSResolverStatusSpeed"]] = UNSET
    stats: Union[Unset, List["DNSResolverStatusStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        speed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.speed, Unset):
            speed = []
            for speed_item_data in self.speed:
                speed_item = speed_item_data.to_dict()
                speed.append(speed_item)

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if speed is not UNSET:
            field_dict["speed"] = speed
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dns_resolver_status_speed import DNSResolverStatusSpeed
        from ..models.dns_resolver_status_stats import DNSResolverStatusStats

        d = src_dict.copy()
        speed = []
        _speed = d.pop("speed", UNSET)
        for speed_item_data in _speed or []:
            speed_item = DNSResolverStatusSpeed.from_dict(speed_item_data)

            speed.append(speed_item)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = DNSResolverStatusStats.from_dict(stats_item_data)

            stats.append(stats_item)

        dns_resolver_status = cls(
            speed=speed,
            stats=stats,
        )

        dns_resolver_status.additional_properties = d
        return dns_resolver_status

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
