from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MDNSRecord")


@_attrs_define
class MDNSRecord:
    """simplified version of a DNS resource record

    Attributes:
        name (str | Unset):
        class_ (str | Unset):
        type_ (str | Unset):
        value (str | Unset): IP address, CNAME, or TXT value
    """

    name: str | Unset = UNSET
    class_: str | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        class_ = self.class_

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if class_ is not UNSET:
            field_dict["class"] = class_
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        class_ = d.pop("class", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        mdns_record = cls(
            name=name,
            class_=class_,
            type_=type_,
            value=value,
        )

        mdns_record.additional_properties = d
        return mdns_record

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
