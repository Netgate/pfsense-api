from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_method_existing_pkcs_12 import CertMethodExistingPkcs12


T = TypeVar("T", bound="UpdatePKCS12CertReq")


@_attrs_define
class UpdatePKCS12CertReq:
    """Update the certificate with PKCS12 appended file upload

    Attributes:
        name (Union[Unset, str]):
        descr (Union[Unset, str]):
        description (Union[Unset, str]):
        method_existing_pkcs12 (Union[Unset, CertMethodExistingPkcs12]): Existing PKCS12 certificate and key; the PKCS12
            payload
            is to be sent as a file upload part in a multi-part request, otherwise
            it can be included as pkcs12_b64 directly within this structure.
    """

    name: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    method_existing_pkcs12: Union[Unset, "CertMethodExistingPkcs12"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        descr = self.descr

        description = self.description

        method_existing_pkcs12: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.method_existing_pkcs12, Unset):
            method_existing_pkcs12 = self.method_existing_pkcs12.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if description is not UNSET:
            field_dict["description"] = description
        if method_existing_pkcs12 is not UNSET:
            field_dict["method_existing_pkcs12"] = method_existing_pkcs12

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_method_existing_pkcs_12 import CertMethodExistingPkcs12

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        description = d.pop("description", UNSET)

        _method_existing_pkcs12 = d.pop("method_existing_pkcs12", UNSET)
        method_existing_pkcs12: Union[Unset, CertMethodExistingPkcs12]
        if isinstance(_method_existing_pkcs12, Unset):
            method_existing_pkcs12 = UNSET
        else:
            method_existing_pkcs12 = CertMethodExistingPkcs12.from_dict(_method_existing_pkcs12)

        update_pkcs12_cert_req = cls(
            name=name,
            descr=descr,
            description=description,
            method_existing_pkcs12=method_existing_pkcs12,
        )

        update_pkcs12_cert_req.additional_properties = d
        return update_pkcs12_cert_req

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
