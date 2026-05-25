from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNClientImportReq")


@_attrs_define
class OpenVPNClientImportReq:
    """
    Attributes:
        ovpn_config (str | Unset): base64 encoded content of the ovpn file
        disable (bool | Unset): disable the client after import
        server_mode (str | Unset): server mode of the openvpn client
        descr (str | Unset):
        if_ident (str | Unset): interface used to originate this openvpn client connection
        username (str | Unset): username if the imported tunnel requires username/password authentication
        password (str | Unset): base64 encoded password if the imported tunnel requires username/password authentication
    """

    ovpn_config: str | Unset = UNSET
    disable: bool | Unset = UNSET
    server_mode: str | Unset = UNSET
    descr: str | Unset = UNSET
    if_ident: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ovpn_config = self.ovpn_config

        disable = self.disable

        server_mode = self.server_mode

        descr = self.descr

        if_ident = self.if_ident

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ovpn_config is not UNSET:
            field_dict["ovpn_config"] = ovpn_config
        if disable is not UNSET:
            field_dict["disable"] = disable
        if server_mode is not UNSET:
            field_dict["server_mode"] = server_mode
        if descr is not UNSET:
            field_dict["descr"] = descr
        if if_ident is not UNSET:
            field_dict["if_ident"] = if_ident
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ovpn_config = d.pop("ovpn_config", UNSET)

        disable = d.pop("disable", UNSET)

        server_mode = d.pop("server_mode", UNSET)

        descr = d.pop("descr", UNSET)

        if_ident = d.pop("if_ident", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        open_vpn_client_import_req = cls(
            ovpn_config=ovpn_config,
            disable=disable,
            server_mode=server_mode,
            descr=descr,
            if_ident=if_ident,
            username=username,
            password=password,
        )

        open_vpn_client_import_req.additional_properties = d
        return open_vpn_client_import_req

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
