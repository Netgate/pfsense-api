from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortIntfRulesetOpt")


@_attrs_define
class SnortIntfRulesetOpt:
    """
    Attributes:
        name (str | Unset): ruleset name
        policy (str | Unset): detection/prevention policy - balanced, security, etc.
        cat (list[str] | Unset):
    """

    name: str | Unset = UNSET
    policy: str | Unset = UNSET
    cat: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        policy = self.policy

        cat: list[str] | Unset = UNSET
        if not isinstance(self.cat, Unset):
            cat = self.cat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if policy is not UNSET:
            field_dict["policy"] = policy
        if cat is not UNSET:
            field_dict["cat"] = cat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        policy = d.pop("policy", UNSET)

        cat = cast(list[str], d.pop("cat", UNSET))

        snort_intf_ruleset_opt = cls(
            name=name,
            policy=policy,
            cat=cat,
        )

        snort_intf_ruleset_opt.additional_properties = d
        return snort_intf_ruleset_opt

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
