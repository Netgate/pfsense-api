from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMEIssuedCert")


@_attrs_define
class ACMEIssuedCert:
    """
    Attributes:
        domain (str | Unset):
        cert_url (str | Unset):
        cert_stable_url (str | Unset):
        private_key (str | Unset):
        certificate (str | Unset):
        issuer_certificate (str | Unset):
        csr (str | Unset):
    """

    domain: str | Unset = UNSET
    cert_url: str | Unset = UNSET
    cert_stable_url: str | Unset = UNSET
    private_key: str | Unset = UNSET
    certificate: str | Unset = UNSET
    issuer_certificate: str | Unset = UNSET
    csr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        cert_url = self.cert_url

        cert_stable_url = self.cert_stable_url

        private_key = self.private_key

        certificate = self.certificate

        issuer_certificate = self.issuer_certificate

        csr = self.csr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if cert_url is not UNSET:
            field_dict["certURL"] = cert_url
        if cert_stable_url is not UNSET:
            field_dict["certStableURL"] = cert_stable_url
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if issuer_certificate is not UNSET:
            field_dict["issuerCertificate"] = issuer_certificate
        if csr is not UNSET:
            field_dict["csr"] = csr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain", UNSET)

        cert_url = d.pop("certURL", UNSET)

        cert_stable_url = d.pop("certStableURL", UNSET)

        private_key = d.pop("privateKey", UNSET)

        certificate = d.pop("certificate", UNSET)

        issuer_certificate = d.pop("issuerCertificate", UNSET)

        csr = d.pop("csr", UNSET)

        acme_issued_cert = cls(
            domain=domain,
            cert_url=cert_url,
            cert_stable_url=cert_stable_url,
            private_key=private_key,
            certificate=certificate,
            issuer_certificate=issuer_certificate,
            csr=csr,
        )

        acme_issued_cert.additional_properties = d
        return acme_issued_cert

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
