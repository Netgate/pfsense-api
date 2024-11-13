from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        cert (Union[Unset, CertificateDetailed]):
    """

    cert: Union[Unset, "CertificateDetailed"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cert, Unset):
            cert = self.cert.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert is not UNSET:
            field_dict["cert"] = cert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.certificate_detailed import CertificateDetailed

        d = src_dict.copy()
        _cert = d.pop("cert", UNSET)
        cert: Union[Unset, CertificateDetailed]
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
