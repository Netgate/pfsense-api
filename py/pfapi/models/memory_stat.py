from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryStat")


@_attrs_define
class MemoryStat:
    """
    Attributes:
        total (Union[Unset, int]):
        reserved (Union[Unset, int]):
        used (Union[Unset, int]):
    """

    total: Union[Unset, int] = UNSET
    reserved: Union[Unset, int] = UNSET
    used: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total

        reserved = self.reserved

        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        reserved = d.pop("reserved", UNSET)

        used = d.pop("used", UNSET)

        memory_stat = cls(
            total=total,
            reserved=reserved,
            used=used,
        )

        memory_stat.additional_properties = d
        return memory_stat

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
