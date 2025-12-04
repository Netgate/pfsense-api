from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticRoute")


@_attrs_define
class StaticRoute:
    """
    Attributes:
        network (str):
        gateway (str):
        descr (str | Unset):
        disabled (bool | Unset):
        interface (str | Unset):
        network_encoded (str | Unset): base64 encoded network; read-only
        gateway_encoded (str | Unset): base64 encoded gateway; read-only
    """

    network: str
    gateway: str
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    interface: str | Unset = UNSET
    network_encoded: str | Unset = UNSET
    gateway_encoded: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        gateway = self.gateway

        descr = self.descr

        disabled = self.disabled

        interface = self.interface

        network_encoded = self.network_encoded

        gateway_encoded = self.gateway_encoded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
                "gateway": gateway,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if interface is not UNSET:
            field_dict["interface"] = interface
        if network_encoded is not UNSET:
            field_dict["network_encoded"] = network_encoded
        if gateway_encoded is not UNSET:
            field_dict["gateway_encoded"] = gateway_encoded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network = d.pop("network")

        gateway = d.pop("gateway")

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        interface = d.pop("interface", UNSET)

        network_encoded = d.pop("network_encoded", UNSET)

        gateway_encoded = d.pop("gateway_encoded", UNSET)

        static_route = cls(
            network=network,
            gateway=gateway,
            descr=descr,
            disabled=disabled,
            interface=interface,
            network_encoded=network_encoded,
            gateway_encoded=gateway_encoded,
        )

        static_route.additional_properties = d
        return static_route

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
