from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_capable_interface import OpenVPNCapableInterface
    from ..models.open_vpn_client_config import OpenVPNClientConfig


T = TypeVar("T", bound="OpenVPNClients")


@_attrs_define
class OpenVPNClients:
    """
    Attributes:
        clients (list[OpenVPNClientConfig] | Unset):
        openvpn_capable_ifs (list[OpenVPNCapableInterface] | Unset):
    """

    clients: list[OpenVPNClientConfig] | Unset = UNSET
    openvpn_capable_ifs: list[OpenVPNCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        openvpn_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.openvpn_capable_ifs, Unset):
            openvpn_capable_ifs = []
            for openvpn_capable_ifs_item_data in self.openvpn_capable_ifs:
                openvpn_capable_ifs_item = openvpn_capable_ifs_item_data.to_dict()
                openvpn_capable_ifs.append(openvpn_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clients is not UNSET:
            field_dict["clients"] = clients
        if openvpn_capable_ifs is not UNSET:
            field_dict["openvpn_capable_ifs"] = openvpn_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_capable_interface import OpenVPNCapableInterface
        from ..models.open_vpn_client_config import OpenVPNClientConfig

        d = dict(src_dict)
        _clients = d.pop("clients", UNSET)
        clients: list[OpenVPNClientConfig] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = OpenVPNClientConfig.from_dict(clients_item_data)

                clients.append(clients_item)

        _openvpn_capable_ifs = d.pop("openvpn_capable_ifs", UNSET)
        openvpn_capable_ifs: list[OpenVPNCapableInterface] | Unset = UNSET
        if _openvpn_capable_ifs is not UNSET:
            openvpn_capable_ifs = []
            for openvpn_capable_ifs_item_data in _openvpn_capable_ifs:
                openvpn_capable_ifs_item = OpenVPNCapableInterface.from_dict(openvpn_capable_ifs_item_data)

                openvpn_capable_ifs.append(openvpn_capable_ifs_item)

        open_vpn_clients = cls(
            clients=clients,
            openvpn_capable_ifs=openvpn_capable_ifs,
        )

        open_vpn_clients.additional_properties = d
        return open_vpn_clients

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
