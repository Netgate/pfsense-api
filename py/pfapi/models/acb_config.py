from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ACBConfig")


@_attrs_define
class ACBConfig:
    """valid values:
    frequency = "cron", "every"
    reverse = "yes", "no"

        Attributes:
            encryption_password (str):
            enable (bool):
            hint (str):
            frequency (str):
            minute (str):
            hour (str):
            month (str):
            day (str):
            dow (str):
            numman (str):
            reverse (str):
    """

    encryption_password: str
    enable: bool
    hint: str
    frequency: str
    minute: str
    hour: str
    month: str
    day: str
    dow: str
    numman: str
    reverse: str
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
        field_dict.update(
            {
                "encryption_password": encryption_password,
                "enable": enable,
                "hint": hint,
                "frequency": frequency,
                "minute": minute,
                "hour": hour,
                "month": month,
                "day": day,
                "dow": dow,
                "numman": numman,
                "reverse": reverse,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encryption_password = d.pop("encryption_password")

        enable = d.pop("enable")

        hint = d.pop("hint")

        frequency = d.pop("frequency")

        minute = d.pop("minute")

        hour = d.pop("hour")

        month = d.pop("month")

        day = d.pop("day")

        dow = d.pop("dow")

        numman = d.pop("numman")

        reverse = d.pop("reverse")

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
