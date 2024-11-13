from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsSocket")


@_attrs_define
class OsSocket:
    """
    Attributes:
        user (Union[Unset, str]):
        command (Union[Unset, str]):
        fd (Union[Unset, str]):
        pid (Union[Unset, str]):
        proto (Union[Unset, str]):
        local (Union[Unset, str]):
        foreign (Union[Unset, str]):
    """

    user: Union[Unset, str] = UNSET
    command: Union[Unset, str] = UNSET
    fd: Union[Unset, str] = UNSET
    pid: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    local: Union[Unset, str] = UNSET
    foreign: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user

        command = self.command

        fd = self.fd

        pid = self.pid

        proto = self.proto

        local = self.local

        foreign = self.foreign

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
