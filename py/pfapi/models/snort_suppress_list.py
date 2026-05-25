from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortSuppressList")


@_attrs_define
class SnortSuppressList:
    """
    Attributes:
        name (str | Unset):
        descr (str | Unset):
        text (str | Unset): text contents of suppression list
        new_name (str | Unset): for updating an existing suppression list
        lua_text (str | Unset):
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    text: str | Unset = UNSET
    new_name: str | Unset = UNSET
    lua_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        text = self.text

        new_name = self.new_name

        lua_text = self.lua_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if text is not UNSET:
            field_dict["text"] = text
        if new_name is not UNSET:
            field_dict["new_name"] = new_name
        if lua_text is not UNSET:
            field_dict["lua_text"] = lua_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        text = d.pop("text", UNSET)

        new_name = d.pop("new_name", UNSET)

        lua_text = d.pop("lua_text", UNSET)

        snort_suppress_list = cls(
            name=name,
            descr=descr,
            text=text,
            new_name=new_name,
            lua_text=lua_text,
        )

        snort_suppress_list.additional_properties = d
        return snort_suppress_list

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
