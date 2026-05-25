from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Freeradiusinterface")


@_attrs_define
class Freeradiusinterface:
    """
    Attributes:
        interfaceip (str | Unset): (General Configuration) Interface IP Address

            Enter the IP address (e.g. 192.168.100.1) of the listening interface.
            If you choose * then it means all interfaces.
            (Default: *)
        interfaceport (str | Unset): (General Configuration) Port

            Enter the port number of the listening interface. Different interface types need different ports.
            Click Info for details.

            You could use this as an example:

            - Authentication: Using port 1812
            - Accounting: Using port 1813
            - Status: Using port 1816

            IMPORTANT:
            For every interface type listening on the same IP address you need different ports.
        interfacetype (str | Unset): (General Configuration) Interface Type (auth, acct, proxy, detail, status, coa)

            Enter the type of the listening interface.
            (Default: Authentication)
        interfaceipversion (str | Unset): (General Configuration) IP Version (ipaddr, ipv6addr)

            Enter the IP version of the listening interface.
            (Default: IPv4)
        description (str | Unset): (General Configuration) Description

            Optionally enter a description here for your reference.
        id (str | Unset): (readonly) ID assigned to this entry
    """

    interfaceip: str | Unset = UNSET
    interfaceport: str | Unset = UNSET
    interfacetype: str | Unset = UNSET
    interfaceipversion: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaceip = self.interfaceip

        interfaceport = self.interfaceport

        interfacetype = self.interfacetype

        interfaceipversion = self.interfaceipversion

        description = self.description

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaceip is not UNSET:
            field_dict["interfaceip"] = interfaceip
        if interfaceport is not UNSET:
            field_dict["interfaceport"] = interfaceport
        if interfacetype is not UNSET:
            field_dict["interfacetype"] = interfacetype
        if interfaceipversion is not UNSET:
            field_dict["interfaceipversion"] = interfaceipversion
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interfaceip = d.pop("interfaceip", UNSET)

        interfaceport = d.pop("interfaceport", UNSET)

        interfacetype = d.pop("interfacetype", UNSET)

        interfaceipversion = d.pop("interfaceipversion", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        freeradiusinterface = cls(
            interfaceip=interfaceip,
            interfaceport=interfaceport,
            interfacetype=interfacetype,
            interfaceipversion=interfaceipversion,
            description=description,
            id=id,
        )

        freeradiusinterface.additional_properties = d
        return freeradiusinterface

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
