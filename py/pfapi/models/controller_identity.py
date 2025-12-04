from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerIdentity")


@_attrs_define
class ControllerIdentity:
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
        oldkey (str | Unset):
        regentokens (bool | Unset):
    """

    name: str | Unset = UNSET
    key: str | Unset = UNSET
    cert: str | Unset = UNSET
    vpn_listenaddr: str | Unset = UNSET
    vpn_address: str | Unset = UNSET
    vpn_pubkey: str | Unset = UNSET
    vpn_netkey: str | Unset = UNSET
    vpn_prefix: str | Unset = UNSET
    oldkey: str | Unset = UNSET
    regentokens: bool | Unset = UNSET
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

        oldkey = self.oldkey

        regentokens = self.regentokens

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
        if oldkey is not UNSET:
            field_dict["oldkey"] = oldkey
        if regentokens is not UNSET:
            field_dict["regentokens"] = regentokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        cert = d.pop("cert", UNSET)

        vpn_listenaddr = d.pop("vpn_listenaddr", UNSET)

        vpn_address = d.pop("vpn_address", UNSET)

        vpn_pubkey = d.pop("vpn_pubkey", UNSET)

        vpn_netkey = d.pop("vpn_netkey", UNSET)

        vpn_prefix = d.pop("vpn_prefix", UNSET)

        oldkey = d.pop("oldkey", UNSET)

        regentokens = d.pop("regentokens", UNSET)

        controller_identity = cls(
            name=name,
            key=key,
            cert=cert,
            vpn_listenaddr=vpn_listenaddr,
            vpn_address=vpn_address,
            vpn_pubkey=vpn_pubkey,
            vpn_netkey=vpn_netkey,
            vpn_prefix=vpn_prefix,
            oldkey=oldkey,
            regentokens=regentokens,
        )

        controller_identity.additional_properties = d
        return controller_identity

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
