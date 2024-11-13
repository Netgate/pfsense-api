from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_separator import FilterSeparator
    from ..models.fw_filter_rule import FWFilterRule


T = TypeVar("T", bound="FwRulesEntry")


@_attrs_define
class FwRulesEntry:
    """
    Attributes:
        rule (Union[Unset, FWFilterRule]):
        separator (Union[Unset, FilterSeparator]):
    """

    rule: Union[Unset, "FWFilterRule"] = UNSET
    separator: Union[Unset, "FilterSeparator"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        separator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.separator, Unset):
            separator = self.separator.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule is not UNSET:
            field_dict["rule"] = rule
        if separator is not UNSET:
            field_dict["separator"] = separator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_separator import FilterSeparator
        from ..models.fw_filter_rule import FWFilterRule

        d = src_dict.copy()
        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, FWFilterRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = FWFilterRule.from_dict(_rule)

        _separator = d.pop("separator", UNSET)
        separator: Union[Unset, FilterSeparator]
        if isinstance(_separator, Unset):
            separator = UNSET
        else:
            separator = FilterSeparator.from_dict(_separator)

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
