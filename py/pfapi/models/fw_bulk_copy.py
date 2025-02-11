from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FwBulkCopy")


@_attrs_define
class FwBulkCopy:
    """
    Attributes:
        iface (str):
        rules (List[str]):
    """

    iface: str
    rules: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iface = self.iface

        rules = self.rules

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iface": iface,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iface = d.pop("iface")

        rules = cast(List[str], d.pop("rules"))

        fw_bulk_copy = cls(
            iface=iface,
            rules=rules,
        )

        fw_bulk_copy.additional_properties = d
        return fw_bulk_copy

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
