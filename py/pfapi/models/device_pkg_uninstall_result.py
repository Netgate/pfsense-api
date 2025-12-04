from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevicePkgUninstallResult")


@_attrs_define
class DevicePkgUninstallResult:
    """
    Attributes:
        device_id (str | Unset):
        uninstall_messages (str | Unset):
        result (str | Unset):
    """

    device_id: str | Unset = UNSET
    uninstall_messages: str | Unset = UNSET
    result: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        uninstall_messages = self.uninstall_messages

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if uninstall_messages is not UNSET:
            field_dict["uninstall_messages"] = uninstall_messages
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("device_id", UNSET)

        uninstall_messages = d.pop("uninstall_messages", UNSET)

        result = d.pop("result", UNSET)

        device_pkg_uninstall_result = cls(
            device_id=device_id,
            uninstall_messages=uninstall_messages,
            result=result,
        )

        device_pkg_uninstall_result.additional_properties = d
        return device_pkg_uninstall_result

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
