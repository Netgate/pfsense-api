from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspDomainFilter")


@_attrs_define
class SnortInspDomainFilter:
    """
    Attributes:
        file (str | Unset): file with list of domains identifying hosts to be filtered
        hosts (str | Unset): list of domains identifying hosts to be filtered
    """

    file: str | Unset = UNSET
    hosts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        hosts = self.hosts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file
        if hosts is not UNSET:
            field_dict["hosts"] = hosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file", UNSET)

        hosts = d.pop("hosts", UNSET)

        snort_insp_domain_filter = cls(
            file=file,
            hosts=hosts,
        )

        snort_insp_domain_filter.additional_properties = d
        return snort_insp_domain_filter

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
