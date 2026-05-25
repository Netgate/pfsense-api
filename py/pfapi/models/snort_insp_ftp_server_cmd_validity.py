from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspFtpServerCmdValidity")


@_attrs_define
class SnortInspFtpServerCmdValidity:
    """
    Attributes:
        command (str | Unset): command string
        format_ (str | Unset): format specification
        length (int | Unset): specify non-default maximum for command { 0:max32 }; default 0
    """

    command: str | Unset = UNSET
    format_: str | Unset = UNSET
    length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        format_ = self.format_

        length = self.length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if format_ is not UNSET:
            field_dict["format"] = format_
        if length is not UNSET:
            field_dict["length"] = length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command", UNSET)

        format_ = d.pop("format", UNSET)

        length = d.pop("length", UNSET)

        snort_insp_ftp_server_cmd_validity = cls(
            command=command,
            format_=format_,
            length=length,
        )

        snort_insp_ftp_server_cmd_validity.additional_properties = d
        return snort_insp_ftp_server_cmd_validity

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
