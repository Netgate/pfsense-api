from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ca_cert_method_existing import CaCertMethodExisting
    from ..models.ca_cert_method_new import CaCertMethodNew


T = TypeVar("T", bound="UpdateCaCertReq")


@_attrs_define
class UpdateCaCertReq:
    """Request for creating a new CA cert or updating an existing one.
    - name: short description about certificate
    - trust: add to OS trusted cert store
    - randomize_serial: use random serial numbers when signing certificates
    - one of: method_internal (self-signed), mehod_existing (import), or method_intermediate (signed by another CA)

        Attributes:
            name (str):
            trust (bool | Unset):
            randomize_serial (bool | Unset):
            method_internal (CaCertMethodNew | Unset): Options for creating/updating an internal CA certificate.
                The values for internal and intermediate certificates are the same,
                with the exception that the intermediate certificate is signed by
                a CA referenced by caref.
                For key type, size and options, query /system/certopts for the
                supported values.

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
                - caref:        signing CA reference ID
            method_existing (CaCertMethodExisting | Unset): Existing PEM certificate and key, either in PEM format or
                base64-encoded
            method_intermediate (CaCertMethodNew | Unset): Options for creating/updating an internal CA certificate.
                The values for internal and intermediate certificates are the same,
                with the exception that the intermediate certificate is signed by
                a CA referenced by caref.
                For key type, size and options, query /system/certopts for the
                supported values.

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
                - caref:        signing CA reference ID
    """

    name: str
    trust: bool | Unset = UNSET
    randomize_serial: bool | Unset = UNSET
    method_internal: CaCertMethodNew | Unset = UNSET
    method_existing: CaCertMethodExisting | Unset = UNSET
    method_intermediate: CaCertMethodNew | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        trust = self.trust

        randomize_serial = self.randomize_serial

        method_internal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_internal, Unset):
            method_internal = self.method_internal.to_dict()

        method_existing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_existing, Unset):
            method_existing = self.method_existing.to_dict()

        method_intermediate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.method_intermediate, Unset):
            method_intermediate = self.method_intermediate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if trust is not UNSET:
            field_dict["trust"] = trust
        if randomize_serial is not UNSET:
            field_dict["randomize_serial"] = randomize_serial
        if method_internal is not UNSET:
            field_dict["method_internal"] = method_internal
        if method_existing is not UNSET:
            field_dict["method_existing"] = method_existing
        if method_intermediate is not UNSET:
            field_dict["method_intermediate"] = method_intermediate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ca_cert_method_existing import CaCertMethodExisting
        from ..models.ca_cert_method_new import CaCertMethodNew

        d = dict(src_dict)
        name = d.pop("name")

        trust = d.pop("trust", UNSET)

        randomize_serial = d.pop("randomize_serial", UNSET)

        _method_internal = d.pop("method_internal", UNSET)
        method_internal: CaCertMethodNew | Unset
        if isinstance(_method_internal, Unset):
            method_internal = UNSET
        else:
            method_internal = CaCertMethodNew.from_dict(_method_internal)

        _method_existing = d.pop("method_existing", UNSET)
        method_existing: CaCertMethodExisting | Unset
        if isinstance(_method_existing, Unset):
            method_existing = UNSET
        else:
            method_existing = CaCertMethodExisting.from_dict(_method_existing)

        _method_intermediate = d.pop("method_intermediate", UNSET)
        method_intermediate: CaCertMethodNew | Unset
        if isinstance(_method_intermediate, Unset):
            method_intermediate = UNSET
        else:
            method_intermediate = CaCertMethodNew.from_dict(_method_intermediate)

        update_ca_cert_req = cls(
            name=name,
            trust=trust,
            randomize_serial=randomize_serial,
            method_internal=method_internal,
            method_existing=method_existing,
            method_intermediate=method_intermediate,
        )

        update_ca_cert_req.additional_properties = d
        return update_ca_cert_req

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
