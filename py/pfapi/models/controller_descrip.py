from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_descrip_host_os import ControllerDescripHostOs
    from ..models.controller_stats import ControllerStats


T = TypeVar("T", bound="ControllerDescrip")


@_attrs_define
class ControllerDescrip:
    """
    Attributes:
        build (str | Unset):
        api_version (str | Unset):
        host (str | Unset):
        host_os (ControllerDescripHostOs | Unset):
        pubkey (str | Unset):
        tls_pubkey (str | Unset): pulibc key of TLS certificate
        tls_key_id (str | Unset): TLS certificate key ID
        public_addresses (list[str] | Unset):
        mim_vpn_addr (str | Unset): multi-instance managment VPN address
        stats (ControllerStats | Unset):
    """

    build: str | Unset = UNSET
    api_version: str | Unset = UNSET
    host: str | Unset = UNSET
    host_os: ControllerDescripHostOs | Unset = UNSET
    pubkey: str | Unset = UNSET
    tls_pubkey: str | Unset = UNSET
    tls_key_id: str | Unset = UNSET
    public_addresses: list[str] | Unset = UNSET
    mim_vpn_addr: str | Unset = UNSET
    stats: ControllerStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build = self.build

        api_version = self.api_version

        host = self.host

        host_os: dict[str, Any] | Unset = UNSET
        if not isinstance(self.host_os, Unset):
            host_os = self.host_os.to_dict()

        pubkey = self.pubkey

        tls_pubkey = self.tls_pubkey

        tls_key_id = self.tls_key_id

        public_addresses: list[str] | Unset = UNSET
        if not isinstance(self.public_addresses, Unset):
            public_addresses = self.public_addresses

        mim_vpn_addr = self.mim_vpn_addr

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build is not UNSET:
            field_dict["build"] = build
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if host is not UNSET:
            field_dict["host"] = host
        if host_os is not UNSET:
            field_dict["host_os"] = host_os
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if tls_pubkey is not UNSET:
            field_dict["tls_pubkey"] = tls_pubkey
        if tls_key_id is not UNSET:
            field_dict["tls_key_id"] = tls_key_id
        if public_addresses is not UNSET:
            field_dict["public_addresses"] = public_addresses
        if mim_vpn_addr is not UNSET:
            field_dict["mim_vpn_addr"] = mim_vpn_addr
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controller_descrip_host_os import ControllerDescripHostOs
        from ..models.controller_stats import ControllerStats

        d = dict(src_dict)
        build = d.pop("build", UNSET)

        api_version = d.pop("api_version", UNSET)

        host = d.pop("host", UNSET)

        _host_os = d.pop("host_os", UNSET)
        host_os: ControllerDescripHostOs | Unset
        if isinstance(_host_os, Unset):
            host_os = UNSET
        else:
            host_os = ControllerDescripHostOs.from_dict(_host_os)

        pubkey = d.pop("pubkey", UNSET)

        tls_pubkey = d.pop("tls_pubkey", UNSET)

        tls_key_id = d.pop("tls_key_id", UNSET)

        public_addresses = cast(list[str], d.pop("public_addresses", UNSET))

        mim_vpn_addr = d.pop("mim_vpn_addr", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: ControllerStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = ControllerStats.from_dict(_stats)

        controller_descrip = cls(
            build=build,
            api_version=api_version,
            host=host,
            host_os=host_os,
            pubkey=pubkey,
            tls_pubkey=tls_pubkey,
            tls_key_id=tls_key_id,
            public_addresses=public_addresses,
            mim_vpn_addr=mim_vpn_addr,
            stats=stats,
        )

        controller_descrip.additional_properties = d
        return controller_descrip

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
