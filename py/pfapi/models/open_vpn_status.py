from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        servers (Union[Unset, List['OpenVPNActiveConn']]):
        sk_servers (Union[Unset, List['OpenVPNActiveConn']]):
        clients (Union[Unset, List['OpenVPNActiveConn']]):
    """

    servers: Union[Unset, List["OpenVPNActiveConn"]] = UNSET
    sk_servers: Union[Unset, List["OpenVPNActiveConn"]] = UNSET
    clients: Union[Unset, List["OpenVPNActiveConn"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        sk_servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sk_servers, Unset):
            sk_servers = []
            for sk_servers_item_data in self.sk_servers:
                sk_servers_item = sk_servers_item_data.to_dict()
                sk_servers.append(sk_servers_item)

        clients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpn_active_conn import OpenVPNActiveConn

        d = src_dict.copy()
        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = OpenVPNActiveConn.from_dict(servers_item_data)

            servers.append(servers_item)

        sk_servers = []
        _sk_servers = d.pop("sk_servers", UNSET)
        for sk_servers_item_data in _sk_servers or []:
            sk_servers_item = OpenVPNActiveConn.from_dict(sk_servers_item_data)

            sk_servers.append(sk_servers_item)

        clients = []
        _clients = d.pop("clients", UNSET)
        for clients_item_data in _clients or []:
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
