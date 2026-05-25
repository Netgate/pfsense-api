from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyClientCrl")


@_attrs_define
class HaproxyClientCrl:
    """
    Attributes:
        cert_crl (str | Unset): CRL

            Reference ID of a certificate revocation list for client certificate checking.
    """

    cert_crl: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_crl = self.cert_crl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_crl is not UNSET:
            field_dict["cert_crl"] = cert_crl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert_crl = d.pop("cert_crl", UNSET)

        haproxy_client_crl = cls(
            cert_crl=cert_crl,
        )

        haproxy_client_crl.additional_properties = d
        return haproxy_client_crl

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
