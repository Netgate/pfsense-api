from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CaptivePortalUserInfo")


@_attrs_define
class CaptivePortalUserInfo:
    """
    Attributes:
        ip_address (str):
        mac_address (str):
        mac_manufacturer (str):
        username (str):
        session_id (str):
        session_start_unix (int):
        session_duration_seconds (int):
        session_remaining_seconds (int):
        idle_time_seconds (int):
        bytes_sent (int):
        bytes_received (int):
        packets_sent (int):
        packets_received (int):
        last_activity (int):
        zone (str):
    """

    ip_address: str
    mac_address: str
    mac_manufacturer: str
    username: str
    session_id: str
    session_start_unix: int
    session_duration_seconds: int
    session_remaining_seconds: int
    idle_time_seconds: int
    bytes_sent: int
    bytes_received: int
    packets_sent: int
    packets_received: int
    last_activity: int
    zone: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip_address = self.ip_address

        mac_address = self.mac_address

        mac_manufacturer = self.mac_manufacturer

        username = self.username

        session_id = self.session_id

        session_start_unix = self.session_start_unix

        session_duration_seconds = self.session_duration_seconds

        session_remaining_seconds = self.session_remaining_seconds

        idle_time_seconds = self.idle_time_seconds

        bytes_sent = self.bytes_sent

        bytes_received = self.bytes_received

        packets_sent = self.packets_sent

        packets_received = self.packets_received

        last_activity = self.last_activity

        zone = self.zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_address": ip_address,
                "mac_address": mac_address,
                "mac_manufacturer": mac_manufacturer,
                "username": username,
                "session_id": session_id,
                "session_start_unix": session_start_unix,
                "session_duration_seconds": session_duration_seconds,
                "session_remaining_seconds": session_remaining_seconds,
                "idle_time_seconds": idle_time_seconds,
                "bytes_sent": bytes_sent,
                "bytes_received": bytes_received,
                "packets_sent": packets_sent,
                "packets_received": packets_received,
                "last_activity": last_activity,
                "zone": zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip_address = d.pop("ip_address")

        mac_address = d.pop("mac_address")

        mac_manufacturer = d.pop("mac_manufacturer")

        username = d.pop("username")

        session_id = d.pop("session_id")

        session_start_unix = d.pop("session_start_unix")

        session_duration_seconds = d.pop("session_duration_seconds")

        session_remaining_seconds = d.pop("session_remaining_seconds")

        idle_time_seconds = d.pop("idle_time_seconds")

        bytes_sent = d.pop("bytes_sent")

        bytes_received = d.pop("bytes_received")

        packets_sent = d.pop("packets_sent")

        packets_received = d.pop("packets_received")

        last_activity = d.pop("last_activity")

        zone = d.pop("zone")

        captive_portal_user_info = cls(
            ip_address=ip_address,
            mac_address=mac_address,
            mac_manufacturer=mac_manufacturer,
            username=username,
            session_id=session_id,
            session_start_unix=session_start_unix,
            session_duration_seconds=session_duration_seconds,
            session_remaining_seconds=session_remaining_seconds,
            idle_time_seconds=idle_time_seconds,
            bytes_sent=bytes_sent,
            bytes_received=bytes_received,
            packets_sent=packets_sent,
            packets_received=packets_received,
            last_activity=last_activity,
            zone=zone,
        )

        captive_portal_user_info.additional_properties = d
        return captive_portal_user_info

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
