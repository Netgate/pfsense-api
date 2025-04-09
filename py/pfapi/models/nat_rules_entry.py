from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_rule import NATRule
    from ..models.separator import Separator


T = TypeVar("T", bound="NATRulesEntry")


@_attrs_define
class NATRulesEntry:
    """
    Attributes:
        rule (Union[Unset, NATRule]):
        separator (Union[Unset, Separator]):
    """

    rule: Union[Unset, "NATRule"] = UNSET
    separator: Union[Unset, "Separator"] = UNSET
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
        from ..models.nat_rule import NATRule
        from ..models.separator import Separator

        d = src_dict.copy()
        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, NATRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = NATRule.from_dict(_rule)

        _separator = d.pop("separator", UNSET)
        separator: Union[Unset, Separator]
        if isinstance(_separator, Unset):
            separator = UNSET
        else:
            separator = Separator.from_dict(_separator)

        nat_rules_entry = cls(
            rule=rule,
            separator=separator,
        )

        nat_rules_entry.additional_properties = d
        return nat_rules_entry

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
