from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrrBgpRpkiCacheServer")


@_attrs_define
class FrrBgpRpkiCacheServer:
    """
    Attributes:
        cacheserver (str | Unset): Address

            Address of the cache server
        port (str | Unset): Port

            Port number to connect to the cache server
        preference (str | Unset): Preference

            Cache server preference
        username (str | Unset): Username

            SSH username to establish an SSH connection to the cache server
        privkeypath (str | Unset): Private Key Path

            Local path that includes the private key file of the router
        pubkeypath (str | Unset): Public Key Path

            Local path that includes the public key file of the router
        id (str | Unset): (readonly) ID assigned to this entry
    """

    cacheserver: str | Unset = UNSET
    port: str | Unset = UNSET
    preference: str | Unset = UNSET
    username: str | Unset = UNSET
    privkeypath: str | Unset = UNSET
    pubkeypath: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cacheserver = self.cacheserver

        port = self.port

        preference = self.preference

        username = self.username

        privkeypath = self.privkeypath

        pubkeypath = self.pubkeypath

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cacheserver is not UNSET:
            field_dict["cacheserver"] = cacheserver
        if port is not UNSET:
            field_dict["port"] = port
        if preference is not UNSET:
            field_dict["preference"] = preference
        if username is not UNSET:
            field_dict["username"] = username
        if privkeypath is not UNSET:
            field_dict["privkeypath"] = privkeypath
        if pubkeypath is not UNSET:
            field_dict["pubkeypath"] = pubkeypath
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cacheserver = d.pop("cacheserver", UNSET)

        port = d.pop("port", UNSET)

        preference = d.pop("preference", UNSET)

        username = d.pop("username", UNSET)

        privkeypath = d.pop("privkeypath", UNSET)

        pubkeypath = d.pop("pubkeypath", UNSET)

        id = d.pop("id", UNSET)

        frr_bgp_rpki_cache_server = cls(
            cacheserver=cacheserver,
            port=port,
            preference=preference,
            username=username,
            privkeypath=privkeypath,
            pubkeypath=pubkeypath,
            id=id,
        )

        frr_bgp_rpki_cache_server.additional_properties = d
        return frr_bgp_rpki_cache_server

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
