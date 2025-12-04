from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BridgeCapableInterface")


@_attrs_define
class BridgeCapableInterface:
    """
    Attributes:
        if_identity (str | Unset):
        if_assigned_name (str | Unset):
    """

    if_identity: str | Unset = UNSET
    if_assigned_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_identity = self.if_identity

        if_assigned_name = self.if_assigned_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_identity is not UNSET:
            field_dict["if_identity"] = if_identity
        if if_assigned_name is not UNSET:
            field_dict["if_assigned_name"] = if_assigned_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        if_identity = d.pop("if_identity", UNSET)

        if_assigned_name = d.pop("if_assigned_name", UNSET)

        bridge_capable_interface = cls(
            if_identity=if_identity,
            if_assigned_name=if_assigned_name,
        )

        bridge_capable_interface.additional_properties = d
        return bridge_capable_interface

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
