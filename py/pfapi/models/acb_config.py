from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACBConfig")


@_attrs_define
class ACBConfig:
    """valid values:
    frequency = "cron", "every"
    reverse = "yes", "no"

        Attributes:
            encryption_password (str | Unset):
            enable (bool | Unset):
            hint (str | Unset):
            frequency (str | Unset):
            minute (str | Unset):
            hour (str | Unset):
            month (str | Unset):
            day (str | Unset):
            dow (str | Unset):
            numman (str | Unset):
            reverse (str | Unset):
    """

    encryption_password: str | Unset = UNSET
    enable: bool | Unset = UNSET
    hint: str | Unset = UNSET
    frequency: str | Unset = UNSET
    minute: str | Unset = UNSET
    hour: str | Unset = UNSET
    month: str | Unset = UNSET
    day: str | Unset = UNSET
    dow: str | Unset = UNSET
    numman: str | Unset = UNSET
    reverse: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption_password = self.encryption_password

        enable = self.enable

        hint = self.hint

        frequency = self.frequency

        minute = self.minute

        hour = self.hour

        month = self.month

        day = self.day

        dow = self.dow

        numman = self.numman

        reverse = self.reverse

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encryption_password is not UNSET:
            field_dict["encryption_password"] = encryption_password
        if enable is not UNSET:
            field_dict["enable"] = enable
        if hint is not UNSET:
            field_dict["hint"] = hint
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if minute is not UNSET:
            field_dict["minute"] = minute
        if hour is not UNSET:
            field_dict["hour"] = hour
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if dow is not UNSET:
            field_dict["dow"] = dow
        if numman is not UNSET:
            field_dict["numman"] = numman
        if reverse is not UNSET:
            field_dict["reverse"] = reverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encryption_password = d.pop("encryption_password", UNSET)

        enable = d.pop("enable", UNSET)

        hint = d.pop("hint", UNSET)

        frequency = d.pop("frequency", UNSET)

        minute = d.pop("minute", UNSET)

        hour = d.pop("hour", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        dow = d.pop("dow", UNSET)

        numman = d.pop("numman", UNSET)

        reverse = d.pop("reverse", UNSET)

        acb_config = cls(
            encryption_password=encryption_password,
            enable=enable,
            hint=hint,
            frequency=frequency,
            minute=minute,
            hour=hour,
            month=month,
            day=day,
            dow=dow,
            numman=numman,
            reverse=reverse,
        )

        acb_config.additional_properties = d
        return acb_config

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
