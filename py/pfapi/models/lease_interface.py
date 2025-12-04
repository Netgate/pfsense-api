from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaseInterface")


@_attrs_define
class LeaseInterface:
    """
    Attributes:
        name (str | Unset):
        start (str | Unset):
        end (str | Unset):
        num (int | Unset):
        capacity (int | Unset):
    """

    name: str | Unset = UNSET
    start: str | Unset = UNSET
    end: str | Unset = UNSET
    num: int | Unset = UNSET
    capacity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start = self.start

        end = self.end

        num = self.num

        capacity = self.capacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if num is not UNSET:
            field_dict["num"] = num
        if capacity is not UNSET:
            field_dict["capacity"] = capacity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        num = d.pop("num", UNSET)

        capacity = d.pop("capacity", UNSET)

        lease_interface = cls(
            name=name,
            start=start,
            end=end,
            num=num,
            capacity=capacity,
        )

        lease_interface.additional_properties = d
        return lease_interface

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
