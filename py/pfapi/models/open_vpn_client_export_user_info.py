from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNClientExportUserInfo")


@_attrs_define
class OpenVPNClientExportUserInfo:
    """
    Attributes:
        userid (str | Unset):
        certid (str | Unset):
        name (str | Unset):
        certname (str | Unset):
    """

    userid: str | Unset = UNSET
    certid: str | Unset = UNSET
    name: str | Unset = UNSET
    certname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        userid = self.userid

        certid = self.certid

        name = self.name

        certname = self.certname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if userid is not UNSET:
            field_dict["userid"] = userid
        if certid is not UNSET:
            field_dict["certid"] = certid
        if name is not UNSET:
            field_dict["name"] = name
        if certname is not UNSET:
            field_dict["certname"] = certname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        userid = d.pop("userid", UNSET)

        certid = d.pop("certid", UNSET)

        name = d.pop("name", UNSET)

        certname = d.pop("certname", UNSET)

        open_vpn_client_export_user_info = cls(
            userid=userid,
            certid=certid,
            name=name,
            certname=certname,
        )

        open_vpn_client_export_user_info.additional_properties = d
        return open_vpn_client_export_user_info

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
