from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CorednsEasySetupReason")


@_attrs_define
class CorednsEasySetupReason:
    """
    Attributes:
        can_easy_setup (bool | Unset):
        reasons (list[str] | Unset):
    """

    can_easy_setup: bool | Unset = UNSET
    reasons: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_easy_setup = self.can_easy_setup

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_easy_setup is not UNSET:
            field_dict["can_easy_setup"] = can_easy_setup
        if reasons is not UNSET:
            field_dict["reasons"] = reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_easy_setup = d.pop("can_easy_setup", UNSET)

        reasons = cast(list[str], d.pop("reasons", UNSET))

        coredns_easy_setup_reason = cls(
            can_easy_setup=can_easy_setup,
            reasons=reasons,
        )

        coredns_easy_setup_reason.additional_properties = d
        return coredns_easy_setup_reason

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
