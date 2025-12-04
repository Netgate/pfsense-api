from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPrivilege")


@_attrs_define
class UserPrivilege:
    """
    Attributes:
        value (str | Unset):
        text (str | Unset):
        descr (str | Unset):
        warn (str | Unset): for high-priv, the warning message to present if enabled
    """

    value: str | Unset = UNSET
    text: str | Unset = UNSET
    descr: str | Unset = UNSET
    warn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        text = self.text

        descr = self.descr

        warn = self.warn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if text is not UNSET:
            field_dict["text"] = text
        if descr is not UNSET:
            field_dict["descr"] = descr
        if warn is not UNSET:
            field_dict["warn"] = warn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        text = d.pop("text", UNSET)

        descr = d.pop("descr", UNSET)

        warn = d.pop("warn", UNSET)

        user_privilege = cls(
            value=value,
            text=text,
            descr=descr,
            warn=warn,
        )

        user_privilege.additional_properties = d
        return user_privilege

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
