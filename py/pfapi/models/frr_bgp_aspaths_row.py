from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrBgpAspathsRow")


@_attrs_define
class FrrBgpAspathsRow:
    """
    Attributes:
        seq (str | Unset): Sequence
        action (str | Unset): Action (deny, permit)

            Permit or deny access to a network.
        regex (str | Unset): Regular Expression
        id (str | Unset): (readonly) ID assigned to this entry
    """

    seq: str | Unset = UNSET
    action: str | Unset = UNSET
    regex: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        action = self.action

        regex = self.regex

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seq is not UNSET:
            field_dict["seq"] = seq
        if action is not UNSET:
            field_dict["action"] = action
        if regex is not UNSET:
            field_dict["regex"] = regex
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq = d.pop("seq", UNSET)

        action = d.pop("action", UNSET)

        regex = d.pop("regex", UNSET)

        id = d.pop("id", UNSET)

        frr_bgp_aspaths_row = cls(
            seq=seq,
            action=action,
            regex=regex,
            id=id,
        )

        frr_bgp_aspaths_row.additional_properties = d
        return frr_bgp_aspaths_row

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
