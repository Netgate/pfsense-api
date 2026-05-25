from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Shellcmdsettings")


@_attrs_define
class Shellcmdsettings:
    """
    Attributes:
        cmd (str | Unset): (Shellcmd Configuration) Command

            Enter the command to run.
        cmdtype (str | Unset): (Shellcmd Configuration) Shellcmd Type (shellcmd, earlyshellcmd,
            afterfilterchangeshellcmd, disabled)

            shellcmd:       Will run the command specified towards the end of the boot process.
            earlyshellcmd:  Will run the command specified at the beginning of the boot process.
            afterfilterchangeshellcmd:   Will run after each filter_configure() call.
            Note: Only one entry of this type can be configured!
            disabledWill save the command in package configuration but it will NOT run on boot.

            See https://docs.netgate.com/pfsense/en/latest/development/boot-commands.html (Executing commands at boot time)
            for detailed explanation.
        description (str | Unset): (Shellcmd Configuration) Description

            Enter a description for this command. (This is for your reference only.)
        id (str | Unset): (readonly) ID assigned to this entry
    """

    cmd: str | Unset = UNSET
    cmdtype: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cmd = self.cmd

        cmdtype = self.cmdtype

        description = self.description

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if cmdtype is not UNSET:
            field_dict["cmdtype"] = cmdtype
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cmd = d.pop("cmd", UNSET)

        cmdtype = d.pop("cmdtype", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        shellcmdsettings = cls(
            cmd=cmd,
            cmdtype=cmdtype,
            description=description,
            id=id,
        )

        shellcmdsettings.additional_properties = d
        return shellcmdsettings

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
