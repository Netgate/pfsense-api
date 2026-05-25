from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtopngLocalnet")


@_attrs_define
class NtopngLocalnet:
    """
    Attributes:
        cidr (str | Unset): Network in cidr format
        cidr_name (str | Unset): Name (optional, word characters only)
    """

    cidr: str | Unset = UNSET
    cidr_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cidr = self.cidr

        cidr_name = self.cidr_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cidr is not UNSET:
            field_dict["cidr"] = cidr
        if cidr_name is not UNSET:
            field_dict["cidr_name"] = cidr_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cidr = d.pop("cidr", UNSET)

        cidr_name = d.pop("cidr_name", UNSET)

        ntopng_localnet = cls(
            cidr=cidr,
            cidr_name=cidr_name,
        )

        ntopng_localnet.additional_properties = d
        return ntopng_localnet

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
