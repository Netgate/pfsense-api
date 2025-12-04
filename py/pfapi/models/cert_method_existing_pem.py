from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertMethodExistingPEM")


@_attrs_define
class CertMethodExistingPEM:
    """Existing PEM certificate and key, either in PEM/pkcs12 format or base64-encoded

    Attributes:
        cert (str | Unset):
        private_key (str | Unset):
    """

    cert: str | Unset = UNSET
    private_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert = self.cert

        private_key = self.private_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert is not UNSET:
            field_dict["cert"] = cert
        if private_key is not UNSET:
            field_dict["private_key"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert = d.pop("cert", UNSET)

        private_key = d.pop("private_key", UNSET)

        cert_method_existing_pem = cls(
            cert=cert,
            private_key=private_key,
        )

        cert_method_existing_pem.additional_properties = d
        return cert_method_existing_pem

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
