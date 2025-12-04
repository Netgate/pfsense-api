from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_mem_stat import AppMemStat


T = TypeVar("T", bound="LoadAvg")


@_attrs_define
class LoadAvg:
    """
    Attributes:
        loadavg (list[int] | Unset):
        memstat (AppMemStat | Unset):
    """

    loadavg: list[int] | Unset = UNSET
    memstat: AppMemStat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loadavg: list[int] | Unset = UNSET
        if not isinstance(self.loadavg, Unset):
            loadavg = self.loadavg

        memstat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memstat, Unset):
            memstat = self.memstat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loadavg is not UNSET:
            field_dict["loadavg"] = loadavg
        if memstat is not UNSET:
            field_dict["memstat"] = memstat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_mem_stat import AppMemStat

        d = dict(src_dict)
        loadavg = cast(list[int], d.pop("loadavg", UNSET))

        _memstat = d.pop("memstat", UNSET)
        memstat: AppMemStat | Unset
        if isinstance(_memstat, Unset):
            memstat = UNSET
        else:
            memstat = AppMemStat.from_dict(_memstat)

        load_avg = cls(
            loadavg=loadavg,
            memstat=memstat,
        )

        load_avg.additional_properties = d
        return load_avg

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
