from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cert_pkcs_12_export_opts_encryption import CertPkcs12ExportOptsEncryption
from ..types import UNSET, Unset

T = TypeVar("T", bound="CertPkcs12ExportOpts")


@_attrs_define
class CertPkcs12ExportOpts:
    """
    Attributes:
        password (Union[Unset, str]): pass-phrase to protect pkcs12 file
        add_certauths (Union[Unset, bool]): add cert authorities to pkcs12 store
        encryption (Union[Unset, CertPkcs12ExportOptsEncryption]): encryption level (high, low, legacy)
    """

    password: Union[Unset, str] = UNSET
    add_certauths: Union[Unset, bool] = UNSET
    encryption: Union[Unset, CertPkcs12ExportOptsEncryption] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        add_certauths = self.add_certauths

        encryption: Union[Unset, str] = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.value

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password", UNSET)

        add_certauths = d.pop("add_certauths", UNSET)

        _encryption = d.pop("encryption", UNSET)
        encryption: Union[Unset, CertPkcs12ExportOptsEncryption]
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
