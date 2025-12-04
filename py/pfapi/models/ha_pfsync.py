from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HAPfsync")


@_attrs_define
class HAPfsync:
    """
    Attributes:
        enabled (bool | Unset): enable pfsync
        sync_assigned_intf (str | Unset): assigned network interface for sync communication
        hostid (str | Unset): max 8 character unique host identifier
        peer_ip (str | Unset): optional - sync to this IP address; default is directed multicast
    """

    enabled: bool | Unset = UNSET
    sync_assigned_intf: str | Unset = UNSET
    hostid: str | Unset = UNSET
    peer_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        sync_assigned_intf = self.sync_assigned_intf

        hostid = self.hostid

        peer_ip = self.peer_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if sync_assigned_intf is not UNSET:
            field_dict["sync_assigned_intf"] = sync_assigned_intf
        if hostid is not UNSET:
            field_dict["hostid"] = hostid
        if peer_ip is not UNSET:
            field_dict["peer_ip"] = peer_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        sync_assigned_intf = d.pop("sync_assigned_intf", UNSET)

        hostid = d.pop("hostid", UNSET)

        peer_ip = d.pop("peer_ip", UNSET)

        ha_pfsync = cls(
            enabled=enabled,
            sync_assigned_intf=sync_assigned_intf,
            hostid=hostid,
            peer_ip=peer_ip,
        )

        ha_pfsync.additional_properties = d
        return ha_pfsync

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
