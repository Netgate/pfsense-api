from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspCip")


@_attrs_define
class SnortInspCip:
    """
    Attributes:
        embedded_cip_path (str | Unset): check embedded CIP path; default false
        unconnected_timeout (int | Unset): unconnected timeout in seconds { 0:360 }; default 300
        max_cip_connections (int | Unset): max cip connections { 1:10000 }; default 100
        max_unconnected_messages (int | Unset): max unconnected cip messages { 1:10000 }; default 100
    """

    embedded_cip_path: str | Unset = UNSET
    unconnected_timeout: int | Unset = UNSET
    max_cip_connections: int | Unset = UNSET
    max_unconnected_messages: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedded_cip_path = self.embedded_cip_path

        unconnected_timeout = self.unconnected_timeout

        max_cip_connections = self.max_cip_connections

        max_unconnected_messages = self.max_unconnected_messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if embedded_cip_path is not UNSET:
            field_dict["embedded_cip_path"] = embedded_cip_path
        if unconnected_timeout is not UNSET:
            field_dict["unconnected_timeout"] = unconnected_timeout
        if max_cip_connections is not UNSET:
            field_dict["max_cip_connections"] = max_cip_connections
        if max_unconnected_messages is not UNSET:
            field_dict["max_unconnected_messages"] = max_unconnected_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        embedded_cip_path = d.pop("embedded_cip_path", UNSET)

        unconnected_timeout = d.pop("unconnected_timeout", UNSET)

        max_cip_connections = d.pop("max_cip_connections", UNSET)

        max_unconnected_messages = d.pop("max_unconnected_messages", UNSET)

        snort_insp_cip = cls(
            embedded_cip_path=embedded_cip_path,
            unconnected_timeout=unconnected_timeout,
            max_cip_connections=max_cip_connections,
            max_unconnected_messages=max_unconnected_messages,
        )

        snort_insp_cip.additional_properties = d
        return snort_insp_cip

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
