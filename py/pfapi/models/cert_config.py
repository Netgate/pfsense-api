from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_detailed import CertificateDetailed


T = TypeVar("T", bound="CertConfig")


@_attrs_define
class CertConfig:
    """
    Attributes:
        cert (CertificateDetailed | Unset):
    """

    cert: CertificateDetailed | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cert, Unset):
            cert = self.cert.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert is not UNSET:
            field_dict["cert"] = cert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_detailed import CertificateDetailed

        d = dict(src_dict)
        _cert = d.pop("cert", UNSET)
        cert: CertificateDetailed | Unset
        if isinstance(_cert, Unset):
            cert = UNSET
        else:
            cert = CertificateDetailed.from_dict(_cert)

        cert_config = cls(
            cert=cert,
        )

        cert_config.additional_properties = d
        return cert_config

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
