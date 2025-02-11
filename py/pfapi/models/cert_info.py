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
        sig_digest (str):
        key_usage (str):
        key_type (str):
        key_size (int):
        dn (str):
        hash_ (str):
        subject_key_id (str):
        auth_key_id (str):
        valid_from (str):
        expires (str):
        raw_data (str):
        private_key (Union[Unset, str]):
    """

    issuer: str
    serial: str
    sig_digest: str
    key_usage: str
    key_type: str
    key_size: int
    dn: str
    hash_: str
    subject_key_id: str
    auth_key_id: str
    valid_from: str
    expires: str
    raw_data: str
    private_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer = self.issuer

        serial = self.serial

        sig_digest = self.sig_digest

        key_usage = self.key_usage

        key_type = self.key_type

        key_size = self.key_size

        dn = self.dn

        hash_ = self.hash_

        subject_key_id = self.subject_key_id

        auth_key_id = self.auth_key_id

        valid_from = self.valid_from

        expires = self.expires

        raw_data = self.raw_data

        private_key = self.private_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuer": issuer,
                "serial": serial,
                "sig_digest": sig_digest,
                "key_usage": key_usage,
                "key_type": key_type,
                "key_size": key_size,
                "dn": dn,
                "hash": hash_,
                "subject_key_id": subject_key_id,
                "auth_key_id": auth_key_id,
                "valid_from": valid_from,
                "expires": expires,
                "raw_data": raw_data,
            }
        )
        if private_key is not UNSET:
            field_dict["private_key"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issuer = d.pop("issuer")

        serial = d.pop("serial")

        sig_digest = d.pop("sig_digest")

        key_usage = d.pop("key_usage")

        key_type = d.pop("key_type")

        key_size = d.pop("key_size")

        dn = d.pop("dn")

        hash_ = d.pop("hash")

        subject_key_id = d.pop("subject_key_id")

        auth_key_id = d.pop("auth_key_id")

        valid_from = d.pop("valid_from")

        expires = d.pop("expires")

        raw_data = d.pop("raw_data")

        private_key = d.pop("private_key", UNSET)

        cert_info = cls(
            issuer=issuer,
            serial=serial,
            sig_digest=sig_digest,
            key_usage=key_usage,
            key_type=key_type,
            key_size=key_size,
            dn=dn,
            hash_=hash_,
            subject_key_id=subject_key_id,
            auth_key_id=auth_key_id,
            valid_from=valid_from,
            expires=expires,
            raw_data=raw_data,
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
