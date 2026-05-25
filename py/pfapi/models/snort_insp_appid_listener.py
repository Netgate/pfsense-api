from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspAppidListener")


@_attrs_define
class SnortInspAppidListener:
    """
    Attributes:
        json_logging (bool | Unset): log appid data in json format; default false
        file (str | Unset): output data to given file
    """

    json_logging: bool | Unset = UNSET
    file: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_logging = self.json_logging

        file = self.file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if json_logging is not UNSET:
            field_dict["json_logging"] = json_logging
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        json_logging = d.pop("json_logging", UNSET)

        file = d.pop("file", UNSET)

        snort_insp_appid_listener = cls(
            json_logging=json_logging,
            file=file,
        )

        snort_insp_appid_listener.additional_properties = d
        return snort_insp_appid_listener

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
