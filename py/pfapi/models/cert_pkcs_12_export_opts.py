from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cert_pkcs_12_export_opts_encryption import CertPkcs12ExportOptsEncryption

T = TypeVar("T", bound="CertPkcs12ExportOpts")


@_attrs_define
class CertPkcs12ExportOpts:
    """
    Attributes:
        password (str): pass-phrase to protect pkcs12 file
        add_certauths (bool): add cert authorities to pkcs12 store
        encryption (CertPkcs12ExportOptsEncryption): encryption level (high, low, legacy)
    """

    password: str
    add_certauths: bool
    encryption: CertPkcs12ExportOptsEncryption
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        add_certauths = self.add_certauths

        encryption = self.encryption.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "add_certauths": add_certauths,
                "encryption": encryption,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        add_certauths = d.pop("add_certauths")

        encryption = CertPkcs12ExportOptsEncryption(d.pop("encryption"))

        cert_pkcs_12_export_opts = cls(
            password=password,
            add_certauths=add_certauths,
            encryption=encryption,
        )

        cert_pkcs_12_export_opts.additional_properties = d
        return cert_pkcs_12_export_opts

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
