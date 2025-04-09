from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_npt_rule import NATNptRule
    from ..models.simple_interface import SimpleInterface


T = TypeVar("T", bound="NATNptRules")


@_attrs_define
class NATNptRules:
    """
    Attributes:
        interfacelist (Union[Unset, List['SimpleInterface']]):
        rules (Union[Unset, List['NATNptRule']]):
    """

    interfacelist: Union[Unset, List["SimpleInterface"]] = UNSET
    rules: Union[Unset, List["NATNptRule"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfacelist: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfacelist, Unset):
            interfacelist = []
            for interfacelist_item_data in self.interfacelist:
                interfacelist_item = interfacelist_item_data.to_dict()
                interfacelist.append(interfacelist_item)

        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfacelist is not UNSET:
            field_dict["interfacelist"] = interfacelist
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_npt_rule import NATNptRule
        from ..models.simple_interface import SimpleInterface

        d = src_dict.copy()
        interfacelist = []
        _interfacelist = d.pop("interfacelist", UNSET)
        for interfacelist_item_data in _interfacelist or []:
            interfacelist_item = SimpleInterface.from_dict(interfacelist_item_data)

            interfacelist.append(interfacelist_item)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = NATNptRule.from_dict(rules_item_data)

            rules.append(rules_item)

        nat_npt_rules = cls(
            interfacelist=interfacelist,
            rules=rules,
        )

        nat_npt_rules.additional_properties = d
        return nat_npt_rules

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
