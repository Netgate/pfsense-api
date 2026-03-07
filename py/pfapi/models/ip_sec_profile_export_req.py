from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecProfileExportReq")


@_attrs_define
class IPSecProfileExportReq:
    """
    Attributes:
        name (str | Unset): the name of the VPN
        server_address (str | Unset): the server address to be used by the client
        server_hostname (str | Unset): address to which clients will connect when server_address value is "Custom
            Hostname"
        vpnclient (str | Unset): (for target apple) the client to export
        external_username (str | Unset): (for target apple) this is the username when vpnclient value is "<external>"
        user_certref (str | Unset): (for target windows) the TLS client certificate to include in the download archive
        download (bool | Unset): indicate whether response http header Content-Disposition is set as attachment for
            front-end to download the exported profile
    """

    name: str | Unset = UNSET
    server_address: str | Unset = UNSET
    server_hostname: str | Unset = UNSET
    vpnclient: str | Unset = UNSET
    external_username: str | Unset = UNSET
    user_certref: str | Unset = UNSET
    download: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server_address = self.server_address

        server_hostname = self.server_hostname

        vpnclient = self.vpnclient

        external_username = self.external_username

        user_certref = self.user_certref

        download = self.download

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if server_address is not UNSET:
            field_dict["server_address"] = server_address
        if server_hostname is not UNSET:
            field_dict["server_hostname"] = server_hostname
        if vpnclient is not UNSET:
            field_dict["vpnclient"] = vpnclient
        if external_username is not UNSET:
            field_dict["external_username"] = external_username
        if user_certref is not UNSET:
            field_dict["user_certref"] = user_certref
        if download is not UNSET:
            field_dict["download"] = download

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        server_address = d.pop("server_address", UNSET)

        server_hostname = d.pop("server_hostname", UNSET)

        vpnclient = d.pop("vpnclient", UNSET)

        external_username = d.pop("external_username", UNSET)

        user_certref = d.pop("user_certref", UNSET)

        download = d.pop("download", UNSET)

        ip_sec_profile_export_req = cls(
            name=name,
            server_address=server_address,
            server_hostname=server_hostname,
            vpnclient=vpnclient,
            external_username=external_username,
            user_certref=user_certref,
            download=download,
        )

        ip_sec_profile_export_req.additional_properties = d
        return ip_sec_profile_export_req

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
