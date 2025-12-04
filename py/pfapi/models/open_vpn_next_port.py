from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNNextPort")


@_attrs_define
class OpenVPNNextPort:
    """
    Attributes:
        protocol (str | Unset):
        if_ident (str | Unset):
        port (int | Unset):
    """

    protocol: str | Unset = UNSET
    if_ident: str | Unset = UNSET
    port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protocol = self.protocol

        if_ident = self.if_ident

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if if_ident is not UNSET:
            field_dict["if_ident"] = if_ident
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        protocol = d.pop("protocol", UNSET)

        if_ident = d.pop("if_ident", UNSET)

        port = d.pop("port", UNSET)

        open_vpn_next_port = cls(
            protocol=protocol,
            if_ident=if_ident,
            port=port,
        )

        open_vpn_next_port.additional_properties = d
        return open_vpn_next_port

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
