from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fw_filter_rule import FWFilterRule


T = TypeVar("T", bound="InsertFilterRule")


@_attrs_define
class InsertFilterRule:
    """
    Attributes:
        reference (str):
        after (bool):
        rule (FWFilterRule):
    """

    reference: str
    after: bool
    rule: "FWFilterRule"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference = self.reference

        after = self.after

        rule = self.rule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
                "after": after,
                "rule": rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_filter_rule import FWFilterRule

        d = src_dict.copy()
        reference = d.pop("reference")

        after = d.pop("after")

        rule = FWFilterRule.from_dict(d.pop("rule"))

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
