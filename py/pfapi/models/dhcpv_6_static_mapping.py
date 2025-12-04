from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dhcpv6StaticMapping")


@_attrs_define
class Dhcpv6StaticMapping:
    """
    Attributes:
        id (str | Unset): read-only (index)
        backend (str | Unset): read-only
        duid (str | Unset):
        ipv6_address (str | Unset):
        hostname (str | Unset):
        description (str | Unset):
        early_dns_reg (str | Unset): default (track) | enable | disable
    """

    id: str | Unset = UNSET
    backend: str | Unset = UNSET
    duid: str | Unset = UNSET
    ipv6_address: str | Unset = UNSET
    hostname: str | Unset = UNSET
    description: str | Unset = UNSET
    early_dns_reg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        backend = self.backend

        duid = self.duid

        ipv6_address = self.ipv6_address

        hostname = self.hostname

        description = self.description

        early_dns_reg = self.early_dns_reg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if backend is not UNSET:
            field_dict["backend"] = backend
        if duid is not UNSET:
            field_dict["duid"] = duid
        if ipv6_address is not UNSET:
            field_dict["ipv6_address"] = ipv6_address
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if description is not UNSET:
            field_dict["description"] = description
        if early_dns_reg is not UNSET:
            field_dict["early_dns_reg"] = early_dns_reg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        backend = d.pop("backend", UNSET)

        duid = d.pop("duid", UNSET)

        ipv6_address = d.pop("ipv6_address", UNSET)

        hostname = d.pop("hostname", UNSET)

        description = d.pop("description", UNSET)

        early_dns_reg = d.pop("early_dns_reg", UNSET)

        dhcpv_6_static_mapping = cls(
            id=id,
            backend=backend,
            duid=duid,
            ipv6_address=ipv6_address,
            hostname=hostname,
            description=description,
            early_dns_reg=early_dns_reg,
        )

        dhcpv_6_static_mapping.additional_properties = d
        return dhcpv_6_static_mapping

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
