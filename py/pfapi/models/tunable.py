from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Tunable")


@_attrs_define
class Tunable:
    """
    Attributes:
        tunable (str):
        value (str):
        descr (str):
        modified (bool):
    """

    tunable: str
    value: str
    descr: str
    modified: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tunable = self.tunable

        value = self.value

        descr = self.descr

        modified = self.modified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tunable": tunable,
                "value": value,
                "descr": descr,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tunable = d.pop("tunable")

        value = d.pop("value")

        descr = d.pop("descr")

        modified = d.pop("modified")

        tunable = cls(
            tunable=tunable,
            value=value,
            descr=descr,
            modified=modified,
        )

        tunable.additional_properties = d
        return tunable

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
