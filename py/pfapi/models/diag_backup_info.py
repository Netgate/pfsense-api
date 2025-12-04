from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagBackupInfo")


@_attrs_define
class DiagBackupInfo:
    """
    Attributes:
        time (int | Unset):
        desc (str | Unset):
        size (int | Unset):
        vers (str | Unset):
    """

    time: int | Unset = UNSET
    desc: str | Unset = UNSET
    size: int | Unset = UNSET
    vers: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        desc = self.desc

        size = self.size

        vers = self.vers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if desc is not UNSET:
            field_dict["desc"] = desc
        if size is not UNSET:
            field_dict["size"] = size
        if vers is not UNSET:
            field_dict["vers"] = vers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        desc = d.pop("desc", UNSET)

        size = d.pop("size", UNSET)

        vers = d.pop("vers", UNSET)

        diag_backup_info = cls(
            time=time,
            desc=desc,
            size=size,
            vers=vers,
        )

        diag_backup_info.additional_properties = d
        return diag_backup_info

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
