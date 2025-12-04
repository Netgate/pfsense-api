from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_alt_name import CertAltName


T = TypeVar("T", bound="CertMethodNew")


@_attrs_define
class CertMethodNew:
    """Options for creating/updating an internal certificate.
    For key type, size and options, query /system/certopts for the
    supported values.

    - caref:        CA (refid) to sign cert
    - key_type:     RSA or ECDSA
    - key_size:     size of key in bits (RSA)
    - key_opt:      curve types (historically ecname)
    - digest_alg:   hash algorithm for signing
    - lifetime:     days to expire
    - cn:           common name
    - country_code: 2-character country code
    - state:        state or province
    - city:         city
    - org:          organization, business name
    - ou:           organization unit
    - server_cert   true for server cert, false for user cert

        Attributes:
            caref (str | Unset): signing cert authority refid, required for method_intermediate
            key_type (str | Unset): rsa, ecdsa
            key_size (int | Unset): rsa key size
            key_opt (str | Unset): key options, eg ecdsa curve
            digest_alg (str | Unset): sha1, sha224, sha256, sha384, sha512
            lifetime (int | Unset): days til expiry
            cn (str | Unset):
            country_code (str | Unset):
            state (str | Unset):
            city (str | Unset):
            org (str | Unset):
            ou (str | Unset):
            server_cert (bool | Unset): true = server cert, false = user cert
            alt_names (list[CertAltName] | Unset):
    """

    caref: str | Unset = UNSET
    key_type: str | Unset = UNSET
    key_size: int | Unset = UNSET
    key_opt: str | Unset = UNSET
    digest_alg: str | Unset = UNSET
    lifetime: int | Unset = UNSET
    cn: str | Unset = UNSET
    country_code: str | Unset = UNSET
    state: str | Unset = UNSET
    city: str | Unset = UNSET
    org: str | Unset = UNSET
    ou: str | Unset = UNSET
    server_cert: bool | Unset = UNSET
    alt_names: list[CertAltName] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caref = self.caref

        key_type = self.key_type

        key_size = self.key_size

        key_opt = self.key_opt

        digest_alg = self.digest_alg

        lifetime = self.lifetime

        cn = self.cn

        country_code = self.country_code

        state = self.state

        city = self.city

        org = self.org

        ou = self.ou

        server_cert = self.server_cert

        alt_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alt_names, Unset):
            alt_names = []
            for alt_names_item_data in self.alt_names:
                alt_names_item = alt_names_item_data.to_dict()
                alt_names.append(alt_names_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caref is not UNSET:
            field_dict["caref"] = caref
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if key_size is not UNSET:
            field_dict["key_size"] = key_size
        if key_opt is not UNSET:
            field_dict["key_opt"] = key_opt
        if digest_alg is not UNSET:
            field_dict["digest_alg"] = digest_alg
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if cn is not UNSET:
            field_dict["cn"] = cn
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if org is not UNSET:
            field_dict["org"] = org
        if ou is not UNSET:
            field_dict["ou"] = ou
        if server_cert is not UNSET:
            field_dict["server_cert"] = server_cert
        if alt_names is not UNSET:
            field_dict["alt_names"] = alt_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cert_alt_name import CertAltName

        d = dict(src_dict)
        caref = d.pop("caref", UNSET)

        key_type = d.pop("key_type", UNSET)

        key_size = d.pop("key_size", UNSET)

        key_opt = d.pop("key_opt", UNSET)

        digest_alg = d.pop("digest_alg", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        cn = d.pop("cn", UNSET)

        country_code = d.pop("country_code", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        org = d.pop("org", UNSET)

        ou = d.pop("ou", UNSET)

        server_cert = d.pop("server_cert", UNSET)

        _alt_names = d.pop("alt_names", UNSET)
        alt_names: list[CertAltName] | Unset = UNSET
        if _alt_names is not UNSET:
            alt_names = []
            for alt_names_item_data in _alt_names:
                alt_names_item = CertAltName.from_dict(alt_names_item_data)

                alt_names.append(alt_names_item)

        cert_method_new = cls(
            caref=caref,
            key_type=key_type,
            key_size=key_size,
            key_opt=key_opt,
            digest_alg=digest_alg,
            lifetime=lifetime,
            cn=cn,
            country_code=country_code,
            state=state,
            city=city,
            org=org,
            ou=ou,
            server_cert=server_cert,
            alt_names=alt_names,
        )

        cert_method_new.additional_properties = d
        return cert_method_new

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
