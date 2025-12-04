from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimm import Dimm
    from ..models.memory_map import MemoryMap
    from ..models.memory_stat import MemoryStat


T = TypeVar("T", bound="Memory")


@_attrs_define
class Memory:
    """
    Attributes:
        memory_map (list[MemoryMap] | Unset):
        dimms (list[Dimm] | Unset):
        stats (MemoryStat | Unset):
    """

    memory_map: list[MemoryMap] | Unset = UNSET
    dimms: list[Dimm] | Unset = UNSET
    stats: MemoryStat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_map: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.memory_map, Unset):
            memory_map = []
            for memory_map_item_data in self.memory_map:
                memory_map_item = memory_map_item_data.to_dict()
                memory_map.append(memory_map_item)

        dimms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimms, Unset):
            dimms = []
            for dimms_item_data in self.dimms:
                dimms_item = dimms_item_data.to_dict()
                dimms.append(dimms_item)

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory_map is not UNSET:
            field_dict["memory_map"] = memory_map
        if dimms is not UNSET:
            field_dict["dimms"] = dimms
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimm import Dimm
        from ..models.memory_map import MemoryMap
        from ..models.memory_stat import MemoryStat

        d = dict(src_dict)
        _memory_map = d.pop("memory_map", UNSET)
        memory_map: list[MemoryMap] | Unset = UNSET
        if _memory_map is not UNSET:
            memory_map = []
            for memory_map_item_data in _memory_map:
                memory_map_item = MemoryMap.from_dict(memory_map_item_data)

                memory_map.append(memory_map_item)

        _dimms = d.pop("dimms", UNSET)
        dimms: list[Dimm] | Unset = UNSET
        if _dimms is not UNSET:
            dimms = []
            for dimms_item_data in _dimms:
                dimms_item = Dimm.from_dict(dimms_item_data)

                dimms.append(dimms_item)

        _stats = d.pop("stats", UNSET)
        stats: MemoryStat | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = MemoryStat.from_dict(_stats)

        memory = cls(
            memory_map=memory_map,
            dimms=dimms,
            stats=stats,
        )

        memory.additional_properties = d
        return memory

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
