from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_rule_state import FWRuleState


T = TypeVar("T", bound="FWSingleRuleStates")


@_attrs_define
class FWSingleRuleStates:
    """
    Attributes:
        rule (Union[Unset, FWRuleState]):
    """

    rule: Union[Unset, "FWRuleState"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_rule_state import FWRuleState

        d = src_dict.copy()
        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, FWRuleState]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = FWRuleState.from_dict(_rule)

        fw_single_rule_states = cls(
            rule=rule,
        )

        fw_single_rule_states.additional_properties = d
        return fw_single_rule_states

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