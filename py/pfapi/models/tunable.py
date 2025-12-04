from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tunable")


@_attrs_define
class Tunable:
    """
    Attributes:
        tunable (str | Unset):
        value (str | Unset):
        descr (str | Unset):
        modified (bool | Unset):
    """

    tunable: str | Unset = UNSET
    value: str | Unset = UNSET
    descr: str | Unset = UNSET
    modified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tunable = self.tunable

        value = self.value

        descr = self.descr

        modified = self.modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tunable is not UNSET:
            field_dict["tunable"] = tunable
        if value is not UNSET:
            field_dict["value"] = value
        if descr is not UNSET:
            field_dict["descr"] = descr
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tunable = d.pop("tunable", UNSET)

        value = d.pop("value", UNSET)

        descr = d.pop("descr", UNSET)

        modified = d.pop("modified", UNSET)

        tunable = cls(
            tunable=tunable,
            value=value,
            descr=descr,
            modified=modified,
        )

        tunable.additional_properties = d
        return tunable

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
