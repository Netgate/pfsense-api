from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_rule import SnortRule


T = TypeVar("T", bound="SnortIntfRuleset")


@_attrs_define
class SnortIntfRuleset:
    """
    Attributes:
        name (str | Unset): source ruleset (archive) name
        ruleset_type (str | Unset):
        rules (list[SnortRule] | Unset):
        cat (list[str] | Unset):
    """

    name: str | Unset = UNSET
    ruleset_type: str | Unset = UNSET
    rules: list[SnortRule] | Unset = UNSET
    cat: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ruleset_type = self.ruleset_type

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        cat: list[str] | Unset = UNSET
        if not isinstance(self.cat, Unset):
            cat = self.cat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ruleset_type is not UNSET:
            field_dict["ruleset_type"] = ruleset_type
        if rules is not UNSET:
            field_dict["rules"] = rules
        if cat is not UNSET:
            field_dict["cat"] = cat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_rule import SnortRule

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        ruleset_type = d.pop("ruleset_type", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: list[SnortRule] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = SnortRule.from_dict(rules_item_data)

                rules.append(rules_item)

        cat = cast(list[str], d.pop("cat", UNSET))

        snort_intf_ruleset = cls(
            name=name,
            ruleset_type=ruleset_type,
            rules=rules,
            cat=cat,
        )

        snort_intf_ruleset.additional_properties = d
        return snort_intf_ruleset

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
