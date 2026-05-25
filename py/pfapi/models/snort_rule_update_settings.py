from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortRuleUpdateSettings")


@_attrs_define
class SnortRuleUpdateSettings:
    """
    Attributes:
        enable (bool | Unset): download schedule is enabled
        interval (str | Unset): daily (default), weekday (day of week), monthday (day of month)
        day (str | Unset): (sun, ..., sat) if weekday or (numeric) monthday
        time (str | Unset): in hh:mm
    """

    enable: bool | Unset = UNSET
    interval: str | Unset = UNSET
    day: str | Unset = UNSET
    time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        interval = self.interval

        day = self.day

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if interval is not UNSET:
            field_dict["interval"] = interval
        if day is not UNSET:
            field_dict["day"] = day
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        interval = d.pop("interval", UNSET)

        day = d.pop("day", UNSET)

        time = d.pop("time", UNSET)

        snort_rule_update_settings = cls(
            enable=enable,
            interval=interval,
            day=day,
            time=time,
        )

        snort_rule_update_settings.additional_properties = d
        return snort_rule_update_settings

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
