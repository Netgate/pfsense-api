from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspSsl")


@_attrs_define
class SnortInspSsl:
    """
    Attributes:
        trust_servers (bool | Unset): disables requirement that application (encrypted) data must be observed on both
            sides; default false
        max_heartbeat_length (int | Unset): maximum length of heartbeat record allowed { 0:65535 }; default 0
    """

    trust_servers: bool | Unset = UNSET
    max_heartbeat_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trust_servers = self.trust_servers

        max_heartbeat_length = self.max_heartbeat_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trust_servers is not UNSET:
            field_dict["trust_servers"] = trust_servers
        if max_heartbeat_length is not UNSET:
            field_dict["max_heartbeat_length"] = max_heartbeat_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trust_servers = d.pop("trust_servers", UNSET)

        max_heartbeat_length = d.pop("max_heartbeat_length", UNSET)

        snort_insp_ssl = cls(
            trust_servers=trust_servers,
            max_heartbeat_length=max_heartbeat_length,
        )

        snort_insp_ssl.additional_properties = d
        return snort_insp_ssl

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
