from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cert_pkcs_12_export_opts_encryption import CertPkcs12ExportOptsEncryption
from ..types import UNSET, Unset

T = TypeVar("T", bound="CertPkcs12ExportOpts")


@_attrs_define
class CertPkcs12ExportOpts:
    """
    Attributes:
        password (str | Unset): pass-phrase to protect pkcs12 file
        add_certauths (bool | Unset): add cert authorities to pkcs12 store
        encryption (CertPkcs12ExportOptsEncryption | Unset): encryption level (high, low, legacy)
    """

    password: str | Unset = UNSET
    add_certauths: bool | Unset = UNSET
    encryption: CertPkcs12ExportOptsEncryption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        add_certauths = self.add_certauths

        encryption: str | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if add_certauths is not UNSET:
            field_dict["add_certauths"] = add_certauths
        if encryption is not UNSET:
            field_dict["encryption"] = encryption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        add_certauths = d.pop("add_certauths", UNSET)

        _encryption = d.pop("encryption", UNSET)
        encryption: CertPkcs12ExportOptsEncryption | Unset
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = CertPkcs12ExportOptsEncryption(_encryption)

        cert_pkcs_12_export_opts = cls(
            password=password,
            add_certauths=add_certauths,
            encryption=encryption,
        )

        cert_pkcs_12_export_opts.additional_properties = d
        return cert_pkcs_12_export_opts

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
