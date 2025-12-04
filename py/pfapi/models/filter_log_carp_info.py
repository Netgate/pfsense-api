from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterLogCARPInfo")


@_attrs_define
class FilterLogCARPInfo:
    """
    Attributes:
        type_ (str | Unset):
        ttl (int | Unset):
        vhid (int | Unset):
        version (int | Unset):
        adv_skew (int | Unset):
        adv_base (int | Unset):
    """

    type_: str | Unset = UNSET
    ttl: int | Unset = UNSET
    vhid: int | Unset = UNSET
    version: int | Unset = UNSET
    adv_skew: int | Unset = UNSET
    adv_base: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ttl = self.ttl

        vhid = self.vhid

        version = self.version

        adv_skew = self.adv_skew

        adv_base = self.adv_base

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if vhid is not UNSET:
            field_dict["vhid"] = vhid
        if version is not UNSET:
            field_dict["version"] = version
        if adv_skew is not UNSET:
            field_dict["adv_skew"] = adv_skew
        if adv_base is not UNSET:
            field_dict["adv_base"] = adv_base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        ttl = d.pop("ttl", UNSET)

        vhid = d.pop("vhid", UNSET)

        version = d.pop("version", UNSET)

        adv_skew = d.pop("adv_skew", UNSET)

        adv_base = d.pop("adv_base", UNSET)

        filter_log_carp_info = cls(
            type_=type_,
            ttl=ttl,
            vhid=vhid,
            version=version,
            adv_skew=adv_skew,
            adv_base=adv_base,
        )

        filter_log_carp_info.additional_properties = d
        return filter_log_carp_info

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
