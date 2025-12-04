from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TracerouteRequest")


@_attrs_define
class TracerouteRequest:
    """
    Attributes:
        host (str | Unset):
        hops (int | Unset):
        icmp (bool | Unset):
        proto (str | Unset):
        rev (bool | Unset):
        src (str | Unset):
    """

    host: str | Unset = UNSET
    hops: int | Unset = UNSET
    icmp: bool | Unset = UNSET
    proto: str | Unset = UNSET
    rev: bool | Unset = UNSET
    src: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        hops = self.hops

        icmp = self.icmp

        proto = self.proto

        rev = self.rev

        src = self.src

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if hops is not UNSET:
            field_dict["hops"] = hops
        if icmp is not UNSET:
            field_dict["icmp"] = icmp
        if proto is not UNSET:
            field_dict["proto"] = proto
        if rev is not UNSET:
            field_dict["rev"] = rev
        if src is not UNSET:
            field_dict["src"] = src

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        hops = d.pop("hops", UNSET)

        icmp = d.pop("icmp", UNSET)

        proto = d.pop("proto", UNSET)

        rev = d.pop("rev", UNSET)

        src = d.pop("src", UNSET)

        traceroute_request = cls(
            host=host,
            hops=hops,
            icmp=icmp,
            proto=proto,
            rev=rev,
            src=src,
        )

        traceroute_request.additional_properties = d
        return traceroute_request

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
