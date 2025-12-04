from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpAccessRestrictions")


@_attrs_define
class NtpAccessRestrictions:
    """
    Attributes:
        kod (bool | Unset):
        nomodify (bool | Unset):
        noquery (bool | Unset):
        noserve (bool | Unset):
        nopeer (bool | Unset):
        notrap (bool | Unset):
    """

    kod: bool | Unset = UNSET
    nomodify: bool | Unset = UNSET
    noquery: bool | Unset = UNSET
    noserve: bool | Unset = UNSET
    nopeer: bool | Unset = UNSET
    notrap: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kod = self.kod

        nomodify = self.nomodify

        noquery = self.noquery

        noserve = self.noserve

        nopeer = self.nopeer

        notrap = self.notrap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kod is not UNSET:
            field_dict["kod"] = kod
        if nomodify is not UNSET:
            field_dict["nomodify"] = nomodify
        if noquery is not UNSET:
            field_dict["noquery"] = noquery
        if noserve is not UNSET:
            field_dict["noserve"] = noserve
        if nopeer is not UNSET:
            field_dict["nopeer"] = nopeer
        if notrap is not UNSET:
            field_dict["notrap"] = notrap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kod = d.pop("kod", UNSET)

        nomodify = d.pop("nomodify", UNSET)

        noquery = d.pop("noquery", UNSET)

        noserve = d.pop("noserve", UNSET)

        nopeer = d.pop("nopeer", UNSET)

        notrap = d.pop("notrap", UNSET)

        ntp_access_restrictions = cls(
            kod=kod,
            nomodify=nomodify,
            noquery=noquery,
            noserve=noserve,
            nopeer=nopeer,
            notrap=notrap,
        )

        ntp_access_restrictions.additional_properties = d
        return ntp_access_restrictions

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
