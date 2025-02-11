from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenVPNConn")


@_attrs_define
class OpenVPNConn:
    """
    Attributes:
        common_name (str):
        remote_host (str):
        virtual_addr (str):
        virtual_addr6 (str):
        bytes_recv (str):
        bytes_sent (str):
        connect_time (str):
        connect_time_unix (str):
        user_name (str):
        client_id (str):
        peer_id (str):
        cipher (str):
    """

    common_name: str
    remote_host: str
    virtual_addr: str
    virtual_addr6: str
    bytes_recv: str
    bytes_sent: str
    connect_time: str
    connect_time_unix: str
    user_name: str
    client_id: str
    peer_id: str
    cipher: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        common_name = self.common_name

        remote_host = self.remote_host

        virtual_addr = self.virtual_addr

        virtual_addr6 = self.virtual_addr6

        bytes_recv = self.bytes_recv

        bytes_sent = self.bytes_sent

        connect_time = self.connect_time

        connect_time_unix = self.connect_time_unix

        user_name = self.user_name

        client_id = self.client_id

        peer_id = self.peer_id

        cipher = self.cipher

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "common_name": common_name,
                "remote_host": remote_host,
                "virtual_addr": virtual_addr,
                "virtual_addr6": virtual_addr6,
                "bytes_recv": bytes_recv,
                "bytes_sent": bytes_sent,
                "connect_time": connect_time,
                "connect_time_unix": connect_time_unix,
                "user_name": user_name,
                "client_id": client_id,
                "peer_id": peer_id,
                "cipher": cipher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        common_name = d.pop("common_name")

        remote_host = d.pop("remote_host")

        virtual_addr = d.pop("virtual_addr")

        virtual_addr6 = d.pop("virtual_addr6")

        bytes_recv = d.pop("bytes_recv")

        bytes_sent = d.pop("bytes_sent")

        connect_time = d.pop("connect_time")

        connect_time_unix = d.pop("connect_time_unix")

        user_name = d.pop("user_name")

        client_id = d.pop("client_id")

        peer_id = d.pop("peer_id")

        cipher = d.pop("cipher")

        open_vpn_conn = cls(
            common_name=common_name,
            remote_host=remote_host,
            virtual_addr=virtual_addr,
            virtual_addr6=virtual_addr6,
            bytes_recv=bytes_recv,
            bytes_sent=bytes_sent,
            connect_time=connect_time,
            connect_time_unix=connect_time_unix,
            user_name=user_name,
            client_id=client_id,
            peer_id=peer_id,
            cipher=cipher,
        )

        open_vpn_conn.additional_properties = d
        return open_vpn_conn

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
