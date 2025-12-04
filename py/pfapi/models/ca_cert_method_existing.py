from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaCertMethodExisting")


@_attrs_define
class CaCertMethodExisting:
    """Existing PEM certificate and key, either in PEM format or base64-encoded

    Attributes:
        cert (str):
        private_key (str | Unset):
        next_serial (int | Unset):
    """

    cert: str
    private_key: str | Unset = UNSET
    next_serial: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert = self.cert

        private_key = self.private_key

        next_serial = self.next_serial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cert": cert,
            }
        )
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if next_serial is not UNSET:
            field_dict["next_serial"] = next_serial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert = d.pop("cert")

        private_key = d.pop("private_key", UNSET)

        next_serial = d.pop("next_serial", UNSET)

        ca_cert_method_existing = cls(
            cert=cert,
            private_key=private_key,
            next_serial=next_serial,
        )

        ca_cert_method_existing.additional_properties = d
        return ca_cert_method_existing

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
