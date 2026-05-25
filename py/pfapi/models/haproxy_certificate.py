from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxyCertificate")


@_attrs_define
class HaproxyCertificate:
    """
    Attributes:
        ssl_certificate (str | Unset): Certificate

            Reference ID of an additional SSL certificate to present.
    """

    ssl_certificate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssl_certificate = self.ssl_certificate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssl_certificate is not UNSET:
            field_dict["ssl_certificate"] = ssl_certificate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ssl_certificate = d.pop("ssl_certificate", UNSET)

        haproxy_certificate = cls(
            ssl_certificate=ssl_certificate,
        )

        haproxy_certificate.additional_properties = d
        return haproxy_certificate

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
