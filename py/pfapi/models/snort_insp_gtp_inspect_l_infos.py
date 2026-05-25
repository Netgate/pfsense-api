from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspGtpInspectLInfos")


@_attrs_define
class SnortInspGtpInspectLInfos:
    """
    Attributes:
        type_ (int | Unset): information element type code { 0:255 }; default 0
        name (str | Unset): information element name
        length (int | Unset): information element type code { 0:255 }; default 0
    """

    type_: int | Unset = UNSET
    name: str | Unset = UNSET
    length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        length = self.length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if length is not UNSET:
            field_dict["length"] = length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        length = d.pop("length", UNSET)

        snort_insp_gtp_inspect_l_infos = cls(
            type_=type_,
            name=name,
            length=length,
        )

        snort_insp_gtp_inspect_l_infos.additional_properties = d
        return snort_insp_gtp_inspect_l_infos

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
