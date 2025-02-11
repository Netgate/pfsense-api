from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InsertFilterSeparator")


@_attrs_define
class InsertFilterSeparator:
    """
    Attributes:
        after (bool):
        color (str):
        rule (str):
        text (str):
    """

    after: bool
    color: str
    rule: str
    text: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after = self.after

        color = self.color

        rule = self.rule

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after": after,
                "color": color,
                "rule": rule,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after = d.pop("after")

        color = d.pop("color")

        rule = d.pop("rule")

        text = d.pop("text")

        insert_filter_separator = cls(
            after=after,
            color=color,
            rule=rule,
            text=text,
        )

        insert_filter_separator.additional_properties = d
        return insert_filter_separator

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
