from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerUpgradeResult")


@_attrs_define
class ControllerUpgradeResult:
    """
    Attributes:
        active_version (str | Unset):
        previous_version (str | Unset):
        restart_time (int | Unset):
        messages (str | Unset):
    """

    active_version: str | Unset = UNSET
    previous_version: str | Unset = UNSET
    restart_time: int | Unset = UNSET
    messages: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_version = self.active_version

        previous_version = self.previous_version

        restart_time = self.restart_time

        messages = self.messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_version is not UNSET:
            field_dict["active_version"] = active_version
        if previous_version is not UNSET:
            field_dict["previous_version"] = previous_version
        if restart_time is not UNSET:
            field_dict["restart_time"] = restart_time
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_version = d.pop("active_version", UNSET)

        previous_version = d.pop("previous_version", UNSET)

        restart_time = d.pop("restart_time", UNSET)

        messages = d.pop("messages", UNSET)

        controller_upgrade_result = cls(
            active_version=active_version,
            previous_version=previous_version,
            restart_time=restart_time,
            messages=messages,
        )

        controller_upgrade_result.additional_properties = d
        return controller_upgrade_result

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
