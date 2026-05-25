from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMEAction")


@_attrs_define
class ACMEAction:
    """
    Attributes:
        command (str | Unset):
        enabled (bool | Unset):
        method (str | Unset): type of this action valid value = shellcommand, php_command, servicerestart,
            xmlrpcservicerestart
    """

    command: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    method: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        enabled = self.enabled

        method = self.method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command", UNSET)

        enabled = d.pop("enabled", UNSET)

        method = d.pop("method", UNSET)

        acme_action = cls(
            command=command,
            enabled=enabled,
            method=method,
        )

        acme_action.additional_properties = d
        return acme_action

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
