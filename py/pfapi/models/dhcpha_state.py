from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DHCPHAState")


@_attrs_define
class DHCPHAState:
    """DHCP service high-availability status

    Attributes:
        server_name (str | Unset): node name
        where (str | Unset): node type - local or remote
        role (str | Unset): primary or standby
        last_heartbeat_sec (int | Unset): how long ago was the last heartbeat, -1 for none
        state (str | Unset): node state - eg hot standby
    """

    server_name: str | Unset = UNSET
    where: str | Unset = UNSET
    role: str | Unset = UNSET
    last_heartbeat_sec: int | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_name = self.server_name

        where = self.where

        role = self.role

        last_heartbeat_sec = self.last_heartbeat_sec

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if where is not UNSET:
            field_dict["where"] = where
        if role is not UNSET:
            field_dict["role"] = role
        if last_heartbeat_sec is not UNSET:
            field_dict["last_heartbeat_sec"] = last_heartbeat_sec
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_name = d.pop("server_name", UNSET)

        where = d.pop("where", UNSET)

        role = d.pop("role", UNSET)

        last_heartbeat_sec = d.pop("last_heartbeat_sec", UNSET)

        state = d.pop("state", UNSET)

        dhcpha_state = cls(
            server_name=server_name,
            where=where,
            role=role,
            last_heartbeat_sec=last_heartbeat_sec,
            state=state,
        )

        dhcpha_state.additional_properties = d
        return dhcpha_state

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
