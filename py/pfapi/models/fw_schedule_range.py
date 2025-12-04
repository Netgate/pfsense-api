from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FWScheduleRange")


@_attrs_define
class FWScheduleRange:
    """
    Attributes:
        position (str | Unset):
        month (str | Unset):
        day (str | Unset):
        hour (str | Unset):
        rangedescr (str | Unset):
    """

    position: str | Unset = UNSET
    month: str | Unset = UNSET
    day: str | Unset = UNSET
    hour: str | Unset = UNSET
    rangedescr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        month = self.month

        day = self.day

        hour = self.hour

        rangedescr = self.rangedescr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if hour is not UNSET:
            field_dict["hour"] = hour
        if rangedescr is not UNSET:
            field_dict["rangedescr"] = rangedescr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        hour = d.pop("hour", UNSET)

        rangedescr = d.pop("rangedescr", UNSET)

        fw_schedule_range = cls(
            position=position,
            month=month,
            day=day,
            hour=hour,
            rangedescr=rangedescr,
        )

        fw_schedule_range.additional_properties = d
        return fw_schedule_range

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
