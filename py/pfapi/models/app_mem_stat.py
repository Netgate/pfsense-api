from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppMemStat")


@_attrs_define
class AppMemStat:
    """
    Attributes:
        mem_alloc (Union[Unset, int]): total allocated memory in use
        heap_alloc (Union[Unset, int]):
        heap_sys (Union[Unset, int]):
        heap_inuse (Union[Unset, int]):
        heap_idle (Union[Unset, int]):
        num_gc (Union[Unset, int]): number of garbage collections
        forced_gc (Union[Unset, int]): number of forced garbage collections
        sys_mem (Union[Unset, int]): total bytes of memory obtained from the OS
        last_gc_time (Union[Unset, str]):
    """

    mem_alloc: Union[Unset, int] = UNSET
    heap_alloc: Union[Unset, int] = UNSET
    heap_sys: Union[Unset, int] = UNSET
    heap_inuse: Union[Unset, int] = UNSET
    heap_idle: Union[Unset, int] = UNSET
    num_gc: Union[Unset, int] = UNSET
    forced_gc: Union[Unset, int] = UNSET
    sys_mem: Union[Unset, int] = UNSET
    last_gc_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mem_alloc = self.mem_alloc

        heap_alloc = self.heap_alloc

        heap_sys = self.heap_sys

        heap_inuse = self.heap_inuse

        heap_idle = self.heap_idle

        num_gc = self.num_gc

        forced_gc = self.forced_gc

        sys_mem = self.sys_mem

        last_gc_time = self.last_gc_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mem_alloc is not UNSET:
            field_dict["mem_alloc"] = mem_alloc
        if heap_alloc is not UNSET:
            field_dict["heap_alloc"] = heap_alloc
        if heap_sys is not UNSET:
            field_dict["heap_sys"] = heap_sys
        if heap_inuse is not UNSET:
            field_dict["heap_inuse"] = heap_inuse
        if heap_idle is not UNSET:
            field_dict["heap_idle"] = heap_idle
        if num_gc is not UNSET:
            field_dict["num_gc"] = num_gc
        if forced_gc is not UNSET:
            field_dict["forced_gc"] = forced_gc
        if sys_mem is not UNSET:
            field_dict["sys_mem"] = sys_mem
        if last_gc_time is not UNSET:
            field_dict["last_gc_time"] = last_gc_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mem_alloc = d.pop("mem_alloc", UNSET)

        heap_alloc = d.pop("heap_alloc", UNSET)

        heap_sys = d.pop("heap_sys", UNSET)

        heap_inuse = d.pop("heap_inuse", UNSET)

        heap_idle = d.pop("heap_idle", UNSET)

        num_gc = d.pop("num_gc", UNSET)

        forced_gc = d.pop("forced_gc", UNSET)

        sys_mem = d.pop("sys_mem", UNSET)

        last_gc_time = d.pop("last_gc_time", UNSET)

        app_mem_stat = cls(
            mem_alloc=mem_alloc,
            heap_alloc=heap_alloc,
            heap_sys=heap_sys,
            heap_inuse=heap_inuse,
            heap_idle=heap_idle,
            num_gc=num_gc,
            forced_gc=forced_gc,
            sys_mem=sys_mem,
            last_gc_time=last_gc_time,
        )

        app_mem_stat.additional_properties = d
        return app_mem_stat

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
