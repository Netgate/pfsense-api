from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_filter_rule import FWFilterRule


T = TypeVar("T", bound="FWSingleFilterRule")


@_attrs_define
class FWSingleFilterRule:
    """
    Attributes:
        rule (FWFilterRule | Unset):
    """

    rule: FWFilterRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_filter_rule import FWFilterRule

        d = dict(src_dict)
        _rule = d.pop("rule", UNSET)
        rule: FWFilterRule | Unset
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = FWFilterRule.from_dict(_rule)

        fw_single_filter_rule = cls(
            rule=rule,
        )

        fw_single_filter_rule.additional_properties = d
        return fw_single_filter_rule

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
