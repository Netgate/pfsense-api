from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptivePortalUserInfo")


@_attrs_define
class CaptivePortalUserInfo:
    """
    Attributes:
        ip_address (Union[Unset, str]):
        mac_address (Union[Unset, str]):
        mac_manufacturer (Union[Unset, str]):
        username (Union[Unset, str]):
        session_id (Union[Unset, str]):
        session_start_unix (Union[Unset, int]):
        session_duration_seconds (Union[Unset, int]):
        session_remaining_seconds (Union[Unset, int]):
        idle_time_seconds (Union[Unset, int]):
        bytes_sent (Union[Unset, int]):
        bytes_received (Union[Unset, int]):
        packets_sent (Union[Unset, int]):
        packets_received (Union[Unset, int]):
        last_activity (Union[Unset, int]):
        zone (Union[Unset, str]):
    """

    ip_address: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    mac_manufacturer: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    session_start_unix: Union[Unset, int] = UNSET
    session_duration_seconds: Union[Unset, int] = UNSET
    session_remaining_seconds: Union[Unset, int] = UNSET
    idle_time_seconds: Union[Unset, int] = UNSET
    bytes_sent: Union[Unset, int] = UNSET
    bytes_received: Union[Unset, int] = UNSET
    packets_sent: Union[Unset, int] = UNSET
    packets_received: Union[Unset, int] = UNSET
    last_activity: Union[Unset, int] = UNSET
    zone: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if mac_manufacturer is not UNSET:
            field_dict["mac_manufacturer"] = mac_manufacturer
        if username is not UNSET:
            field_dict["username"] = username
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if session_start_unix is not UNSET:
            field_dict["session_start_unix"] = session_start_unix
        if session_duration_seconds is not UNSET:
            field_dict["session_duration_seconds"] = session_duration_seconds
        if session_remaining_seconds is not UNSET:
            field_dict["session_remaining_seconds"] = session_remaining_seconds
        if idle_time_seconds is not UNSET:
            field_dict["idle_time_seconds"] = idle_time_seconds
        if bytes_sent is not UNSET:
            field_dict["bytes_sent"] = bytes_sent
        if bytes_received is not UNSET:
            field_dict["bytes_received"] = bytes_received
        if packets_sent is not UNSET:
            field_dict["packets_sent"] = packets_sent
        if packets_received is not UNSET:
            field_dict["packets_received"] = packets_received
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip_address = d.pop("ip_address", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        mac_manufacturer = d.pop("mac_manufacturer", UNSET)

        username = d.pop("username", UNSET)

        session_id = d.pop("session_id", UNSET)

        session_start_unix = d.pop("session_start_unix", UNSET)

        session_duration_seconds = d.pop("session_duration_seconds", UNSET)

        session_remaining_seconds = d.pop("session_remaining_seconds", UNSET)

        idle_time_seconds = d.pop("idle_time_seconds", UNSET)

        bytes_sent = d.pop("bytes_sent", UNSET)

        bytes_received = d.pop("bytes_received", UNSET)

        packets_sent = d.pop("packets_sent", UNSET)

        packets_received = d.pop("packets_received", UNSET)

        last_activity = d.pop("last_activity", UNSET)

        zone = d.pop("zone", UNSET)

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
