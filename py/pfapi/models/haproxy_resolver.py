from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyResolver")


@_attrs_define
class HaproxyResolver:
    """
    Attributes:
        name (str | Unset): Resolver Name

            Unique name for this DNS resolver entry.
        server (str | Unset): DNS Server

            IP address of the DNS server.
        port (str | Unset): DNS Port

            TCP/UDP port of the DNS server.
            (Default: 53)
        id (str | Unset): (readonly) ID assigned to this entry
    """

    name: str | Unset = UNSET
    server: str | Unset = UNSET
    port: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server = self.server

        port = self.port

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if server is not UNSET:
            field_dict["server"] = server
        if port is not UNSET:
            field_dict["port"] = port
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        server = d.pop("server", UNSET)

        port = d.pop("port", UNSET)

        id = d.pop("id", UNSET)

        haproxy_resolver = cls(
            name=name,
            server=server,
            port=port,
            id=id,
        )

        haproxy_resolver.additional_properties = d
        return haproxy_resolver

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
