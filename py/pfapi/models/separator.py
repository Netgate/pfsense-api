from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Separator")


@_attrs_define
class Separator:
    """
    Attributes:
        id (str | Unset):
        row (str | Unset):
        text (str | Unset):
        color (str | Unset):
        if_ (str | Unset):
    """

    id: str | Unset = UNSET
    row: str | Unset = UNSET
    text: str | Unset = UNSET
    color: str | Unset = UNSET
    if_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        row = self.row

        text = self.text

        color = self.color

        if_ = self.if_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if row is not UNSET:
            field_dict["row"] = row
        if text is not UNSET:
            field_dict["text"] = text
        if color is not UNSET:
            field_dict["color"] = color
        if if_ is not UNSET:
            field_dict["if"] = if_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        row = d.pop("row", UNSET)

        text = d.pop("text", UNSET)

        color = d.pop("color", UNSET)

        if_ = d.pop("if", UNSET)

        separator = cls(
            id=id,
            row=row,
            text=text,
            color=color,
            if_=if_,
        )

        separator.additional_properties = d
        return separator

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
