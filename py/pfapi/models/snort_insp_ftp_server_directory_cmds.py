from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspFtpServerDirectoryCmds")


@_attrs_define
class SnortInspFtpServerDirectoryCmds:
    """
    Attributes:
        dir_cmd (str | Unset): directory command
        rsp_code (int | Unset): expected successful response code for command { 200:max32 }; default 200
    """

    dir_cmd: str | Unset = UNSET
    rsp_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dir_cmd = self.dir_cmd

        rsp_code = self.rsp_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dir_cmd is not UNSET:
            field_dict["dir_cmd"] = dir_cmd
        if rsp_code is not UNSET:
            field_dict["rsp_code"] = rsp_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dir_cmd = d.pop("dir_cmd", UNSET)

        rsp_code = d.pop("rsp_code", UNSET)

        snort_insp_ftp_server_directory_cmds = cls(
            dir_cmd=dir_cmd,
            rsp_code=rsp_code,
        )

        snort_insp_ftp_server_directory_cmds.additional_properties = d
        return snort_insp_ftp_server_directory_cmds

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
