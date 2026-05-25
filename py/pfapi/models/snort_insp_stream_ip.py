from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspStreamIp")


@_attrs_define
class SnortInspStreamIp:
    """
    Attributes:
        max_frags (int | Unset): maximum number of simultaneous fragments being tracked { 1:max32 }; default 8192
        max_overlaps (int | Unset): maximum allowed overlaps per datagram; 0 is unlimited { 0:max32 }; default 0
        min_frag_length (int | Unset): alert if fragment length is below this limit before or after trimming { 0:65535
            }; default 0
        min_ttl (int | Unset): discard fragments with TTL below the minimum { 1:255 }; default 1
        policy (str | Unset): fragment reassembly policy { first | linux | bsd | bsd_right | last | windows | solaris };
            default linux
        session_timeout (int | Unset): session tracking timeout { 1:max31 }; default 60
    """

    max_frags: int | Unset = UNSET
    max_overlaps: int | Unset = UNSET
    min_frag_length: int | Unset = UNSET
    min_ttl: int | Unset = UNSET
    policy: str | Unset = UNSET
    session_timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_frags = self.max_frags

        max_overlaps = self.max_overlaps

        min_frag_length = self.min_frag_length

        min_ttl = self.min_ttl

        policy = self.policy

        session_timeout = self.session_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_frags is not UNSET:
            field_dict["max_frags"] = max_frags
        if max_overlaps is not UNSET:
            field_dict["max_overlaps"] = max_overlaps
        if min_frag_length is not UNSET:
            field_dict["min_frag_length"] = min_frag_length
        if min_ttl is not UNSET:
            field_dict["min_ttl"] = min_ttl
        if policy is not UNSET:
            field_dict["policy"] = policy
        if session_timeout is not UNSET:
            field_dict["session_timeout"] = session_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_frags = d.pop("max_frags", UNSET)

        max_overlaps = d.pop("max_overlaps", UNSET)

        min_frag_length = d.pop("min_frag_length", UNSET)

        min_ttl = d.pop("min_ttl", UNSET)

        policy = d.pop("policy", UNSET)

        session_timeout = d.pop("session_timeout", UNSET)

        snort_insp_stream_ip = cls(
            max_frags=max_frags,
            max_overlaps=max_overlaps,
            min_frag_length=min_frag_length,
            min_ttl=min_ttl,
            policy=policy,
            session_timeout=session_timeout,
        )

        snort_insp_stream_ip.additional_properties = d
        return snort_insp_stream_ip

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
