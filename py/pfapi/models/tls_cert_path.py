from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TLSCertPath")


@_attrs_define
class TLSCertPath:
    """
    Attributes:
        cert_path (Union[Unset, str]):
        key_path (Union[Unset, str]):
    """

    cert_path: Union[Unset, str] = UNSET
    key_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert_path = self.cert_path

        key_path = self.key_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_path is not UNSET:
            field_dict["cert_path"] = cert_path
        if key_path is not UNSET:
            field_dict["key_path"] = key_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert_path = d.pop("cert_path", UNSET)

        key_path = d.pop("key_path", UNSET)

        tls_cert_path = cls(
            cert_path=cert_path,
            key_path=key_path,
        )

        tls_cert_path.additional_properties = d
        return tls_cert_path

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