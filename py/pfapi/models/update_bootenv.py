from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBootenv")


@_attrs_define
class UpdateBootenv:
    """
    Attributes:
        old_name (str):
        name (str | Unset):
        descr (str | Unset):
        protect (bool | Unset):
    """

    old_name: str
    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    protect: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_name = self.old_name

        name = self.name

        descr = self.descr

        protect = self.protect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old_name": old_name,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if protect is not UNSET:
            field_dict["protect"] = protect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        old_name = d.pop("old_name")

        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        protect = d.pop("protect", UNSET)

        update_bootenv = cls(
            old_name=old_name,
            name=name,
            descr=descr,
            protect=protect,
        )

        update_bootenv.additional_properties = d
        return update_bootenv

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
