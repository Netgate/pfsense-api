from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cert_alt_name import CertAltName


T = TypeVar("T", bound="CertMethodNew")


@_attrs_define
class CertMethodNew:
    """Options for creating/updating an internal certificate.
    For key type, size and options, query /system/certopts for the
    supported values.

    - caref:        CA (refid) to sign cert
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
    - server_cert   true for server cert, false for user cert

        Attributes:
            caref (str):
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
            server_cert (bool):
            alt_names (List['CertAltName']):
    """

    caref: str
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
    server_cert: bool
    alt_names: List["CertAltName"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        caref = self.caref

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

        server_cert = self.server_cert

        alt_names = []
        for alt_names_item_data in self.alt_names:
            alt_names_item = alt_names_item_data.to_dict()
            alt_names.append(alt_names_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "caref": caref,
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
                "server_cert": server_cert,
                "alt_names": alt_names,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_alt_name import CertAltName

        d = src_dict.copy()
        caref = d.pop("caref")

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

        server_cert = d.pop("server_cert")

        alt_names = []
        _alt_names = d.pop("alt_names")
        for alt_names_item_data in _alt_names:
            alt_names_item = CertAltName.from_dict(alt_names_item_data)

            alt_names.append(alt_names_item)

        cert_method_new = cls(
            caref=caref,
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
            server_cert=server_cert,
            alt_names=alt_names,
        )

        cert_method_new.additional_properties = d
        return cert_method_new

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
