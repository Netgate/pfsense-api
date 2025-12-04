from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SysFirmwareInfo")


@_attrs_define
class SysFirmwareInfo:
    """
    Attributes:
        current_version (str | Unset): current firmware of the system
        latest_version (str | Unset): firmware version for upgrading to
        status (str | Unset): status message, if the firmware upgrade is in progress
        message (str | Unset): message to display, e.g. error or expectation after upgrading
    """

    current_version: str | Unset = UNSET
    latest_version: str | Unset = UNSET
    status: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_version = self.current_version

        latest_version = self.latest_version

        status = self.status

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_version is not UNSET:
            field_dict["current_version"] = current_version
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_version = d.pop("current_version", UNSET)

        latest_version = d.pop("latest_version", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        sys_firmware_info = cls(
            current_version=current_version,
            latest_version=latest_version,
            status=status,
            message=message,
        )

        sys_firmware_info.additional_properties = d
        return sys_firmware_info

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
