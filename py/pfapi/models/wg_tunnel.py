from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wgip_address import WGIPAddress


T = TypeVar("T", bound="WGTunnel")


@_attrs_define
class WGTunnel:
    """valid values:
    enabled = "yes", "no"

        Attributes:
            name (str):
            privatekey (str):
            publickey (str):
            descr (str | Unset):
            enabled (bool | Unset):
            listenport (int | Unset):
            mtu (str | Unset):
            addresses (list[WGIPAddress] | Unset):
    """

    name: str
    privatekey: str
    publickey: str
    descr: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    listenport: int | Unset = UNSET
    mtu: str | Unset = UNSET
    addresses: list[WGIPAddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        privatekey = self.privatekey

        publickey = self.publickey

        descr = self.descr

        enabled = self.enabled

        listenport = self.listenport

        mtu = self.mtu

        addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "privatekey": privatekey,
                "publickey": publickey,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if listenport is not UNSET:
            field_dict["listenport"] = listenport
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wgip_address import WGIPAddress

        d = dict(src_dict)
        name = d.pop("name")

        privatekey = d.pop("privatekey")

        publickey = d.pop("publickey")

        descr = d.pop("descr", UNSET)

        enabled = d.pop("enabled", UNSET)

        listenport = d.pop("listenport", UNSET)

        mtu = d.pop("mtu", UNSET)

        _addresses = d.pop("addresses", UNSET)
        addresses: list[WGIPAddress] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = WGIPAddress.from_dict(addresses_item_data)

                addresses.append(addresses_item)

        wg_tunnel = cls(
            name=name,
            privatekey=privatekey,
            publickey=publickey,
            descr=descr,
            enabled=enabled,
            listenport=listenport,
            mtu=mtu,
            addresses=addresses,
        )

        wg_tunnel.additional_properties = d
        return wg_tunnel

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
