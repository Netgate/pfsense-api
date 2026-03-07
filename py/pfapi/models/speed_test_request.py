from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpeedTestRequest")


@_attrs_define
class SpeedTestRequest:
    """
    Attributes:
        device_id (str | Unset): ID of device
        duration (int | Unset): optional number of seconds to run each upload/download test for, default 10
        upload_mb (int | Unset): optional number of MB to send to device, default 100. Duration has priority.
        download_mb (int | Unset): optional number of MB to receive from device, default 10. Duration has priority.
    """

    device_id: str | Unset = UNSET
    duration: int | Unset = UNSET
    upload_mb: int | Unset = UNSET
    download_mb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        duration = self.duration

        upload_mb = self.upload_mb

        download_mb = self.download_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if upload_mb is not UNSET:
            field_dict["upload_mb"] = upload_mb
        if download_mb is not UNSET:
            field_dict["download_mb"] = download_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("device_id", UNSET)

        duration = d.pop("duration", UNSET)

        upload_mb = d.pop("upload_mb", UNSET)

        download_mb = d.pop("download_mb", UNSET)

        speed_test_request = cls(
            device_id=device_id,
            duration=duration,
            upload_mb=upload_mb,
            download_mb=download_mb,
        )

        speed_test_request.additional_properties = d
        return speed_test_request

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
