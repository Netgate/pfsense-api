from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LogStats")


@_attrs_define
class LogStats:
    """
    Attributes:
        clock_statistics (bool):
        discipline_statistics (bool):
        peer_statistics (bool):
    """

    clock_statistics: bool
    discipline_statistics: bool
    peer_statistics: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clock_statistics = self.clock_statistics

        discipline_statistics = self.discipline_statistics

        peer_statistics = self.peer_statistics

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clock_statistics": clock_statistics,
                "discipline_statistics": discipline_statistics,
                "peer_statistics": peer_statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clock_statistics = d.pop("clock_statistics")

        discipline_statistics = d.pop("discipline_statistics")

        peer_statistics = d.pop("peer_statistics")

        log_stats = cls(
            clock_statistics=clock_statistics,
            discipline_statistics=discipline_statistics,
            peer_statistics=peer_statistics,
        )

        log_stats.additional_properties = d
        return log_stats

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
