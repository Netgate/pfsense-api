from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsertFilterSeparator")


@_attrs_define
class InsertFilterSeparator:
    """
    Attributes:
        after (bool | Unset):
        color (str | Unset):
        rule (str | Unset):
        text (str | Unset):
    """

    after: bool | Unset = UNSET
    color: str | Unset = UNSET
    rule: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        color = self.color

        rule = self.rule

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if color is not UNSET:
            field_dict["color"] = color
        if rule is not UNSET:
            field_dict["rule"] = rule
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        color = d.pop("color", UNSET)

        rule = d.pop("rule", UNSET)

        text = d.pop("text", UNSET)

        insert_filter_separator = cls(
            after=after,
            color=color,
            rule=rule,
            text=text,
        )

        insert_filter_separator.additional_properties = d
        return insert_filter_separator

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
