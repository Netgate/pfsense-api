from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
            key_type (str):
            key_size (int):
            key_opt (str):
            digest_alg (str):
            lifetime (int):
            cn (str):
            country_code (str):
            state (str):
            city (str):
            org (str):
            ou (str):
            caref (str):
    """

    key_type: str
    key_size: int
    key_opt: str
    digest_alg: str
    lifetime: int
    cn: str
    country_code: str
    state: str
    city: str
    org: str
    ou: str
    caref: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_type = self.key_type

        key_size = self.key_size

        key_opt = self.key_opt

        digest_alg = self.digest_alg

        lifetime = self.lifetime

        cn = self.cn

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
                "key_size": key_size,
                "key_opt": key_opt,
                "digest_alg": digest_alg,
                "lifetime": lifetime,
                "cn": cn,
                "country_code": country_code,
                "state": state,
                "city": city,
                "org": org,
                "ou": ou,
                "caref": caref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_type = d.pop("key_type")

        key_size = d.pop("key_size")

        key_opt = d.pop("key_opt")

        digest_alg = d.pop("digest_alg")

        lifetime = d.pop("lifetime")

        cn = d.pop("cn")

        country_code = d.pop("country_code")

        state = d.pop("state")

        city = d.pop("city")

        org = d.pop("org")

        ou = d.pop("ou")

        caref = d.pop("caref")

        ca_cert_method_new = cls(
            key_type=key_type,
            key_size=key_size,
            key_opt=key_opt,
            digest_alg=digest_alg,
            lifetime=lifetime,
            cn=cn,
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
