from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_active_conn import OpenVPNActiveConn


T = TypeVar("T", bound="OpenVPNStatus")


@_attrs_define
class OpenVPNStatus:
    """
    Attributes:
        servers (list[OpenVPNActiveConn] | Unset):
        sk_servers (list[OpenVPNActiveConn] | Unset):
        clients (list[OpenVPNActiveConn] | Unset):
    """

    servers: list[OpenVPNActiveConn] | Unset = UNSET
    sk_servers: list[OpenVPNActiveConn] | Unset = UNSET
    clients: list[OpenVPNActiveConn] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        sk_servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sk_servers, Unset):
            sk_servers = []
            for sk_servers_item_data in self.sk_servers:
                sk_servers_item = sk_servers_item_data.to_dict()
                sk_servers.append(sk_servers_item)

        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if servers is not UNSET:
            field_dict["servers"] = servers
        if sk_servers is not UNSET:
            field_dict["sk_servers"] = sk_servers
        if clients is not UNSET:
            field_dict["clients"] = clients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_active_conn import OpenVPNActiveConn

        d = dict(src_dict)
        _servers = d.pop("servers", UNSET)
        servers: list[OpenVPNActiveConn] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = OpenVPNActiveConn.from_dict(servers_item_data)

                servers.append(servers_item)

        _sk_servers = d.pop("sk_servers", UNSET)
        sk_servers: list[OpenVPNActiveConn] | Unset = UNSET
        if _sk_servers is not UNSET:
            sk_servers = []
            for sk_servers_item_data in _sk_servers:
                sk_servers_item = OpenVPNActiveConn.from_dict(sk_servers_item_data)

                sk_servers.append(sk_servers_item)

        _clients = d.pop("clients", UNSET)
        clients: list[OpenVPNActiveConn] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = OpenVPNActiveConn.from_dict(clients_item_data)

                clients.append(clients_item)

        open_vpn_status = cls(
            servers=servers,
            sk_servers=sk_servers,
            clients=clients,
        )

        open_vpn_status.additional_properties = d
        return open_vpn_status

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
