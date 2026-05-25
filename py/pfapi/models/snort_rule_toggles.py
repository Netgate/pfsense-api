from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_rule_toggle_entry import SnortRuleToggleEntry


T = TypeVar("T", bound="SnortRuleToggles")


@_attrs_define
class SnortRuleToggles:
    """
    Attributes:
        rule_options (list[SnortRuleToggleEntry] | Unset):
        reset_all (bool | Unset): reset all rule overrides; rule_options is ignored
    """

    rule_options: list[SnortRuleToggleEntry] | Unset = UNSET
    reset_all: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rule_options, Unset):
            rule_options = []
            for rule_options_item_data in self.rule_options:
                rule_options_item = rule_options_item_data.to_dict()
                rule_options.append(rule_options_item)

        reset_all = self.reset_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_options is not UNSET:
            field_dict["rule_options"] = rule_options
        if reset_all is not UNSET:
            field_dict["reset_all"] = reset_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_rule_toggle_entry import SnortRuleToggleEntry

        d = dict(src_dict)
        _rule_options = d.pop("rule_options", UNSET)
        rule_options: list[SnortRuleToggleEntry] | Unset = UNSET
        if _rule_options is not UNSET:
            rule_options = []
            for rule_options_item_data in _rule_options:
                rule_options_item = SnortRuleToggleEntry.from_dict(rule_options_item_data)

                rule_options.append(rule_options_item)

        reset_all = d.pop("reset_all", UNSET)

        snort_rule_toggles = cls(
            rule_options=rule_options,
            reset_all=reset_all,
        )

        snort_rule_toggles.additional_properties = d
        return snort_rule_toggles

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
