from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_alt_name import CertAltName


T = TypeVar("T", bound="CertMethodSignCSR")


@_attrs_define
class CertMethodSignCSR:
    """Sign a certificate signing request with the selected CA.
    An existing csr_refid or new CSR (base64 encoded "csr") must be provided.

        Attributes:
            caref (str | Unset):
            csr_refid (str | Unset):
            csr (str | Unset):
            priv_key (str | Unset):
            lifetime (int | Unset):
            digest_alg (str | Unset):
            server_cert (bool | Unset):
            alt_names (list[CertAltName] | Unset):
    """

    caref: str | Unset = UNSET
    csr_refid: str | Unset = UNSET
    csr: str | Unset = UNSET
    priv_key: str | Unset = UNSET
    lifetime: int | Unset = UNSET
    digest_alg: str | Unset = UNSET
    server_cert: bool | Unset = UNSET
    alt_names: list[CertAltName] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caref = self.caref

        csr_refid = self.csr_refid

        csr = self.csr

        priv_key = self.priv_key

        lifetime = self.lifetime

        digest_alg = self.digest_alg

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
        if csr_refid is not UNSET:
            field_dict["csr_refid"] = csr_refid
        if csr is not UNSET:
            field_dict["csr"] = csr
        if priv_key is not UNSET:
            field_dict["priv_key"] = priv_key
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if digest_alg is not UNSET:
            field_dict["digest_alg"] = digest_alg
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

        csr_refid = d.pop("csr_refid", UNSET)

        csr = d.pop("csr", UNSET)

        priv_key = d.pop("priv_key", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        digest_alg = d.pop("digest_alg", UNSET)

        server_cert = d.pop("server_cert", UNSET)

        _alt_names = d.pop("alt_names", UNSET)
        alt_names: list[CertAltName] | Unset = UNSET
        if _alt_names is not UNSET:
            alt_names = []
            for alt_names_item_data in _alt_names:
                alt_names_item = CertAltName.from_dict(alt_names_item_data)

                alt_names.append(alt_names_item)

        cert_method_sign_csr = cls(
            caref=caref,
            csr_refid=csr_refid,
            csr=csr,
            priv_key=priv_key,
            lifetime=lifetime,
            digest_alg=digest_alg,
            server_cert=server_cert,
            alt_names=alt_names,
        )

        cert_method_sign_csr.additional_properties = d
        return cert_method_sign_csr

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
