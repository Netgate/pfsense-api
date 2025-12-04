from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterLogVersion4Info")


@_attrs_define
class FilterLogVersion4Info:
    """
    Attributes:
        tos (str | Unset):
        ecn (str | Unset):
        ttl (str | Unset):
        id (str | Unset):
        offset (str | Unset):
        flags (str | Unset):
    """

    tos: str | Unset = UNSET
    ecn: str | Unset = UNSET
    ttl: str | Unset = UNSET
    id: str | Unset = UNSET
    offset: str | Unset = UNSET
    flags: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tos = self.tos

        ecn = self.ecn

        ttl = self.ttl

        id = self.id

        offset = self.offset

        flags = self.flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tos is not UNSET:
            field_dict["tos"] = tos
        if ecn is not UNSET:
            field_dict["ecn"] = ecn
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if id is not UNSET:
            field_dict["id"] = id
        if offset is not UNSET:
            field_dict["offset"] = offset
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tos = d.pop("tos", UNSET)

        ecn = d.pop("ecn", UNSET)

        ttl = d.pop("ttl", UNSET)

        id = d.pop("id", UNSET)

        offset = d.pop("offset", UNSET)

        flags = d.pop("flags", UNSET)

        filter_log_version_4_info = cls(
            tos=tos,
            ecn=ecn,
            ttl=ttl,
            id=id,
            offset=offset,
            flags=flags,
        )

        filter_log_version_4_info.additional_properties = d
        return filter_log_version_4_info

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
