from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayGroupPriority")


@_attrs_define
class GatewayGroupPriority:
    """
    Attributes:
        gateway (str | Unset):
        priority (str | Unset):
        vaddress (str | Unset):
    """

    gateway: str | Unset = UNSET
    priority: str | Unset = UNSET
    vaddress: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway

        priority = self.priority

        vaddress = self.vaddress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if priority is not UNSET:
            field_dict["priority"] = priority
        if vaddress is not UNSET:
            field_dict["vaddress"] = vaddress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway = d.pop("gateway", UNSET)

        priority = d.pop("priority", UNSET)

        vaddress = d.pop("vaddress", UNSET)

        gateway_group_priority = cls(
            gateway=gateway,
            priority=priority,
            vaddress=vaddress,
        )

        gateway_group_priority.additional_properties = d
        return gateway_group_priority

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
