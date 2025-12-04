from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlledDeviceAuth")


@_attrs_define
class ControlledDeviceAuth:
    """
    Attributes:
        vpn_pubkey (str | Unset): MIM public key of device
        vpn_address (str | Unset): IPv6 VPN address of device
        vpn_listenaddr (str | Unset): Listening addresses of device's VPN service
        cert (str | Unset): certificate
    """

    vpn_pubkey: str | Unset = UNSET
    vpn_address: str | Unset = UNSET
    vpn_listenaddr: str | Unset = UNSET
    cert: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_pubkey = self.vpn_pubkey

        vpn_address = self.vpn_address

        vpn_listenaddr = self.vpn_listenaddr

        cert = self.cert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_pubkey is not UNSET:
            field_dict["vpn_pubkey"] = vpn_pubkey
        if vpn_address is not UNSET:
            field_dict["vpn_address"] = vpn_address
        if vpn_listenaddr is not UNSET:
            field_dict["vpn_listenaddr"] = vpn_listenaddr
        if cert is not UNSET:
            field_dict["cert"] = cert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        cert = d.pop("cert", UNSET)

        controlled_device_auth = cls(
            vpn_pubkey=vpn_pubkey,
            vpn_address=vpn_address,
            vpn_listenaddr=vpn_listenaddr,
            cert=cert,
        )

        controlled_device_auth.additional_properties = d
        return controlled_device_auth

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
