from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FwBulkToggle")


@_attrs_define
class FwBulkToggle:
    """
    Attributes:
        rules (Union[Unset, List[str]]):
        value (Union[Unset, bool]):
    """

    rules: Union[Unset, List[str]] = UNSET
    value: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rules: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rules is not UNSET:
            field_dict["rules"] = rules
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rules = cast(List[str], d.pop("rules", UNSET))

        value = d.pop("value", UNSET)

        fw_bulk_toggle = cls(
            rules=rules,
            value=value,
        )

        fw_bulk_toggle.additional_properties = d
        return fw_bulk_toggle

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
