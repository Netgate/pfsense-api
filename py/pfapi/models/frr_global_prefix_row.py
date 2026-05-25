from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrGlobalPrefixRow")


@_attrs_define
class FrrGlobalPrefixRow:
    """
    Attributes:
        seq (str | Unset): Sequence
        action (str | Unset): Action (deny, permit)

            Permit or deny access to a network.
        source (str | Unset): Network
        any_ (str | Unset): Any
        ge (str | Unset): Minimum Prefix
        le (str | Unset): Maximum Prefix
        id (str | Unset): (readonly) ID assigned to this entry
    """

    seq: str | Unset = UNSET
    action: str | Unset = UNSET
    source: str | Unset = UNSET
    any_: str | Unset = UNSET
    ge: str | Unset = UNSET
    le: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        action = self.action

        source = self.source

        any_ = self.any_

        ge = self.ge

        le = self.le

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seq is not UNSET:
            field_dict["seq"] = seq
        if action is not UNSET:
            field_dict["action"] = action
        if source is not UNSET:
            field_dict["source"] = source
        if any_ is not UNSET:
            field_dict["any"] = any_
        if ge is not UNSET:
            field_dict["ge"] = ge
        if le is not UNSET:
            field_dict["le"] = le
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq = d.pop("seq", UNSET)

        action = d.pop("action", UNSET)

        source = d.pop("source", UNSET)

        any_ = d.pop("any", UNSET)

        ge = d.pop("ge", UNSET)

        le = d.pop("le", UNSET)

        id = d.pop("id", UNSET)

        frr_global_prefix_row = cls(
            seq=seq,
            action=action,
            source=source,
            any_=any_,
            ge=ge,
            le=le,
            id=id,
        )

        frr_global_prefix_row.additional_properties = d
        return frr_global_prefix_row

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
