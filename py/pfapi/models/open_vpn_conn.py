from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNConn")


@_attrs_define
class OpenVPNConn:
    """
    Attributes:
        common_name (str | Unset):
        remote_host (str | Unset):
        virtual_addr (str | Unset):
        virtual_addr6 (str | Unset):
        bytes_recv (str | Unset):
        bytes_sent (str | Unset):
        connect_time (str | Unset):
        connect_time_unix (str | Unset):
        user_name (str | Unset):
        client_id (str | Unset):
        peer_id (str | Unset):
        cipher (str | Unset):
    """

    common_name: str | Unset = UNSET
    remote_host: str | Unset = UNSET
    virtual_addr: str | Unset = UNSET
    virtual_addr6: str | Unset = UNSET
    bytes_recv: str | Unset = UNSET
    bytes_sent: str | Unset = UNSET
    connect_time: str | Unset = UNSET
    connect_time_unix: str | Unset = UNSET
    user_name: str | Unset = UNSET
    client_id: str | Unset = UNSET
    peer_id: str | Unset = UNSET
    cipher: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if common_name is not UNSET:
            field_dict["common_name"] = common_name
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if virtual_addr is not UNSET:
            field_dict["virtual_addr"] = virtual_addr
        if virtual_addr6 is not UNSET:
            field_dict["virtual_addr6"] = virtual_addr6
        if bytes_recv is not UNSET:
            field_dict["bytes_recv"] = bytes_recv
        if bytes_sent is not UNSET:
            field_dict["bytes_sent"] = bytes_sent
        if connect_time is not UNSET:
            field_dict["connect_time"] = connect_time
        if connect_time_unix is not UNSET:
            field_dict["connect_time_unix"] = connect_time_unix
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if peer_id is not UNSET:
            field_dict["peer_id"] = peer_id
        if cipher is not UNSET:
            field_dict["cipher"] = cipher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        common_name = d.pop("common_name", UNSET)

        remote_host = d.pop("remote_host", UNSET)

        virtual_addr = d.pop("virtual_addr", UNSET)

        virtual_addr6 = d.pop("virtual_addr6", UNSET)

        bytes_recv = d.pop("bytes_recv", UNSET)

        bytes_sent = d.pop("bytes_sent", UNSET)

        connect_time = d.pop("connect_time", UNSET)

        connect_time_unix = d.pop("connect_time_unix", UNSET)

        user_name = d.pop("user_name", UNSET)

        client_id = d.pop("client_id", UNSET)

        peer_id = d.pop("peer_id", UNSET)

        cipher = d.pop("cipher", UNSET)

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
