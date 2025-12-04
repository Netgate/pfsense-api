from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageInstallProgress")


@_attrs_define
class PackageInstallProgress:
    """
    Attributes:
        name (str | Unset):
        version (str | Unset):
        messages (list[str] | Unset):
        percent (int | Unset):
        error (str | Unset):
        action (str | Unset):
    """

    name: str | Unset = UNSET
    version: str | Unset = UNSET
    messages: list[str] | Unset = UNSET
    percent: int | Unset = UNSET
    error: str | Unset = UNSET
    action: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        messages: list[str] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        percent = self.percent

        error = self.error

        action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if messages is not UNSET:
            field_dict["messages"] = messages
        if percent is not UNSET:
            field_dict["percent"] = percent
        if error is not UNSET:
            field_dict["error"] = error
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        messages = cast(list[str], d.pop("messages", UNSET))

        percent = d.pop("percent", UNSET)

        error = d.pop("error", UNSET)

        action = d.pop("action", UNSET)

        package_install_progress = cls(
            name=name,
            version=version,
            messages=messages,
            percent=percent,
            error=error,
            action=action,
        )

        package_install_progress.additional_properties = d
        return package_install_progress

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
