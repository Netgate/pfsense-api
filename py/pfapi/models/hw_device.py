from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HWDevice")


@_attrs_define
class HWDevice:
    """
    Attributes:
        name (str | Unset):
        location (str | Unset):
        type_ (str | Unset):
        vendor (str | Unset):
        class_ (str | Unset):
    """

    name: str | Unset = UNSET
    location: str | Unset = UNSET
    type_: str | Unset = UNSET
    vendor: str | Unset = UNSET
    class_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        location = self.location

        type_ = self.type_

        vendor = self.vendor

        class_ = self.class_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if location is not UNSET:
            field_dict["location"] = location
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if class_ is not UNSET:
            field_dict["class"] = class_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        location = d.pop("location", UNSET)

        type_ = d.pop("type", UNSET)

        vendor = d.pop("vendor", UNSET)

        class_ = d.pop("class", UNSET)

        hw_device = cls(
            name=name,
            location=location,
            type_=type_,
            vendor=vendor,
            class_=class_,
        )

        hw_device.additional_properties = d
        return hw_device

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
