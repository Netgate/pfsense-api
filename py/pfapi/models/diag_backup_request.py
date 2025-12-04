from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagBackupRequest")


@_attrs_define
class DiagBackupRequest:
    """
    Attributes:
        area (str | Unset):
        nopkg (bool | Unset):
        norrd (bool | Unset):
        enc (bool | Unset): file is encrypted
        pwd (str | Unset): password to decrypt file
        filename (str | Unset):
        contents (str | Unset):
        reboot (bool | Unset): reboot system on applying
    """

    area: str | Unset = UNSET
    nopkg: bool | Unset = UNSET
    norrd: bool | Unset = UNSET
    enc: bool | Unset = UNSET
    pwd: str | Unset = UNSET
    filename: str | Unset = UNSET
    contents: str | Unset = UNSET
    reboot: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area = self.area

        nopkg = self.nopkg

        norrd = self.norrd

        enc = self.enc

        pwd = self.pwd

        filename = self.filename

        contents = self.contents

        reboot = self.reboot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if nopkg is not UNSET:
            field_dict["nopkg"] = nopkg
        if norrd is not UNSET:
            field_dict["norrd"] = norrd
        if enc is not UNSET:
            field_dict["enc"] = enc
        if pwd is not UNSET:
            field_dict["pwd"] = pwd
        if filename is not UNSET:
            field_dict["filename"] = filename
        if contents is not UNSET:
            field_dict["contents"] = contents
        if reboot is not UNSET:
            field_dict["reboot"] = reboot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        area = d.pop("area", UNSET)

        nopkg = d.pop("nopkg", UNSET)

        norrd = d.pop("norrd", UNSET)

        enc = d.pop("enc", UNSET)

        pwd = d.pop("pwd", UNSET)

        filename = d.pop("filename", UNSET)

        contents = d.pop("contents", UNSET)

        reboot = d.pop("reboot", UNSET)

        diag_backup_request = cls(
            area=area,
            nopkg=nopkg,
            norrd=norrd,
            enc=enc,
            pwd=pwd,
            filename=filename,
            contents=contents,
            reboot=reboot,
        )

        diag_backup_request.additional_properties = d
        return diag_backup_request

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
