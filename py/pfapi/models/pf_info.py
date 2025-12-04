from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PfInfo")


@_attrs_define
class PfInfo:
    """
    Attributes:
        info (str | Unset):
        memory (str | Unset):
        timeouts (str | Unset):
        interfaces (str | Unset):
    """

    info: str | Unset = UNSET
    memory: str | Unset = UNSET
    timeouts: str | Unset = UNSET
    interfaces: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info = self.info

        memory = self.memory

        timeouts = self.timeouts

        interfaces = self.interfaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info
        if memory is not UNSET:
            field_dict["memory"] = memory
        if timeouts is not UNSET:
            field_dict["timeouts"] = timeouts
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        info = d.pop("info", UNSET)

        memory = d.pop("memory", UNSET)

        timeouts = d.pop("timeouts", UNSET)

        interfaces = d.pop("interfaces", UNSET)

        pf_info = cls(
            info=info,
            memory=memory,
            timeouts=timeouts,
            interfaces=interfaces,
        )

        pf_info.additional_properties = d
        return pf_info

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
