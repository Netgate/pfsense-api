from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_method_existing_pem import CertMethodExistingPEM
    from ..models.cert_method_existing_pkcs_12 import CertMethodExistingPkcs12
    from ..models.cert_method_new import CertMethodNew
    from ..models.cert_method_sign_csr import CertMethodSignCSR
    from ..models.cert_method_signing_request import CertMethodSigningRequest


T = TypeVar("T", bound="NewCertReq")


@_attrs_define
class NewCertReq:
    """Request for creating a cert or updating an existing one.
    - name: short description about certificate
    - userid: user-ID for user-specific certificate, eg for VPN
    - description:  Descriptive name
    - one of the method_xxxx

        Attributes:
            name (str | Unset):
            descr (str | Unset):
            description (str | Unset):
            userid (int | Unset):
            method_internal (CertMethodNew | Unset): Options for creating/updating an internal certificate.
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
            method_existing_pem (CertMethodExistingPEM | Unset): Existing PEM certificate and key, either in PEM/pkcs12
                format or base64-encoded
            method_existing_pkcs12 (CertMethodExistingPkcs12 | Unset): Existing PKCS12 certificate and key; the PKCS12
                payload
                is to be sent as a file upload part in a multi-part request, otherwise
                it can be included as pkcs12_b64 directly within this structure.
            method_csr (CertMethodSigningRequest | Unset):
            method_sign (CertMethodSignCSR | Unset): Sign a certificate signing request with the selected CA.
                An existing csr_refid or new CSR (base64 encoded "csr") must be provided.
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    description: str | Unset = UNSET
    userid: int | Unset = UNSET
    method_internal: CertMethodNew | Unset = UNSET
    method_existing_pem: CertMethodExistingPEM | Unset = UNSET
    method_existing_pkcs12: CertMethodExistingPkcs12 | Unset = UNSET
    method_csr: CertMethodSigningRequest | Unset = UNSET
    method_sign: CertMethodSignCSR | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        description = self.description

        userid = self.userid

        method_internal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_internal, Unset):
            method_internal = self.method_internal.to_dict()

        method_existing_pem: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_existing_pem, Unset):
            method_existing_pem = self.method_existing_pem.to_dict()

        method_existing_pkcs12: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_existing_pkcs12, Unset):
            method_existing_pkcs12 = self.method_existing_pkcs12.to_dict()

        method_csr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_csr, Unset):
            method_csr = self.method_csr.to_dict()

        method_sign: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_sign, Unset):
            method_sign = self.method_sign.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if description is not UNSET:
            field_dict["description"] = description
        if userid is not UNSET:
            field_dict["userid"] = userid
        if method_internal is not UNSET:
            field_dict["method_internal"] = method_internal
        if method_existing_pem is not UNSET:
            field_dict["method_existing_pem"] = method_existing_pem
        if method_existing_pkcs12 is not UNSET:
            field_dict["method_existing_pkcs12"] = method_existing_pkcs12
        if method_csr is not UNSET:
            field_dict["method_csr"] = method_csr
        if method_sign is not UNSET:
            field_dict["method_sign"] = method_sign

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cert_method_existing_pem import CertMethodExistingPEM
        from ..models.cert_method_existing_pkcs_12 import CertMethodExistingPkcs12
        from ..models.cert_method_new import CertMethodNew
        from ..models.cert_method_sign_csr import CertMethodSignCSR
        from ..models.cert_method_signing_request import CertMethodSigningRequest

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        description = d.pop("description", UNSET)

        userid = d.pop("userid", UNSET)

        _method_internal = d.pop("method_internal", UNSET)
        method_internal: CertMethodNew | Unset
        if isinstance(_method_internal, Unset):
            method_internal = UNSET
        else:
            method_internal = CertMethodNew.from_dict(_method_internal)

        _method_existing_pem = d.pop("method_existing_pem", UNSET)
        method_existing_pem: CertMethodExistingPEM | Unset
        if isinstance(_method_existing_pem, Unset):
            method_existing_pem = UNSET
        else:
            method_existing_pem = CertMethodExistingPEM.from_dict(_method_existing_pem)

        _method_existing_pkcs12 = d.pop("method_existing_pkcs12", UNSET)
        method_existing_pkcs12: CertMethodExistingPkcs12 | Unset
        if isinstance(_method_existing_pkcs12, Unset):
            method_existing_pkcs12 = UNSET
        else:
            method_existing_pkcs12 = CertMethodExistingPkcs12.from_dict(_method_existing_pkcs12)

        _method_csr = d.pop("method_csr", UNSET)
        method_csr: CertMethodSigningRequest | Unset
        if isinstance(_method_csr, Unset):
            method_csr = UNSET
        else:
            method_csr = CertMethodSigningRequest.from_dict(_method_csr)

        _method_sign = d.pop("method_sign", UNSET)
        method_sign: CertMethodSignCSR | Unset
        if isinstance(_method_sign, Unset):
            method_sign = UNSET
        else:
            method_sign = CertMethodSignCSR.from_dict(_method_sign)

        new_cert_req = cls(
            name=name,
            descr=descr,
            description=description,
            userid=userid,
            method_internal=method_internal,
            method_existing_pem=method_existing_pem,
            method_existing_pkcs12=method_existing_pkcs12,
            method_csr=method_csr,
            method_sign=method_sign,
        )

        new_cert_req.additional_properties = d
        return new_cert_req

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
