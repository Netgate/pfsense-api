from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        loadavg (Union[Unset, List[int]]):
        memstat (Union[Unset, AppMemStat]):
    """

    loadavg: Union[Unset, List[int]] = UNSET
    memstat: Union[Unset, "AppMemStat"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        loadavg: Union[Unset, List[int]] = UNSET
        if not isinstance(self.loadavg, Unset):
            loadavg = self.loadavg

        memstat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.memstat, Unset):
            memstat = self.memstat.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loadavg is not UNSET:
            field_dict["loadavg"] = loadavg
        if memstat is not UNSET:
            field_dict["memstat"] = memstat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_mem_stat import AppMemStat

        d = src_dict.copy()
        loadavg = cast(List[int], d.pop("loadavg", UNSET))

        _memstat = d.pop("memstat", UNSET)
        memstat: Union[Unset, AppMemStat]
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
