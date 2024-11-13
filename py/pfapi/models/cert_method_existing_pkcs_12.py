from typing import Any, Dict, List, Type, TypeVar, Union

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
            password (Union[Unset, str]):
            intermediates (Union[Unset, bool]):
            pkcs12_b64 (Union[Unset, str]):
    """

    password: Union[Unset, str] = UNSET
    intermediates: Union[Unset, bool] = UNSET
    pkcs12_b64: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password

        intermediates = self.intermediates

        pkcs12_b64 = self.pkcs12_b64

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
