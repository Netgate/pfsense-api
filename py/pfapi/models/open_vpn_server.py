from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_server_config import OpenVPNServerConfig


T = TypeVar("T", bound="OpenVPNServer")


@_attrs_define
class OpenVPNServer:
    """
    Attributes:
        authservers (list[str] | Unset):
        server (OpenVPNServerConfig | Unset):
    """

    authservers: list[str] | Unset = UNSET
    server: OpenVPNServerConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authservers: list[str] | Unset = UNSET
        if not isinstance(self.authservers, Unset):
            authservers = self.authservers

        server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authservers is not UNSET:
            field_dict["authservers"] = authservers
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_server_config import OpenVPNServerConfig

        d = dict(src_dict)
        authservers = cast(list[str], d.pop("authservers", UNSET))

        _server = d.pop("server", UNSET)
        server: OpenVPNServerConfig | Unset
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = OpenVPNServerConfig.from_dict(_server)

        open_vpn_server = cls(
            authservers=authservers,
            server=server,
        )

        open_vpn_server.additional_properties = d
        return open_vpn_server

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
