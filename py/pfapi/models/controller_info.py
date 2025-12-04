from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_vpn import DeviceVpn


T = TypeVar("T", bound="ControllerInfo")


@_attrs_define
class ControllerInfo:
    """
    Attributes:
        name (str | Unset):
        key (str | Unset):
        cert (str | Unset):
        vpn_listenaddr (str | Unset):
        vpn_address (str | Unset):
        vpn_pubkey (str | Unset):
        vpn_netkey (str | Unset):
        vpn_prefix (str | Unset):
        tag (str | Unset):
        noise_secret (str | Unset):
        device_pubkey (str | Unset):
        device_vpn (DeviceVpn | Unset): The device's VPN settings
    """

    name: str | Unset = UNSET
    key: str | Unset = UNSET
    cert: str | Unset = UNSET
    vpn_listenaddr: str | Unset = UNSET
    vpn_address: str | Unset = UNSET
    vpn_pubkey: str | Unset = UNSET
    vpn_netkey: str | Unset = UNSET
    vpn_prefix: str | Unset = UNSET
    tag: str | Unset = UNSET
    noise_secret: str | Unset = UNSET
    device_pubkey: str | Unset = UNSET
    device_vpn: DeviceVpn | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        key = self.key

        cert = self.cert

        vpn_listenaddr = self.vpn_listenaddr

        vpn_address = self.vpn_address

        vpn_pubkey = self.vpn_pubkey

        vpn_netkey = self.vpn_netkey

        vpn_prefix = self.vpn_prefix

        tag = self.tag

        noise_secret = self.noise_secret

        device_pubkey = self.device_pubkey

        device_vpn: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_vpn, Unset):
            device_vpn = self.device_vpn.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if cert is not UNSET:
            field_dict["cert"] = cert
        if vpn_listenaddr is not UNSET:
            field_dict["vpn_listenaddr"] = vpn_listenaddr
        if vpn_address is not UNSET:
            field_dict["vpn_address"] = vpn_address
        if vpn_pubkey is not UNSET:
            field_dict["vpn_pubkey"] = vpn_pubkey
        if vpn_netkey is not UNSET:
            field_dict["vpn_netkey"] = vpn_netkey
        if vpn_prefix is not UNSET:
            field_dict["vpn_prefix"] = vpn_prefix
        if tag is not UNSET:
            field_dict["tag"] = tag
        if noise_secret is not UNSET:
            field_dict["noise_secret"] = noise_secret
        if device_pubkey is not UNSET:
            field_dict["device_pubkey"] = device_pubkey
        if device_vpn is not UNSET:
            field_dict["device_vpn"] = device_vpn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_vpn import DeviceVpn

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        cert = d.pop("cert", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_netkey = d.pop("vpn_netkey", UNSET)

        vpn_prefix = d.pop("vpn_prefix", UNSET)

        tag = d.pop("tag", UNSET)

        noise_secret = d.pop("noise_secret", UNSET)

        device_pubkey = d.pop("device_pubkey", UNSET)

        _device_vpn = d.pop("device_vpn", UNSET)
        device_vpn: DeviceVpn | Unset
        if isinstance(_device_vpn, Unset):
            device_vpn = UNSET
        else:
            device_vpn = DeviceVpn.from_dict(_device_vpn)

        controller_info = cls(
            name=name,
            key=key,
            cert=cert,
            vpn_listenaddr=vpn_listenaddr,
            vpn_address=vpn_address,
            vpn_pubkey=vpn_pubkey,
            vpn_netkey=vpn_netkey,
            vpn_prefix=vpn_prefix,
            tag=tag,
            noise_secret=noise_secret,
            device_pubkey=device_pubkey,
            device_vpn=device_vpn,
        )

        controller_info.additional_properties = d
        return controller_info

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
