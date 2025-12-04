from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_capable_interface import OpenVPNCapableInterface
    from ..models.open_vpn_server_config import OpenVPNServerConfig


T = TypeVar("T", bound="OpenVPNServers")


@_attrs_define
class OpenVPNServers:
    """
    Attributes:
        authservers (list[str] | Unset):
        servers (list[OpenVPNServerConfig] | Unset):
        openvpn_capable_ifs (list[OpenVPNCapableInterface] | Unset):
    """

    authservers: list[str] | Unset = UNSET
    servers: list[OpenVPNServerConfig] | Unset = UNSET
    openvpn_capable_ifs: list[OpenVPNCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authservers: list[str] | Unset = UNSET
        if not isinstance(self.authservers, Unset):
            authservers = self.authservers

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        openvpn_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.openvpn_capable_ifs, Unset):
            openvpn_capable_ifs = []
            for openvpn_capable_ifs_item_data in self.openvpn_capable_ifs:
                openvpn_capable_ifs_item = openvpn_capable_ifs_item_data.to_dict()
                openvpn_capable_ifs.append(openvpn_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authservers is not UNSET:
            field_dict["authservers"] = authservers
        if servers is not UNSET:
            field_dict["servers"] = servers
        if openvpn_capable_ifs is not UNSET:
            field_dict["openvpn_capable_ifs"] = openvpn_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_capable_interface import OpenVPNCapableInterface
        from ..models.open_vpn_server_config import OpenVPNServerConfig

        d = dict(src_dict)
        authservers = cast(list[str], d.pop("authservers", UNSET))

        _servers = d.pop("servers", UNSET)
        servers: list[OpenVPNServerConfig] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = OpenVPNServerConfig.from_dict(servers_item_data)

                servers.append(servers_item)

        _openvpn_capable_ifs = d.pop("openvpn_capable_ifs", UNSET)
        openvpn_capable_ifs: list[OpenVPNCapableInterface] | Unset = UNSET
        if _openvpn_capable_ifs is not UNSET:
            openvpn_capable_ifs = []
            for openvpn_capable_ifs_item_data in _openvpn_capable_ifs:
                openvpn_capable_ifs_item = OpenVPNCapableInterface.from_dict(openvpn_capable_ifs_item_data)

                openvpn_capable_ifs.append(openvpn_capable_ifs_item)

        open_vpn_servers = cls(
            authservers=authservers,
            servers=servers,
            openvpn_capable_ifs=openvpn_capable_ifs,
        )

        open_vpn_servers.additional_properties = d
        return open_vpn_servers

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
