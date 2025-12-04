from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWTarget")


@_attrs_define
class FWTarget:
    """
    Attributes:
        name (str):
        descr (str | Unset):
        updatefreq (str | Unset):
    """

    name: str
    descr: str | Unset = UNSET
    updatefreq: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        updatefreq = self.updatefreq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if updatefreq is not UNSET:
            field_dict["updatefreq"] = updatefreq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        descr = d.pop("descr", UNSET)

        updatefreq = d.pop("updatefreq", UNSET)

        fw_target = cls(
            name=name,
            descr=descr,
            updatefreq=updatefreq,
        )

        fw_target.additional_properties = d
        return fw_target

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
