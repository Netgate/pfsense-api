from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertMethodExistingPkcs12")


@_attrs_define
class CertMethodExistingPkcs12:
    """Existing PKCS12 certificate and key; the PKCS12 payload
    is to be sent as a file upload part in a multi-part request, otherwise
    it can be included as pkcs12_b64 directly within this structure.

        Attributes:
            password (str | Unset): base64 encoded
            intermediates (bool | Unset):
            pkcs12_b64 (str | Unset):
    """

    password: str | Unset = UNSET
    intermediates: bool | Unset = UNSET
    pkcs12_b64: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        intermediates = self.intermediates

        pkcs12_b64 = self.pkcs12_b64

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if intermediates is not UNSET:
            field_dict["intermediates"] = intermediates
        if pkcs12_b64 is not UNSET:
            field_dict["pkcs12_b64"] = pkcs12_b64

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        intermediates = d.pop("intermediates", UNSET)

        pkcs12_b64 = d.pop("pkcs12_b64", UNSET)

        cert_method_existing_pkcs_12 = cls(
            password=password,
            intermediates=intermediates,
            pkcs12_b64=pkcs12_b64,
        )

        cert_method_existing_pkcs_12.additional_properties = d
        return cert_method_existing_pkcs_12

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
