from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyBindAddress")


@_attrs_define
class HaproxyBindAddress:
    """
    Attributes:
        extaddr (str | Unset): Bind Address

            Interface or address to bind to. Values include interface identifiers
            (e.g. wan_ipv4, lan_ipv4, localhost, any), virtual IPs, or "custom"
            for a manually specified address.
        extaddr_custom (str | Unset): Custom Address

            Custom IP address to bind to. Only used when extaddr is set to "custom".
        extaddr_port (str | Unset): Port

            TCP port to listen on for this bind address.
        extaddr_ssl (bool | Unset): SSL

            Enable SSL/TLS on this bind address.
        extaddr_advanced (str | Unset): Advanced Bind Options

            Additional raw bind-line options appended to this bind directive.
    """

    extaddr: str | Unset = UNSET
    extaddr_custom: str | Unset = UNSET
    extaddr_port: str | Unset = UNSET
    extaddr_ssl: bool | Unset = UNSET
    extaddr_advanced: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extaddr = self.extaddr

        extaddr_custom = self.extaddr_custom

        extaddr_port = self.extaddr_port

        extaddr_ssl = self.extaddr_ssl

        extaddr_advanced = self.extaddr_advanced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extaddr is not UNSET:
            field_dict["extaddr"] = extaddr
        if extaddr_custom is not UNSET:
            field_dict["extaddr_custom"] = extaddr_custom
        if extaddr_port is not UNSET:
            field_dict["extaddr_port"] = extaddr_port
        if extaddr_ssl is not UNSET:
            field_dict["extaddr_ssl"] = extaddr_ssl
        if extaddr_advanced is not UNSET:
            field_dict["extaddr_advanced"] = extaddr_advanced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extaddr = d.pop("extaddr", UNSET)

        extaddr_custom = d.pop("extaddr_custom", UNSET)

        extaddr_port = d.pop("extaddr_port", UNSET)

        extaddr_ssl = d.pop("extaddr_ssl", UNSET)

        extaddr_advanced = d.pop("extaddr_advanced", UNSET)

        haproxy_bind_address = cls(
            extaddr=extaddr,
            extaddr_custom=extaddr_custom,
            extaddr_port=extaddr_port,
            extaddr_ssl=extaddr_ssl,
            extaddr_advanced=extaddr_advanced,
        )

        haproxy_bind_address.additional_properties = d
        return haproxy_bind_address

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
