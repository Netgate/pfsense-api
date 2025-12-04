from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecSAD")


@_attrs_define
class IPSecSAD:
    """
    Attributes:
        src (str | Unset):
        dst (str | Unset):
        proto (str | Unset):
        spi (str | Unset):
        reqid (str | Unset):
        ealgo (str | Unset):
        aalgo (str | Unset):
        data (str | Unset):
    """

    src: str | Unset = UNSET
    dst: str | Unset = UNSET
    proto: str | Unset = UNSET
    spi: str | Unset = UNSET
    reqid: str | Unset = UNSET
    ealgo: str | Unset = UNSET
    aalgo: str | Unset = UNSET
    data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src

        dst = self.dst

        proto = self.proto

        spi = self.spi

        reqid = self.reqid

        ealgo = self.ealgo

        aalgo = self.aalgo

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if src is not UNSET:
            field_dict["src"] = src
        if dst is not UNSET:
            field_dict["dst"] = dst
        if proto is not UNSET:
            field_dict["proto"] = proto
        if spi is not UNSET:
            field_dict["spi"] = spi
        if reqid is not UNSET:
            field_dict["reqid"] = reqid
        if ealgo is not UNSET:
            field_dict["ealgo"] = ealgo
        if aalgo is not UNSET:
            field_dict["aalgo"] = aalgo
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = d.pop("src", UNSET)

        dst = d.pop("dst", UNSET)

        proto = d.pop("proto", UNSET)

        spi = d.pop("spi", UNSET)

        reqid = d.pop("reqid", UNSET)

        ealgo = d.pop("ealgo", UNSET)

        aalgo = d.pop("aalgo", UNSET)

        data = d.pop("data", UNSET)

        ip_sec_sad = cls(
            src=src,
            dst=dst,
            proto=proto,
            spi=spi,
            reqid=reqid,
            ealgo=ealgo,
            aalgo=aalgo,
            data=data,
        )

        ip_sec_sad.additional_properties = d
        return ip_sec_sad

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
