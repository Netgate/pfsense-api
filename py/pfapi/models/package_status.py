from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageStatus")


@_attrs_define
class PackageStatus:
    """
    Attributes:
        name (str | Unset):
        version (str | Unset):
        descr (str | Unset):
        enabled (bool | Unset):
    """

    name: str | Unset = UNSET
    version: str | Unset = UNSET
    descr: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        descr = self.descr

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if descr is not UNSET:
            field_dict["descr"] = descr
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        descr = d.pop("descr", UNSET)

        enabled = d.pop("enabled", UNSET)

        package_status = cls(
            name=name,
            version=version,
            descr=descr,
            enabled=enabled,
        )

        package_status.additional_properties = d
        return package_status

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
