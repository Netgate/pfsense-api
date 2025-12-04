from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CRLCert")


@_attrs_define
class CRLCert:
    """
    Attributes:
        refid (str | Unset):
        ca_refid (str | Unset):
        descr (str | Unset):
        type_ (str | Unset):
        cert (str | Unset):
        privkey (str | Unset):
        serial (int | Unset):
        reason (str | Unset):
        revoke_time (int | Unset):
    """

    refid: str | Unset = UNSET
    ca_refid: str | Unset = UNSET
    descr: str | Unset = UNSET
    type_: str | Unset = UNSET
    cert: str | Unset = UNSET
    privkey: str | Unset = UNSET
    serial: int | Unset = UNSET
    reason: str | Unset = UNSET
    revoke_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refid = self.refid

        ca_refid = self.ca_refid

        descr = self.descr

        type_ = self.type_

        cert = self.cert

        privkey = self.privkey

        serial = self.serial

        reason = self.reason

        revoke_time = self.revoke_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if ca_refid is not UNSET:
            field_dict["ca_refid"] = ca_refid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type_ is not UNSET:
            field_dict["type"] = type_
        if cert is not UNSET:
            field_dict["cert"] = cert
        if privkey is not UNSET:
            field_dict["privkey"] = privkey
        if serial is not UNSET:
            field_dict["serial"] = serial
        if reason is not UNSET:
            field_dict["reason"] = reason
        if revoke_time is not UNSET:
            field_dict["revoke_time"] = revoke_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refid = d.pop("refid", UNSET)

        ca_refid = d.pop("ca_refid", UNSET)

        descr = d.pop("descr", UNSET)

        type_ = d.pop("type", UNSET)

        cert = d.pop("cert", UNSET)

        privkey = d.pop("privkey", UNSET)

        serial = d.pop("serial", UNSET)

        reason = d.pop("reason", UNSET)

        revoke_time = d.pop("revoke_time", UNSET)

        crl_cert = cls(
            refid=refid,
            ca_refid=ca_refid,
            descr=descr,
            type_=type_,
            cert=cert,
            privkey=privkey,
            serial=serial,
            reason=reason,
            revoke_time=revoke_time,
        )

        crl_cert.additional_properties = d
        return crl_cert

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
