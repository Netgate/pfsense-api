from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HAPfsync")


@_attrs_define
class HAPfsync:
    """
    Attributes:
        enabled (bool): enable pfsync
        sync_assigned_intf (str): assigned network interface for sync communication
        hostid (str): max 8 character unique host identifier
        peer_ip (str): optional - sync to this IP address; default is directed multicast
    """

    enabled: bool
    sync_assigned_intf: str
    hostid: str
    peer_ip: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        sync_assigned_intf = self.sync_assigned_intf

        hostid = self.hostid

        peer_ip = self.peer_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "sync_assigned_intf": sync_assigned_intf,
                "hostid": hostid,
                "peer_ip": peer_ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        sync_assigned_intf = d.pop("sync_assigned_intf")

        hostid = d.pop("hostid")

        peer_ip = d.pop("peer_ip")

        ha_pfsync = cls(
            enabled=enabled,
            sync_assigned_intf=sync_assigned_intf,
            hostid=hostid,
            peer_ip=peer_ip,
        )

        ha_pfsync.additional_properties = d
        return ha_pfsync

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
