from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecSPD")


@_attrs_define
class IPSecSPD:
    """
    Attributes:
        dir_ (str | Unset):
        scope (str | Unset):
        ifname (str | Unset):
        srcid (str | Unset):
        dstid (str | Unset):
        proto (str | Unset):
        src (str | Unset):
        dst (str | Unset):
        unique (str | Unset):
    """

    dir_: str | Unset = UNSET
    scope: str | Unset = UNSET
    ifname: str | Unset = UNSET
    srcid: str | Unset = UNSET
    dstid: str | Unset = UNSET
    proto: str | Unset = UNSET
    src: str | Unset = UNSET
    dst: str | Unset = UNSET
    unique: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dir_ = self.dir_

        scope = self.scope

        ifname = self.ifname

        srcid = self.srcid

        dstid = self.dstid

        proto = self.proto

        src = self.src

        dst = self.dst

        unique = self.unique

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if scope is not UNSET:
            field_dict["scope"] = scope
        if ifname is not UNSET:
            field_dict["ifname"] = ifname
        if srcid is not UNSET:
            field_dict["srcid"] = srcid
        if dstid is not UNSET:
            field_dict["dstid"] = dstid
        if proto is not UNSET:
            field_dict["proto"] = proto
        if src is not UNSET:
            field_dict["src"] = src
        if dst is not UNSET:
            field_dict["dst"] = dst
        if unique is not UNSET:
            field_dict["unique"] = unique

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dir_ = d.pop("dir", UNSET)

        scope = d.pop("scope", UNSET)

        ifname = d.pop("ifname", UNSET)

        srcid = d.pop("srcid", UNSET)

        dstid = d.pop("dstid", UNSET)

        proto = d.pop("proto", UNSET)

        src = d.pop("src", UNSET)

        dst = d.pop("dst", UNSET)

        unique = d.pop("unique", UNSET)

        ip_sec_spd = cls(
            dir_=dir_,
            scope=scope,
            ifname=ifname,
            srcid=srcid,
            dstid=dstid,
            proto=proto,
            src=src,
            dst=dst,
            unique=unique,
        )

        ip_sec_spd.additional_properties = d
        return ip_sec_spd

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
