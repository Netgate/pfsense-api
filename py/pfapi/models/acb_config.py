from typing import Any, Dict, List, Type, TypeVar, Union

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
            encryption_password (Union[Unset, str]):
            enable (Union[Unset, bool]):
            hint (Union[Unset, str]):
            frequency (Union[Unset, str]):
            minute (Union[Unset, str]):
            hour (Union[Unset, str]):
            month (Union[Unset, str]):
            day (Union[Unset, str]):
            dow (Union[Unset, str]):
            numman (Union[Unset, str]):
            reverse (Union[Unset, str]):
    """

    encryption_password: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    hint: Union[Unset, str] = UNSET
    frequency: Union[Unset, str] = UNSET
    minute: Union[Unset, str] = UNSET
    hour: Union[Unset, str] = UNSET
    month: Union[Unset, str] = UNSET
    day: Union[Unset, str] = UNSET
    dow: Union[Unset, str] = UNSET
    numman: Union[Unset, str] = UNSET
    reverse: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
