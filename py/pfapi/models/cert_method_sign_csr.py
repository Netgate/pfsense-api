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
            caref (Union[Unset, str]):
            csr_refid (Union[Unset, str]):
            csr (Union[Unset, str]):
            priv_key (Union[Unset, str]):
            lifetime (Union[Unset, int]):
            digest_alg (Union[Unset, str]):
            server_cert (Union[Unset, bool]):
            alt_names (Union[Unset, List['CertAltName']]):
    """

    caref: Union[Unset, str] = UNSET
    csr_refid: Union[Unset, str] = UNSET
    csr: Union[Unset, str] = UNSET
    priv_key: Union[Unset, str] = UNSET
    lifetime: Union[Unset, int] = UNSET
    digest_alg: Union[Unset, str] = UNSET
    server_cert: Union[Unset, bool] = UNSET
    alt_names: Union[Unset, List["CertAltName"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        caref = self.caref

        csr_refid = self.csr_refid

        csr = self.csr

        priv_key = self.priv_key

        lifetime = self.lifetime

        digest_alg = self.digest_alg

        server_cert = self.server_cert

        alt_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alt_names, Unset):
            alt_names = []
            for alt_names_item_data in self.alt_names:
                alt_names_item = alt_names_item_data.to_dict()
                alt_names.append(alt_names_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caref is not UNSET:
            field_dict["caref"] = caref
        if csr_refid is not UNSET:
            field_dict["csr_refid"] = csr_refid
        if csr is not UNSET:
            field_dict["csr"] = csr
        if priv_key is not UNSET:
            field_dict["priv_key"] = priv_key
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if digest_alg is not UNSET:
            field_dict["digest_alg"] = digest_alg
        if server_cert is not UNSET:
            field_dict["server_cert"] = server_cert
        if alt_names is not UNSET:
            field_dict["alt_names"] = alt_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_alt_name import CertAltName

        d = src_dict.copy()
        caref = d.pop("caref", UNSET)

        csr_refid = d.pop("csr_refid", UNSET)

        csr = d.pop("csr", UNSET)

        priv_key = d.pop("priv_key", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        digest_alg = d.pop("digest_alg", UNSET)

        server_cert = d.pop("server_cert", UNSET)

        alt_names = []
        _alt_names = d.pop("alt_names", UNSET)
        for alt_names_item_data in _alt_names or []:
            alt_names_item = CertAltName.from_dict(alt_names_item_data)

            alt_names.append(alt_names_item)

        cert_method_sign_csr = cls(
            caref=caref,
            csr_refid=csr_refid,
            csr=csr,
            priv_key=priv_key,
            lifetime=lifetime,
            digest_alg=digest_alg,
            server_cert=server_cert,
            alt_names=alt_names,
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
