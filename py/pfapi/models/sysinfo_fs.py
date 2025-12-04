from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SysinfoFs")


@_attrs_define
class SysinfoFs:
    """
    Attributes:
        path (str | Unset):
        fs_name (str | Unset):
        fs_type (str | Unset):
        total (int | Unset):
        used (int | Unset):
    """

    path: str | Unset = UNSET
    fs_name: str | Unset = UNSET
    fs_type: str | Unset = UNSET
    total: int | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        fs_name = self.fs_name

        fs_type = self.fs_type

        total = self.total

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if fs_name is not UNSET:
            field_dict["fs_name"] = fs_name
        if fs_type is not UNSET:
            field_dict["fs_type"] = fs_type
        if total is not UNSET:
            field_dict["total"] = total
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        fs_name = d.pop("fs_name", UNSET)

        fs_type = d.pop("fs_type", UNSET)

        total = d.pop("total", UNSET)

        used = d.pop("used", UNSET)

        sysinfo_fs = cls(
            path=path,
            fs_name=fs_name,
            fs_type=fs_type,
            total=total,
            used=used,
        )

        sysinfo_fs.additional_properties = d
        return sysinfo_fs

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
