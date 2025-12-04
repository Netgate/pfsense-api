from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogStats")


@_attrs_define
class LogStats:
    """
    Attributes:
        clock_statistics (bool | Unset):
        discipline_statistics (bool | Unset):
        peer_statistics (bool | Unset):
    """

    clock_statistics: bool | Unset = UNSET
    discipline_statistics: bool | Unset = UNSET
    peer_statistics: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clock_statistics = self.clock_statistics

        discipline_statistics = self.discipline_statistics

        peer_statistics = self.peer_statistics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clock_statistics is not UNSET:
            field_dict["clock_statistics"] = clock_statistics
        if discipline_statistics is not UNSET:
            field_dict["discipline_statistics"] = discipline_statistics
        if peer_statistics is not UNSET:
            field_dict["peer_statistics"] = peer_statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clock_statistics = d.pop("clock_statistics", UNSET)

        discipline_statistics = d.pop("discipline_statistics", UNSET)

        peer_statistics = d.pop("peer_statistics", UNSET)

        log_stats = cls(
            clock_statistics=clock_statistics,
            discipline_statistics=discipline_statistics,
            peer_statistics=peer_statistics,
        )

        log_stats.additional_properties = d
        return log_stats

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
