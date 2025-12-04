from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LimiterInfo")


@_attrs_define
class LimiterInfo:
    """
    Attributes:
        pipes (str | Unset):
        sched (str | Unset):
        queues (str | Unset):
    """

    pipes: str | Unset = UNSET
    sched: str | Unset = UNSET
    queues: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipes = self.pipes

        sched = self.sched

        queues = self.queues

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipes is not UNSET:
            field_dict["pipes"] = pipes
        if sched is not UNSET:
            field_dict["sched"] = sched
        if queues is not UNSET:
            field_dict["queues"] = queues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pipes = d.pop("pipes", UNSET)

        sched = d.pop("sched", UNSET)

        queues = d.pop("queues", UNSET)

        limiter_info = cls(
            pipes=pipes,
            sched=sched,
            queues=queues,
        )

        limiter_info.additional_properties = d
        return limiter_info

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
