from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_server_info import NtpServerInfo


T = TypeVar("T", bound="NtpStatus")


@_attrs_define
class NtpStatus:
    """
    Attributes:
        enabled (bool | Unset):
        query_enabled (bool | Unset):
        servers (list[NtpServerInfo] | Unset):
    """

    enabled: bool | Unset = UNSET
    query_enabled: bool | Unset = UNSET
    servers: list[NtpServerInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        query_enabled = self.query_enabled

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if query_enabled is not UNSET:
            field_dict["query_enabled"] = query_enabled
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ntp_server_info import NtpServerInfo

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        query_enabled = d.pop("query_enabled", UNSET)

        _servers = d.pop("servers", UNSET)
        servers: list[NtpServerInfo] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = NtpServerInfo.from_dict(servers_item_data)

                servers.append(servers_item)

        ntp_status = cls(
            enabled=enabled,
            query_enabled=query_enabled,
            servers=servers,
        )

        ntp_status.additional_properties = d
        return ntp_status

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
