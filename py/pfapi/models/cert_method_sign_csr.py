from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_alt_name import CertAltName


T = TypeVar("T", bound="CertMethodSignCSR")


@_attrs_define
class CertMethodSignCSR:
    """Sign a certificate signing request with the selected CA.
    An existing csr_refid or new CSR (base64 encoded "csr") must be provided.

        Attributes:
            caref (str):
            csr_refid (str):
            csr (str):
            lifetime (int):
            digest_alg (str):
            server_cert (bool):
            alt_names (List['CertAltName']):
            priv_key (Union[Unset, str]):
    """

    caref: str
    csr_refid: str
    csr: str
    lifetime: int
    digest_alg: str
    server_cert: bool
    alt_names: List["CertAltName"]
    priv_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        caref = self.caref

        csr_refid = self.csr_refid

        csr = self.csr

        lifetime = self.lifetime

        digest_alg = self.digest_alg

        server_cert = self.server_cert

        alt_names = []
        for alt_names_item_data in self.alt_names:
            alt_names_item = alt_names_item_data.to_dict()
            alt_names.append(alt_names_item)

        priv_key = self.priv_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "caref": caref,
                "csr_refid": csr_refid,
                "csr": csr,
                "lifetime": lifetime,
                "digest_alg": digest_alg,
                "server_cert": server_cert,
                "alt_names": alt_names,
            }
        )
        if priv_key is not UNSET:
            field_dict["priv_key"] = priv_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_alt_name import CertAltName

        d = src_dict.copy()
        caref = d.pop("caref")

        csr_refid = d.pop("csr_refid")

        csr = d.pop("csr")

        lifetime = d.pop("lifetime")

        digest_alg = d.pop("digest_alg")

        server_cert = d.pop("server_cert")

        alt_names = []
        _alt_names = d.pop("alt_names")
        for alt_names_item_data in _alt_names:
            alt_names_item = CertAltName.from_dict(alt_names_item_data)

            alt_names.append(alt_names_item)

        priv_key = d.pop("priv_key", UNSET)

        cert_method_sign_csr = cls(
            caref=caref,
            csr_refid=csr_refid,
            csr=csr,
            lifetime=lifetime,
            digest_alg=digest_alg,
            server_cert=server_cert,
            alt_names=alt_names,
            priv_key=priv_key,
        )

        cert_method_sign_csr.additional_properties = d
        return cert_method_sign_csr

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
