from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecMobileKey")


@_attrs_define
class IPSecMobileKey:
    """
    Attributes:
        ident (str | Unset):
        type_ (str | Unset):
        pre_shared_key (str | Unset):
        ident_type (str | Unset):
        pool_address (str | Unset):
        pool_netbits (str | Unset):
        dns_address (str | Unset):
    """

    ident: str | Unset = UNSET
    type_: str | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    ident_type: str | Unset = UNSET
    pool_address: str | Unset = UNSET
    pool_netbits: str | Unset = UNSET
    dns_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ident = self.ident

        type_ = self.type_

        pre_shared_key = self.pre_shared_key

        ident_type = self.ident_type

        pool_address = self.pool_address

        pool_netbits = self.pool_netbits

        dns_address = self.dns_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ident is not UNSET:
            field_dict["ident"] = ident
        if type_ is not UNSET:
            field_dict["type"] = type_
        if pre_shared_key is not UNSET:
            field_dict["pre_shared_key"] = pre_shared_key
        if ident_type is not UNSET:
            field_dict["ident_type"] = ident_type
        if pool_address is not UNSET:
            field_dict["pool_address"] = pool_address
        if pool_netbits is not UNSET:
            field_dict["pool_netbits"] = pool_netbits
        if dns_address is not UNSET:
            field_dict["dns_address"] = dns_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ident = d.pop("ident", UNSET)

        type_ = d.pop("type", UNSET)

        pre_shared_key = d.pop("pre_shared_key", UNSET)

        ident_type = d.pop("ident_type", UNSET)

        pool_address = d.pop("pool_address", UNSET)

        pool_netbits = d.pop("pool_netbits", UNSET)

        dns_address = d.pop("dns_address", UNSET)

        ip_sec_mobile_key = cls(
            ident=ident,
            type_=type_,
            pre_shared_key=pre_shared_key,
            ident_type=ident_type,
            pool_address=pool_address,
            pool_netbits=pool_netbits,
            dns_address=dns_address,
        )

        ip_sec_mobile_key.additional_properties = d
        return ip_sec_mobile_key

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
