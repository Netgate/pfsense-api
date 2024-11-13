from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        memory_map (Union[Unset, List['MemoryMap']]):
        dimms (Union[Unset, List['Dimm']]):
        stats (Union[Unset, MemoryStat]):
    """

    memory_map: Union[Unset, List["MemoryMap"]] = UNSET
    dimms: Union[Unset, List["Dimm"]] = UNSET
    stats: Union[Unset, "MemoryStat"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        memory_map: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.memory_map, Unset):
            memory_map = []
            for memory_map_item_data in self.memory_map:
                memory_map_item = memory_map_item_data.to_dict()
                memory_map.append(memory_map_item)

        dimms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dimms, Unset):
            dimms = []
            for dimms_item_data in self.dimms:
                dimms_item = dimms_item_data.to_dict()
                dimms.append(dimms_item)

        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dimm import Dimm
        from ..models.memory_map import MemoryMap
        from ..models.memory_stat import MemoryStat

        d = src_dict.copy()
        memory_map = []
        _memory_map = d.pop("memory_map", UNSET)
        for memory_map_item_data in _memory_map or []:
            memory_map_item = MemoryMap.from_dict(memory_map_item_data)

            memory_map.append(memory_map_item)

        dimms = []
        _dimms = d.pop("dimms", UNSET)
        for dimms_item_data in _dimms or []:
            dimms_item = Dimm.from_dict(dimms_item_data)

            dimms.append(dimms_item)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, MemoryStat]
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
