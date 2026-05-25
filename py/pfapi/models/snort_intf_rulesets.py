from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_intf_ruleset import SnortIntfRuleset


T = TypeVar("T", bound="SnortIntfRulesets")


@_attrs_define
class SnortIntfRulesets:
    """
    Attributes:
        rulesets (list[SnortIntfRuleset] | Unset):
    """

    rulesets: list[SnortIntfRuleset] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rulesets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rulesets, Unset):
            rulesets = []
            for rulesets_item_data in self.rulesets:
                rulesets_item = rulesets_item_data.to_dict()
                rulesets.append(rulesets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rulesets is not UNSET:
            field_dict["rulesets"] = rulesets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_intf_ruleset import SnortIntfRuleset

        d = dict(src_dict)
        _rulesets = d.pop("rulesets", UNSET)
        rulesets: list[SnortIntfRuleset] | Unset = UNSET
        if _rulesets is not UNSET:
            rulesets = []
            for rulesets_item_data in _rulesets:
                rulesets_item = SnortIntfRuleset.from_dict(rulesets_item_data)

                rulesets.append(rulesets_item)

        snort_intf_rulesets = cls(
            rulesets=rulesets,
        )

        snort_intf_rulesets.additional_properties = d
        return snort_intf_rulesets

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
