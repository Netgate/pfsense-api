from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CRLPackageInfo")


@_attrs_define
class CRLPackageInfo:
    """
    Attributes:
        used_by (list[str] | Unset):
        count (int | Unset):
    """

    used_by: list[str] | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used_by: list[str] | Unset = UNSET
        if not isinstance(self.used_by, Unset):
            used_by = self.used_by

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_by is not UNSET:
            field_dict["used_by"] = used_by
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used_by = cast(list[str], d.pop("used_by", UNSET))

        count = d.pop("count", UNSET)

        crl_package_info = cls(
            used_by=used_by,
            count=count,
        )

        crl_package_info.additional_properties = d
        return crl_package_info

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
