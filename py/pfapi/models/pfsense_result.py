from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PfsenseResult")


@_attrs_define
class PfsenseResult:
    """
    Attributes:
        msg (str):
        alrt (bool | Unset):
        sb (bool | Unset):
        alrtoln (bool | Unset):
        alrtclr (str | Unset):
        auth (bool | Unset):
        status (str | Unset):
        message (str | Unset):
    """

    msg: str
    alrt: bool | Unset = UNSET
    sb: bool | Unset = UNSET
    alrtoln: bool | Unset = UNSET
    alrtclr: str | Unset = UNSET
    auth: bool | Unset = UNSET
    status: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        msg = self.msg

        alrt = self.alrt

        sb = self.sb

        alrtoln = self.alrtoln

        alrtclr = self.alrtclr

        auth = self.auth

        status = self.status

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "msg": msg,
            }
        )
        if alrt is not UNSET:
            field_dict["alrt"] = alrt
        if sb is not UNSET:
            field_dict["sb"] = sb
        if alrtoln is not UNSET:
            field_dict["alrtoln"] = alrtoln
        if alrtclr is not UNSET:
            field_dict["alrtclr"] = alrtclr
        if auth is not UNSET:
            field_dict["auth"] = auth
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        msg = d.pop("msg")

        alrt = d.pop("alrt", UNSET)

        sb = d.pop("sb", UNSET)

        alrtoln = d.pop("alrtoln", UNSET)

        alrtclr = d.pop("alrtclr", UNSET)

        auth = d.pop("auth", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        pfsense_result = cls(
            msg=msg,
            alrt=alrt,
            sb=sb,
            alrtoln=alrtoln,
            alrtclr=alrtclr,
            auth=auth,
            status=status,
            message=message,
        )

        pfsense_result.additional_properties = d
        return pfsense_result

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
