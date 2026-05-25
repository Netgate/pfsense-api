from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspSsh")


@_attrs_define
class SnortInspSsh:
    """
    Attributes:
        max_encrypted_packets (int | Unset): ignore session after this many encrypted packets { 0:65535 }; default 25
        max_client_bytes (int | Unset): number of unanswered bytes before alerting on challenge-response overflow or
            CRC32 { 0:65535 }; default 19600
        max_server_version_len (int | Unset): limit before alerting on secure CRT server version string overflow { 0:255
            }; default 80
    """

    max_encrypted_packets: int | Unset = UNSET
    max_client_bytes: int | Unset = UNSET
    max_server_version_len: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_encrypted_packets = self.max_encrypted_packets

        max_client_bytes = self.max_client_bytes

        max_server_version_len = self.max_server_version_len

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_encrypted_packets is not UNSET:
            field_dict["max_encrypted_packets"] = max_encrypted_packets
        if max_client_bytes is not UNSET:
            field_dict["max_client_bytes"] = max_client_bytes
        if max_server_version_len is not UNSET:
            field_dict["max_server_version_len"] = max_server_version_len

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_encrypted_packets = d.pop("max_encrypted_packets", UNSET)

        max_client_bytes = d.pop("max_client_bytes", UNSET)

        max_server_version_len = d.pop("max_server_version_len", UNSET)

        snort_insp_ssh = cls(
            max_encrypted_packets=max_encrypted_packets,
            max_client_bytes=max_client_bytes,
            max_server_version_len=max_server_version_len,
        )

        snort_insp_ssh.additional_properties = d
        return snort_insp_ssh

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
