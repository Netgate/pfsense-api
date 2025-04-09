from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaCertMethodNew")


@_attrs_define
class CaCertMethodNew:
    """Options for creating/updating an internal CA certificate.
    The values for internal and intermediate certificates are the same,
    with the exception that the intermediate certificate is signed by
    a CA referenced by caref.
    For key type, size and options, query /system/certopts for the
    supported values.

    - key_type:     RSA or ECDSA
    - key_size:     size of key in bits (RSA)
    - key_opt:      curve types (historically ecname)
    - digest_alg:   hash algorithm for signing
    - lifetime:     days to expire
    - cn:           common name
    - country_code: 2-character country code
    - state:        state or province
    - city:         city
    - org:          organization, business name
    - ou:           organization unit
    - caref:        signing CA reference ID

        Attributes:
            key_type (str): rsa, ecdsa
            cn (str):
            key_size (Union[Unset, int]): rsa key size
            key_opt (Union[Unset, str]): key options, eg ecdsa curve
            digest_alg (Union[Unset, str]): sha1, sha224, sha256, sha384, sha512
            lifetime (Union[Unset, int]): days til expiry
            country_code (Union[Unset, str]):
            state (Union[Unset, str]):
            city (Union[Unset, str]):
            org (Union[Unset, str]):
            ou (Union[Unset, str]):
            caref (Union[Unset, str]):
    """

    key_type: str
    cn: str
    key_size: Union[Unset, int] = UNSET
    key_opt: Union[Unset, str] = UNSET
    digest_alg: Union[Unset, str] = UNSET
    lifetime: Union[Unset, int] = UNSET
    country_code: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    org: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    caref: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_type = self.key_type

        cn = self.cn

        key_size = self.key_size

        key_opt = self.key_opt

        digest_alg = self.digest_alg

        lifetime = self.lifetime

        country_code = self.country_code

        state = self.state

        city = self.city

        org = self.org

        ou = self.ou

        caref = self.caref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_type": key_type,
                "cn": cn,
            }
        )
        if key_size is not UNSET:
            field_dict["key_size"] = key_size
        if key_opt is not UNSET:
            field_dict["key_opt"] = key_opt
        if digest_alg is not UNSET:
            field_dict["digest_alg"] = digest_alg
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if org is not UNSET:
            field_dict["org"] = org
        if ou is not UNSET:
            field_dict["ou"] = ou
        if caref is not UNSET:
            field_dict["caref"] = caref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_type = d.pop("key_type")

        cn = d.pop("cn")

        key_size = d.pop("key_size", UNSET)

        key_opt = d.pop("key_opt", UNSET)

        digest_alg = d.pop("digest_alg", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        country_code = d.pop("country_code", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        org = d.pop("org", UNSET)

        ou = d.pop("ou", UNSET)

        caref = d.pop("caref", UNSET)

        ca_cert_method_new = cls(
            key_type=key_type,
            cn=cn,
            key_size=key_size,
            key_opt=key_opt,
            digest_alg=digest_alg,
            lifetime=lifetime,
            country_code=country_code,
            state=state,
            city=city,
            org=org,
            ou=ou,
            caref=caref,
        )

        ca_cert_method_new.additional_properties = d
        return ca_cert_method_new

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
