from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_filter_rule import FWFilterRule


T = TypeVar("T", bound="InsertFilterRule")


@_attrs_define
class InsertFilterRule:
    """
    Attributes:
        reference (Union[Unset, str]):
        after (Union[Unset, bool]):
        rule (Union[Unset, FWFilterRule]):
    """

    reference: Union[Unset, str] = UNSET
    after: Union[Unset, bool] = UNSET
    rule: Union[Unset, "FWFilterRule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference = self.reference

        after = self.after

        rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference is not UNSET:
            field_dict["reference"] = reference
        if after is not UNSET:
            field_dict["after"] = after
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_filter_rule import FWFilterRule

        d = src_dict.copy()
        reference = d.pop("reference", UNSET)

        after = d.pop("after", UNSET)

        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, FWFilterRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = FWFilterRule.from_dict(_rule)

        insert_filter_rule = cls(
            reference=reference,
            after=after,
            rule=rule,
        )

        insert_filter_rule.additional_properties = d
        return insert_filter_rule

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
