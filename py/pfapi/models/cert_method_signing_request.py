from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cert_alt_name import CertAltName


T = TypeVar("T", bound="CertMethodSigningRequest")


@_attrs_define
class CertMethodSigningRequest:
    """
    Attributes:
        key_type (Union[Unset, str]): rsa, ecdsa
        key_size (Union[Unset, int]): rsa key size
        key_opt (Union[Unset, str]): key options, eg ecdsa curve
        digest_alg (Union[Unset, str]): sha1, sha224, sha256, sha384, sha512
        cn (Union[Unset, str]):
        country_code (Union[Unset, str]):
        state (Union[Unset, str]):
        city (Union[Unset, str]):
        org (Union[Unset, str]):
        ou (Union[Unset, str]):
        server_cert (Union[Unset, bool]): true = server cert, false = user cert
        alt_names (Union[Unset, List['CertAltName']]):
    """

    key_type: Union[Unset, str] = UNSET
    key_size: Union[Unset, int] = UNSET
    key_opt: Union[Unset, str] = UNSET
    digest_alg: Union[Unset, str] = UNSET
    cn: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    org: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    server_cert: Union[Unset, bool] = UNSET
    alt_names: Union[Unset, List["CertAltName"]] = UNSET
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

        alt_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alt_names, Unset):
            alt_names = []
            for alt_names_item_data in self.alt_names:
                alt_names_item = alt_names_item_data.to_dict()
                alt_names.append(alt_names_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if key_size is not UNSET:
            field_dict["key_size"] = key_size
        if key_opt is not UNSET:
            field_dict["key_opt"] = key_opt
        if digest_alg is not UNSET:
            field_dict["digest_alg"] = digest_alg
        if cn is not UNSET:
            field_dict["cn"] = cn
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
        if server_cert is not UNSET:
            field_dict["server_cert"] = server_cert
        if alt_names is not UNSET:
            field_dict["alt_names"] = alt_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cert_alt_name import CertAltName

        d = src_dict.copy()
        key_type = d.pop("key_type", UNSET)

        key_size = d.pop("key_size", UNSET)

        key_opt = d.pop("key_opt", UNSET)

        digest_alg = d.pop("digest_alg", UNSET)

        cn = d.pop("cn", UNSET)

        country_code = d.pop("country_code", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        org = d.pop("org", UNSET)

        ou = d.pop("ou", UNSET)

        server_cert = d.pop("server_cert", UNSET)

        alt_names = []
        _alt_names = d.pop("alt_names", UNSET)
        for alt_names_item_data in _alt_names or []:
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
