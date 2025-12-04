from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTagOption")


@_attrs_define
class DeviceTagOption:
    """
    Attributes:
        tags (list[str] | Unset):
        devices (list[str] | Unset):
        action (str | Unset):
    """

    tags: list[str] | Unset = UNSET
    devices: list[str] | Unset = UNSET
    action: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        devices: list[str] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices

        action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if devices is not UNSET:
            field_dict["devices"] = devices
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags", UNSET))

        devices = cast(list[str], d.pop("devices", UNSET))

        action = d.pop("action", UNSET)

        device_tag_option = cls(
            tags=tags,
            devices=devices,
            action=action,
        )

        device_tag_option.additional_properties = d
        return device_tag_option

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
