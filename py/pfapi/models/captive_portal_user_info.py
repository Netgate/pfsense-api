from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptivePortalUserInfo")


@_attrs_define
class CaptivePortalUserInfo:
    """
    Attributes:
        ip_address (str | Unset):
        mac_address (str | Unset):
        mac_manufacturer (str | Unset):
        username (str | Unset):
        session_id (str | Unset):
        session_start_unix (int | Unset):
        session_duration_seconds (int | Unset):
        session_remaining_seconds (int | Unset):
        idle_time_seconds (int | Unset):
        bytes_sent (int | Unset):
        bytes_received (int | Unset):
        packets_sent (int | Unset):
        packets_received (int | Unset):
        last_activity (int | Unset):
        zone (str | Unset):
    """

    ip_address: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    mac_manufacturer: str | Unset = UNSET
    username: str | Unset = UNSET
    session_id: str | Unset = UNSET
    session_start_unix: int | Unset = UNSET
    session_duration_seconds: int | Unset = UNSET
    session_remaining_seconds: int | Unset = UNSET
    idle_time_seconds: int | Unset = UNSET
    bytes_sent: int | Unset = UNSET
    bytes_received: int | Unset = UNSET
    packets_sent: int | Unset = UNSET
    packets_received: int | Unset = UNSET
    last_activity: int | Unset = UNSET
    zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
