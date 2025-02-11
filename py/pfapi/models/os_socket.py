from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OsSocket")


@_attrs_define
class OsSocket:
    """
    Attributes:
        user (str):
        command (str):
        fd (str):
        pid (str):
        proto (str):
        local (str):
        foreign (str):
    """

    user: str
    command: str
    fd: str
    pid: str
    proto: str
    local: str
    foreign: str
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
        field_dict.update(
            {
                "user": user,
                "command": command,
                "fd": fd,
                "pid": pid,
                "proto": proto,
                "local": local,
                "foreign": foreign,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        command = d.pop("command")

        fd = d.pop("fd")

        pid = d.pop("pid")

        proto = d.pop("proto")

        local = d.pop("local")

        foreign = d.pop("foreign")

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
