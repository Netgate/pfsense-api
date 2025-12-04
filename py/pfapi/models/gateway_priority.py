from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayPriority")


@_attrs_define
class GatewayPriority:
    """
    Attributes:
        priority (str | Unset):
        priority_descr (str | Unset):
    """

    priority: str | Unset = UNSET
    priority_descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority = self.priority

        priority_descr = self.priority_descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority is not UNSET:
            field_dict["priority"] = priority
        if priority_descr is not UNSET:
            field_dict["priority_descr"] = priority_descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        priority = d.pop("priority", UNSET)

        priority_descr = d.pop("priority_descr", UNSET)

        gateway_priority = cls(
            priority=priority,
            priority_descr=priority_descr,
        )

        gateway_priority.additional_properties = d
        return gateway_priority

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
