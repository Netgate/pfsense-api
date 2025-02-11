from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cert_alt_name import CertAltName


T = TypeVar("T", bound="CertMethodSigningRequest")


@_attrs_define
class CertMethodSigningRequest:
    """
    Attributes:
        key_type (str):
        key_size (int):
        key_opt (str):
        digest_alg (str):
        cn (str):
        country_code (str):
        state (str):
        city (str):
        org (str):
        ou (str):
        server_cert (bool):
        alt_names (List['CertAltName']):
    """

    key_type: str
    key_size: int
    key_opt: str
    digest_alg: str
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
        key_type = self.key_type

        key_size = self.key_size

        key_opt = self.key_opt

        digest_alg = self.digest_alg

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
                "key_type": key_type,
                "key_size": key_size,
                "key_opt": key_opt,
                "digest_alg": digest_alg,
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
        key_type = d.pop("key_type")

        key_size = d.pop("key_size")

        key_opt = d.pop("key_opt")

        digest_alg = d.pop("digest_alg")

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

        cert_method_signing_request = cls(
            key_type=key_type,
            key_size=key_size,
            key_opt=key_opt,
            digest_alg=digest_alg,
            cn=cn,
            country_code=country_code,
            state=state,
            city=city,
            org=org,
            ou=ou,
            server_cert=server_cert,
            alt_names=alt_names,
        )

        cert_method_signing_request.additional_properties = d
        return cert_method_signing_request

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
