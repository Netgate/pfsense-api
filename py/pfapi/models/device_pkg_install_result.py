from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevicePkgInstallResult")


@_attrs_define
class DevicePkgInstallResult:
    """
    Attributes:
        device_id (str | Unset):
        previous_version (str | Unset): previous version of system
        active_version (str | Unset): current running version (after upgrade attempt)
        install_messages (str | Unset): log of upgrade process(es)
        result (str | Unset): success or failure for this device
    """

    device_id: str | Unset = UNSET
    previous_version: str | Unset = UNSET
    active_version: str | Unset = UNSET
    install_messages: str | Unset = UNSET
    result: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        previous_version = self.previous_version

        active_version = self.active_version

        install_messages = self.install_messages

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if previous_version is not UNSET:
            field_dict["previous_version"] = previous_version
        if active_version is not UNSET:
            field_dict["active_version"] = active_version
        if install_messages is not UNSET:
            field_dict["install_messages"] = install_messages
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("device_id", UNSET)

        previous_version = d.pop("previous_version", UNSET)

        active_version = d.pop("active_version", UNSET)

        install_messages = d.pop("install_messages", UNSET)

        result = d.pop("result", UNSET)

        device_pkg_install_result = cls(
            device_id=device_id,
            previous_version=previous_version,
            active_version=active_version,
            install_messages=install_messages,
            result=result,
        )

        device_pkg_install_result.additional_properties = d
        return device_pkg_install_result

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
