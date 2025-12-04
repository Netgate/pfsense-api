from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsAliasRequest")


@_attrs_define
class DnsAliasRequest:
    """
    Attributes:
        aliasname (str | Unset):
        address (str | Unset):
    """

    aliasname: str | Unset = UNSET
    address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliasname = self.aliasname

        address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliasname is not UNSET:
            field_dict["aliasname"] = aliasname
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aliasname = d.pop("aliasname", UNSET)

        address = d.pop("address", UNSET)

        dns_alias_request = cls(
            aliasname=aliasname,
            address=address,
        )

        dns_alias_request.additional_properties = d
        return dns_alias_request

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
