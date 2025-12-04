from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderPlanSetting")


@_attrs_define
class ProviderPlanSetting:
    """
    Attributes:
        name (str):
        apn (str):
        username (str):
        password (str | Unset):
        number (str | Unset):
    """

    name: str
    apn: str
    username: str
    password: str | Unset = UNSET
    number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        apn = self.apn

        username = self.username

        password = self.password

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "apn": apn,
                "username": username,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        apn = d.pop("apn")

        username = d.pop("username")

        password = d.pop("password", UNSET)

        number = d.pop("number", UNSET)

        provider_plan_setting = cls(
            name=name,
            apn=apn,
            username=username,
            password=password,
            number=number,
        )

        provider_plan_setting.additional_properties = d
        return provider_plan_setting

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
