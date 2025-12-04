from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptiveElement")


@_attrs_define
class CaptiveElement:
    """
    Attributes:
        name (str | Unset):
        size (str | Unset):
        nocontent (str | Unset):
    """

    name: str | Unset = UNSET
    size: str | Unset = UNSET
    nocontent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        size = self.size

        nocontent = self.nocontent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if nocontent is not UNSET:
            field_dict["nocontent"] = nocontent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        nocontent = d.pop("nocontent", UNSET)

        captive_element = cls(
            name=name,
            size=size,
            nocontent=nocontent,
        )

        captive_element.additional_properties = d
        return captive_element

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
