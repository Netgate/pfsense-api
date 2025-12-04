from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagPingRequest")


@_attrs_define
class DiagPingRequest:
    """
    Attributes:
        host (str | Unset): host name or address to ping
        count (int | Unset): number of packets to send
        wait_sec (int | Unset): number of seconds between ping packets
        ipv6 (bool | Unset): if hostname is provided, use IPv6 instead of IPv4
        source_addr (str | Unset): local IP address or name of interface to use, default "" (any)
    """

    host: str | Unset = UNSET
    count: int | Unset = UNSET
    wait_sec: int | Unset = UNSET
    ipv6: bool | Unset = UNSET
    source_addr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        count = self.count

        wait_sec = self.wait_sec

        ipv6 = self.ipv6

        source_addr = self.source_addr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if count is not UNSET:
            field_dict["count"] = count
        if wait_sec is not UNSET:
            field_dict["wait_sec"] = wait_sec
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if source_addr is not UNSET:
            field_dict["source_addr"] = source_addr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        count = d.pop("count", UNSET)

        wait_sec = d.pop("wait_sec", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        source_addr = d.pop("source_addr", UNSET)

        diag_ping_request = cls(
            host=host,
            count=count,
            wait_sec=wait_sec,
            ipv6=ipv6,
            source_addr=source_addr,
        )

        diag_ping_request.additional_properties = d
        return diag_ping_request

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
