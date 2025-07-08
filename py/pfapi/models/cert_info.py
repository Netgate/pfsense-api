from typing import Any, Dict, List, Type, TypeVar, Union

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
        sig_digest (Union[Unset, str]):
        dn (Union[Unset, str]):
        san (Union[Unset, str]):
        key_usage (Union[Unset, str]):
        key_type (Union[Unset, str]):
        key_size (Union[Unset, int]):
        ext_key_usage (Union[Unset, str]):
        hash_ (Union[Unset, str]):
        subject (Union[Unset, str]):
        subject_key_id (Union[Unset, str]):
        auth_key_id (Union[Unset, str]):
        valid_from (Union[Unset, str]):
        expires (Union[Unset, str]):
        raw_data (Union[Unset, str]):
        cert_fingerprint (Union[Unset, str]): sha256 hash of the raw certificate
        self_signed (Union[Unset, bool]):
        private_key (Union[Unset, str]):
    """

    issuer: str
    serial: str
    sig_digest: Union[Unset, str] = UNSET
    dn: Union[Unset, str] = UNSET
    san: Union[Unset, str] = UNSET
    key_usage: Union[Unset, str] = UNSET
    key_type: Union[Unset, str] = UNSET
    key_size: Union[Unset, int] = UNSET
    ext_key_usage: Union[Unset, str] = UNSET
    hash_: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    subject_key_id: Union[Unset, str] = UNSET
    auth_key_id: Union[Unset, str] = UNSET
    valid_from: Union[Unset, str] = UNSET
    expires: Union[Unset, str] = UNSET
    raw_data: Union[Unset, str] = UNSET
    cert_fingerprint: Union[Unset, str] = UNSET
    self_signed: Union[Unset, bool] = UNSET
    private_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
