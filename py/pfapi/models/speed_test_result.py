from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpeedTestResult")


@_attrs_define
class SpeedTestResult:
    """
    Attributes:
        errors (str | Unset): if any errors
        device_id (str | Unset): ID of device
        duration (int | Unset): number of seconds test ran for
        upload_mps (float | Unset): upload MB/s
        download_mps (float | Unset): download MB/s
    """

    errors: str | Unset = UNSET
    device_id: str | Unset = UNSET
    duration: int | Unset = UNSET
    upload_mps: float | Unset = UNSET
    download_mps: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors

        device_id = self.device_id

        duration = self.duration

        upload_mps = self.upload_mps

        download_mps = self.download_mps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if upload_mps is not UNSET:
            field_dict["upload_mps"] = upload_mps
        if download_mps is not UNSET:
            field_dict["download_mps"] = download_mps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errors = d.pop("errors", UNSET)

        device_id = d.pop("device_id", UNSET)

        duration = d.pop("duration", UNSET)

        upload_mps = d.pop("upload_mps", UNSET)

        download_mps = d.pop("download_mps", UNSET)

        speed_test_result = cls(
            errors=errors,
            device_id=device_id,
            duration=duration,
            upload_mps=upload_mps,
            download_mps=download_mps,
        )

        speed_test_result.additional_properties = d
        return speed_test_result

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
