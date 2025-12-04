from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsSocket")


@_attrs_define
class OsSocket:
    """
    Attributes:
        user (str | Unset):
        command (str | Unset):
        fd (str | Unset):
        pid (str | Unset):
        proto (str | Unset):
        local (str | Unset):
        foreign (str | Unset):
    """

    user: str | Unset = UNSET
    command: str | Unset = UNSET
    fd: str | Unset = UNSET
    pid: str | Unset = UNSET
    proto: str | Unset = UNSET
    local: str | Unset = UNSET
    foreign: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        command = self.command

        fd = self.fd

        pid = self.pid

        proto = self.proto

        local = self.local

        foreign = self.foreign

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if command is not UNSET:
            field_dict["command"] = command
        if fd is not UNSET:
            field_dict["fd"] = fd
        if pid is not UNSET:
            field_dict["pid"] = pid
        if proto is not UNSET:
            field_dict["proto"] = proto
        if local is not UNSET:
            field_dict["local"] = local
        if foreign is not UNSET:
            field_dict["foreign"] = foreign

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = d.pop("user", UNSET)

        command = d.pop("command", UNSET)

        fd = d.pop("fd", UNSET)

        pid = d.pop("pid", UNSET)

        proto = d.pop("proto", UNSET)

        local = d.pop("local", UNSET)

        foreign = d.pop("foreign", UNSET)

        os_socket = cls(
            user=user,
            command=command,
            fd=fd,
            pid=pid,
            proto=proto,
            local=local,
            foreign=foreign,
        )

        os_socket.additional_properties = d
        return os_socket

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
