from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertInfo")


@_attrs_define
class CertInfo:
    """
    Attributes:
        issuer (str):
        serial (str):
        sig_digest (str | Unset):
        dn (str | Unset):
        san (str | Unset):
        key_usage (str | Unset):
        key_type (str | Unset):
        key_size (int | Unset):
        ext_key_usage (str | Unset):
        hash_ (str | Unset):
        subject (str | Unset):
        subject_key_id (str | Unset):
        auth_key_id (str | Unset):
        valid_from (str | Unset):
        expires (str | Unset):
        raw_data (str | Unset):
        cert_fingerprint (str | Unset): sha256 hash of the raw certificate
        self_signed (bool | Unset):
        private_key (str | Unset):
    """

    issuer: str
    serial: str
    sig_digest: str | Unset = UNSET
    dn: str | Unset = UNSET
    san: str | Unset = UNSET
    key_usage: str | Unset = UNSET
    key_type: str | Unset = UNSET
    key_size: int | Unset = UNSET
    ext_key_usage: str | Unset = UNSET
    hash_: str | Unset = UNSET
    subject: str | Unset = UNSET
    subject_key_id: str | Unset = UNSET
    auth_key_id: str | Unset = UNSET
    valid_from: str | Unset = UNSET
    expires: str | Unset = UNSET
    raw_data: str | Unset = UNSET
    cert_fingerprint: str | Unset = UNSET
    self_signed: bool | Unset = UNSET
    private_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer = self.issuer

        serial = self.serial

        sig_digest = self.sig_digest

        dn = self.dn

        san = self.san

        key_usage = self.key_usage

        key_type = self.key_type

        key_size = self.key_size

        ext_key_usage = self.ext_key_usage

        hash_ = self.hash_

        subject = self.subject

        subject_key_id = self.subject_key_id

        auth_key_id = self.auth_key_id

        valid_from = self.valid_from

        expires = self.expires

        raw_data = self.raw_data

        cert_fingerprint = self.cert_fingerprint

        self_signed = self.self_signed

        private_key = self.private_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuer": issuer,
                "serial": serial,
            }
        )
        if sig_digest is not UNSET:
            field_dict["sig_digest"] = sig_digest
        if dn is not UNSET:
            field_dict["dn"] = dn
        if san is not UNSET:
            field_dict["san"] = san
        if key_usage is not UNSET:
            field_dict["key_usage"] = key_usage
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if key_size is not UNSET:
            field_dict["key_size"] = key_size
        if ext_key_usage is not UNSET:
            field_dict["ext_key_usage"] = ext_key_usage
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if subject is not UNSET:
            field_dict["subject"] = subject
        if subject_key_id is not UNSET:
            field_dict["subject_key_id"] = subject_key_id
        if auth_key_id is not UNSET:
            field_dict["auth_key_id"] = auth_key_id
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if expires is not UNSET:
            field_dict["expires"] = expires
        if raw_data is not UNSET:
            field_dict["raw_data"] = raw_data
        if cert_fingerprint is not UNSET:
            field_dict["cert_fingerprint"] = cert_fingerprint
        if self_signed is not UNSET:
            field_dict["self_signed"] = self_signed
        if private_key is not UNSET:
            field_dict["private_key"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issuer = d.pop("issuer")

        serial = d.pop("serial")

        sig_digest = d.pop("sig_digest", UNSET)

        dn = d.pop("dn", UNSET)

        san = d.pop("san", UNSET)

        key_usage = d.pop("key_usage", UNSET)

        key_type = d.pop("key_type", UNSET)

        key_size = d.pop("key_size", UNSET)

        ext_key_usage = d.pop("ext_key_usage", UNSET)

        hash_ = d.pop("hash", UNSET)

        subject = d.pop("subject", UNSET)

        subject_key_id = d.pop("subject_key_id", UNSET)

        auth_key_id = d.pop("auth_key_id", UNSET)

        valid_from = d.pop("valid_from", UNSET)

        expires = d.pop("expires", UNSET)

        raw_data = d.pop("raw_data", UNSET)

        cert_fingerprint = d.pop("cert_fingerprint", UNSET)

        self_signed = d.pop("self_signed", UNSET)

        private_key = d.pop("private_key", UNSET)

        cert_info = cls(
            issuer=issuer,
            serial=serial,
            sig_digest=sig_digest,
            dn=dn,
            san=san,
            key_usage=key_usage,
            key_type=key_type,
            key_size=key_size,
            ext_key_usage=ext_key_usage,
            hash_=hash_,
            subject=subject,
            subject_key_id=subject_key_id,
            auth_key_id=auth_key_id,
            valid_from=valid_from,
            expires=expires,
            raw_data=raw_data,
            cert_fingerprint=cert_fingerprint,
            self_signed=self_signed,
            private_key=private_key,
        )

        cert_info.additional_properties = d
        return cert_info

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
