from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWFilterRuleNAT")


@_attrs_define
class FWFilterRuleNAT:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        source (Union[Unset, str]): address to apply to the NAT64 rule
        type (Union[Unset, str]): auto, network, alias, interface
    """

    enabled: Union[Unset, bool] = UNSET
    source: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        source = self.source

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if source is not UNSET:
            field_dict["source"] = source
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        source = d.pop("source", UNSET)

        type = d.pop("type", UNSET)

        fw_filter_rule_nat = cls(
            enabled=enabled,
            source=source,
            type=type,
        )

        fw_filter_rule_nat.additional_properties = d
        return fw_filter_rule_nat

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
