from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.filter_separator import FilterSeparator
    from ..models.fw_filter_rule import FWFilterRule


T = TypeVar("T", bound="FwRulesEntry")


@_attrs_define
class FwRulesEntry:
    """
    Attributes:
        rule (FWFilterRule):
        separator (FilterSeparator):
    """

    rule: "FWFilterRule"
    separator: "FilterSeparator"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule = self.rule.to_dict()

        separator = self.separator.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "separator": separator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_separator import FilterSeparator
        from ..models.fw_filter_rule import FWFilterRule

        d = src_dict.copy()
        rule = FWFilterRule.from_dict(d.pop("rule"))

        separator = FilterSeparator.from_dict(d.pop("separator"))

        fw_rules_entry = cls(
            rule=rule,
            separator=separator,
        )

        fw_rules_entry.additional_properties = d
        return fw_rules_entry

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
