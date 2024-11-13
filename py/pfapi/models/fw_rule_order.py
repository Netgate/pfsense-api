from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.separator import Separator


T = TypeVar("T", bound="FWRuleOrder")


@_attrs_define
class FWRuleOrder:
    """
    Attributes:
        rule (Union[Unset, List[int]]):
        separator (Union[Unset, List['Separator']]):
    """

    rule: Union[Unset, List[int]] = UNSET
    separator: Union[Unset, List["Separator"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule: Union[Unset, List[int]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule

        separator: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.separator, Unset):
            separator = []
            for separator_item_data in self.separator:
                separator_item = separator_item_data.to_dict()
                separator.append(separator_item)

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
        from ..models.separator import Separator

        d = src_dict.copy()
        rule = cast(List[int], d.pop("rule", UNSET))

        separator = []
        _separator = d.pop("separator", UNSET)
        for separator_item_data in _separator or []:
            separator_item = Separator.from_dict(separator_item_data)

            separator.append(separator_item)

        fw_rule_order = cls(
            rule=rule,
            separator=separator,
        )

        fw_rule_order.additional_properties = d
        return fw_rule_order

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
